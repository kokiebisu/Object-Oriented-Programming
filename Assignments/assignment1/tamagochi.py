# from pikachu import Pikachu
import time
import datetime
import random
import datetime
import abc


class Tamagochi(abc.ABC):
    """
    A tamagotchi class tha models a tamagotchi with a health, happiness and hunge.

    THis class srves a s base class and should be inherited from if any
    tamagotchis are required with specialized behaviors.
    A tamagotchi has a health, happiness, hunger.
    """

    def __init__(self):
        """
        Initializes the constructed Tamagotchi instance
        """
        self._health = 100.0
        self._happiness = 100.0
        self._hunger = 0
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
        spawning_tamagotchi = random.randint(0, 2)
        if spawning_tamagotchi == 0:
            return Pikachu()
        elif spawning_tamagotchi == 1:
            return Mew()
        else:
            return Jigglypuff()

    def time_elapsed(self):
        return self._time_elapsed

    @abc.abstractmethod
    def decrease_health(self, amount, time):
        """
        Decreases the health of the tamgotchi based on the time elapsed and the type of tamagotchi it is.
        :param amount: an int in the range of 0 and 100
        :param time: an int
        :precondition: amount and time must be an int greater than 0
        """
        self._health = self._health - amount * time

    @abc.abstractmethod
    def decrease_happiness(self, amount, time):
        """
        Decreases the health of the tamagotchi based on the time elapsed and the type of tamagotchi it is.
        :param amount: an int in the range of 0 and 100
        :param time: an int
        :precondition: amount and time must be an int greater than 0
        """
        self._happiness = self._happiness - amount * time
        if self._happiness <= 0:
            self._happiness = 0

    @abc.abstractmethod
    def increase_hunger(self, amount, time):
        """
        Increases the hunger of the tamagotchi based on the time elapsed and the type of tamagotchi it is.
        :param amount: an int it te range of 0 and 100
        :param time: an int
        :precondition: amount and time must be an int greater than 0
        """
        self._hunger = self._hunger + amount * time
        if self._hunger > 100:
            self._hunger = 100

    @abc.abstractmethod
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

    @abc.abstractmethod
    def play(self, phrase, happiness_amount):
        """
        Prints a random message of how the user played with the tamagotchi and increases it's happiness based on the tamagotchi.
        :param phrase: a string
        :param happiness_amount: a float
        """

        self._happiness = self._happiness + happiness_amount
        if self._happiness > 100:
            self._happiness = 100
        print(phrase)

    @abc.abstractmethod
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

    @abc.abstractmethod
    def is_sick(self, sick_value):
        """
        Checks whether if the tamagotchi is sick or not
        :param sick_value: an int
        :return: a boolean, true if it is sick
        """
        return self._is_sick

    def get_sick(self, sick_value):
        """
        Changes the isSick property of your tamagotchi
        """
        return self._is_sick

    def __str__(self):
        """
        String representation of the class
        :return: A user friendly formatted string depicting the tamagotchi attributes
        """
        return f"Tamagochi here"


class Pikachu(Tamagochi):
    """
    Pikachu is a specialized tamagotchi.
    """
    base_amount = 0.5
    rate = 2
    health_increase_amount = 50
    happiness_increase_amount = 50
    hunger_decrease_amount = 50
    pikachu_get_sick = 60
    preferred_food = {"Apple", "Orange"}
    playlist = ["\nYou played a game with Pikachu\n",
                "\nYou did hide and seek with Pikachu\n",
                "\nYou played soccer with Pikachu\n",
                "\nYou played tag with Pikachu\n"]

    def decrease_health(self, time):
        """
        Overrides the tamagotchi's decrease_health function with pikachu's own unique speed of decreasing.
        :param time: a float
        """
        super().decrease_health(self.base_amount, time)

    def decrease_happiness(self, time):
        """
        Overrides the tamagotchi's decrease_happiness function with pikachu's own unique speed of decreasing
        :param time: a float
        """
        super().decrease_happiness(self.base_amount, time)

    def increase_hunger(self, time):
        """
        Overrides the tamagotchi's increase_hunger function with pikachu's own uniqued speed of increasing
        :param time: a float
        """
        super().increase_hunger(self.base_amount, time)

    def give_food(self, food):
        """
        Overrides the tamagotchi's give_food function with pikachu's own unique amount of decreasing hunge
        :param food: a float
        """
        super().give_food(food, self.preferred_food, self.hunger_decrease_amount)

    def play(self, play_input):
        """
        Overrides the tamagotchi's play function with pikachu's own unique amount of increasing happiness
        :param play_input: a float
        """
        super().play(self.playlist[play_input], self.happiness_increase_amount)

    def born(self):
        """
        Prints a message that Pikachu was born.
        """
        super().born("Pikachu")

    def update_status(self):
        """
        Overrides the tamagotchi's update_status function with pikachu's unique way of decreasing the
        health, happiness and increasing hunger
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
        :return: a boolean
        """
        return self._health < 60

    def __str__(self):
        """
        Prints Pikachu's status
        """
        if self._is_sick:
            return f"\nPikachu: health: {round(self._health)}, happiness: {round(self._happiness)}," \
                   f" hunger: {round(self._hunger)}, time elapsed: {self._time_elapsed}, Your tamagotchi is sick!\n"
        else:
            return f"\nPikachu: health: {round(self._health)}, happiness: {round(self._happiness)}," \
                f" hunger: {round(self._hunger)}, time elapsed: {self._time_elapsed}\n"


