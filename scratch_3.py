import json
import time
from pprint import pprint
from xmltodict import parse

# pprint(x.get("record:record").get("common:orcid-identifier"))
# pprint(x.get("record:record").get("history:history"))

start = time.time()
with open("xmls/000.xml", "r", encoding="utf-8") as file:
    data = parse(file.read())
print("Read file time: {}".format(time.time() - start))
start1 = time.time()
with open("testing5.json", "w", encoding="utf-8") as file:
    file.write(json.dumps(data, indent=4))

print("Write file time: {}".format(time.time() - start1))
print("Total execution time: {}".format(time.time() - start))