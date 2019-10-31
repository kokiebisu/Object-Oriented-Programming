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

    def test_prompt_with_invalid_cheese_number(self):
        """
        Checks when a cheese that doesn't exist is entered in the add cheese screen
        """
        controller = Controller()
        controller.add_cheese(4)
        self.assertRaises(ValueError)

    def test_prompt_with_invalid_topping_number(self):
        """
        Checks when a topping that doesn't exist is entered in the add topping screen
        """
        controller = Controller()
        controller.add_topping(8)
        self.assertRaises(ValueError)

    def test_prompt_with_valid_cheese_number(self):
        """
        Checks when a valid cheese number is entered in the add ingredient screen
        """
        controller = Controller()
        controller.add_cheese(1)
        self.assertEqual(controller.pay(), "Pizza Ingredients: \nSignature Crust \nParmigiano Reggiano"
                                           " \nTotal Cost: $9.98 \n")

    def test_prompt_with_valid_topping_number(self):
        """
        Checks when a valid topping number is entered in the add ingredient screen
        """
        controller = Controller()
        controller.add_topping(1)
        self.assertEqual(controller.pay(
        ), "Pizza Ingredients: \nSignature Crust \nPeppers \nTotal Cost: $6.49 \n")

    def test_prompt_with_multiple_ingredients(self):
        """
        Checks when multiple valid ingredients are added to the pizza
        """
        controller = Controller()
        controller.add_cheese(1)
        controller.add_topping(1)
        self.assertEqual(controller.pay(), "Pizza Ingredients: \nSignature Crust \nParmigiano Reggiano "
                         "\nPeppers \nTotal Cost: $11.48 \n")
