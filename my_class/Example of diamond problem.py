from pprint import pprint


class BaceClass:
    num_base_calls = 0

    def __init__(self, a, b, **kwargs):
        self.a = a
        self.b = b

    def call_me(self):
        print("calling method on BaceClass")
        self.num_base_calls += 1


class LeftSubClass(BaceClass):
    num_left_calls = 0

    def __init__(self, c, **kwargs):
        super().__init__(**kwargs)
        self.c = c

    def call_me(self):
        super().call_me()
        print("calling method on LeftSubClass")
        self.num_left_calls += 1


class RightSubClass(BaceClass):
    num_right_calls = 0

    def __init__(self, d, e, f, **kwargs):
        super().__init__(**kwargs)
        self.d = d
        self.e = e
        self.f = f

    def call_me(self):
        super().call_me()
        print("calling method on RightSubClass")
        self.num_right_calls += 1


class SubClass(LeftSubClass, RightSubClass):
    num_sub_calls = 0

    def __init__(self, g, **kwargs):
        super().__init__(**kwargs)
        self.g = g

    def call_me(self):
        super().call_me()
        print("calling method on SubClass")
        self.num_sub_calls += 1


s = SubClass(a=1, b=2, c=3, d=4, e=5, f=6, g=7)
s.call_me()
print(s.num_sub_calls, s.num_left_calls, s.num_right_calls, s.num_base_calls)
pprint([s.a, s.b, s.c, s.d, s.e, s.f, s.g])
