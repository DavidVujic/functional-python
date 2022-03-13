from dataclasses import dataclass


@dataclass
class Fail:
    exception: Exception | None = None


def failed(res) -> bool:
    return isinstance(res, Fail)


def succeeded(res) -> bool:
    return not failed(res)
