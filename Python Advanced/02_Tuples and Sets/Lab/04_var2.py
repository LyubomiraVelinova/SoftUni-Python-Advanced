class Parking:
    def __int__(self, reg_num):
        self.__reg_num = reg_num


class Parking:
    def __init__(self):
        self.__cars = set()

    def process_car(self, direction, car: car):
        if direction == "IN":
            self.__cars.add(car)

        elif direction == "OUT" and car in self.__cars:
            self.__cars.remove(car)

    def print_status(self):
        if self.__cars:
            print("\n".join([car.reg_num for car in self.__cars]))


parking = Parking()

n = int(input())
for _ in range(n):
    direction, reg_num = input().split(", ")
    car = car(reg_num)
    parking.process_car(direction,car)


