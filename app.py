import os
import json

directory = os.path.join(os.path.dirname(__file__), 'data')
files = os.listdir(directory)
result = {}
key_to_extract = "MEANINGS"
file_name = 'result3.json'

def get_value(obj, key_to_extract):
    result = {}
    for key in obj:
        if key_to_extract in obj[key]:
            result[key] = [word.lower() for word in obj[key][key_to_extract] if word.lower() != key.lower()]
    return result

if isinstance(files, list):
    for file in files:
        with open(os.path.join(directory, file)) as f:
            file_data = json.loads(f.read())
            result = {**result, **get_value(file_data, key_to_extract)}

print("Working...")

with open(os.path.join(os.path.dirname(__file__), file_name), 'w') as f:
    json.dump(result, f, indent=2)

print("Done.")
