from project.food.main_dish import MainDish
from typing import ClassVar


class Salmon(MainDish):
    SALMON_GRAMS: ClassVar[int] = 22

    def __init__(self, name, price):
        super().__init__(name, price, self.SALMON_GRAMS)
