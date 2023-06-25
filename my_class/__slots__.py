class ParentClass:
    __slots__ = ("a", "b")

    def __init__(self, a, b):
        self.a = a
        self.b = b


class MyClass(ParentClass):
    __slots__ = ("c",)

    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c


obj = MyClass(1, 2, 3)
print(obj.a)
print(obj.b)
print(obj.c)
# print(obj.__dict__) نمیشود به خاطر اسلاتس دیکت را مشاهده و یا آرگومانی جز نعریف شده برای دیکت ایجاد کرد
