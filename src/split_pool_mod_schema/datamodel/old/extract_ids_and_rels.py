import yaml

neon_sample_degree_file = "everything-degree-3.yaml"

# Open the YAML file
with open(neon_sample_degree_file, 'r') as stream:
    try:
        # Load the YAML content into a dictionary
        data = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)
