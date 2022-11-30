from abc import ABC, abstractmethod


class Vehicle(ABC):
    fuel_quantity: int
    fuel_consumption: int

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        fuel_needed = distance * (self.fuel_consumption + self._CONSUMPTION_PER_KM)
        if self.fuel_quantity >= fuel_needed:
            self.fuel_quantity -= fuel_needed

    @abstractmethod
    def refuel(self, fuel: int):
        self.fuel_quantity += fuel

    @property
    @abstractmethod
    def _CONSUMPTION_PER_KM(self):
        pass


class Car(Vehicle):
    _CONSUMPTION_PER_KM = 0.9

    def refuel(self, fuel):
        super().refuel(fuel)


class Truck(Vehicle):
    _CONSUMPTION_PER_KM = 1.6

    def refuel(self, fuel):
        super().refuel(fuel * 0.95)


# def tests():
#     Car(fuel_quantity=10, fuel_consumption=2)
#     Truck(fuel_quantity=20, fuel_consumption=4)
#     print("test passed")
#
#
# def test_vehicles():
#     # car = Car(fuel_quantity=10, fuel_consumption=2)
#     truck = Truck(fuel_quantity=100, fuel_consumption=15)
#     # car.drive(2)
#     truck.drive(5)
#     # assert car.fuel_quantity == 4.2
#     assert truck.fuel_quantity == 17.0
#     print("test passed")

car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

