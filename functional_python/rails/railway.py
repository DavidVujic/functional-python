from typing import Callable

from functional_python.rails.funcs import get_func
from functional_python.rails.result import failed
from functional_python.rails.track import Track


def tracks(fn: Callable, track=Track.try_catch):
    "Wraps a plain function into a two-tracked function."

    def wrapper(fn, *args, **kwargs):
        if len(args) and failed(args[0]):
            return args[0]

        rail_fn = get_func(track)

        return rail_fn(fn, *args, **kwargs)

    return wrapper
