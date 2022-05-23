import csv


def parse(path):
    try:
        with open(path, mode="r") as f:
            return list(csv.DictReader(f))
    except Exception:
        return None


def get_headers(data):
    try:
        return data[0].keys()
    except Exception:
        return None


def has_valid_headers(headers):
    try:
        is_valid = True

        for header in headers:
            if not header:
                is_valid = False
                break

            return is_valid
    except Exception:
        return False


def is_valid_csv(path) -> bool:
    data = parse(path)
    headers = get_headers(data)

    res = has_valid_headers(headers)

    return res


path = "./functional_python/rails_experiments/data.csv"
is_valid_csv(path)
