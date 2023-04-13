# -------------------1-----------------------
# شبیه ساز enumerate با ژنراتور
# lst = ["neda", "ali", "sasan", ]
#
# def Enumerate(seuence,start=0):
#     a = start
#     for i in seuence:
#         yield a, i
#         a += 1
#
#
# for i, j in Enumerate(lst):
#     print(i, j)

# -------------------2-----------------------
# ژنراتور برای تولید دنباله فیبوناچی
# def fibonachi():
#     f1 = 0
#     yield f1
#     f2 = 1
#     yield f2
#     while True:
#         f3 = f1 + f2
#         yield f3
#         f1 = f2
#         f2 = f3
# f = fibonachi()
# for _ in range(100):
#     print(next(f))
# -------------------3-----------------------
# ژنراتور جمع عناصر یک لیست(هر بار یک عنصر جدید جمع شود)
# def sum_gen(lst):
#     Sum = 0
#     for i in lst:
#         Sum += i
#         yield Sum
#
# l = [1, 2, 3, 4, 5,6]
# s_g = sum_gen(l)
# for i in s_g:
#     print(i)
# -------------------4-----------------------
# ژنراتور معکوس کننده رشته(هر بار یک کاراکتر)
# def rev_string(s):
#     f = len(s)
#     for i in range(f-1,-1,-1):
#         yield s[i]
#
# str = "hadis"
# rev = rev_string(str)
# for ch in rev:
#     print(ch)
# -------------------5-----------------------
#  ژتراتور بی نهایت از اعداد زوج یا فرد
# def gen(even_our_odd="e"):
#     start = 0
#     if even_our_odd == "o":
#         start = 1
#     while True:
#         yield start
#         start+=2
#
# ali = gen("o")
# for i in range(10):
#     print(next(ali))
# -------------------6-----------------------
# ژنراتور چاپ نوعی خروجی خاص (1   2 2   3 3 3 و...)
def print_number():
    c = 1
    while True:
        s = ""
        for i in range(1,c+1):
            s += f"{c}\t"
        yield s
        c += 1

n = print_number()
for i in range(10):
    print(next(n))

