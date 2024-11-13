import json


def task() -> float:
    with open('input.json', 'r') as f:
        data = json.load(f)

    sum_products = 0
    for item in data:
        sum_products += item["score"]
        var = item["weight"]

    return round(sum_products, 3)


print(task())
