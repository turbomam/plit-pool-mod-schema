import click

import pprint
import time
from typing import List, Dict, Any

import requests
import yaml
import os

session_obj = requests.Session()


def get_classes_from_sample_tag(sample_tag: str, api_token: str = None,
                                base_url="https://data.neonscience.org/api/v0/samples/classes",
                                param="sampleTag",
                                verbose=False) -> List[str]:
    assembled_url = f"{base_url}?{param}={sample_tag}"

    if api_token:
        session_obj.headers.update(
            {'X-API-Token': api_token})

    api_response = session_obj.get(assembled_url)
    headers = api_response.headers
    if verbose:
        click.echo(pprint.pformat(dict(headers)))
    # possibly sleep here if number of burst requests getting low?

    api_data = api_response.json()

    discovered_classes = []
    if "data" in api_data and api_data['data']:
        if "sampleClasses" in api_data['data'] and api_data['data']['sampleClasses']:
            discovered_classes = api_data['data']['sampleClasses']
    return discovered_classes


def get_sample_view_from_tag_and_classes(sample_tag: str,
                                         sample_classes: List[str],
                                         min_burst_remaining: int,
                                         sleep_secs: float,
                                         api_token: str = None,
                                         base_url="https://data.neonscience.org/api/v0/samples/view",
                                         param1="sampleTag",
                                         param2="sampleClass",
                                         verbose=False) -> Dict[str, Any]:
    if api_token:
        session_obj.headers.update(
            {'X-API-Token': api_token})

    sample_data = {}
    for associated_class in sample_classes:
        assembled_url = f"{base_url}?{param1}={sample_tag}&{param2}={associated_class}"

        raw = session_obj.get(assembled_url)

        headers = raw.headers
        if verbose:
            click.echo(pprint.pformat(dict(headers)))

        remaining = int(headers['X-RateLimit-Remaining'])
        if remaining < min_burst_remaining:
            click.echo(
                f"burst requests remaining = {remaining} and {min_burst_remaining = } so sleeping {sleep_secs} seconds")
            time.sleep(sleep_secs)

        sample_data[associated_class] = raw.json()

    return sample_data


def get_sample_view_from_uuid(sample_uuid: str,
                              min_burst_remaining: int,
                              sleep_secs: float,
                              api_token: str = None,
                              base_url="https://data.neonscience.org/api/v0/samples/view",
                              param1="sampleUuid",
                              verbose=False) -> Dict[str, Any]:
    if api_token:
        session_obj.headers.update(
            {'X-API-Token': api_token})

    assembled_url = f"{base_url}?{param1}={sample_uuid}"

    raw = session_obj.get(assembled_url)

    headers = raw.headers
    if verbose:
        click.echo(pprint.pformat(dict(headers)))

    remaining = int(headers['X-RateLimit-Remaining'])
    if remaining < min_burst_remaining:
        click.echo(
            f"burst requests remaining = {remaining} and {min_burst_remaining = } so sleeping {sleep_secs} seconds")
        time.sleep(sleep_secs)

    return raw.json()


# def get_self_uuids_from_sample_details(sample_view: dict) -> List[str]:
#     uuids = []
#     for ok, ov in sample_view.items():
#         for i in ov['data']['sampleViews']:
#             uuids.append(i['sampleUuid'])
#     return uuids
#
#
# def get_sample_details_from_uuid(sample_uuid: str, base_url="https://data.neonscience.org/api/v0/samples/view",
#                                  param_name="sampleUuid") -> Dict[str, Any]:
#     assembled_url = f"{base_url}?{param_name}={sample_uuid}"
#
#     raw = session.get(assembled_url)
#
#     # headers = raw.headers
#     # possibly sleep here if number of burst requests getting low?
#     # time.sleep(sleep_time)
#
#     temp = raw.json()
#
#     return temp
#
#
# def write_yaml_from_tag(sample_tag: str, dest_dir: dest_dir):
#     sample_details_from_tag_and_classes = get_sample_view_from_tag_and_classes(sample_tag)
#
#     self_uuids_from_sample_details = get_self_uuids_from_sample_details(sample_details_from_tag_and_classes)
#
#     for i in self_uuids_from_sample_details:
#         print(i)
#         my_view = get_sample_details_from_uuid(i)
#         yaml.dump(my_view, open(f"{dest_dir}/{i}.yaml", "w"))
#
#
# def extract_tags_from_csv(source_file, source_col):
#     df = pd.read_csv(source_file, sep=',')
#     tag_list = df[source_col].tolist()
#     tag_list = list(set(tag_list))
#     tag_list.sort()
#     return tag_list
#
#
# def fetch_and_write_from_tag_list(tag_list, dest_dir):
#     for i in tag_list:
#         print(i)
#         write_yaml_from_tag(i, dest_dir)

