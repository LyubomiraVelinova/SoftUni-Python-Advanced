from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        available_distance = self.fuel_quantity / self.fuel_consumption
        if distance <= available_distance:
            self.fuel_quantity -= distance * self.fuel_consumption

    @abstractmethod
    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Car(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance):
        self.fuel_consumption *= 0.9

    def refuel(self, refuel):
        pass


class Truck(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance):
        self.fuel_consumption *= 1.65

    def refuel(self, refuel):
        self.fuel_quantity *= 0.95
        print(self.fuel_quantity)


#
# truck = Truck(100, 15)
# truck.drive(5)
# print(truck.fuel_quantity)
# truck.refuel(50)
# print(truck.fuel_quantity)

def tests():
    Car(fuel_quantity=10, fuel_consumption=2)
    Truck(fuel_quantity=10, fuel_consumption=4)
    print("test passed")


tests()
