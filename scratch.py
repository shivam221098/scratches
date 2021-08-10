import json


with open("scratch.json", "r", encoding="utf-8") as file:

    file_data = file.read()
    file_data = file_data.replace("'", '"')
    print(len(json.loads(file_data)))
