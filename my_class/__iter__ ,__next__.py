class PowTwo:
    def __init__(self, max_pow):
        self.max_pow = max_pow
        self.n = 0

    # زمانی ک سلف برگشت داده شود یعنی آبجکت برگشت داده میشود و آبجکت دارای متد نکست میباشد
    def __iter__(self):
        return self

    def __next__(self):
        if self.n <= self.max_pow:
            result = self.n ** 2
            self.n += 1
            return result
        else:
            raise StopIteration


n = PowTwo(5)

for i in n:
    print(i)
