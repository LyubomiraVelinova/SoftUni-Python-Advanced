from project.food.food import Food


class Dessert(Food):
    calories: float

    def __init__(self, name, price, grams, calories: float):
        super().__init__(name, price, grams)
        self._calories = calories

    @property
    def calories(self):
        return self._calories
