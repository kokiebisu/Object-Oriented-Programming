from tamagochi import Tamagochi
from pikachu import Pikachu
import random


class Menu:
    @staticmethod
    def prompt():
        print("Welcome to Tamagochi\n")
        print("You don't have a tamagochi yet? Would you like to get one?")
        print("1. Yes 2. No")

    @classmethod
    def createTamagochi(cls):
        cls.character = Tamagochi.spawn()
        cls.character.showStatus()
        cls.character.decreaseHealth()
        cls.character.decreaseHappiness()
        cls.character.increaseHunger()
        cls.character.showStatus()

    # @classmethod
    # def action(cls):
    #     cls.character.decreaseHealth()
    #     cls.character.showStatus()


Menu.createTamagochi()
# Menu.action()
