x = int(input("x: "))
y = int(input("y: "))
op = input("op: ")

# if op == "+":
#     print(x+y)
# elif op == "-":
#     print(x-y)
# elif op == "*":
#     print(x*y)
# elif op == "/":
#     print(x/y)
# else:
#     print("Invalid operator!")
match op:
    case "+":
        print(x+y)
    case "-":
        print(x-y)
    case "*":
        print(x*y)
    case "/":
        print(x/y)
    case _:
        print("Invalid operator!")

# ------------------------------------------------

from random import randint

x = randint(1, 6)
y = randint(1, 6)
print(x, y)
match (x, y):
    case (6, 6):
        print("win")
    case (1, 1):
        print("lost")
    case (6, y) if 1 <= x <= 6 and 1 <= y <= 6:
        print("repeat")
    case (x, 6) if 1 <= x <= 6 and 1 <= y <= 6:
        print("repeat")
    case (x, y) if 1 <= x <= 6 and 1 <= y <= 6:
        print("next player")
    case _:
        print("Error")
