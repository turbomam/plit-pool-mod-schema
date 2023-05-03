import os
import pprint

import yaml
import csv

# neon_json_dir = "/Users/MAM/Documents/gitrepos/split-pool-mod-schema/neon-notes/focused"
neon_json_dir = "/Users/MAM/neon_samples_yaml"

file_list = []
extension = ".yaml"

for entry in os.scandir(neon_json_dir):
    if entry.is_file() and entry.name.endswith(extension):
        file_list.append(entry.name)

file_list = list(set(file_list))
file_list.sort()

sample_details = []

for current_file in file_list:
    print(current_file)
    with open(f"{neon_json_dir}/{current_file}", "r") as f:
        loaded_data = yaml.safe_load(f)
        # pprint.pprint(loaded_data)
        sampleView = loaded_data['data']['sampleViews'][0]
        parent_count = 0
        if "parentSampleIdentifiers" in sampleView and sampleView['parentSampleIdentifiers']:
            parent_count = len(sampleView['parentSampleIdentifiers'])
        current_details = {
            "sampleUuid": sampleView['sampleUuid'],
            "sampleTag": sampleView['sampleTag'],
            "sampleClass": sampleView['sampleClass'],
            "parent_count": parent_count,
        }
        sample_details.append(current_details)

# pprint.pprint(sample_details)

# Open the TSV file for writing
with open("parent_count_by_sample_class.tsv", "w", newline="") as f:
    # Get the headers from the first dictionary
    headers = list(sample_details[0].keys())

    # Create a DictWriter object with tab delimiter
    writer = csv.DictWriter(f, fieldnames=headers, delimiter="\t")

    # Write the header row to the TSV file
    writer.writeheader()

    # Write each dictionary in the list to a row in the TSV file
    for d in sample_details:
        writer.writerow(d)
