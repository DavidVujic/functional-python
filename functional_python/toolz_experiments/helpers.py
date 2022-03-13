from urllib.request import urlopen


def slurp(url: str) -> str:
    with urlopen(url) as response:
        return response.read().decode("utf-8")
