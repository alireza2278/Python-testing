from functools import wraps
from functools import update_wrapper


def decorator(cls):
    @wraps(cls)
    def wrapper_decorator(*args, **kwargs):
        print("*"*19)
        v = cls(*args, **kwargs)
        print("+" * 19)
        return v

    return wrapper_decorator


@decorator
class Test:
    pass
# -------------------------------------------------


class MyClassDecorator:
    def __init__(self, func):
        update_wrapper(self, func)
        self.func = func

    def __call__(self):
        print("*" * 30)
        return self.func()


@MyClassDecorator
def my_func():
    """my func"""
    print("sasan")


my_func()

# ---------------------------------------------


class MyClassDecorator1:
    def __init__(self, cls):
        update_wrapper(self, cls)
        self.cls = cls

    def __call__(self):
        print("*" * 30)
        print(self.cls.__name__)
        oj = self.cls()
        print("*" * 30)
        return oj


@MyClassDecorator1
class Test1:
    pass


obj = Test1()
print(obj)
