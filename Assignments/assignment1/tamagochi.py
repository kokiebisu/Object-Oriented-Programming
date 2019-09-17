# from pikachu import Pikachu
import time
import datetime
import random
import datetime


class Tamagochi:
    """
    A tamagotchi class tha models a tamagotchi with a health, happiness and hunge.

    THis class srves a s base class and should be inherited from if any
    tamagotchis are required with specialized behaviors.
    A tamagotchi has a health, happiness, hunger.
    """

    def __init__(self, health=100, happiness=100, hunger=100, is_alive=True):
        """
        Initialize the tamagotchi object with health, happiness and a isAlive state
        :param health: an int
        :param happiness: an int
        :param hunger: an int
        :param isAlive: a boolean
        :precondition health: must be a zero or positive int
        :precondition happiness: must be a zero or positive int
        :precondition hunger: must be a zero or positive int
        """
        self._health = health
        self._happiness = happiness
        self._hunger = hunger
        self._is_alive = True
        self._is_sick = False
        self._last_checked = datetime.datetime.now()
        self._time_elapsed = 0

    @staticmethod
    def spawn():
        """
        Spawns a tamagotchi randomly out of the three types: Pikachu, Mew, Jigglypuff.
        :return: an instance that has the type of either Pikachu, Mew, or Jigglypuff
        """
        pikachu = Pikachu(100, 100, 0, True)
        return pikachu

    def decrease_health(self, amount, time):
        """
        Decreases the health of the tamgotchi based on the time elapsed and the type of tamagotchi it is.
        :param amount: an int in the range of 0 and 100
        :param time: a positive int
        :precondition: amount and time must be an int greater than 0
        """
        self._health = self._health - amount * time

    def decrease_happiness(self, amount, time):
        """
        Decreases the health of the tamagotchi based on the time elapsed and the type of tamagotchi it is.
        :param amount: an int in the range of 0 and 100
        :param time: a positive int
        :precondition: amount and time must be an int greater than 0
        """
        self._happiness = self._happiness - amount * time
        if self._happiness <= 0:
            self._happiness = 0

    def increase_hunger(self, amount, time):
        """
        Increases the hunger of the tamagotchi based on the time elapsed and the type of tamagotchi it is.
        :param amount:
        :param time:
        :precondition: amount and time must be an int greater than 0
        """
        self._hunger = self._hunger + amount * time
        if self._hunger > 100:
            self._hunger = 100

    def give_food(self, food, preferred_food, hunger_amount):
        """
        Decreases the hunger property of the tamagotchi based on the food being given and the type of tamagotchi it is.
        :param food: a string
        :param preferred_food: a list of food string names
        :param hunger_amount: an int
        :precondition: hungerAmount must be a positive int
        """
        if food in preferred_food:
            self._hunger = self._hunger - 1.1 * hunger_amount
        else:
            self._hunger = self._hunger - hunger_amount
        if self._hunger <= 0:
            self._hunger = 0

    def give_medicine(self):
        """
        Increases the health property of the tamagotchi to the maximum range.
        """
        self._health = 100

    def play(self, phrase, happiness_amount):
        """
        Prints a random message of how the user played with the tamagotchi and increases it's happiness based on the tamagotchi.
        :param phrase:
        :param happiness_amount:
        """
        self._happiness = self._happiness + happiness_amount
        if self._happiness > 100:
            self._happiness = 100
        print(phrase)

    def born(self, character):
        """
        Notifies the user which type of tamagotchi was being spawned.
        :param character: a string
        """
        print(f"Say hello to your new {character}!\n")

    def die(self):
        """
        Changes the isAlive property of the tamagotchi to false.
        """
        self._is_alive = False

    def show_status(self):
        """
        Shows the current health, happiness and hunger properties of your tamagotchi.
        :return:
        """
        print(self.__str__())

    def is_dead(self):
        """
        Checks whether if your tamagotchi died or not.
        :return: a boolean, true if it died
        """
        if self._health <= 0:
            print("Oh No! Your tamagochi died!")
            self.die()
            return True

    def is_sick(self, sick_value):
        """
        Checks whether if the tamagotchi is sick or not
        :param sickValue: an int
        :return: a boolean, true if it is sick
        """
        if self._health < 60:
            self._is_sick = True

    def get_sick(self):
        """
        Changes the isSick property of your tamagotchi
        """
        return self._is_sick

    def __str__(self):
        """
        :return: A user friendly formatted string depicting the tamagotchi attributes
        """
        return f"Tamagochi here"


class Pikachu(Tamagochi):
    """
    Pikachu is a specialied tamagotchi.
    """
    amount = 2
    rate = 1
    happiness_amount = 40
    hunger_base_amount = 60
    pikachu_sick = 60
    pikachu_happinessAmount = 1
    preferred_food = {"Apple", "Orange"}
    playlist = ["You played a game with Pikachu",
                "You did hide and seek with Pikachu",
                "You played soccer with Pikachu"]

    def __init__(self, health=100, happiness=100, hunger=0, is_alive=True, last_checked=0):
        """
        Initialize a pikachu object with a default health, happiness count of 100, hunger of 0 and a isAlive state of True
        :param health: an int
        :param happiness: an int
        :param hunger: an int
        :param is_alive: a boolean
        :param last_checked: a datetime objecy
        """
        super().__init__(
            health, happiness, hunger, is_alive)

    def decrease_health(self, time):
        """
        Overrides the tamagotchi's decrease_health function with pikachu's own unique speed of decreasing.
        :param time: an int
        """
        super().decrease_health(self.amount, time)

    def decrease_happiness(self, time):
        """
        Overrides the tamagotchi's decrease_happiness function with pikachu's own unique speed of decreasing
        :param time: an int
        """
        super().decrease_happiness(self.amount, time)

    def increase_hunger(self, time):
        """
        Overrides the tamagotchi's increase_hunger function with pikachu's own uniqued speed of increasing
        :param time: an int
        """
        super().increase_hunger(self.amount, time)

    def give_food(self, food):
        """
        Overrides the tamagotchi's give_food function with pikachu's own unique amount of decreasing hunge
        :param food: an int
        """
        super().give_food(food, self.preferred_food, self.hunger_base_amount)

    def play(self, play_input):
        """
        Overrides the tamagotchi's play function with pikachu's own unique amount of increasing happiness
        :param playInput: an int
        """
        super().play(self.playlist[play_input], self.happiness_amount)

    def update_status(self):
        """
        Overrides the tamagotchi's update_status function with pikachu's unique way of decreasing the
        health, happiness and increasing hunge
        """
        time_elapsed = datetime.datetime.now() - self._last_checked
        time_elapsed_in_seconds = time_elapsed.total_seconds()
        self._time_elapsed = time_elapsed
        self.decrease_health(time_elapsed_in_seconds)
        self.decrease_happiness(time_elapsed_in_seconds)
        self.increase_hunger(time_elapsed_in_seconds)
        self._last_checked = datetime.datetime.now()

    def is_sick(self):
        """
        Overrides the tamagotchi's is_sick function with pikachu's standard value of getting sick
        """
        super().is_sick(self.pikachu_sick)

    def __str__(self):
        """
        Overriden to print the pikchu's attributes
        """
        return f"\nPikachu: health: {round(self._health)}, happiness: {round(self._happiness)}, hunger: {round(self._hunger)}, time elapsed: {self._time_elapsed}\n"
