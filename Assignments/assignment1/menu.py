from tamagochi import Tamagochi
import random
import time
import datetime


class Menu:
    food = {1: "Apple", 2: "Orange", 3: "Kiwi"}
    character = []
    @staticmethod
    def prompt():

        print("\n#####################\n")
        print("Welcome to Tamagochi\n")
        print("#######################\n")
        print("You don't have a tamagochi yet? Would you like to get one?")
        print("1. Yes 2. No")

    @classmethod
    def createTamagochi(cls):
        print("creating tamagochi...\n")
        # time.sleep(3)
        cls.character = Tamagochi.spawn()
        cls.character.born(type(cls.character))

    @classmethod
    def showOptions(cls):
        print("What would you like to do?")
        print("1. Check the status")
        print("2. Feed your tamagotchi")
        print("3. Play with your tamagotchi")

    @classmethod
    def showStatus(cls):
        cls.character.updateStatus()
        print(datetime)
        cls.character.showStatus()

    @classmethod
    def feedFood(cls, number):
        selectedFood = cls.food.get(number)
        cls.character.giveFood(selectedFood)
        print("Great! Your tamagochi is happier than before!")


Menu.prompt()
numberInput = int(input())
if numberInput == 1:
    Menu.createTamagochi()
while True:
    Menu.showOptions()
    optionInput = int(input())
    if optionInput == 1:
        Menu.showStatus()
    elif optionInput == 2:
        print("Which food would you like to give?")
        print("1. Apple")
        print("2. Orange")
        print("3. Kiwi")
        foodInput = int(input())
        Menu.feedFood(foodInput)
