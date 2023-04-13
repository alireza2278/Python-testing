from time import perf_counter
import functools

def time_calculation(func):
    @functools.wraps(func)
    def wrapper_decorator(*args,**kwargs):
        start_time = perf_counter()
        value = func(*args,**kwargs)
        end_time = perf_counter()
        run_time = end_time - start_time
        print("the run time of",func.__name__,"is:",run_time)
        return value
    return wrapper_decorator