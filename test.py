def func(x, y, n):
    try:
        s = x + y
        result = s / n
        print(result)
    except TypeError as Ty:
        print(Ty.__class__.__name__)
    except ZeroDivisionError as ZDE:
        print(ZDE.__class__.__name__)


func(4, 2, "0")