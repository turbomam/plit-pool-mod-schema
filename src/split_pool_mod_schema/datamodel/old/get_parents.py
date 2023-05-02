import pprint

import requests
import json

import yaml

BASE_URL = "https://data.neonscience.org/api/v0/samples/view"

class SampleResponse:
    def __init__(self, sample_uuid):
        self.sample_uuid = sample_uuid
        url = f"{BASE_URL}?sampleUuid={sample_uuid}"
        response_json = requests.get(url).json()
        self.data_sample_views = response_json["data"]["sampleViews"]
        self.response_dict = {"sample_uuid": sample_uuid, "response_json": response_json}

    def get_parent_uuids(self):
        all_parents = set()
        for sample_view in self.data_sample_views:
            parent_uuids = sample_view["parentSampleIdentifiers"]
            if not parent_uuids:
                continue

            for parent in parent_uuids:
                parent_uuid = parent["sampleUuid"]
                all_parents.add(parent_uuid)

        return all_parents

    def get_child_uuids(self):
        all_children = set()
        for sample_view in self.data_sample_views:
            child_uuids = sample_view["childSampleIdentifiers"]
            if not child_uuids:
                continue

            for child in child_uuids:
                child_uuid = child["sampleUuid"]
                all_children.add(child_uuid)

        return all_children


class SampleResponseAggregator:
    def __init__(self):
        self.responses = {}
        self.fetched_uuids = set()

    def add_sample_response(self, sample_uuid):
        if sample_uuid in self.fetched_uuids:
            print(f"Skipping {sample_uuid} - already fetched")
            return

        print(f"Fetching {sample_uuid}...")
        response = SampleResponse(sample_uuid)
        self.responses[sample_uuid] = response.response_dict
        self.fetched_uuids.add(sample_uuid)

        all_parents = response.get_parent_uuids()
        for parent_uuid in all_parents:
            self.add_sample_response(parent_uuid)

        all_children = response.get_child_uuids()
        for child_uuid in all_children:
            self.add_sample_response(child_uuid)

    def get_all_parent_uuids(self):
        all_parents = set()
        for sample_uuid, response_dict in self.responses.items():
            sample_response = SampleResponse(sample_uuid)
            all_parents.update(sample_response.get_parent_uuids())
        return all_parents

    def get_all_child_uuids(self):
        all_children = set()
        for sample_uuid, response_dict in self.responses.items():
            sample_response = SampleResponse(sample_uuid)
            all_children.update(sample_response.get_child_uuids())
        return all_children


# Example usage
seed_uuid = "db838e1d-ce63-4729-a3f5-066dfb0a3110"

response_aggregator = SampleResponseAggregator()
response_aggregator.add_sample_response(seed_uuid)

# print(json.dumps(response_aggregator.responses, indent=2))
#
# # json.dump(response_aggregator.responses, open("sample_responses.json", "w"), indent=2)
#
# yaml.dump(response_aggregator.responses, open("sample_responses.yaml", "w"), indent=2)

# with open('sample_responses.yaml', 'r') as file:
#     data = yaml.safe_load(file)
#
# relationships = []
# for k, v in data.items():
#     for i in v['response_json']['data']['sampleViews']:
#         print(f"{i['sampleUuid'] = }")
#         print(f"{i['sampleClass'] = }")
#         print(f"{i['sampleTag'] = }")
#     # parent_id = None
#     # child_ids = []
#     # for sample in entry['response_json']['data']['sampleViews']:
#     #     if sample['parentSampleIdentifiers'] is not None:
#     #         parent_id = sample['parentSampleIdentifiers'][0]['sampleUuid']
#     #     if sample['childSampleIdentifiers'] is not None:
#     #         child_ids.extend([child['sampleUuid'] for child in sample['childSampleIdentifiers']])
#     # relationships.append({'parent': parent_id, 'children': child_ids})
#
# # Print the list of parent and child relationships
# pprint.pprint(relationships)
