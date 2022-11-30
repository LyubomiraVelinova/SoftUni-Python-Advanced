from project.beverage.hot_beverage import HotBeverage
from typing import ClassVar


class Coffee(HotBeverage):
    COFFEE_MILLILITERS: ClassVar[int] = 50
    COFFEE_PRICE: ClassVar[float] = 3.50
    __caffeine: float

    def __init__(self, name: str, caffeine: float):
        super().__init__(name, self.COFFEE_PRICE, self.COFFEE_MILLILITERS)
        self.__caffeine = caffeine

    @property
    def caffeine(self):
        return self.__caffeine

