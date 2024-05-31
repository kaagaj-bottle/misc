from typing import Any, Dict
import sys

rules = {
    "age": {"type": int, "min": 18, "max": 40},
    "salary": {"type": float, "min": 10000, "max": 50000},
    "name": {"type": str, "min": 10, "max": 25},
}

data = {
    "age": 23,
    "salary": 30000,
    "name": "Zishan Siddique",
    "location": ["Kathmandu", "Nepal"],
}


def validate_type(value, type) -> bool:
    isValid = False
    if type == "int":
        return isinstance(value, int) and not isinstance(value, bool)
    elif type == "float":
        return isinstance(value, float)
    elif type == "bool":
        return isinstance(value, bool)
    elif type == "str":
        return isinstance(value, str)
    elif type == "list":
        return isinstance(value, list)
    else:
        return False


def int_validator(rule: Dict, value: int) -> bool:
    if not validate_type(value, "int"):
        print("Invalid Type")
        return False

    isMinValid = value >= rule.get("min", -sys.maxsize)
    isMaxValid = value <= rule.get("max", sys.maxsize)
    if isMinValid and isMaxValid:
        return True
    else:
        print(f"isMinValid: {isMinValid}")
        print(f"isMaxValid: {isMaxValid}")
        return False


def float_validator(rule: Dict, value: float) -> bool:
    if not validate_type(value, "float"):
        print("Invalid Type")
        return False

    isMinValid = value >= rule.get("min", -sys.maxsize)
    isMaxValid = value <= rule.get("max", sys.maxsize)
    if isMinValid and isMaxValid:
        return True
    else:
        print(f"isMinValid: {isMinValid}")
        print(f"isMaxValid: {isMaxValid}")
        return False


def bool_validator(rule: Dict, value: bool) -> bool:
    if not validate_type(value, "bool"):
        print("Invalid Type")
        return False

    isBoolValid = True
    if "bool" in rule:
        isBoolValid = value == rule["value"]
    if isBoolValid:
        return True
    else:
        print(f"isBoolValid: {isBoolValid}")
        return False


def str_validator(rule: Dict, value: str) -> bool:
    if not validate_type(value, "str"):
        print("Invalid Type")
        return False

    isMinValid = len(value) >= rule.get("min", 0)
    isMaxValid = True
    if "max" in rule:
        isMaxValid = len(value) <= rule["max"]

    if isMinValid and isMinValid:
        return True
    else:
        print(f"isMinValid: {isMinValid}")
        print(f"isMaxValid: {isMaxValid}")
        return False


def list_validator(rule: Dict, value: list) -> bool:
    if not validate_type(value, "list"):
        print("Invalid Type")
        return False

    isLenValid = True
    isItemTypeValid = True
    if "length" in rule:
        minLen = rule["length"].get("min", 0)
        maxLen = rule["length"].get("max", -1)
        isLenValid = len(value) >= minLen and (len(value) <= maxLen or maxLen == -1)
    if "itemType" in rule and len(value) > 0:
        for item in value:
            isItemTypeValid = validate_type(item, rule["itemType"])
            if not isItemTypeValid:
                break

    if isLenValid and isItemTypeValid:
        return True
    else:
        print(f"isLenValid: {isLenValid}")
        print(f"isItemTypeValid: {isItemTypeValid}")
        return False


def validator(rule: Dict, data: Any) -> bool:
    if rule["type"] == "int":
        return int_validator(rule, data)
    if rule["type"] == "float":
        return float_validator(rule, data)
    elif rule["type"] == "bool":
        return bool_validator(rule, data)
    elif rule["type"] == "str":
        return str_validator(rule, data)
    elif rule["type"] == "list":
        return list_validator(rule, data)
    else:
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
