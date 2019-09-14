from tamagochi import Tamagochi


class Pikachu(Tamagochi):
    # decreaseRate = 1
    # increaseRate = 1
    # hungerBaseAmount = 1
    # pikachuHappinessAmount = 1
    # preferredFood = {"dogFood", "catFood"}

    def __init__(self, health=100, happiness=100, hunger=0, isAlive=100, lastChecked=0):
        super().__init__(
            health, happiness, hunger, isAlive)

    # def decreaseHealth():
    #     super().decreaseHealth()

    # @classmethod
    # def decreaseHappiness(cls):
    #     super().decreaseHappiness(cls.decreaseRate)

    # @classmethod
    # def increaseHunger(cls):
    #     super().increaseHunger(cls.increaseRate)

    # @classmethod
    # def giveFood(cls, food):
    #     super().giveFood(food, cls.hungerBaseAmount)

    # @classmethod
    # def play(cls, happinessAmount):
    #     super().play(cls.pikachuHappinessAmount)
