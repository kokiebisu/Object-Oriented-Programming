""" Module that drives the program"""
from pizza import ConcretePizza, ParmigianoReggianoDecorator, FreshMozzarellaDecorator, VeganCheeseDecorator, PeppersDecorator, PineappleDecorator, MushroomsDecorator, FreshBasilDecorator, SpinachDecorator, PepperoniDecorator, BeyondMeatDecorator


class Controller:
    """
    Class that deals with the Pizza relevant classes
    """

    def __init__(self):
        """ Initializes the Controller class"""
        self.pizza = ConcretePizza()

    def run(self):
        """
        Runs the program
        """
        option_input = Controller.display_options()
        self.prompt(option_input)

    def prompt(self, user_input):
        try:
            if user_input == 1:
                ingredient_input = int(input(f"What do you want to add for topping?\n"
                                             "1. Parmigiano Reggiano\n"
                                             "2. Fresh Mozarella\n"
                                             "3. Vegan Cheese\n"
                                             "4. Peppers\n"
                                             "5. Pineapple\n"
                                             "6. Mushrooms\n"
                                             "7. Fresh Basil\n"
                                             "8. Spinach\n"
                                             "9. Pepperoni\n"
                                             "10. Beyond Meat\n"
                                             ))
                self.add_ingredient(ingredient_input)
                option_input = Controller.display_options()
                self.prompt(option_input)
                return True
            elif user_input == 2:
                return self.pay()
            else:
                raise ValueError
        except ValueError:
            print("Number must be either 1 or 2!")

    @staticmethod
    def display_options():
        """
        Displays the available options for the user to choose
        :return: an int
        """
        return int(input("What would you like to do?\n"
                         f"1. Add Ingredients\n"
                         f"2. Pay\n"
                         ))

    def add_ingredient(self, ingredient_input):
        """
        Provided option that allows adding toppings to the pizza
        """
        try:
            if ingredient_input == 1:
                self.pizza = ParmigianoReggianoDecorator(self.pizza)
            elif ingredient_input == 2:
                self.pizza = FreshMozzarellaDecorator(self.pizza)
            elif ingredient_input == 3:
                self.pizza = VeganCheeseDecorator(self.pizza)
            elif ingredient_input == 4:
                self.pizza = PeppersDecorator(self.pizza)
            elif ingredient_input == 5:
                self.pizza = PineappleDecorator(self.pizza)
            elif ingredient_input == 6:
                self.pizza = MushroomsDecorator(self.pizza)
            elif ingredient_input == 7:
                self.pizza = FreshBasilDecorator(self.pizza)
            elif ingredient_input == 8:
                self.pizza = SpinachDecorator(self.pizza)
            elif ingredient_input == 9:
                self.pizza = PepperoniDecorator(self.pizza)
            elif ingredient_input == 10:
                self.pizza = BeyondMeatDecorator(self.pizza)
            else:
                raise TypeError
        except TypeError:
            print("Doesn't seem like a valid number! Try Again!")

    def pay(self):
        """
        Provided option to the user to finish the transaction by paying the total cost
        """
        print(f"{self.pizza.get_description()} \nTotal Cost: {self.pizza.get_cost()}\n")


if __name__ == '__main__':
    controller = Controller()
    controller.run()
