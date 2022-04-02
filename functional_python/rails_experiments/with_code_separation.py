import csv


def parse(path):
    with open(path, mode="r") as f:
        return list(csv.DictReader(f))


def get_headers(data):
    return data[0].keys()


def has_valid_headers(headers):
    is_valid = True

    for header in headers:
        if not header:
            is_valid = False
            break

    return is_valid


def is_valid_csv(path) -> bool:
    data = parse(path)
    headers = get_headers(data)

    res = has_valid_headers(headers)

    return res


path = "./functional_python/rails_experiments/data.csv"
is_valid_csv(path)
