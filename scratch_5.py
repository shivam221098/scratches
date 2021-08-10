import json
import time
from pprint import pprint
import re


def remove_special_symbols(dictionary: dict) -> None:
    keys = frozenset(dictionary.keys())
    for key in keys:
        value = dictionary.get(key)
        if isinstance(value, dict):
            remove_special_symbols(value)

        elif isinstance(value, list):
            for list_dict in value:
                if isinstance(list_dict, dict):
                    remove_special_symbols(list_dict)

        dict_value = dictionary.pop(key)
        # my_new_string = re.sub('[^a-zA-Z0-9 \n\.]', '', my_str)
        new_key = re.sub('[^a-zA-Z0-9 \n\.]', '_', key)
        new_key = re.sub("[0-9]", "", new_key)
        dictionary.update({new_key: dict_value})
        # pprint(dictionary)


with open("testing5.json", "r", encoding="utf-8") as file:
    data = json.loads(file.read())

    start = time.time()
    remove_special_symbols(data)
    print(f"Time taken to remove: {time.time() - start}")

with open("testing6.json", "w", encoding="utf-8") as file:
    file.write(json.dumps(data, indent=4))