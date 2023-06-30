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
