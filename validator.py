from typing import Dict


def str_validator(value, rule):
    isMinValid = True
    isMaxValid = True
    if "min" in rule:
        isMinValid = len(value) >= rule["min"]
    if "max" in rule:
        isMaxValid = len(value) <= rule["max"]
    return isMaxValid and isMinValid


def bool_validator(value, rule):
    isBoolValid = True
    if "bool" in rule:
        isBoolValid = value == rule["value"]
    return isBoolValid


def int_validator(value, rule):
    isMinValid = True
    isMaxValid = True
    if "min" in rule:
        isMinValid = value >= rule["min"]
    if "max" in rule:
        isMaxValid = value <= rule["max"]
    return isMinValid and isMaxValid


def list_length_validator(value, rule):
    isLenValid = True
    max_len = rule.get("max", -1)
    min_len = rule.get("min", 0)
    isLenValid = len(value) >= min_len and (len(value) < max_len or max_len == -1)

    return isLenValid


def salary_validator(value, rule):
    if not (isinstance(value, int) or isinstance(value, float)):
        return False
    return int_validator(value, rule)


def name_validator(value, rule):
    if not isinstance(value, str):
        return False
    return str_validator(value, rule)
    # isMinValid = True # checking min length
    # isMaxValid = True # checking max length
    # if "min" in rule:
    #     isMinValid = len(value) >= rule["min"]
    # if "max" in rule:
    #     isMaxValid = len(value) <= rule["max"]
    # return isMaxValid and isMinValid


def working_yet_validator(value, rule):
    if not isinstance(value, bool):
        print("not of type bool")
        return False
    isBoolValid = value == rule.get("value", True)
    return isBoolValid


def location_validator(value, rule):
    if not isinstance(value, list):  # location value must be in list format
        return False
    if (
        not len(value) == 2
    ):  # there must be two values in list 0th value for district and 1st value for country
        return False
    isDistrictValid = False
    isCountryValid = False
    if isinstance(value[0], str) and isinstance(value[1], str):
        district = value[0]
        country = value[1]
        isDistrictValid = str_validator(district, rule["district"])
        isCountryValid = str_validator(country, rule["country"])
        # districtLen=len(value[0])
        # countryLen=len(value[1])
        # isDistrictValid=districtLen>=rule["district"]["min"] and districtLen<=rule["district"]["max"]
        # isCountryValid=countryLen>=rule["country"]["min"] and countryLen<=rule["country"]["max"]
        return isDistrictValid and isCountryValid
    else:
        return False


def hobbies_validator(value, rule):
    if not isinstance(value, list):
        return False
    if not list_length_validator(value, rule["length"]):
        return False
    for hobby in value:
        if not isinstance(hobby, str) or not str_validator(hobby, rule["hobbyLength"]):
            return False
    return True


def education_validator(value, rule):
    if not isinstance(value, list):
        return False
    # basically the education should be more than the number of degrees required
    if not list_length_validator(value, rule["length"]):
        return False
    for degree in value:
        if not isinstance(degree, str) or not str_validator(
            degree, rule["degreeLength"]
        ):  # checking length of degree string
            return False

    return True


def feedback_validator(value, rule):
    if not isinstance(value, str):
        return False
    return str_validator(value, rule)


def validator(data: Dict, rules: Dict) -> bool:
    isFullNameValid = False
    isSalaryValid = False
    isWorkingYetValid = False
    isLocationValid = False
    isHobbiesValid = False
    isEducationValid = False
    isFeedbackValid = True  # is optional but if the value is used than the value must be validated against the provided rule

    for key, value in data.items():
        if key == "fullName":
            isFullNameValid = name_validator(value, rules["fullName"])
        elif key == "salary":
            isSalaryValid = salary_validator(value, rules["salary"])
        elif key == "isWorkingYet":
            isWorkingYetValid = working_yet_validator(value, rules["isWorkingYet"])
        elif key == "location":
            isLocationValid = location_validator(value, rules["location"])
        elif key == "hobbies":
            isHobbiesValid = hobbies_validator(value, rules["hobbies"])
        elif key == "education":
            isEducationValid = education_validator(value, rules["education"])
        elif key == "feedback":
            isFeedbackValid = feedback_validator(value, rules["feedback"])
        else:
            return False

    if (
        isFullNameValid
        and isSalaryValid
        and isWorkingYetValid
        and isLocationValid
        and isHobbiesValid
        and isEducationValid
        and isFeedbackValid
    ):
        return True
    else:
        print(f"isFullNameValid: {isFullNameValid}")
        print(f"isSalaryValid: {isSalaryValid}")
        print(f"isWorkingYetValid: {isWorkingYetValid}")
        print(f"isLocationValid: {isLocationValid}")
        print(f"isHobbiesValid: {isHobbiesValid}")
        print(f"isEducationValid:{isEducationValid}")
        print(f"isFeedbackValid: {isFeedbackValid}")
        return False


rules = {
    "fullName": {"min": 5, "max": 30},
    "salary": {"min": 1000, "max": 3000},
    "isWorkingYet": {"value": True},
    "location": {"district": {"min": 4, "max": 30}, "country": {"min": 3, "max": 40}},
    "hobbies": {"length": {"min": 2, "max": 5}, "hobbyLength": {"min": 4, "max": 30}},
    "education": {
        "length": {"min": 1, "max": 5},
        "degreeLength": {"min": 2, "max": 50},
    },
    "feedback": {"min": 20, "max": 100},
}

data = {
    "fullName": "Paul Call",
    "salary": 2000,
    "isWorkingYet": True,
    "location": ["Kathmandu", "Nepal"],
    "hobbies": ["baseball", "Football"],
    "education": ["SLC", "+2"],
    "feedback": "Hello, World This is my name",
}

validator(data=data, rules=rules)