def write_yaml_from_sample_obj(sample_obj: Dict[str, Any], dest_dir: str):
    if 'data' in sample_obj and 'sampleViews' in sample_obj['data'] and len(
            sample_obj['data']['sampleViews']) > 0 and 'sampleUuid' in sample_obj['data']['sampleViews'][0]:
        current_uuid = sample_obj['data']['sampleViews'][0]['sampleUuid']

        # Create the directory if it does not exist
        os.makedirs(dest_dir, exist_ok=True)

        # Define the file path
        file_path = os.path.join(dest_dir, f"{current_uuid}.yaml")

        # Dump the sample_obj dictionary to the YAML file
        with open(file_path, "w") as f:
            yaml.dump(sample_obj, f)
            return current_uuid, str(file_path)

    else:
        click.echo()
        return


# Do something else if any of the keys are missing


# if 'data' in sample_obj and len(my_dict['data']['sampleViews']) > 0:
#     first_item = my_dict['data']['sampleViews'][0]
#     # do something with first_item
# else:
#     print("data key or sampleViews list is not present in the dictionary")


# if sample_obj.get('data', {}).get('sampleViews', {}).get('sampleUuid') is not None:
#     uuid = sample_obj['data']['sampleViews']['sampleUuid']
#     print(uuid)
# # do something
# else:
#     return
# # the path is not available in the dictionary
# uuid = sample_obj['data']['sampleViews']['sampleUuid']
# print(dest_dir)
# pprint.pprint(sample_obj)
# # with open
# # sample_details_from_tag_and_classes = get_sample_view_from_tag_and_classes(sample_tag)
# #
# # self_uuids_from_sample_details = get_self_uuids_from_sample_details(sample_details_from_tag_and_classes)
# #
# # for uuid, sample_obj in self_uuids_from_sample_details:
# #     # print(i)
# #     # my_view = get_sample_details_from_uuid(i)
# #     # yaml.dump(my_view, open(f"{dest_dir}/{i}.yaml", "w"))

def determine_relatives(sample_obj):
    if 'data' in sample_obj and 'sampleViews' in sample_obj['data'] and len(
            sample_obj['data']['sampleViews']) > 0:
        inner_obj = sample_obj['data']['sampleViews'][0]
        rel_uuids = []
        for rel_type in ["childSampleIdentifiers", "parentSampleIdentifiers"]:
            click.echo(f"Checking {rel_type}")
            if rel_type in inner_obj and inner_obj[rel_type]:
                rel_objs = inner_obj[rel_type]
                for current_rel_obj in rel_objs:
                    if "sampleUuid" in current_rel_obj and current_rel_obj["sampleUuid"]:
                        rel_uuids.append(current_rel_obj["sampleUuid"])
                    else:
                        click.echo(f"No {rel_type} uuids found")
            else:
                click.echo(f"No {rel_type} found")
        rel_uuids = list(set(rel_uuids))
        rel_uuids.sort()
        return rel_uuids
    else:
        click.echo("Couldn't find a path to relatives")
        return


def list_files_present(directory: str, extension: str):
    """Finds all files in the given directory whose names end in the extension ".yaml".

    Args:
      directory: The directory to search.
      extension: Limit the results to files with this extension

    Returns:
      A list of the names of all files in the directory whose names end in the extension ".yaml".
    """

    files = []
    for file in os.listdir(directory):
        if file.endswith(extension):
            files.append(file)

    return files


def get_sample_view_from_file(file_path: str):
    # todo add error handling
    with open(file_path, "r") as f:
        sample_obj = yaml.load(f, Loader=yaml.FullLoader)
        return sample_obj


