import csv
import sys

data1 = {
    "District": "KPI_1",
    "Kathmandu": 0.8,
    "Dhanusa": 0.85,
    "Kavre palanchowk": 0.75,
}
data2 = {
    "District": "KPI_2",
    "Kathmandu": 0.35,
    "Kavrepalanchowk": 0.65,
    "Dhanusha": 0.6,
}


def euclideanDistance(a: str, b: str) -> int:
    a = a.replace(" ", "").lower()
    b = b.replace(" ", "").lower()
    distance = 0
    n = min(len(a), len(b))
    for i in range(n):
        distance += (ord(a[i]) - ord(b[i])) ** 2

    return distance


def findSimilarKey(key, data2_keys):

    minDistance = sys.maxsize
    idx = 0

    for i in range(len(data2_keys)):
        distance = euclideanDistance(key, data2_keys[i])

        if distance < minDistance:
            idx = i
            minDistance = distance
    return data2_keys[idx]


def merge(data1: dict, data2: dict):
    data2_keys = list(data2.keys())
    result = []

    for key, _ in data1.items():
        if key in data2:
            result.append([key, data1[key], data2[key]])
            continue
        similarKey = findSimilarKey(key, data2_keys)
        result.append([key, data1[key], data2[similarKey]])

    return result


def write_to_csv(data):
    with open("districtKPI.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows(data)


write_to_csv(merge(data1, data2))
