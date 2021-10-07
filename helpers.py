from urllib.request import urlopen
from collections.abc import Iterable


def slurp(url: str) -> str:
    return urlopen(url).read().decode("utf-8")


def to_lower(coll: list[str]) -> Iterable[str]:
    return map(lambda s: s.lower(), coll)