class Mew(Tamagochi):
    """
    Mew is a specialized tamagotchi.
    """
    base_amount = 0.25
    rate = 3
    health_increase_amount = 70
    happiness_increase_amount = 70
    hunger_decrease_amount = 70
    mew_get_sick = 30
    preferred_food = {"Apple", "Orange"}
    playlist = ["\nYou played a game with Mew\n",
                "\nYou did hide and seek with Mew\n",
                "\nYou played soccer with Mew\n",
                "\nYou played tag with Mew\n"]

    def decrease_health(self, time):
        """
        Overrides the tamagotchi's decrease_health function with Mew's own unique speed of decreasing.
        :param time: a float
        """
        super().decrease_health(self.base_amount, time)

    def decrease_happiness(self, time):
        """
        Overrides the tamagotchi's decrease_happiness function with Mew's own unique speed of decreasing
        :param time: a float
        """
        super().decrease_happiness(self.base_amount, time)

    def increase_hunger(self, time):
        """
        Overrides the tamagotchi's increase_hunger function with Mew's own uniqued speed of increasing
        :param time: a float
        """
        super().increase_hunger(self.base_amount, time)

    def give_food(self, food):
        """
        Overrides the tamagotchi's give_food function with Mew's own unique amount of decreasing hunge
        :param food: a float
        """
        super().give_food(food, self.preferred_food, self.hunger_decrease_amount)

    def play(self, play_input):
        """
        Overrides the tamagotchi's play function with Mew's own unique amount of increasing happiness
        :param play_input: a float
        """
        super().play(self.playlist[play_input], self.happiness_increase_amount)

    def born(self):
        """
        Prints the message that Mew was born.
        """
        super().born("Mew")

    def update_status(self):
        """
        Overrides the tamagotchi's update_status function with Mew's unique way of decreasing the
        health, happiness and increasing hunger
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
        Overrides the tamagotchi's is_sick function with Mew's standard value of getting sick
        :return: a boolean
        """
        return self._health < 60

    def __str__(self):
        """
        Prints Mew's status
        """
        if self._is_sick:
            return f"\nMew: health: {round(self._health)}, happiness: {round(self._happiness)}," \
                   f" hunger: {round(self._hunger)}, time elapsed: {self._time_elapsed}, Your tamagotchi is sick!\n"
        else:
            return f"\nMew: health: {round(self._health)}, happiness: {round(self._happiness)}," \
                f" hunger: {round(self._hunger)}, time elapsed: {self._time_elapsed}\n"


class Jigglypuff(Tamagochi):
    """
    Jigglypuff is a specialized tamagotchi.
    """
    base_amount = 0.75
    rate = 5
    health_increase_amount = 30
    happiness_increase_amount = 30
    hunger_decrease_amount = 30
    jigglypuff_get_sick = 30
    preferred_food = {"Apple", "Orange"}
    playlist = ["\nYou played a game with Jigglypuff\n",
                "\nYou did hide and seek with Jigglypuff\n",
                "\nYou played soccer with Jigglypuff\n",
                "\nYou played tag with Jigglypuff\n"]

    def decrease_health(self, time):
        """
        Overrides the tamagotchi's decrease_health function with Jigglypuff's own unique speed of decreasing.
        :param time: a float
        """
        super().decrease_health(self.base_amount, time)

    def decrease_happiness(self, time):
        """
        Overrides the tamagotchi's decrease_happiness function with Jigglypuff's own unique speed of decreasing
        :param time: a float
        """
        super().decrease_happiness(self.base_amount, time)

    def increase_hunger(self, time):
        """
        Overrides the tamagotchi's increase_hunger function with Jigglypuff's own uniqued speed of increasing
        :param time: a float
        """
        super().increase_hunger(self.base_amount, time)

    def give_food(self, food):
        """
        Overrides the tamagotchi's give_food function with Jigglypuff's own unique amount of decreasing hunge
        :param food: an int
        """
        super().give_food(food, self.preferred_food, self.hunger_decrease_amount)

    def play(self, play_input):
        """
        Overrides the tamagotchi's play function with Jigglypuff's own unique amount of increasing happiness
        :param play_input: an int
        """
        super().play(self.playlist[play_input], self.happiness_increase_amount)

    def born(self):
        """
        Prints a message that Jigglypuff was born
        :return:
        """
        super().born("Jigglypuff")

    def update_status(self):
        """
        Overrides the tamagotchi's update_status function with Jigglypuff's unique way of decreasing the
        health, happiness and increasing hunger
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
        Overrides the tamagotchi's is_sick function with Jigglypuff's standard value of getting sick
        :return: a boolean
        """
        return self._health < 60

    def __str__(self):
        """
        Prints Jigglypuff's status
        """
        if self._is_sick:
            return f"\nJigglypuff: health: {round(self._health)}, happiness: {round(self._happiness)}," \
                   f" hunger: {round(self._hunger)}, time elapsed: {self._time_elapsed}, Your tamagotchi is sick!\n"
        else:
            return f"\nJigglypuff: health: {round(self._health)}, happiness: {round(self._happiness)}," \
                f" hunger: {round(self._hunger)}, time elapsed: {self._time_elapsed}\n"
