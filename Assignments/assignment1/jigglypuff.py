from tamagochi import Tamagochi
import datetime

class Jigglypuff(Tamagochi):
    amount = 2
    rate = 1
    happinessAmount = 40
    hungerBaseAmount = 60
    jigglypuffSick = 60
    # pikachuHappinessAmount = 1
    preferredFood = {"Apple", "Orange"}
    playList = ["You played a game with Jigglypuff",
                "You did hide and seek with Jigglypuff",
                "You played soccer with Jigglypuff"]

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

    def play(self, playInput):
        super().play(self.playList[playInput], self.happinessAmount)

    def updateStatus(self):
        timeElapsed = datetime.datetime.now() - self._lastChecked
        timeElapsedInSeconds = timeElapsed.total_seconds()
        self._timeElapsed = timeElapsed
        self.decreaseHealth(timeElapsedInSeconds)
        self.decreaseHappiness(timeElapsedInSeconds)
        self.increaseHunger(timeElapsedInSeconds)
        self._lastChecked = datetime.datetime.now()

    def isSick(self):
        super().isSick(self.jigglypuffSick)

    def __str__(self):
        return f"\nJigglypuff: health: {round(self._health)}, happiness: {round(self._happiness)}, hunger: {round(self._hunger)}, time elapsed: {self._timeElapsed}\n"
