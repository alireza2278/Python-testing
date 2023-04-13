#  نمونه های comprehension
# ---------------------------------1-----------------
# جدول ماتریکس
print("--"*20)

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
# --------------------------------------------------
s = []
for i in range(4):
    row = []
    for j in matrix:
        row.append(j[i])
    s.append(row)
for g in s:
    print(g)
# --------------------------------------------------
print("--"*20)

ls = [[j[i]for j in matrix] for i in range(4)]
for g in ls:
    print(g)
# --------------------------------------------------
print("--"*20)
l = list(zip(*matrix))
for g in l:
    print(g)
# ---------------------------------2-----------------
# ساخت اعداد تصادفی بالای 100
from random import randrange
def func():
    return randrange(50,150)

ls = [x for i in range(10) if (x:= func()) > 100]
print(ls)
# ---------------------------------3-----------------
