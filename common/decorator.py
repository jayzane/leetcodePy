import time
from functools import wraps


def time_func(func):
    """
    to print func consumed secs
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        t1: float = time.time()
        res: float = func(*args, **kwargs)
        t2: float = time.time()
        print('%s time consumed %.8f secs' % (func.__name__, t2 - t1))
        return res

    return wrapper
