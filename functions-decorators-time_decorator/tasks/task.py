import time
from typing import Dict
from functools import wraps

execution_time: Dict[str, float] = {}


def time_decorator(fn):
    """
    Create a decorator function `time_decorator`
    which has to calculate decorated function execution time
    and put this time value to `execution_time` dictionary where `key` is
    decorated function name and `value` is this function execution time.
    """
    @wraps(fn)
    def wrapper(*args, **kwargs):
        global execution_time
        t_start = time.time()
        res = fn(*args, **kwargs)
        t_finish = time.time()
        execution_time[fn.__name__] = t_finish - t_start
        return res
    return wrapper



@time_decorator
def func_add(a, b):
    time.sleep(0.2)
    return a + b

