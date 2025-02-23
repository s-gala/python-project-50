import json


def generate_diff(path_to_file_json1, path_to_file_json2):
    json_data1 = json.load(open(path_to_file_json1))
    json_data2 = json.load(open(path_to_file_json2))
    data1 = json.dumps(json_data1)
    data2 = json.dumps(json_data2)
    return data1, data2

