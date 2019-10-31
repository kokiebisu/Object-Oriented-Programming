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
                cheese_or_topping_input = input(
                    f"Would you like to add cheese or topping?\n").strip().lower()
                try:
                    if cheese_or_topping_input == "cheese":
                        cheese_input = int(input(f"Which Cheese do you want to add?\n"
                                                 "1. Parmigiano Reggiano: $4.99\n"
                                                 "2. Fresh Mozarella: $3.99\n"
                                                 "3. Vegan Cheese: $5.99\n"
                                                 ))
                        self.add_cheese(cheese_input)
                    elif cheese_or_topping_input == "topping":
                        topping_input = int(input(f"Which Topping do you want to add\n"
                                                  "1. Peppers: $1.5\n"
                                                  "2. Pineapple: $2\n"
                                                  "3. Mushrooms: $1.5\n"
                                                  "4. Fresh Basil: $2\n"
                                                  "5. Spinach: $1\n"
                                                  "6. Pepperoni: $3\n"
                                                  "7. Beyond Meat: $4\n"
                                                  ))
                        self.add_topping(topping_input)
                    else:
                        raise TypeError
                except TypeError:
                    print("Not a valid option!")
                option_input = Controller.display_options()
                self.prompt(option_input)
                return True
            elif user_input == 2:
                print(self.pay())
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

    def add_cheese(self, cheese_input):
        """
        Provided option that allows adding toppings to the pizza
        """
        try:
            if cheese_input == 1:
                self.pizza = ParmigianoReggianoDecorator(self.pizza)
            elif cheese_input == 2:
                self.pizza = FreshMozzarellaDecorator(self.pizza)
            elif cheese_input == 3:
                self.pizza = VeganCheeseDecorator(self.pizza)
            else:
                raise TypeError
        except TypeError:
            print("Doesn't seem like a valid number! Try Again!")

    def add_topping(self, topping_input):
        try:
            if topping_input == 1:
                self.pizza = PeppersDecorator(self.pizza)
            elif topping_input == 2:
                self.pizza = PineappleDecorator(self.pizza)
            elif topping_input == 3:
                self.pizza = MushroomsDecorator(self.pizza)
            elif topping_input == 4:
                self.pizza = FreshBasilDecorator(self.pizza)
            elif topping_input == 5:
                self.pizza = SpinachDecorator(self.pizza)
            elif topping_input == 6:
                self.pizza = PepperoniDecorator(self.pizza)
            elif topping_input == 7:
                self.pizza = BeyondMeatDecorator(self.pizza)
            else:
                raise TypeError
        except TypeError:
            print("Doesn't seem like a valid number! Try Again!")

    def pay(self):
        """
        Provided option to the user to finish the transaction by paying the total cost
        """
        return f"{self.pizza.get_ingredient()} \nTotal Cost: ${self.pizza.get_cost()} \n"


if __name__ == '__main__':
    controller = Controller()
    controller.run()
