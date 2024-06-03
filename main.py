import json
import sys

from generic_validator import validate

rules = None
data = None
rules_json_path = None
data_json_path = None


def read_json_file(path):
    data = None
    try:
        with open(path, "r") as reader:
            data = json.loads(reader.read())
    except FileNotFoundError:
        print(f"{path} File Not Found")
    except:
        print(f"Error Reading the FIle {path}")

    return data


try:
    if sys.argv[1]:
        rules_json_path = sys.argv[1]
        rules = read_json_file(rules_json_path)
except:
    print("rules json file path missing")

try:
    if sys.argv[2]:
        data_json_path = sys.argv[2]
        data = read_json_file(data_json_path)
except:
    print("data json file path missing")

if rules and data:
    print(validate(rules, data))

# The following data has been converted to json format in rules.json and data.json files
rules = {
    "age": {"type": "int", "min": 18, "max": 40},
    "salary": {"type": "float", "min": 10000, "max": 50000},
    "name": {"type": "str", "min": 10, "max": 25},
    "location": {"type": "list", "length": {"min": 2, "max": 4}, "itemType": "str"},
    "hobbies": {"type": "list", "length": {"min": 1}, "itemType": "int"},
    "isWorkingYet": {"type": "bool", "value": True},
    "dictValue": {
        "type": "dict",
        "value": {
            "age": {"type": "int", "min": 18, "max": 40},
            "salary": {"type": "float", "min": 10000, "max": 50000},
            "name": {"type": "str", "min": 10, "max": 25},
            "location": {
                "type": "list",
                "length": {"min": 2, "max": 4},
                "itemtype": "str",
            },
            "hobbies": {"type": "list", "length": {"min": 1}, "itemType": "int"},
            "isWorkingYet": {"type": "bool", "value": True},
        },
    },
}

data = {
    "age": 23,
    "salary": 30000.0,
    "name": "Zishan Siddique",
    "location": ["Kathmandu", "Nepal"],
    "hobbies": [1, 2, 3],
    "isWorkingYet": False,
    "dictValue": {
        "age": 23,
        "salary": 30000.0,
        "name": "Zishan Siddique",
        "location": ["Kathmandu", "Nepal"],
        "hobbies": [1, 2, 3],
        "isWorkingYet": False,
    },
}
