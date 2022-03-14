import csv

from functional_python import railway


@railway.tracks
def _parse(path):
    with open(path, mode="r") as f:
        return list(csv.DictReader(f))


@railway.tracks
def _get_headers(data):
    return data[0].keys()


@railway.tracks_boolean
def _has_valid_headers(headers):
    true_or_false = map(lambda header: True if header else False, headers)

    return False not in set(true_or_false)


def comment():
    path = "./functional_python/rails_experiments/data.csv"
    data = _parse(path)
    headers = _get_headers(data)

    _has_valid_headers(headers)
