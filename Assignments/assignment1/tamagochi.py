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
        pikachu = Pikachu(100, 100, 0, True)
        return pikachu

    def decreaseHealth(self, amount, time):
        self._health = self._health - amount * time

    def decreaseHappiness(self, amount, time):
        self._happiness = self._happiness - amount * time

    def increaseHunger(self, amount, time):
        self._hunger = self._hunger + amount * time

    def giveFood(self, food, preferredFood, hungerAmount):
        if food in preferredFood:
            self._hunger = self._hunger - 1.1 * hungerAmount
        else:
            self._hunger = self._hunger - hungerAmount
        if self._hunger <= 0:
            self._hunger = 0

    def play(self, happinessAmount):
        self._happiness = self._happiness + happinessAmount

    def born(self, character):
        print(f"Say hello to your new {character}!\n")

    def die(self):
        self._isAlive = False

    def showStatus(self):
        print(self.__str__())

    def isDead(self):
        if self._health <= 0:
            print("Oh No! Your tamagochi died!")
            self.die()
            return True

    def isSick(self, sickValue):
        if self._health < sickValue:
            return True

    def __str__(self):
        return f"Tamagochi here"


class Pikachu(Tamagochi):
    amount = 2
    rate = 1
    happinessAmount = 100
    hungerBaseAmount = 100
    pikachuSick = 60
    # pikachuHappinessAmount = 1
    preferredFood = {"Apple", "Orange"}

    def __init__(self, health=100, happiness=100, hunger=0, isAlive=100, lastChecked=0):
        super().__init__(
            health, happiness, hunger, isAlive)

    def decreaseHealth(self, time):
        super().decreaseHealth(self.amount, time)

    def decreaseHappiness(self, time):
        super().decreaseHappiness(self.amount, time)

    def increaseHunger(self, time):
        super().increaseHunger(self.amount, time)

    def giveFood(self, food):
        super().giveFood(food, self.preferredFood, self.hungerBaseAmount)

    def play(self):
        super().play(self.happinessAmount)

    def updateStatus(self):
        timeElapsed = datetime.datetime.now() - self._lastChecked
        timeElapsedInSeconds = timeElapsed.total_seconds()
        self.decreaseHealth(timeElapsedInSeconds)
        self.decreaseHappiness(timeElapsedInSeconds)
        self.increaseHunger(timeElapsedInSeconds)
        self._lastChecked = datetime.datetime.now()

    def isSick(self):
        super().isSick(self.pikachuSick)

    def __str__(self):
        return f"\nPikachu: health: {round(self._health)}, happiness: {round(self._happiness)}, hunger: {round(self._hunger)}\n"
