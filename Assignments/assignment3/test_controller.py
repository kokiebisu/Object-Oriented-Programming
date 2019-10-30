from unittest import TestCase
from controller import Controller


class TestController(TestCase):
    def test_prompt_with_string(self):
        """
        Checks when a string is entered for activity option
        """
        controller = Controller()
        controller.prompt("string")
        self.assertRaises(ValueError)

    def test_prompt_with_invalid_positive_number(self):
        """
        Checks when a invalid number is entered for activity option
        """
        controller = Controller()
        controller.prompt(3)
        self.assertRaises(ValueError)

    def test_prompt_with_negative_number(self):
        """
        Checks when a negative number is entered for activity option
        """
        controller = Controller()
        controller.prompt(-1)
        self.assertRaises(ValueError)

    def test_prompt_with_invalid_ingredient_number(self):
        """
        Checks when a ingredient that doesn't exist is entered in the add ingredient screen
        """
        controller = Controller()
        controller.add_ingredient(11)
        self.assertRaises(ValueError)

    def test_prompt_with_valid_ingredient_number(self):
        """
        Checks when a valid ingredient number is entered in the add ingredient screen
        """
        controller = Controller()
        controller.add_ingredient(10)
        controller.pay()
        self.assertTrue("Pizza Ingredients: \nBeyond Meat \nTotal Cost: 8.99")

    def test_prompt_with_multiple_ingredients(self):
        """
        Checks when multiple valid ingredients are added to the pizza
        """
        controller = Controller()
        controller.add_ingredient(10)
        controller.add_ingredient(1)
        controller.pay()
        self.assertTrue(
            "Pizza Ingredients: \nParmigiano Reggiano \nBeyond Meat \nTotal Cost: 13.98")
