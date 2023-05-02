import pprint
import uuid

from linkml_runtime import SchemaView
from linkml_runtime.dumpers import yaml_dumper

import yaml

import os

from split_pool_mod_schema import Process, Database, MaterialEntity, MicDnaExtractionInSoilDnaSample, \
    MicDnaExtractionInSubsample, MmsMetagenomeSequencingInProcessedSeqFileName, SlsMetagenomicsPoolingInCompositeSample, \
    SlsSoilCoreCollectionInGeneticArchiveSample1, SlsSoilCoreCollectionInGeneticArchiveSample2, \
    SlsSoilCoreCollectionInGeneticArchiveSample3, SlsSoilCoreCollectionInGeneticArchiveSample4, \
    SlsSoilCoreCollectionInGeneticArchiveSample5, SlsSoilCoreCollectionInGeneticSample, SlsSoilCoreCollectionInSample, \
    SlsSoilMoistureInMoistureSample, SlsSoilpHInPhSample, DnaSamplePrepComposite, DnaSamplePrepSimple, Pooling, \
    Sequencing, SubsampleDnaExtract, GeneticSamplePrep, MoistureSamplePrep, PhSamplePrep

# cwd = os.getcwd()
# print("Current working directory:", cwd)

neon_json_dir = "/Users/MAM/Documents/gitrepos/split-pool-mod-schema/neon-notes/focused"
schema_file = "/Users/MAM/Documents/gitrepos/split-pool-mod-schema/src/split_pool_mod_schema/schema/split_pool_mod_schema.yaml"
materialize_generic_processes = False

schema_view = SchemaView(schema_file)
material_entity_name_list = schema_view.class_children("MaterialEntity")

neon_to_mat_ent_dict = {}
for matent in material_entity_name_list:
    matent_obj = schema_view.get_class(matent)
    matent_annotations = matent_obj.annotations
    if 'neon_term' in matent_annotations:
        matent_neon_annoation = matent_annotations['neon_term']
        if "value" in matent_neon_annoation:
            matent_neon_annoation_value = matent_neon_annoation['value']
            neon_to_mat_ent_dict[matent_neon_annoation_value] = matent

class_to_db_pred_dict = {}
db_obj = schema_view.get_class("Database")
db_preds = db_obj.slots
for pred in db_preds:
    pred_obj = schema_view.get_slot(pred)
    pred_range = pred_obj.range
    class_to_db_pred_dict[pred_range] = pred

xputs_to_process_dict = {}
process_name_list = schema_view.class_children("Process")
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

# # #

file_list = []
extension = ".yaml"

for entry in os.scandir(neon_json_dir):
    if entry.is_file() and entry.name.endswith(extension):
        file_list.append(entry.name)

file_list = list(set(file_list))
file_list.sort()

database = Database(id="example:db1", name="Example Database 1")

class_lookup_dict = {}

for current_file in file_list:
    print(fr"Reading from {current_file}")
    with open(f"{neon_json_dir}/{current_file}", "r") as f:
        loaded_data = yaml.safe_load(f)
        sample_view = loaded_data['data']['sampleViews'][0]

        current_mat_ent = MaterialEntity(
            id=f"NEON_SAMP_UUID:{sample_view['sampleUuid']}",
            name=sample_view['sampleTag'],
            neon_sample_class=sample_view['sampleClass'],
        )

        if 'sampleClass' in sample_view:
            class_lookup_dict[f"NEON_SAMP_UUID:{sample_view['sampleUuid']}"] = sample_view['sampleClass']

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
    print(f"Mining sample {i['id']}")
    if 'has_parents' in i and i['has_parents']:
        for p in i['has_parents']:
            # would be nice to bundle xputs into a smaller number of processes
            creation_uuid = uuid.uuid4()
            if (class_lookup_dict[p], i['neon_sample_class']) in xputs_to_process_dict:
                ideal_class = xputs_to_process_dict[(class_lookup_dict[p], i['neon_sample_class'])]
                class_obj = globals()[ideal_class]
                instance = class_obj(id=f"example:{creation_uuid}")
                instance.has_inputs = [p]
                instance.has_outputs = [i['id']]
                ideal_pred = class_to_db_pred_dict[ideal_class]
                database[ideal_pred].append(instance)
            elif materialize_generic_processes:
                generic_process = Process(id=f"example:{creation_uuid}")
                generic_process.has_inputs = [p]
                generic_process.has_outputs = [i['id']]
                database['process_set'].append(generic_process)
        del i['has_parents']

    if 'has_children' in i and i['has_children']:
        for c in i['has_children']:
            creation_uuid = uuid.uuid4()
            if (class_lookup_dict[c], i['neon_sample_class']) in xputs_to_process_dict:
                ideal_class = xputs_to_process_dict[(class_lookup_dict[c], i['neon_sample_class'])]
                class_obj = globals()[ideal_class]
                instance = class_obj(id=f"example:{creation_uuid}")
                instance.has_inputs = [i['id']]
                instance.has_outputs = [c]
                ideal_pred = class_to_db_pred_dict[ideal_class]
                database[ideal_pred].append(instance)
            elif materialize_generic_processes:
                generic_process = Process(id=f"example:{creation_uuid}")
                generic_process.has_inputs = [i['id']]
                generic_process.has_outputs = [c]
                database['process_set'].append(generic_process)

        disposition_uuid = uuid.uuid4()
        self_disposition = Process(id=f"example:{disposition_uuid}")
        self_disposition.has_inputs = [i['id']]
        self_disposition.has_outputs = i['has_children']
        database['process_set'].append(self_disposition)
        del i['has_children']

    # finer typing of material entities
    #  if a material entity can't be typed finer, it will currently be deleted below!
    if 'neon_sample_class' in i:
        if i['neon_sample_class'] in neon_to_mat_ent_dict:
            ideal_class = neon_to_mat_ent_dict[i['neon_sample_class']]

            temp_yaml = yaml_dumper.dumps(i)
            temp_dict = yaml.safe_load(temp_yaml)

            class_obj = globals()[ideal_class]
            instance = class_obj(**temp_dict)

            ideal_pred = class_to_db_pred_dict[ideal_class]

            database[ideal_pred].append(instance)
        else:
            print(f"no ideal class for {i['neon_sample_class']}")
    else:
        print(f"no neon_sample_class for {i['id']}")

del database['material_entity_set']

yaml_dumper.dump(database, "/Users/MAM/Documents/gitrepos/split-pool-mod-schema/neon-notes/Database.yaml")

# poetry run linkml-convert --output neon-notes/Database.ttl --schema src/split_pool_mod_schema/schema/split_pool_mod_schema.yaml neon-notes/Database.yaml
