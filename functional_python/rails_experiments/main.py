import csv


def is_valid_csv(path: str) -> bool:
    with open(path, mode="r") as f:
        data = list(csv.DictReader(f))

    headers = data[0].keys()

    is_valid = True

    for header in headers:
        if not header:
            is_valid = False
            break

    return is_valid


is_valid_csv("./functional_python/rails_experiments/data.csv")
