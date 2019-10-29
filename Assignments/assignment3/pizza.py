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
    def get_ingredients(self):
        pass

    @abc.abstractmethod
    def get_cost(self):
        pass


class ConcretePizza(AbstractPizza):
    """
    A ConcretePizza is responsible for getting the list of ingredients,
    getting the total cost of it, and adding ingredients.
    It implements the Pizza Interface as defined by the parent
    Pizza class. This is the object that we want to add optional
    behaviours to.
    """

    def __init__(self):
        self.ingredients = []
        self.cost = 4.99

    def get_ingredients(self):
        return self.ingredients

    def get_cost(self):
        return self.cost

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)


class AbstractPizzaDecorator(AbstractPizza):
    """
    This is the base decorator. This is a wrapper around the concrete
    Pizza object and does not add any new behaviours or implementation. 
    All other decorators inherit from this class.
    """

    def __init__(self, decorated_pizza):
        self.decorated_pizza = decorated_pizza

    def get_ingredients(self):
        return self.decorated_pizza.get_ingredients()

    def get_cost(self):
        return self.decorated_pizza.get_cost()

    def add_ingredient(self, ingredient):
        self.decorated_pizza.add_ingredient(ingredient)


class ParmigianoReggianoDecorator(AbstractPizzaDecorator):
    """
    Decorator that adds 'ParmigianoReggianoDecorator' to the Pizza
    """

    def get_ingredients(self):
        return super().get_ingredients()

    def get_cost(self):
        return super().get_cost() + 4.99

    def add_ingredient(self):
        """
        Adds the ingredient 'Parmigiano Reggiano'
        """
        super().add_ingredient('Parmigiano Reggiano')


class FreshMozzarellaDecorator(AbstractPizzaDecorator):
    """
    Decorator that adds 'ParmigianoReggianoDecorator' to the Pizza
    """

    def get_ingredients(self):
        return super().get_ingredients()

    def get_cost(self):
        return super().get_cost() + 3.99

    def add_ingredient(self):
        """
        Adds the ingredient 'Fresh Mozzarella'
        """
        super().add_ingredient('Fresh Mozzarella')


class VeganCheeseDecorator(AbstractPizzaDecorator):
    """
    Decorator that adds 'ParmigianoReggianoDecorator' to the Pizza
    """

    def get_ingredients(self):
        self.add_ingredient()
        return super().get_ingredients()

    def get_cost(self):
        return super().get_cost() + 5.99

    def add_ingredient(self):
        """
        Adds the ingredient 'Vegan Cheese'
        """
        super().add_ingredient('Vegan Cheese')
