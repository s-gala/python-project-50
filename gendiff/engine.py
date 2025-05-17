import json


def generate_diff(path_to_file_json1, path_to_file_json2):
    data1 = json.load(open(path_to_file_json1))
    data2 = json.load(open(path_to_file_json2))
    data_sort1 = dict(sorted(data1.items()))
    data_sort2 = dict(sorted(data2.items()))  
    data_diff = {}

    for key in sorted((data_sort1 | data_sort2).keys()):
        if key in data_sort1 and key not in data_sort2:
            data_diff[f'- {key}'] = data_sort1[key]
        if key not in data_sort1 and key in data_sort2:
            data_diff[f'+ {key}'] = data_sort2[key]
        if key in data_sort1 and key in data_sort2:
            if data_sort1[key] == data_sort2[key]:
                data_diff[f'  {key}'] = data_sort1[key]
            else:
                data_diff[f'- {key}'] = data_sort1[key]
                data_diff[f'+ {key}'] = data_sort2[key]
    data_diff = str(data_diff)
    data_diff = data_diff.replace("'", "")
    data_diff = data_diff.replace(",", "\n ")
    data_diff = data_diff.replace("{", "{\n  ")
    data_diff = data_diff.replace("}", "\n  }")
    return (data_diff)
