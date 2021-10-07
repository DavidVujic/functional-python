from urllib.request import urlopen


def slurp(url: str) -> str:
    return urlopen(url).read().decode("utf-8")


def lower(s: str) -> str:
    return s.lower()
