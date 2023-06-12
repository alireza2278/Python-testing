class WiFiMixin:
    def connect_to_wifi(self):
        print("Connection successful")


class Vehicle:
    def move(self):
        pass


class Car(Vehicle, WiFiMixin):
    pass


class AirPlane(Vehicle):
    pass


class MotorCycle(Vehicle):
    pass

car = Car()
car.connect_to_wifi()
