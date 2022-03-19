import csv

from functional_python import railway


@railway.tracks
def parse(path):
    with open(path, mode="r") as f:
        return list(csv.DictReader(f))


@railway.tracks
def get_headers(data):
    return data[0].keys()


@railway.tracks_boolean
def has_valid_headers(headers):
    true_or_false = map(lambda header: True if header else False, headers)

    return False not in set(true_or_false)


def comment():
    path = "./functional_python/rails_experiments/data.csv"
    data = parse(path)
    headers = get_headers(data)

    res = has_valid_headers(headers)

    railway.succeeded(res)
