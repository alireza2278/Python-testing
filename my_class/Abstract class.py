# Abstract Base Class
from abc import ABC, abstractmethod


# Abstract Base Class
class Vehicle(ABC):
    @abstractmethod
    def move(self):
        """this method should be implemented!"""
    @abstractmethod
    def repair(self):
        """this method should be implemented!"""

    def class_name(self):
        print(self.__class__)


# Abstract Base Class
class LandV(Vehicle):
    @abstractmethod
    def brake(self):
        """this method should be implemented!"""


# Abstract Base Class
class AirV(Vehicle):
    @abstractmethod
    def eject(self):
        """this method should be implemented!"""


class Car(LandV):
    def move(self):
        print("Driving...")

    def repair(self):
        print("under repair...")

    def brake(self):
        print("braking")


class Airplane(AirV):
    def move(self):
        print("Flying...")

    def repair(self):
        print("under repair...")

    def eject(self):
        print("ejecting")


car = Car()
car.class_name()
car.move()
car.repair()
car.brake()

car = Car()
car.class_name()
car.move()
car.repair()
car.brake()
