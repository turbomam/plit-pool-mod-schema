import pprint
import time
from typing import List, Dict, Any

import pandas as pd
import requests
import yaml

# do these sample files contain all the data values that one would get from downloading a data product?
# is there a better way to determine which samples to include besides downloading a data product first?
# what is the relation between sample classes and data products
# does NEON do process modelling?

# since we're writing to YAML,
#   it's a little harder to tell if the results are incomplete (due to aborting a running program)
# also be on the lookout for undersized files with the text "" due to submitting requests too quickly

# sample_tag = "YELL_046-M-4.5-0.5-20191002-GEN-DNA2"
# sample_tag = "BMI_HY5W2BGXG_Plate19S_31WellG3_R1.fastq.gz" -> TypeError: 'NoneType' object is not subscriptable
# sample_tag = "YELL_052-O-20190820-COMP-DNA1"

# from NEON.D12.YELL.DP1.10107.001.mms_rawDataFiles.2019-08.expanded.20230113T225346Z
# or mms_rawDataFiles.csv

source_file = "mms_rawDataFiles.csv"
source_col = "dnaSampleID"
dest_dir = "dest_dir"
sleep_time = 0.3

session = requests.Session()

session.headers.update(
    {'X-API-Token':
         'eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiJ9.eyJhdWQiOiJodHRwczovL2RhdGEubmVvbnNjaWVuY2Uub3JnL2FwaS92MC8iLCJzdWIiOiJNQU1AbGJsLmdvdiIsInNjb3BlIjoicmF0ZTpwdWJsaWMiLCJpc3MiOiJodHRwczovL2RhdGEubmVvbnNjaWVuY2Uub3JnLyIsImV4cCI6MTg0MDYzMTY3MywiaWF0IjoxNjgyOTUxNjczLCJlbWFpbCI6Ik1BTUBsYmwuZ292In0.H0P7ke_WL7syECGAA4khEddZ8f6sR__vA3TFherLVt8I1omtYNjspqwWZh42ZkoCbCmRTIr4b4OG8uqPhICv8g'
     })


def get_classes_from_sample_tag(sample_id: str, base_url="https://data.neonscience.org/api/v0/samples/classes",
                                param="sampleTag") -> List[str]:
    assembled_url = f"{base_url}?{param}={sample_id}"
    raw = session.get(assembled_url)

    # headers = raw.headers
    # possibly sleep here if number of burst requests getting low?

    temp = raw.json()["data"]["sampleClasses"]
    return temp


def get_sample_details_from_tag_and_classes(sample_id: str, base_url="https://data.neonscience.org/api/v0/samples/view",
                                            param1="sampleTag", param2="sampleClass") -> Dict[str, Any]:
    sample_data = {}
    classes = get_classes_from_sample_tag(sample_id)
    for associated_class in classes:
        assembled_url = f"{base_url}?{param1}={sample_id}&{param2}={associated_class}"

        raw = session.get(assembled_url)

        headers = raw.headers
        remaining = int(headers['X-RateLimit-Remaining'])
        print(f"{remaining} burst requests remaining")

        sample_data[associated_class] = raw.json()

        if remaining < 100:
            print("sleeping")
            time.sleep(sleep_time)

    return sample_data


def get_self_uuids_from_sample_details(sample_details: dict) -> List[str]:
    uuids = []
    for ok, ov in sample_details.items():
        for i in ov['data']['sampleViews']:
            uuids.append(i['sampleUuid'])
    return uuids


def get_sample_details_from_uuid(sample_uuid: str, base_url="https://data.neonscience.org/api/v0/samples/view",
                                 param_name="sampleUuid") -> Dict[str, Any]:
    assembled_url = f"{base_url}?{param_name}={sample_uuid}"

    raw = session.get(assembled_url)

    # headers = raw.headers
    # possibly sleep here if number of burst requests getting low?
    # time.sleep(sleep_time)

    temp = raw.json()

    return temp


def write_yaml_from_tag(sample_tag: str, dest_dir: dest_dir):
    sample_details_from_tag_and_classes = get_sample_details_from_tag_and_classes(sample_tag)

    self_uuids_from_sample_details = get_self_uuids_from_sample_details(sample_details_from_tag_and_classes)

    for i in self_uuids_from_sample_details:
        print(i)
        my_view = get_sample_details_from_uuid(i)
        yaml.dump(my_view, open(f"{dest_dir}/{i}.yaml", "w"))


def extract_tags_from_csv(source_file, source_col):
    df = pd.read_csv(source_file, sep=',')
    tag_list = df[source_col].tolist()
    tag_list = list(set(tag_list))
    tag_list.sort()
    return tag_list


def fetch_and_write_from_tag_list(tag_list, dest_dir):
    for i in tag_list:
        print(i)
        write_yaml_from_tag(i, dest_dir)


my_tag_list = extract_tags_from_csv(source_file, source_col)
my_tag_list = list(set(my_tag_list))
my_tag_list.sort()

fetch_and_write_from_tag_list(my_tag_list, dest_dir)
