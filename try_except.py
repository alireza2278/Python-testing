try:
    x = int(input("x: "))
    y = int(input("y: "))
    z = x / y + "y"
except(ZeroDivisionError, ValueError) as F:
    print(F.__class__.__name__)

except TypeError:
    print("TypeError")

except Exception as Ex:
    print(Ex.__class__.__name__)

print("end")
#----------------------------------------


def div(q, r, z):
    try:
        f = q + r
        result = f / z

# مدریت خطا برای تایپ ارور
    except TypeError as Ty:
        print(Ty.__class__.__name__)

# مدریت خطا برای مخرج صفر تقسیم
    except ZeroDivisionError as zde:
        print(zde.__class__.__name__)

# زمانی اجرا میشود ک ترای بدون هیچ خطا انجام شود
    else:
        print(result)
#  صد در اجرا میشود در هر حالت حتی با وجود خطا یا ریترن در قسمت ترای و ریترن ترای حذف میشود
    finally:
        print("Ok")


def func():
    try:
        a = int(input("a: "))
        b = int(input("b: "))
        c = int(input("c: "))
        div(a, b, c)
    except ValueError as va:
        print("**", va.__class__.__name__)
# اگر تابع دیو مدریت خطا مخرج صفر نداشته باشد میآید این تابع را نیز برای مدریت خطا برسی میکند
    except ZeroDivisionError:
        print("Error")


func()
#-------------------------------


#ایجاد استثنا دستی , (raise)کردن استثنا
def sol(x, y, z):
    if z == 0:
        raise ZeroDivisionError("No Enter zero")
    s = x+y
    d = s / z
    print(d)


sol(4, 2, 0)

