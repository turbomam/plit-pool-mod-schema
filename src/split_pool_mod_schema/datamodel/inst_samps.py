import inspect
import os
import pprint
import uuid

import click
import yaml
from linkml_runtime import SchemaView
from linkml_runtime.dumpers import yaml_dumper

import split_pool_mod_schema
from split_pool_mod_schema import Database, Process, MaterialEntity, MaterialEntity, MicDnaExtractionInSoilDnaSample, \
    MicDnaExtractionInSubsample, MmsMetagenomeSequencingInProcessedSeqFileName, SlsMetagenomicsPoolingInCompositeSample, \
    SlsSoilCoreCollectionInGeneticArchiveSample1, SlsSoilCoreCollectionInGeneticArchiveSample2, \
    SlsSoilCoreCollectionInGeneticArchiveSample3, SlsSoilCoreCollectionInGeneticArchiveSample4, \
    SlsSoilCoreCollectionInGeneticArchiveSample5, SlsSoilCoreCollectionInGeneticSample, SlsSoilCoreCollectionInSample, \
    SlsSoilMoistureInMoistureSample, SlsSoilpHInPhSample, DnaSamplePrepComposite, DnaSamplePrepSimple, Pooling, \
    Sequencing, SubsampleDnaExtract, GeneticSamplePrep, MoistureSamplePrep, PhSamplePrep, \
    GeneticArchiving1, GeneticArchiving2, GeneticArchiving3, GeneticArchiving4, GeneticArchiving5, \
    BiomassSamplePrep, KclSamplePrep, CnSamplePrep, BgcArchiving


# for name, obj in inspect.getmembers(split_pool_mod_schema):
#     if inspect.isclass(obj):
#         print(name)
#
# x = Database(id="example:processes_db1")


@click.group()
def cli():
    pass


