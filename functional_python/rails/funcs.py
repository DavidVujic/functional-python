from typing import Callable

from functional_python.rails.result import Fail
from functional_python.rails.track import Track


def try_catch(fn, *args, **kwargs):
    try:
        return fn(*args, **kwargs)
    except Exception as e:
        return Fail(exception=e)


def true_false(fn, *args, **kwargs):
    res = fn(*args, **kwargs)

    return Fail() if res is False else res


def get_func(track: Track) -> Callable:
    return try_catch if track == Track.try_catch else true_false