def list_uuids_still_needed(directory: str, extension: str = ".yaml"):
    files_present = list_files_present(directory, extension)
    uuids_present = remove_extension(files_present.copy(), extension)
    relatives_mentioned = []
    for present_file in files_present:
        sample_view = get_sample_view_from_file(os.path.join(directory, present_file))
        current_relatives = determine_relatives(sample_view)
        relatives_mentioned.extend(current_relatives)
    uuids_still_needed = list(set(relatives_mentioned) - set(uuids_present))
    uuids_still_needed = list(set(uuids_still_needed))
    uuids_still_needed.sort()
    return uuids_still_needed


def remove_extension(filenames, extension):
    """Removes the extension ".yaml" from the end of a list of strings.

    Args:
      filenames: A list of filenames, with each item's value potentially ending in the extension
      extension: A string that might be found at the end of filenames

    Returns:
      The list of strings with the extension removed.
    """

    for i, string in enumerate(filenames):
        if string.endswith(extension):
            filenames[i] = string[:-len(extension)]

    return filenames


def process_relatives(directory: str, min_burst_remaining, sleep_secs, api_token, dest_dir: str, verbose=False,
                      extension: str = ".yaml"):
    uuids_still_needed = list_uuids_still_needed(directory, extension)
    if uuids_still_needed:
        for needed_uuid in uuids_still_needed:
            print(f"Getting {needed_uuid}")
            sample_obj = get_sample_view_from_uuid(needed_uuid,
                                                   min_burst_remaining=min_burst_remaining,
                                                   sleep_secs=sleep_secs,
                                                   api_token=api_token,
                                                   verbose=verbose)
            # click.echo(pprint.pformat(sample_obj))
            written_file = write_yaml_from_sample_obj(sample_obj, dest_dir=dest_dir)
            click.echo(f"Wrote {written_file}")
        process_relatives(directory=dest_dir, min_burst_remaining=min_burst_remaining, sleep_secs=sleep_secs,
                          api_token=api_token, dest_dir=dest_dir, verbose=verbose, extension=extension)
    else:
        click.echo("No relatives left to process")


@click.group()
def cli():
    pass


@cli.command()
@click.option('--sample-tag', prompt=False, required=True, help='Enter a NEON sample tag')
@click.option('--api-token', prompt=False, required=False,
              help='Enter a NEON REST API token if you have one. Downloads will be faster.')
@click.option('--min-burst-remaining', prompt=False, default=100,
              help='Start sleeping a little if the number of burst requests is below this threshold.')
@click.option('--sleep-secs', prompt=False, default=0.5,
              help='Sleep this long between requests if the min-burst-remaining threshold has been crossed.')
@click.option('--dest-dir', prompt=False, default=".",
              help='Where should the sample YAML files be written?')
@click.option('--get-relatives/--no-relatives', default=False)
def by_tag(sample_tag, api_token, min_burst_remaining, sleep_secs, dest_dir, get_relatives):
    """Retrieve NEON's definition for one sample by tag. Requires sample class lookup. Saves result as YAML."""
    neon_classes = get_classes_from_sample_tag(sample_tag, api_token, verbose=True)
    sample_view = get_sample_view_from_tag_and_classes(sample_tag,
                                                       neon_classes,
                                                       min_burst_remaining=min_burst_remaining,
                                                       sleep_secs=sleep_secs,
                                                       api_token=api_token,
                                                       verbose=True)
    for sample_uuid, sample_obj in sample_view.items():
        written_file = write_yaml_from_sample_obj(sample_obj, dest_dir=dest_dir)
        if written_file:
            click.echo(f"Wrote {written_file[0]} as {written_file[1]}")
            if get_relatives:
                process_relatives(directory=dest_dir, extension=".yaml", min_burst_remaining=min_burst_remaining,
                                  sleep_secs=sleep_secs, api_token=api_token, verbose=True, dest_dir=dest_dir)
            else:
                click.echo("Won't get relatives")
        else:
            click.echo("Nothing written")


@cli.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt=True, help='The person to greet.')
def greet(count, name):
    """Greet someone multiple times."""
    for _ in range(count):
        click.echo(f'Hello, {name}!')


if __name__ == '__main__':
    cli()
