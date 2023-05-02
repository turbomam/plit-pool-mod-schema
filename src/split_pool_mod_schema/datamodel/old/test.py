import pprint
from typing import List, Dict, Any

import requests


def get_classes_from_sample_tag(sample_id: str, base_url="https://data.neonscience.org/api/v0/samples/classes",
                                param="sampleTag") -> List[str]:
    assembled_url = f"{base_url}?{param}={sample_id}"
    return requests.get(assembled_url).json()["data"]["sampleClasses"]


def get_sample_details_from_tag_and_classes(sample_id: str, base_url="https://data.neonscience.org/api/v0/samples/view",
                                            param1="sampleTag", param2="sampleClass") -> Dict[str, Any]:
    sample_data = {}
    classes = get_classes_from_sample_tag(sample_id)
    for associated_class in classes:
        assembled_url = f"{base_url}?{param1}={sample_id}&{param2}={associated_class}"
        sample_data[associated_class] = requests.get(assembled_url).json()["data"]
    return sample_data


def get_self_uuids_from_sample_details(sample_details: dict) -> List[str]:
    uuids = []
    for ok, ov in sample_details.items():
        for i in ov['sampleViews']:
            uuids.append(i['sampleUuid'])
    return uuids


def get_sample_details_from_uuid(sample_uuid: str, base_url="https://data.neonscience.org/api/v0/samples/view",
                                 param_name="sampleUuid") -> Dict[str, Any]:
    assembled_url = f"{base_url}?{param_name}={sample_uuid}"
    return requests.get(assembled_url).json()["data"]


sample_details_from_tag_and_classes = get_sample_details_from_tag_and_classes("YELL_046-M-4.5-0.5-20191002-GEN-DNA2")

# self_uuids_from_sample_details = get_self_uuids_from_sample_details(sample_details_from_tag_and_classes)
#
# for i in self_uuids_from_sample_details:
#     pprint.pprint(get_sample_details_from_uuid(i))
