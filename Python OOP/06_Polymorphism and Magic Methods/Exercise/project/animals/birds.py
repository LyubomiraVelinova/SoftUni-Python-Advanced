from project.animals.animal import Animal
from project.animals.animal import Bird
from project.food import Food
from project.food import Meat
from project.food import Fruit
from project.food import Vegetable
from project.food import Seed


class Owl(Bird):
    _FOOD_PREFERENCES = tuple([Meat])
    _WEIGHT_GAIN_PER_FOOD = 0.25

    def make_sound(self):
        return "Hoot Hoot"


class Hen(Bird):
    _FOOD_PREFERENCES = None
    _WEIGHT_GAIN_PER_FOOD = 0.35

    def make_sound(self):
        return "Cluck"


owl = Owl("Pip", 10, 10)
print(owl)
meat = Meat(4)
print(owl.make_sound())
owl.feed(meat)
veg = Vegetable(1)
print(owl.feed(veg))
print(owl)
