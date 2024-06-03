from typing import Any, Dict, Union
import sys
import json


def validate_type(value, type) -> bool:
    typeDict = {
        "int": int,
        "float": float,
        "bool": bool,
        "str": str,
        "list": list,
        "dict": dict,
    }
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


def int_float_validator(rule: Dict, value: Union[int, float], type) -> bool:
    if not validate_type(value, type):
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


def dict_validator(rule: Dict, value: Dict) -> bool:
    if not validate_type(rule, "dict"):
        print("Invalid Type")
        return False
    return validate(rule["value"], value)


def validator(rule: Dict, data: Any) -> bool:
    validatorDict = {
        "int": lambda rule, data: int_float_validator(rule, data, "int"),
        "float": lambda rule, data: int_float_validator(rule, data, "float"),
        "bool": bool_validator,
        "str": str_validator,
        "list": list_validator,
        "dict": dict_validator,
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
