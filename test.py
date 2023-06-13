class Shape:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


s = Shape(a=5, b=6)
print(s.a)
