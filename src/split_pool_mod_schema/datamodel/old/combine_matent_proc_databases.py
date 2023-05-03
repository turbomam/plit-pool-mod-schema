import datetime

import yaml
from linkml_runtime.dumpers import yaml_dumper

material_entity_database_file = "/Users/MAM/Documents/gitrepos/split-pool-mod-schema/neon-notes/Database-material_entity_set-neon-soil-metagenome.yaml"
proc_database_file = "/Users/MAM/Documents/gitrepos/split-pool-mod-schema/neon-notes/Database-process_set.yaml"

now = datetime.datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
with open(material_entity_database_file, "r") as f:
    material_entities = yaml.safe_load(f)
now = datetime.datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

with open(proc_database_file, "r") as f:
    processes = yaml.safe_load(f)
now = datetime.datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

combined_dict = {
    "id": "example:material_entity_and_process_db",
    "name": "Material Entity and Process Database",
    'material_entity_set': material_entities['material_entity_set'],
    'process_set': processes['process_set']
}

yaml_dumper.dump(combined_dict, "example_material_entity_and_process_database.yaml")
