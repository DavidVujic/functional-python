def transform(data: dict) -> dict:
    del data["id"]

    return data


def transform_alt(data: dict) -> dict:
    d = {"name": data["name"], "value": data["value"]}

    return d


my_data = {"id": 1, "name": "hello", "value": "world"}

res = transform(my_data)

print(res)
