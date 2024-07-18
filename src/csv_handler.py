import json
import pandas as pd


def handle(path: str) -> str:
    file = open(path)
    data = json.load(file)
    key_val = get_key_value(data, {}, [], 0)   
    file_path = 'data.json'
    
    
    
    pd.DataFrame(get_csv_friendly_values(key_val)).to_csv('dict_file.csv', header=True)

    with open(file_path, 'w') as json_file:
        json.dump(key_val, json_file, indent=4)
    return ""

def get_csv_friendly_values(data: dict) -> list:
    values = []
    for key, value  in zip(data.keys(), data.values()):
        values.append(dict(key=key,en=value,sw='',fr='',de='',ar=''))
    return values


def get_key_value(data: dict, le_dict: dict, previous_keys, level) -> dict:
    level = level + 1 
    for key, value  in zip(data.keys(), data.values()):
        previous_keys.append(key)
        if isinstance(value, dict):
            get_key_value(value, le_dict, previous_keys, level)
        else:
            concated_keys = ".".join(previous_keys[-level:])
            le_dict[concated_keys] = value
            previous_keys.pop()
                    
             
           
    return le_dict       
           
           