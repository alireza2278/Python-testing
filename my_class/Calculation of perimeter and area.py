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


# length, width
class Rectangle(Shape):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def calculate_area(self):
        self.area = self.length * self.width

    def calculate_environment(self):
        self.environment = 2 * (self.length + self.width)


# length
class Square(Shape):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def calculate_area(self):
        self.area = self.length**2

    def calculate_environment(self):
        self.environment = 4 * self.length


# base, height, side1, side2
class Triangle(Shape):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def calculate_area(self):
        self.area = (self.base * self.height) / 2

    def calculate_environment(self):
        self.environment = self.base + self.side1 + self.side2


# diameter1, diameter2 , length
class Rhombus(Shape):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def calculate_area(self):
        self.area = (self.diameter1 * self.diameter2) / 2

    def calculate_environment(self):
        self.environment = self.length * 4


# length, height, width
class Parallelogram(Shape):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def calculate_area(self):
        self.area = self.length * self.height

    def calculate_environment(self):
        self.environment = (self.length * self.width) * 2


# height, base, top, side1, side2
class Trapezium(Shape):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def calculate_area(self):
        self.area = 1/2 * self.height * (self.top+self.base)

    def calculate_environment(self):
        self.environment = self.top + self.base + self.side1 + self.side2


# radius
class Circle(Shape):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def calculate_area(self):
        self.area = self.radius ** 2 * 3.14

    def calculate_environment(self):
        self.environment = 2 * self.radius * 3.14

r = Rectangle(length=2, width=6)
r.calculate_area()
r.calculate_environment()
print(r)
r.show()
print(40*"-")

s = Square(length=2)
s.calculate_area()
s.calculate_environment()
print(s)
s.show()
print(40*"-")

t = Triangle(base=4, height=3, side1=3, side2=5)
t.calculate_area()
t.calculate_environment()
print(t)
t.show()
print(40*"-")

rh = Rhombus(diameter1=2, diameter2=6, length=4)
rh.calculate_area()
rh.calculate_environment()
print(rh)
rh.show()
print(40*"-")

p = Parallelogram(length=6, height=4, width=1)
p.calculate_area()
p.calculate_environment()
print(p)
p.show()
print(40*"-")

tr = Trapezium(height=1, base=1, top=4, side1=9, side2=4)
tr.calculate_area()
tr.calculate_environment()
print(tr)
tr.show()
print(40*"-")

c = Circle(radius=8)
c.calculate_area()
c.calculate_environment()
print(c)
c.show()
print(40*"-")
