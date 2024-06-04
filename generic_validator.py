from typing import Any, Dict, Union


def logger(logs: dict) -> None:
    for key, value in logs.items():
        print(f"{key}: {value}")


def validate_type(type, value) -> bool:
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
    print("Invalid Type")
    return False


def range_validator(rule: Dict, value: Union[int, float]) -> bool:

    checkConditions = {
        "min": True,
        "max": True,
    }

    if "min" in rule:
        checkConditions["min"] = value >= rule["min"]
    if "max" in rule:
        checkConditions["max"] = value <= rule["max"]

    if all(val == True for val in checkConditions.values()):
        return True

    logger(checkConditions)
    return False


# def int_float_validator(rule: Dict, value: Union[int, float]) -> bool:
#     return range_validator(rule, value)
int_float_validator = lambda rule, value: range_validator(rule, value)


def bool_validator(rule: Dict, value: bool) -> bool:

    checkConditions = {"value": True}
    if "value" in rule:
        checkConditions["value"] = value == rule["value"]

    if all(val == True for val in checkConditions.values()):
        return True

    logger(checkConditions)
    return False


# def str_validator(rule: Dict, value: str) -> bool:
#     return range_validator(rule, len(value))
str_validator = lambda rule, value: range_validator(rule, len(value))


def list_validator(rule: Dict, value: list) -> bool:
    checkConditions = {"length": True, "itemType": True}

    if "length" in rule:
        checkConditions["length"] = range_validator(rule["length"], len(value))

    if "itemType" in rule and len(value) > 0:
        for item in value:
            checkConditions["itemType"] = validate_type(rule["itemType"], item)
            if not checkConditions["itemType"]:
                break

    if all(val == True for val in checkConditions.values()):
        return True

    logger(checkConditions)
    return False


# def dict_validator(rule: Dict, value: Dict) -> bool:
#     return validate(rule["value"], value)
dict_validator = lambda rule, value: validate(rule["value"], value)


def validator(rule: Dict, data: Any) -> bool:
    if not validate_type(rule["type"], data):
        return False

    validatorDict = {
        "int": int_float_validator,
        "float": int_float_validator,
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
