import os
import pprint

import logging
import time
from typing import Dict, Any

import requests
import yaml

source_dir = "/Users/MAM/Documents/gitrepos/split-pool-mod-schema/neon-notes/focused"
dest_dir = source_dir
extension = ".yaml"

sleep_time = 0.3

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

session = requests.Session()

session.headers.update(
    {'X-API-Token':
         'eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiJ9.eyJhdWQiOiJodHRwczovL2RhdGEubmVvbnNjaWVuY2Uub3JnL2FwaS92MC8iLCJzdWIiOiJNQU1AbGJsLmdvdiIsInNjb3BlIjoicmF0ZTpwdWJsaWMiLCJpc3MiOiJodHRwczovL2RhdGEubmVvbnNjaWVuY2Uub3JnLyIsImV4cCI6MTg0MDYzMTY3MywiaWF0IjoxNjgyOTUxNjczLCJlbWFpbCI6Ik1BTUBsYmwuZ292In0.H0P7ke_WL7syECGAA4khEddZ8f6sR__vA3TFherLVt8I1omtYNjspqwWZh42ZkoCbCmRTIr4b4OG8uqPhICv8g'
     })


def get_file_paths_from_dir(source_dir, extension):
    return [os.path.join(source_dir, file_name) for file_name in os.listdir(source_dir) if
            file_name.endswith(extension)]


def get_related_uuids_from_file_list(file_list):
    file_list.sort()
    relations_list = []
    for file_path in file_list:
        with open(file_path, "r") as f:
            # logger.info(f"Processing file: {file_path}")
            try:
                content = yaml.safe_load(f)
            except yaml.YAMLError as exc:
                logger.error(f"Error while parsing YAML in {file_path}: {exc}")
                continue
            if "data" not in content:
                logger.warning(f"No data in {file_path}")
                continue
            if "sampleViews" not in content["data"]:
                logger.warning(f"No sampleViews in {file_path}")
                continue
            for view in content["data"]["sampleViews"]:
                if "childSampleIdentifiers" in view and view["childSampleIdentifiers"] is not None:
                    for child in view["childSampleIdentifiers"]:
                        if "sampleUuid" in child:
                            relations_list.append(child["sampleUuid"])
                        else:
                            logger.warning(f"No childSampleIdentifiers sampleUuids in {file_path}")
                else:
                    logger.warning(f"No childSampleIdentifiers in {file_path}")
                if "parentSampleIdentifiers" in view and view["parentSampleIdentifiers"] is not None:
                    for parent in view["parentSampleIdentifiers"]:
                        if "sampleUuid" in parent:
                            relations_list.append(parent["sampleUuid"])
                        else:
                            logger.warning(f"No parentSampleIdentifiers sampleUuids in {file_path}")
                else:
                    logger.warning(f"No parentSampleIdentifiers in {file_path}")
    return relations_list


def check_file_existence(directory, file_name):
    logger.info(f"checking {os.path.join(directory, file_name)}")
    return os.path.isfile(os.path.join(directory, file_name))


def get_sample_details_from_uuid(sample_uuid: str, base_url="https://data.neonscience.org/api/v0/samples/view",
                                 param_name="sampleUuid") -> Dict[str, Any]:
    assembled_url = f"{base_url}?{param_name}={sample_uuid}"

    raw = session.get(assembled_url)

    headers = raw.headers
    remaining = int(headers['X-RateLimit-Remaining'])
    print(f"{remaining} burst requests remaining")

    if remaining < 100:
        print("sleeping")
        time.sleep(sleep_time)

    return raw.json()


def write_yaml_from_uuid(sample_uuid: str, dest_dir=dest_dir):
    sample_details = get_sample_details_from_uuid(sample_uuid)
    # pprint.pprint(sample_details)
    yaml.dump(sample_details, open(f"{dest_dir}/{sample_uuid}.yaml", "w"))
    # time.sleep(0.6)


my_list = get_file_paths_from_dir(source_dir, extension)
my_list.sort()

related_uuids = get_related_uuids_from_file_list(my_list)
related_uuids = list(set(related_uuids))
related_uuids.sort()

for current_uuid in related_uuids:
    current_file_name = f"{current_uuid}{extension}"
    if check_file_existence(source_dir, current_file_name):
        pass
    else:
        logger.warning(f"File {current_file_name} is not available locally. Fetching from API.")
        write_yaml_from_uuid(current_uuid)
