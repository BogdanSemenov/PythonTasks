import functools
from collections import OrderedDict


def cache(n):
    a = OrderedDict()

    def wrap(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = args + tuple((kwargs.items()))
            if key not in a and len(a) < n:
                a[key] = func(*args, **kwargs)
            elif key not in a and len(a) >= n:
                a.popitem(last=False)
                a[key] = func(*args, **kwargs)
            return a[key]
        return wrapper
    return wrap