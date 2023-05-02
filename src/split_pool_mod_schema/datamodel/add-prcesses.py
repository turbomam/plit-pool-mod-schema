import pprint

import yaml

import datetime

import uuid

from linkml_runtime.dumpers import yaml_dumper

from split_pool_mod_schema import Database, MaterialEntity, Process

material_entity_database_file = \
    "/Users/MAM/Documents/gitrepos/split-pool-mod-schema/neon-notes/Database-material_entity_set-neon-soil-metagenome.yaml"

now = datetime.datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
with open(material_entity_database_file, "r") as f:
    data = yaml.safe_load(f)
now = datetime.datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

process_database = Database(id="example:processes_db1", name="Example Process Database 1")

for i in data['material_entity_set']:
    pprint.pprint(i['id'])
    if 'parent_sample_identifiers' in i and i['parent_sample_identifiers']:
        creation_uuid = uuid.uuid4()
        self_creation = Process(id=f"example:{creation_uuid}")
        self_creation.has_inputs = i['parent_sample_identifiers']
        # could there be other outputs?
        #  would have to consult the inputs
        self_creation.has_outputs = [i['id']]
        # print(yaml_dumper.dumps(self_creation))
        process_database['process_set'].append(self_creation)
    if 'child_sample_identifiers' in i and i['child_sample_identifiers']:
        disposition_uuid = uuid.uuid4()
        self_disposition = Process(id=f"example:{disposition_uuid}")
        self_disposition.has_inputs = [i['id']]
        self_disposition.has_outputs = i['child_sample_identifiers']
        # print(yaml_dumper.dumps(self_disposition))
        process_database['process_set'].append(self_disposition)

yaml_dumper.dump(process_database, "example_process_database_1.yaml")
