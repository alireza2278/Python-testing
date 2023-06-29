class Vehicle:
    def __init__(self, color="", speed="", **kwargs):
        super().__init__(**kwargs)
        self.speed = speed
        self.color = color

    def info(self):
        pass

    def move(self):
        pass


class Airplane(Vehicle):
    def __init__(self, capacity, **kwargs):
        super().__init__(**kwargs)
        self.capacity = capacity

    def info(self):
        print(f"The plane has a capacity of {self.capacity} passengers and its body color is {self.color}.")

    def move(self):
        print(f"The plane flies and its speed is {self.speed} km/h")


class Bicycle(Vehicle):
    def __init__(self, pedal, **kwargs):
        super().__init__(**kwargs)
        self.pedal = pedal

    def info(self):
        print(f"The bicycle has a speed of {self.speed} kilometers per hour and its color is {self.color}")

    def move(self):
        print(f"The bike is ground and has {self.pedal} pedals")


class Car(Vehicle):
    def __init__(self, Type, the_number_of_tire, **kwargs):
        super().__init__(**kwargs)
        self.the_number_of_tire = the_number_of_tire
        self.Type = Type

    def info(self):
        print(f"The car has {self.the_number_of_tire} wheels")

    def move(self):
        print(f"The car has different speed and power depending on its {self.Type}")


class Lamborghini(Car):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def info(self):
        print(f"Lamborghini {self.Type} car has a {self.color} color and a speed of {self.speed} km/h")

    def move(self):
        print(f"Lamborghini has {self.the_number_of_tire} wheels and is on the ground")


class Benz(Car):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def info(self):
        print(f"Benz {self.Type} car has a {self.color} color and a speed of {self.speed} km/h")

    def move(self):
        print(f"Benz has {self.the_number_of_tire} wheels and is on the ground")


lamborghini = Lamborghini(Type="sport", the_number_of_tire=4, speed=370, color="yellow")
print(lamborghini.__dict__)
lamborghini.info()
