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


def test_vehicle_can_be_instantianted():
    Car(fuel_quantity=10, fuel_consumption=2)
    Truck(fuel_quantity=20, fuel_consumption=4)


def test_vehicle_should_be_able_to_drive():
    car = Car(fuel_quantity=10, fuel_consumption=2)
    car.drive(2)
    assert car.fuel_quantity == 4.2, car.fuel_quantity
    print("test_vechicle_should_be_able_to_drive passed")


def test_vechicle_gain_fuel_when_refueled():
    car = Car(fuel_quantity=5, fuel_consumption=3)
    car.refuel(10)
    assert car.fuel_quantity == 15, car.fuel_quantity

    truck = Truck(17.0, 15)
    truck.refuel(50)
    assert truck.fuel_quantity == 64.5, truck.fuel_quantity

    print("test_vechicle_gain_fuel_when_refueled passed")


def test_drive_longer_then_being_able():
    car = Car(fuel_quantity=5, fuel_consumption=3)
    car.drive(10000)
    assert car.fuel_quantity == 5, car.fuel_quantity

    truck = Truck(fuel_quantity=5, fuel_consumption=3)
    truck.drive(10000)
    assert truck.fuel_quantity == 5, truck.fuel_quantity

    print("test_drive_longer_then_being_able passed")

if __name__ == "__main__":
    test_vehicle_can_be_instantianted()
    test_vehicle_should_be_able_to_drive()
    test_vechicle_gain_fuel_when_refueled()
    test_drive_longer_then_being_able()
