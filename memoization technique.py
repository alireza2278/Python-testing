import functools

def decorator(func):
    memory = {}
    @functools.wraps(func)
    def wrapper_decorator(x):
        if x not in memory:
            memory[x] = func(x)
        return memory[x]
    return wrapper_decorator



@decorator
def fib(x):
    if x == 0 or x == 1:
        return x
    return fib(x-1) + fib(x-2)
print(fib(450))
