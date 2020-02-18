import os
from insight.util.json_read_write import load_json


def path_finder(config_type):
    if config_type == 'swagger':
        try:
            abs_path = os.path.abspath('.')
            path_to_file = os.path.join(abs_path, "config/_swagger.json")
            swagger_data = load_json(path_to_file)
            return swagger_data
        except RuntimeError:
            raise RuntimeError("path not resolving")
    elif config_type == 'vertica':
        try:
            abs_path = os.path.abspath('.')
            path_to_file = os.path.join(abs_path, "config/db_config.json")
            config_data = load_json(path_to_file)
            return config_data
        except RuntimeError:
            raise RuntimeError("path not resolving")
    elif config_type == 'desktop_traffic':
        try:
            abs_path = os.path.abspath('.')
            path_to_file = os.path.join(abs_path, "config/desktop_traffic.json")
            config_data = load_json(path_to_file)
            return config_data
        except RuntimeError:
            raise RuntimeError("path not resolving")
    elif config_type == 'desktop_sdk_traffic':
        try:
            abs_path = os.path.abspath('.')
            path_to_file = os.path.join(abs_path, "config/desktop_sdk_traffic.json")
            config_data = load_json(path_to_file)
            return config_data
        except RuntimeError:
            raise RuntimeError("path not resolving")


# if __name__ == '__main__':
#     dum = path_finder('desktop_sdk_traffic')
#     print(dum)
