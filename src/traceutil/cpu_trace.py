from functools import wraps
from psutil import cpu_times

def cpu_trace(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        before = cpu_times()._asdict()
        result = func(*args, **kwargs)
        after = cpu_times()._asdict()

        increment = {}
        for key in after.keys():
            increment[key] = after[key] - before[key]
        total = sum(increment.values())
        rate = dict( (key, value / total ) for key, value in increment.items())
        print(rate)

        return result

    return wrapper
