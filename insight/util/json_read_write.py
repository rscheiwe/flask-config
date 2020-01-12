import os
import json


def load_json(path):
    """Simple path execution to read json files
    """
    if os.path.exists(path):
        with open(path) as outfile:
            json_data = json.load(outfile)
            return json_data


def write_json_to_file(json_data, path):
    """Method to write json to file
    """
    if not os.path.exists(path):
        dir_path = os.path.dirname(path)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

    with open(path, 'w') as outfile:
        json.dump(json_data, outfile, indent=4)
