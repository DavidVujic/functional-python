def add_things(data: dict) -> dict:
    data["hello"] = "world"

    return data


my_data = {"name": "David"}

res = add_things(my_data)

print(res)
