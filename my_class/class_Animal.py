class Animal:
    def __init__(self, name="", color=""):
        self.name = name
        self.color = color

    def info(self):
        print(f"hello, i am a Animal. My name is {self.name}, I am {self.color}")

    def make_sound(self):
        print("I can make sounds!")


class Cat(Animal):
    def __init__(self, name="", color=""):
        super().__init__(name, color)

    def info(self):
        print(f"hello, i am a cat. My name is {self.name}, I am {self.color}")

    def make_sound(self):
        print("Meow...")

class Cow(Animal):
    def __init__(self, name="", color=""):
        super().__init__(name, color)

    def info(self):
        print(f"hello, i am a cow. My name is {self.name}, I am {self.color}")

    def make_sound(self):
        print("Moo...")


animal = Animal()
cat = Cat("Zebel", "black")
cow = Cow("Gavi", "brown")
cat.make_sound()
cow.make_sound()
animal.make_sound()
animal.info()