@cli.command()
@click.option('--destination-file', required=True)
@click.option('--materialize-generic-processes/--no-materialize-generic-processes', default=False)
@click.option('--neon-yaml-dir', required=True)
@click.option('--schema-file', required=True)
@click.option('--extension', default=".yaml")
def instantiate(neon_yaml_dir, schema_file, destination_file, materialize_generic_processes, extension):
    # click.echo(f"neon_yaml_dir: {neon_yaml_dir}")

    schema_view = SchemaView(schema_file)
    material_entity_name_list = schema_view.class_descendants("MaterialEntity")

    neon_classes_to_material_entities = {}
    for matent in material_entity_name_list:
        matent_obj = schema_view.get_class(matent)
        matent_annotations = matent_obj.annotations
        if 'neon_term' in matent_annotations:
            matent_neon_annoation = matent_annotations['neon_term']
            if "value" in matent_neon_annoation:
                matent_neon_annoation_value = matent_neon_annoation['value']
                neon_classes_to_material_entities[matent_neon_annoation_value] = matent
            else:
                click.echo(f"WARNING: {matent} has neon_term annotation but no value")
        else:
            click.echo(f"WARNING: {matent} has no neon_term annotation")

    class_to_db_pred_dict = {}
    db_obj = schema_view.get_class("Database")
    db_preds = db_obj.slots
    click.echo(pprint.pformat(db_preds))
    for pred in db_preds:
        click.echo(pred)
        pred_obj = schema_view.get_slot(pred)
        pred_range = pred_obj.range
        click.echo(pred_range)
        class_to_db_pred_dict[pred_range] = pred

    xputs_to_process_dict = {}
    process_name_list = schema_view.class_descendants("Process")
    for process in process_name_list:
        process_obj = schema_view.get_class(process)
        process_annotations = process_obj.annotations
        process_input_annoation_value = None
        if 'neon_input_class' in process_annotations:
            process_input = process_annotations['neon_input_class']
            if "value" in process_input:
                process_input_annoation_value = process_input['value']
        process_output_annoation_value = None
        if 'neon_output_class' in process_annotations:
            process_output = process_annotations['neon_output_class']
            if "value" in process_output:
                process_output_annoation_value = process_output['value']
        if process_input_annoation_value and process_output_annoation_value:
            xputs_to_process_dict[(process_input_annoation_value, process_output_annoation_value)] = process

    file_list = []

    for entry in os.scandir(neon_yaml_dir):
        if entry.is_file() and entry.name.endswith(extension):
            file_list.append(entry.name)

    file_list = list(set(file_list))
    file_list.sort()
    # click.echo(pprint.pformat(file_list))

    neon_samples_to_neon_classes = {}

    database = Database(id="example:db1", name="Example Database 1")

    for current_file in file_list:
        print(fr"Reading from {current_file}")
        with open(f"{neon_yaml_dir}/{current_file}", "r") as f:
            loaded_data = yaml.safe_load(f)
            sample_view = loaded_data['data']['sampleViews'][0]
            sample_uuid = sample_view['sampleUuid']

            current_mat_ent = MaterialEntity(
                id=f"NEON_SAMP_UUID:{sample_uuid}",
                name=sample_view['sampleTag'],
                neon_sample_class=sample_view['sampleClass'],
            )

            if 'sampleClass' in sample_view:
                sample_class = sample_view['sampleClass']
                # print(f"sampleClass: {sample_view['sampleClass']}")
                neon_samples_to_neon_classes[f"NEON_SAMP_UUID:{sample_uuid}"] = sample_class
            else:
                print(f"WARNING: {sample_uuid} has no sampleClass")

            child_list = []
            if sample_view['childSampleIdentifiers']:
                for i in sample_view['childSampleIdentifiers']:
                    child_list.append(f"NEON_SAMP_UUID:{i['sampleUuid']}")

            parent_list = []
            if sample_view['parentSampleIdentifiers']:
                for i in sample_view['parentSampleIdentifiers']:
                    parent_list.append(f"NEON_SAMP_UUID:{i['sampleUuid']}")

            current_mat_ent.has_children = child_list
            current_mat_ent.has_parents = parent_list

            database['material_entity_set'].append(current_mat_ent)

    for i in database['material_entity_set']:
        self_uuid = i['id']
        self_type = None
        if self_uuid in neon_samples_to_neon_classes:
            self_type = neon_samples_to_neon_classes[self_uuid]
        print(f"Mining sample {self_uuid}")
        if 'has_parents' in i and i['has_parents']:
            for p in i['has_parents']:
                # p_type = None
                if p in neon_samples_to_neon_classes:
                    creation_uuid = str(uuid.uuid4())
                    p_type = neon_samples_to_neon_classes[p]
                    ideal_process_class = "Process"
                    if (neon_samples_to_neon_classes[p], i['neon_sample_class']) in xputs_to_process_dict:
                        ideal_process_class = xputs_to_process_dict[
                            (neon_samples_to_neon_classes[p], i['neon_sample_class'])]
                    else:
                        click.echo(f"    NO PROCESS for {self_type} with {p_type} parent yet")
                    class_obj = globals()[ideal_process_class]
                    instance = class_obj(id=f"example:{creation_uuid}")
                    instance.has_inputs = [p]
                    instance.has_outputs = [i['id']]
                    ideal_pred = class_to_db_pred_dict[ideal_process_class]
                    click.echo(f"ideal_pred: {ideal_pred}")
                    database['name'] = ideal_pred
                #     database[ideal_pred].append(instance)
                # else:
                #     click.echo(f"    NO CLASS for {p} yet")

    #     if 'has_children' in i and i['has_children']:
    #         for c in i['has_children']:
    #             creation_uuid = uuid.uuid4()
    #             if (neon_samples_to_neon_classes[c], i['neon_sample_class']) in xputs_to_process_dict:
    #                 ideal_class = xputs_to_process_dict[(neon_samples_to_neon_classes[c], i['neon_sample_class'])]
    #                 class_obj = globals()[ideal_class]
    #                 instance = class_obj(id=f"example:{creation_uuid}")
    #                 instance.has_inputs = [i['id']]
    #                 instance.has_outputs = [c]
    #                 ideal_pred = class_to_db_pred_dict[ideal_class]
    #                 database[ideal_pred].append(instance)
    #             elif materialize_generic_processes:
    #                 generic_process = Process(id=f"example:{creation_uuid}")
    #                 generic_process.has_inputs = [i['id']]
    #                 generic_process.has_outputs = [c]
    #                 database['process_set'].append(generic_process)
    #
    #         # disposition_uuid = uuid.uuid4()
    #         # self_disposition = Process(id=f"example:{disposition_uuid}")
    #         # self_disposition.has_inputs = [i['id']]
    #         # self_disposition.has_outputs = i['has_children']
    #         # database['process_set'].append(self_disposition)
    #         del i['has_children']
    #
    #     # finer typing of material entities
    #     #  if a material entity can't be typed finer, it will currently be deleted below!
    #     if 'neon_sample_class' in i:
    #         if i['neon_sample_class'] in neon_classes_to_material_entities:
    #             ideal_class = neon_classes_to_material_entities[i['neon_sample_class']]
    #
    #             temp_yaml = yaml_dumper.dumps(i)
    #             temp_dict = yaml.safe_load(temp_yaml)
    #
    #             class_obj = globals()[ideal_class]
    #             instance = class_obj(**temp_dict)
    #
    #             ideal_pred = class_to_db_pred_dict[ideal_class]
    #
    #             database[ideal_pred].append(instance)
    #         else:
    #             print(f"no ideal class for {i['neon_sample_class']}")
    #     else:
    #         print(f"no neon_sample_class for {i['id']}")
    #
    # del database['material_entity_set']

    # pprint.pprint(neon_samples_to_neon_classes)
    #
    # pprint.pprint(neon_classes_to_material_entities)

    neon_samples_to_material_entities = {}
    for k, v in neon_samples_to_neon_classes.items():
        if v not in neon_classes_to_material_entities:
            click.echo(f"WARNING: {v} not in neon_classes_to_material_entities")
            # print(f"no ideal class for {v}")
        else:
            neon_samples_to_material_entities[k] = neon_classes_to_material_entities[v]

    pprint.pprint(neon_samples_to_material_entities)

    yaml_dumper.dump(database, destination_file)


if __name__ == '__main__':
    cli()
