class Shape:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.area = 0
        self.environment = 0

    def calculate_area(self):
        pass

    def calculate_environment(self):
        pass

    def show(self):
        info = ""
        for key, value in self.__dict__.items():
            if value > 0:
                info += f"{key}:{value:.2f}\n"
        print(info)
    def __str__(self):
        return self.__class__.__name__

class Rectangle(Shape):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def calculate_area(self):
        self.area = self.length * self.width

    def calculate_environment(self):
        self.environment = 2 * (self.length + self.width)


r = Rectangle(length=6, width=5)
print(r)
r.calculate_environment()
r.calculate_area()
r.show()


