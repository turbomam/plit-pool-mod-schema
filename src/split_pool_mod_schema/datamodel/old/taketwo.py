import pprint

import requests


class SampleRelationship:
    def __init__(self, seed_uuid):
        self.sample_details = {}
        self.relationships = {}
        print(f"Fetching relationships for {seed_uuid}...")
        self.build_sample_relationships(seed_uuid)

    def build_sample_relationships(self, uuid):
        print(f"Fetching details for {uuid}...")
        details = self.get_sample_details(uuid)
        self.sample_details[uuid] = details

        # check if sample has children
        if details['data']['sampleViews'][0]['childSampleIdentifiers']:
            child_uuids = [c['sampleUuid'] for c in details['data']['sampleViews'][0]['childSampleIdentifiers']]
            self.relationships[uuid] = child_uuids

            # recursively build relationships for children
            for child_uuid in child_uuids:
                self.build_sample_relationships(child_uuid)

        # check if sample has parents
        if details['data']['sampleViews'][0]['parentSampleIdentifiers']:
            parent_uuids = [p['sampleUuid'] for p in details['data']['sampleViews'][0]['parentSampleIdentifiers']]
            self.relationships[uuid] = parent_uuids

            # recursively build relationships for parents
            for parent_uuid in parent_uuids:
                self.build_sample_relationships(parent_uuid)

    def get_sample_details(self, uuid):
        if uuid in self.sample_details:
            print(f"Found cached details for {uuid}")
            return self.sample_details[uuid]

        url = f'https://data.neonscience.org/api/v0/samples/view?sampleUuid={uuid}'
        print(f"Fetching details for {url}...")
        response = requests.get(url)
        response_json = response.json()
        pprint.pprint(response_json)

        # # check if response is valid
        # if response_json['status'] != 'success':
        #     raise ValueError(f"Failed to get sample details for uuid {uuid}: {response_json['message']}")

        # check if sample has data
        if not response_json['data']['sampleViews']:
            raise ValueError(f"No sample details found for uuid {uuid}")

        # cache and return details
        self.sample_details[uuid] = response_json
        return response_json


# example usage
relationships = SampleRelationship('db838e1d-ce63-4729-a3f5-066dfb0a3110')

for uuid, uuid_details in relationships.sample_details.items():
    print(f"UUID: {uuid}")
    print(f"Tag: {uuid_details.details['data']['sampleViews'][0]['sampleTag']}")
    print(f"Class: {uuid_details.details['data']['sampleViews'][0]['sampleClass']}")
    print(f"Parent UUIDs: {uuid_details.parent_uuids}")
    print(f"Child UUIDs: {uuid_details.child_uuids}")
    print("--------------------------")
