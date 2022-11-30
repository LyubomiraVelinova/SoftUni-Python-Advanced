from math import pi
from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def calculate_area(self):
        return pi * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * pi * self.radius


class Rectangle(Shape):
    def __init__(self, h, w):
        super().__init__()
        self.h = h
        self.w = w

    def calculate_area(self):
        return self.h * self.w

    def calculate_perimeter(self):
        return 2 * self.h + 2 * self.w


rectangle = Rectangle(10, 20)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())
