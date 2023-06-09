from pprint import pprint


class BaceClass:
    num_base_calls = 0

    def call_me(self):
        print("calling method on BaceClass")
        self.num_base_calls += 1


class LeftSubClass(BaceClass):
    num_left_calls = 0

    def call_me(self):
        super().call_me()
        print("calling method on LeftSubClass")
        self.num_left_calls += 1


class RightSubClass(BaceClass):
    num_right_calls = 0

    def call_me(self):
        super().call_me()
        print("calling method on RightSubClass")
        self.num_right_calls += 1


class SubClass(LeftSubClass, RightSubClass):
    num_sub_calls = 0

    def call_me(self):
        super().call_me()
        print("calling method on SubClass")
        self.num_sub_calls += 1


s = SubClass()
s.call_me()
print(s.num_sub_calls, s.num_left_calls, s.num_right_calls, s.num_base_calls)
print()
pprint(SubClass.__mro__)
