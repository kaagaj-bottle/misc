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


def int_float_validator(rule: Dict, value: Union[int, float]) -> bool:
    return range_validator(rule, value)


def bool_validator(rule: Dict, value: bool) -> bool:

    isBoolValid = True
    if "bool" in rule:
        isBoolValid = value == rule["value"]
    if isBoolValid:
        return True

    print(f"isBoolValid: {isBoolValid}")
    return False


def str_validator(rule: Dict, value: str) -> bool:
    return range_validator(rule, len(value))


def list_validator(rule: Dict, value: list) -> bool:
    isLenValid = True
    isItemTypeValid = True

    if "length" in rule:
        isLenValid = range_validator(rule["length"], len(value))

    if "itemType" in rule and len(value) > 0:
        for item in value:
            isItemTypeValid = validate_type(rule["itemType"], item)
            if not isItemTypeValid:
                break

    if isLenValid and isItemTypeValid:
        return True

    print(f"isLenValid: {isLenValid}")
    print(f"isItemTypeValid: {isItemTypeValid}")
    return False


def dict_validator(rule: Dict, value: Dict) -> bool:
    return validate(rule["value"], value)


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
