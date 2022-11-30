import unittest

from project.factory.paint_factory import PaintFactory


class TestPaintFactory(unittest.TestCase):
    def test_init(self):
        p = PaintFactory("Test1", 10)
        self.assertEqual(p.name, "Test1")
        self.assertEqual(p.capacity, 10)
        self.assertEqual(p.valid_ingredients, ["white", "yellow", "blue", "green", "red"])

    def test_ingredient_type_not_in_valid_ingredients(self):
        p = PaintFactory("Test1", 10)
        with self.assertRaises(TypeError) as ex:
            p.add_ingredient("orange", 5)
        self.assertEqual(str(ex.exception), "Ingredient of type orange not allowed in PaintFactory")

    def test_factory_capacity_less_than_ingredient_quantity(self):
        p = PaintFactory("Test1", 10)
        with self.assertRaises(ValueError) as ex:
            p.add_ingredient("yellow", 20)
        self.assertEqual(str(ex.exception), "Not enough space in factory")

    def test_ingredient_type_not_in_ingredients(self):
        p = PaintFactory("Test1", 30)
        p.ingredients["white"] = 5
        self.assertEqual(p.ingredients, {"white": 5})
        p.add_ingredient("yellow", 20)
        self.assertEqual(p.ingredients, {"white": 5, "yellow": 20})

    def test_ingredient_type_in_ingredients(self):
        p = PaintFactory("Test1", 30)
        p.ingredients["yellow"] = 5
        p.add_ingredient("yellow", 20)
        self.assertEqual(p.ingredients, {"yellow": 25})

    def test_remove_ingredient_if_not_in_ingredients(self):
        p = PaintFactory("Test1", 30)
        with self.assertRaises(KeyError) as ex:
            p.remove_ingredient("yellow", 20)
        # self.assertEqual(str(ex.exception), "No such product in the factory")

    #         elif quantity > self.ingredients[ingredient_type]:
    #             raise ValueError("Ingredient quantity cannot be less than zero")
    def test_quantity_more_than_ingredients_qty(self):
        p = PaintFactory("Test1", 30)
        p.ingredients["yellow"] = 10
        with self.assertRaises(ValueError) as ex:
            p.remove_ingredient("yellow", 20)
        self.assertEqual(str(ex.exception), "Ingredient quantity cannot be less than zero")

    def test_remove_ingredients(self):
        p = PaintFactory("Test1", 30)
        p.ingredients["yellow"] = 20
        p.remove_ingredient("yellow", 10)
        self.assertEqual(p.ingredients, {"yellow": 10})

    def test_products(self):
        p = PaintFactory("Test1", 30)
        p.ingredients["yellow"] = 20
        self.assertEqual(p.products, {"yellow": 20})
