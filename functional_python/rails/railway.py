from enum import Enum
from typing import Callable

from functional_python.rails.result import Fail


class Track(Enum):
    try_catch = 1
    boolean = 2


def try_catch(fn, *args, **kwargs):
    try:
        return fn(*args, **kwargs)
    except Exception as e:
        return Fail(exception=e)


def true_false(fn, *args, **kwargs):
    res = fn(*args, **kwargs)

    return Fail() if res is False else res


def pick_adapter_fn(track: Track) -> Callable:
    return try_catch if track == Track.try_catch else true_false


def tracks(fn: Callable, track=Track.try_catch):
    "Wraps a plain function into a two-tracked function."

    def wrapper(fn, *args, **kwargs):
        if len(args) and isinstance(args[0], Fail):
            return args[0]

        adapter_fn = pick_adapter_fn(track)

        return adapter_fn(fn, *args, **kwargs)

    return wrapper
