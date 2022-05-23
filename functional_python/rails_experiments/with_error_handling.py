import csv


def is_valid_csv(path: str) -> bool:
    try:
        with open(path, mode="r") as f:
            data = list(csv.DictReader(f))
    except Exception:
        return False

    try:
        headers = data[0].keys()
    except Exception:
        return False

    is_valid = True

    try:
        for header in headers:
            if not header:
                is_valid = False
                break

        return is_valid
    except Exception:
        return False


path = "./functional_python/rails_experiments/data.csv"
is_valid_csv(path)
