from typing import Any, Dict, Union
import sys
import json


def validate_type(value, type) -> bool:
    typeDict = {"int": int, "float": float, "bool": bool, "str": str, "list": list}
    inferredType = typeDict.get(type, False)
    if inferredType and isinstance(value, inferredType):
        return True

    return False


def range_validator(rule: Dict, value: Union[int, float]) -> bool:

    isMinValid = True
    isMaxValid = True

    if "min" in rule:
        isMinValid = value >= rule["min"]
    if "max" in rule:
        isMaxValid = value <= rule["max"]

    if isMinValid and isMaxValid:
        return True
   
    print(f"isMinValid: {isMinValid}")
    print(f"isMaxValid: {isMaxValid}")
    return False


def int_validator(rule: Dict, value: int) -> bool:
    if not validate_type(value, "int"):
        print("Invalid Type")
        return False
    return range_validator(rule, value)


def float_validator(rule: Dict, value: float) -> bool:
    if not validate_type(value, "float"):
        print("Invalid Type")
        return False
    return range_validator(rule, value)


def bool_validator(rule: Dict, value: bool) -> bool:
    if not validate_type(value, "bool"):
        print("Invalid Type")
        return False

    isBoolValid = True
    if "bool" in rule:
        isBoolValid = value == rule["value"]
    if isBoolValid:
        return True
    
    print(f"isBoolValid: {isBoolValid}")
    return False


def str_validator(rule: Dict, value: str) -> bool:
    if not validate_type(value, "str"):
        print("Invalid Type")
        return False

    return range_validator(rule, len(value))


def list_validator(rule: Dict, value: list) -> bool:
    if not validate_type(value, "list"):
        print("Invalid Type")
        return False

    isLenValid = True
    isItemTypeValid = True

    if "length" in rule:
        isLenValid = range_validator(rule["length"], len(value))

    if "itemType" in rule and len(value) > 0:
        for item in value:
            isItemTypeValid = validate_type(item, rule["itemType"])
            if not isItemTypeValid:
                break

    if isLenValid and isItemTypeValid:
        return True
    
    print(f"isLenValid: {isLenValid}")
    print(f"isItemTypeValid: {isItemTypeValid}")
    return False


def validator(rule: Dict, data: Any) -> bool:
    validatorDict = {
        "int": int_validator,
        "float": float_validator,
        "bool": bool_validator,
        "str": str_validator,
        "list": list_validator,
    }
    isTypeAvailable = rule["type"] in validatorDict

    if isTypeAvailable:
        validator_fn = validatorDict[rule["type"]]
        return validator_fn(rule, data)
    return True


def validate(rules: Dict, data: Dict):

    for field, rule in rules.items():
        print(f"validating {field}")
        if not field in data:
            print(f"field {field} doesn't exist in the data")
            return False
        if not validator(rule, data[field]):
            return False
        print(f"{field} is validated")
        print(" ")
    return True


rules = None
data = None
rules_json_path = None
data_json_path = None
print("hello")


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
}

data = {
    "age": 23,
    "salary": 30000.0,
    "name": "Zishan Siddique",
    "location": ["Kathmandu", "Nepal"],
    "hobbies": [1, 2, 3],
    "isWorkingYet": False,
}
