"""
This module implements a decorator pattern to decorate a pizza.

Each pizza should start with one ingredient, the signature crust and have a starting price of $4.99.
All subsequent ingredients should be decorators that wrap around a pizza.
Pick and implement 1 cheese and 2 toppings.
"""

import abc


class AbstractPizza(abc.ABC):
    """
    The interface of a Pizza that all concrete Pizza and
    decorators must adhere to. This interface defines the abstract method 
    to get the ingredients included and the cost of the total ingredients 
    that do not have an implementation.
    """
    @abc.abstractmethod
    def get_ingredient(self):
        """
        An abstract method that gets the ingredient
        """
        pass

    @abc.abstractmethod
    def get_cost(self):
        """
        An abstract method that gets the cost
        """
        pass


class ConcretePizza(AbstractPizza):
    """
    A ConcretePizza is responsible for getting the list of ingredients,
    getting the total cost of it, and adding ingredients.
    It implements the Pizza Interface as defined by the parent
    Pizza class. This is the object that we want to add optional
    behaviours to.
    """

    def get_ingredient(self):
        """
        Gets the ingredients of the pizza
        :return: a string
        """
        ingredient = "Signature Crust"
        return f"Pizza Ingredients: \n{ingredient}"

    def get_cost(self):
        """
        Gets the base cost of the pizza
        :return: an int
        """
        cost = 4.99
        return cost


class IngredientDecorator(AbstractPizza, abc.ABC):
    """
    This is the base decorator. This is a wrapper around the concrete
    Pizza object and does not add any new behaviours or implementation.
    All other decorators inherit from this class.
    """
    @abc.abstractmethod
    def get_ingredient(self):
        """
        An abstract method that gets the ingredient
        """
        pass


class ParmigianoReggianoDecorator(IngredientDecorator):
    """
    Decorator that adds 'Parmigiano Reggiano' to the Pizza
    """

    def __init__(self, decorated_pizza):
        """
        Attach the decorator to the existing pizza
        :param decorated_pizza: a pizza object
        """
        self.pizza = decorated_pizza

    def get_ingredient(self):
        """
        Gets the ingredients with Parmigiano Reggiano added
        :return: a string
        """
        ingredient = "Parmigiano Reggiano"
        return f"{self.pizza.get_ingredient()} \n{ingredient}"

    def get_cost(self):
        """
        Gets the cost with Parmigiano Reggiano added
        :return: an int
        """
        cost = 4.99
        return self.pizza.get_cost() + cost


class FreshMozzarellaDecorator(IngredientDecorator):
    """
    Decorator that adds 'Fresh Mozzarella' to the Pizza
    """

    def __init__(self, decorated_pizza):
        """
        Attach th decorator to the existing pizza
        :param decorated_pizza: a pizza object
        """
        self.pizza = decorated_pizza

    def get_ingredient(self):
        """
        Gets the ingredient with Fresh Mozzarella added
        :return: a string
        """
        ingredient = "Fresh Mozzarella"
        return f"{self.pizza.get_ingredient()} \n{ingredient}"

    def get_cost(self):
        """
        Gets the cost with Fresh Mozzarella added
        :return:
        """
        cost = 3.99
        return self.pizza.get_cost() + cost


class VeganCheeseDecorator(IngredientDecorator):
    """
    Decorator that adds 'Vegan Cheese' to the Pizza
    """

    def __init__(self, decorated_pizza):
        """
        Attach the decorator to the existing pizza
        :param decorated_pizza: a pizza object
        """
        self.pizza = decorated_pizza

    def get_ingredient(self):
        """
        Gets the ingredient with Vegan Cheese added
        :return: a string
        """
        ingredient = "Vegan Cheese"
        return f"{self.pizza.get_ingredient()} \n{ingredient}"

    def get_cost(self):
        """
        Gets the cost with Vegan Cheese added
        :return: an int
        """
        cost = 5.99
        return self.pizza.get_cost() + cost


class PeppersDecorator(IngredientDecorator):
    """
    Decorator that adds 'Peppers' to the Pizza
    """

    def __init__(self, decorated_pizza):
        """
        Attach the decorator to the existing pizza
        :param decorated_pizza: a pizza object
        """
        self.pizza = decorated_pizza

    def get_ingredient(self):
        """
        Gets the ingredient with Peppers added
        :return: a string
        """
        ingredient = "Peppers"
        return f"{self.pizza.get_ingredient()} \n{ingredient}"

    def get_cost(self):
        """
        Gets the cost with Peppers added
        :return: an int
        """
        cost = 1.5
        return self.pizza.get_cost() + cost


