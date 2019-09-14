import time
import datetime
import random


class Tamagochi:
    def __init__(self, health=100, happiness=100, hunger=100, isAlive=True):
        self._health = health
        self._happiness = happiness
        self._hunger = hunger
        self._isAlive = True
        self._lastChecked = datetime.datetime.now()

    def spawn():
        pikachu = Pikachu(100, 100, 100, True)
        return pikachu

    def showStatus(self):
        print(self.__str__)

    def __str__(self):
        return f"Tamagochi here"


class Pikachu(Tamagochi):
    # decreaseRate = 1
    # increaseRate = 1
    # hungerBaseAmount = 1
    # pikachuHappinessAmount = 1
    # preferredFood = {"dogFood", "catFood"}

    def __init__(self, health=100, happiness=100, hunger=0, isAlive=100, lastChecked=0):
        super().__init__(
            health, happiness, hunger, isAlive)

    def showStatus(self):
        print(self.__str__())

    def decreaseHealth(self):
        self._health = self._health - 5

    def decreaseHappiness(self):
        self._happiness = self._happiness - 5

    def increaseHunger(self):
        self._hunger = self._hunger + 5

    def __str__(self):
        return f"Pikachu: health: {self._health}, happiness: {self._happiness}, hunger: {self._hunger}, isAlive: {self._isAlive}, last_checked: {self._lastChecked}"
