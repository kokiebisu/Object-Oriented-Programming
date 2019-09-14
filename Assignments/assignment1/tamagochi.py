import time
import datetime
import random
import datetime


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

    def decreaseHealth(self, amount, time):
        self._health = self._health - amount

    def decreaseHappiness(self, amount):
        self._happiness = self._happiness - time * rate

    def increaseHunger(self, amount):
        self._hunger = self._hunger - amount

    def giveFood(self, food, preferredFood, hungerAmount):
        if food in preferredFood:
            self._hunger = self._hunger - 1.1 * hungerAmount
        else:
            self._hunger = self._hunger - hungerAmount

    def born(self, character):
        print(f"Say hello to your new {character}!\n")

    def showStatus(self):
        print(self.__str__())

    def __str__(self):
        return f"Tamagochi here"


class Pikachu(Tamagochi):
    amount = 2
    rate = 1
    hungerBaseAmount = 1
    # pikachuHappinessAmount = 1
    preferredFood = {"dogFood", "catFood"}

    def __init__(self, health=100, happiness=100, hunger=0, isAlive=100, lastChecked=0):
        super().__init__(
            health, happiness, hunger, isAlive)

    def decreaseHealth(self):
        timeElapsed = datetime.datetime.now() - self._lastChecked
        super().decreaseHealth(self.amount, timeElapsed)

    def decreaseHappiness(self):
        super().decreaseHappiness(self.amount)

    def increaseHunger(self):
        super().increaseHunger(self.amount)

    def giveFood(self, food):
        super().giveFood(food, self.preferredFood, self.hungerBaseAmount)

    def updateStatus(self):
        self.decreaseHealth()

    def __str__(self):
        return f"\nPikachu: health: {self._health}, happiness: {self._happiness}, hunger: {self._hunger}, isAlive: {self._isAlive}, last_checked: {self._lastChecked}\n"
