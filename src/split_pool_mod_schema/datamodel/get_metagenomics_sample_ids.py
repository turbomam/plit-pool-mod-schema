import pprint

import pandas as pd
import requests
import yaml

# REST with paths to downloadable files
# GraphQL... nothing for samples? nothing that spans endpoints?
# R... efficient download of tables (but not sample data)
#  NMDC SW engineers don't really want to add R as a dependency
# bulk downloads form data portal

# what analyses do we care about? soli/surface/benthic shotgun metagenomics
# but the sequencing is pretty shallow
# can interactively retrieve these data products in bulk
# what other products do we care about?
# anything that will fill in a nmdc-schema Biosample slot
#  OR add another fields that a user might want ot search/filter on
# can find related samples and see what data is available for them
#  doesn't seem to include soil physical and chemical properties
# would be nice to see the relationships between sample classes and products
# could also run queries at the site level to see what other products are available
#  if the data don't come from the same sample, then we would want to find something that is temporo-spatially close
# speaking of which, do we want to bother converting the center coordinates of a plot,
#  the reference corner of the plot, the uncertainties, and the uncertainties into coordinates for the sampling locations?
# will still need to convert to nmdc-schema LinkML classes
# what about visualization

# getting degree-9 sample relations from evey soil metagenome sample relations is wasteful
# save results as files?
# save in a database like mongodb?

input_file = "/Users/MAM/Downloads/NEON_seq-metagenomic-microbe-soil/mms_metagenomeDnaExtraction.csv"

sample_class = "mic_dnaExtraction_in.soilDnaSampleID"
degree = 9
last_record = 999999

# Read the CSV file into a DataFrame
df = pd.read_csv(input_file)

# print(df.shape)

# Filter the DataFrame to only include rows where sequenceAnalysisType is "metagenomics" or "marker gene and metagenomics"
filter_condition = (df["sequenceAnalysisType"] == "metagenomics") | (
        df["sequenceAnalysisType"] == "marker gene and metagenomics")
filtered_df = df[filter_condition]

# Retrieve the "dnaSampleID" values for the filtered rows
dnaSampleID_list = filtered_df["dnaSampleID"].tolist()
dnaSampleID_list.sort()

# # already unique
# dnaSampleID_list_unique = list(set(dnaSampleID_list))
# print(len(dnaSampleID_list_unique))

# output_file = "dnaSampleID_list.tsv"
#
# # Write the list to a TSV file
# with open(output_file, "w") as f:
#     for item in dnaSampleID_list:
#         f.write("%s\n" % item)
#
# input_file = "/Users/MAM/Documents/gitrepos/split-pool-mod-schema/src/split_pool_mod_schema/datamodel/dnaSampleID_list.tsv"
#
# # Read the file into a list
# with open(input_file, "r") as f:
#     dnaSampleID_list = [line.strip() for line in f.readlines()]
#
# print(dnaSampleID_list)

# mic_dnaExtraction_in.soilDnaSampleID
# https://data.neonscience.org/api/v0/samples/download?sampleTag=GUAN_002-M-20190930-COMP-DNA1&sampleClass=mic_dnaExtraction_in.soilDnaSampleID&degree=99


everything = {}
sample_ids_relations = {}
for dnaSampleID in dnaSampleID_list[0:last_record]:
    print(dnaSampleID)
    url = f"https://data.neonscience.org/api/v0/samples/download?sampleTag={dnaSampleID}&sampleClass={sample_class}&degree={degree}"
    response_json = requests.get(url).json()
    sample_views = response_json["data"]["sampleViews"]

    # pprint.pprint(sample_views)

    for root_sample in sample_views:
        del root_sample["sampleEvents"]
        child_uuids = set()
        parent_uuids = set()
        print(f" {root_sample['sampleUuid'] = }:")
        # print(f" {root_sample['sampleClass'] = }:")
        # print(f" {root_sample['sampleTag'] = }:")
        if root_sample["childSampleIdentifiers"]:
            for child in root_sample["childSampleIdentifiers"]:
                print(f"{root_sample['sampleUuid']}  {child['sampleUuid'] = }:")
                # print(f" {child['sampleClass'] = }:")
                # print(f" {child['sampleTag'] = }:")
                child_uuids.add(child['sampleUuid'])
                if child['sampleUuid'] not in sample_ids_relations:
                    sample_ids_relations[child['sampleUuid']] = {
                        "sampleClass": child['sampleClass'],
                        "sampleTag": child['sampleTag'],
                        "sampleUuid": child['sampleUuid'],
                        "parentSampleIdentifiers": {root_sample['sampleUuid']},
                        "childSampleIdentifiers": set()
                    }
                else:
                    sample_ids_relations[child['sampleUuid']]["parentSampleIdentifiers"].add(
                        root_sample['sampleUuid'])
        if root_sample["parentSampleIdentifiers"]:
            for parent in root_sample["parentSampleIdentifiers"]:
                print(f"{root_sample['sampleUuid']} {parent['sampleUuid'] = }:")
                # print(f" {parent['sampleClass'] = }:")
                # print(f" {parent['sampleTag'] = }:")
                parent_uuids.add(parent['sampleUuid'])
                if parent['sampleUuid'] not in sample_ids_relations:
                    sample_ids_relations[parent['sampleUuid']] = {
                        "sampleClass": parent['sampleClass'],
                        "sampleTag": parent['sampleTag'],
                        "sampleUuid": parent['sampleUuid'],
                        "childSampleIdentifiers": {root_sample['sampleUuid']},
                        "parentSampleIdentifiers": set()
                    }
                else:
                    sample_ids_relations[parent['sampleUuid']]["childSampleIdentifiers"].add(
                        root_sample['sampleUuid'])
        if root_sample['sampleUuid'] not in sample_ids_relations:
            sample_ids_relations[root_sample['sampleUuid']] = {
                "sampleClass": root_sample['sampleClass'],
                "sampleTag": root_sample['sampleTag'],
                "sampleUuid": root_sample['sampleUuid'],
                "parentSampleIdentifiers": parent_uuids,
                "childSampleIdentifiers": child_uuids
            }


# pprint.pprint(sample_ids_relations)


def convert_sets_to_lists(obj):
    if isinstance(obj, set):
        return list(obj)
    elif isinstance(obj, dict):
        return {k: convert_sets_to_lists(v) for k, v in obj.items()}
    elif isinstance(obj, (list, tuple)):
        return [convert_sets_to_lists(item) for item in obj]
    else:
        return obj


sample_ids_relations = convert_sets_to_lists(sample_ids_relations)

yaml.dump(sample_ids_relations, open("sample_ids_relations-degree-9.yaml", "w"))

#     everything[dnaSampleID] = response_json
#
# yaml.dump(everything, open("everything-degree-3.yaml", "w"))