class PineappleDecorator(IngredientDecorator):
    """
    Decorator that adds 'Pineapple' to the Pizza
    """

    def __init__(self, decorated_pizza):
        """
        Attach the decorator to the existing pizza
        :param decorated_pizza: a pizza object
        """
        self.pizza = decorated_pizza

    def get_ingredient(self):
        """
        Gets the ingredients with Pineapple added
        :return: a string
        """
        ingredient = "Pineapple"
        return f"{self.pizza.get_ingredient()} \n{ingredient}"

    def get_cost(self):
        """
        Gets the cost with Pineapple added
        :return: an int
        """
        cost = 2
        return self.pizza.get_cost() + cost


class MushroomsDecorator(IngredientDecorator):
    """
    Decorator that adds 'Mushrooms' to the Pizza
    """

    def __init__(self, decorated_pizza):
        """
        Attach the decorator to the existing pizza
        :param decorated_pizza: a pizza object
        """
        self.pizza = decorated_pizza

    def get_ingredient(self):
        """
        Gets the ingredients with Mushrooms added
        :return: a string
        """
        ingredient = "Mushrooms"
        return f"{self.pizza.get_ingredient()} \n{ingredient}"

    def get_cost(self):
        """
        Gets the cost with Mushrooms added
        :return: an int
        """
        cost = 1.5
        return self.pizza.get_cost() + cost


class FreshBasilDecorator(IngredientDecorator):
    """
    Decorator that adds 'Fresh Basil' to the Pizza
    """

    def __init__(self, decorated_pizza):
        """
        Attach the decorator to the existing pizza
        :param decorated_pizza: a pizza object
        """
        self.pizza = decorated_pizza

    def get_ingredient(self):
        """
        Gets the ingredients with Fresh Basil added
        :return: a string
        """
        ingredient = "Fresh Basil"
        return f"{self.pizza.get_ingredient()} \n{ingredient}"

    def get_cost(self):
        """
        Gets the cost with Fresh Basil added
        :return: an int
        """
        cost = 2
        return self.pizza.get_cost() + cost


class SpinachDecorator(IngredientDecorator):
    """
    Decorator that adds 'Spinach' to the Pizza
    """

    def __init__(self, decorated_pizza):
        """
        Attach the decorator to the existing pizza
        :param decorated_pizza: a pizza object
        """
        self.pizza = decorated_pizza

    def get_ingredient(self):
        """
        Gets the ingredients with Spinach added
        :return: a string
        """
        ingredient = "Spinach"
        return f"{self.pizza.get_ingredient()} \n{ingredient}"

    def get_cost(self):
        """
        Gets the cost with Spinach added
        :return: an int
        """
        cost = 1
        return self.pizza.get_cost() + cost


class PepperoniDecorator(IngredientDecorator):
    """
    Decorator that adds 'Pepperoni' to the Pizza
    """

    def __init__(self, decorated_pizza):
        """
        Attach the decorator to the existing pizza
        :param decorated_pizza: a pizza object
        """
        self.pizza = decorated_pizza

    def get_ingredient(self):
        """
        Gets the ingredients with Pepperoni added
        :return: a string
        """
        ingredient = "Pepperoni"
        return f"{self.pizza.get_ingredient()} \n{ingredient}"

    def get_cost(self):
        """
        Gets the cost with Pepperoni added
        :return: an int
        """
        cost = 3
        return self.pizza.get_cost() + cost


class BeyondMeatDecorator(IngredientDecorator):
    """
    Decorator that adds 'Beyond Meat' to the Pizza
    """

    def __init__(self, decorated_pizza):
        """
        Attach the decorator to the existing pizza
        :param decorated_pizza: a pizza object
        """
        self.pizza = decorated_pizza

    def get_ingredient(self):
        """
        Gets the ingredients with Beyond Meat added
        :return: a string
        """
        ingredient = "Beyond Meat"
        return f"{self.pizza.get_ingredient()} \n{ingredient}"

    def get_cost(self):
        """
        Gets the cost with Beyond Meat added
        :return: an int
        """
        cost = 4
        return self.pizza.get_cost() + cost
