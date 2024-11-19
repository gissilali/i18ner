import json
import pandas as pd


def handle(path: str, save_to_json: bool = False):
    file = open(path)
    data = json.load(file)
    translation_key_value_pair = get_translation_key_value_pair(data, {}, None)
    # print(translation_key_value_pair)
    if save_to_json:
        write_to_json_file("en-flattened.json", translation_key_value_pair)  
    pd.DataFrame(transform_to_csv_friendly_list(translation_key_value_pair)).to_csv('dict_file.csv', header=True)

def transform_to_csv_friendly_list(data: dict) -> list:
    values = []
    for key, value  in zip(data.keys(), data.values()):
        values.append(dict(key=key,en=value,sw='',fr='',de='',ar=''))
    return values

def write_to_json_file(filename: str, data: any):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)


def get_translation_key_value_pair(data: dict, translation_key_value_pair: dict, previous_keys: list) -> dict:
    if previous_keys == None:
        previous_keys = []
    for key, value in zip(data.keys(), data.values()):
        if isinstance(value, str):
            translation_key_value_pair['.'.join(previous_keys + [key])] = value
        else:
            get_translation_key_value_pair(value, translation_key_value_pair, previous_keys + [key])
                    
    return translation_key_value_pair    