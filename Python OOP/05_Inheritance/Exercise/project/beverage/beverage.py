from project.product import Product


class Beverage(Product):
    name: str
    price: float
    milliliters: float

    def __init__(self, name: str, price: float, milliliters: float):
        super().__init__(name, price)
        self._milliliters = milliliters

    @property
    def milliliters(self):
        return self._milliliters
