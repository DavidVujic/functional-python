from functional_python.railway.result import Fail


def try_catch(fn, *args, **kwargs):
    try:
        return fn(*args, **kwargs)
    except Exception as e:
        return Fail(exception=e, args=args, kwargs=kwargs)


def true_false(fn, *args, **kwargs):
    res = fn(*args, **kwargs)

    return Fail() if res is False else res
