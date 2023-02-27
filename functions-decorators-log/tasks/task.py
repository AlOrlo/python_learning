import time
from functools import wraps


def log(fn):
    """
    Add your code here or call it from here   
    """
    @wraps(fn)
    def wrapper(*args, **kwargs):
        exec_time: Dict[str, float] = {}
        start_time = time.time()
        result = fn(*args, **kwargs)
        exec_time[fn.__name__] = time.time() - start_time
        with open('log.txt', 'a') as f:
            f.write(fn.__name__)
            f.write('; ')
            if args:
                a1 = 'args: '
                res = dict(zip(list(map(chr, range(97, 123))), [i for i in args]))
                for i in res:
                    a1 += f'{i}=' + str(res[i]) + str(', ')
                a1 = a1[:-2] + '; '
                f.write(a1)
            if kwargs:
                k1 = 'kwargs: '
                for i in kwargs:
                    k1 += f'{i}=' + str(kwargs[i]) + str(', ')
                k1 = k1[:-2] + '; '
                f.write(k1)
            w = 'execution_time: ' + str(round(exec_time[fn.__name__], 2)) + ' sec.'
            f.write(w + '\n')
        return result
    return wrapper