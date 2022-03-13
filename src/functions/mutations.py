def bad_example(data: dict) -> dict:
    data["hello"] = "world"

    return data


def good_example(data: dict) -> dict:
    return data | {"hello": "world"}
