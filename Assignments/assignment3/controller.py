""" Module that drives the program"""
from pizza import ConcretePizza, ParmigianoReggianoDecorator, FreshMozzarellaDecorator


class Controller:
    """
    Class that deals with the Pizza relevant classes
    """
    def __init__(self):
        """ Initializes the Controller class"""
        self.pizza = ConcretePizza()
        self.run()

    def run(self):
        """
        Runs the program
        """
        flag = True
        while flag:
            option_input = Controller.display_options()
            if option_input == 1:
                self.add_ingredient()
            elif option_input == 2:
                self.check_ingredients()
            elif option_input == 3:
                self.pay()
            else:
                pass

    @staticmethod
    def display_options():
        """
        Displays the available options for the user to choose
        :return:
        """
        return int(input("What would you like to do?\n"
                         f"1. Add Ingredients\n"
                         f"2. Check Added Ingredients\n"
                         f"3. Pay\n"
                         ))

    def add_ingredient(self):
        """
        Provided option that allows adding toppings to the pizza
        """
        ingredient_input = int(input(f"What do you want to add for topping?\n"
                                     "1. Parmigiano Reggiano\n"
                                     "2. Fresh Mozarella\n"
                                     ))
        if ingredient_input == 1:
            self.pizza = ParmigianoReggianoDecorator(self.pizza)
            self.pizza.add_ingredient()
        if ingredient_input == 2:
            self.pizza = FreshMozzarellaDecorator(self.pizza)
            self.pizza.add_ingredient()

    def check_ingredients(self):
        """
        Provided option to the user to check the added ingredients
        :return:
        """
        print(f"Ingredients: {self.pizza.get_ingredients()}")

    def pay(self):
        """
        Provided option to the user to finish the transaction by paying the total cost
        """
        print(f"Total is {self.pizza.get_cost()}. Have a good day.")
        flag = False


if __name__ == '__main__':
    Controller()
