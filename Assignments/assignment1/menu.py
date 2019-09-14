from tamagochi import Tamagochi
import random
import time
import datetime


class Menu:
    food = {1: "Apple", 2: "Orange", 3: "Kiwi"}
    character = []
    @staticmethod
    def welcome():
        print("\n#####################\n")
        print("Welcome to Tamagochi\n")
        print("#######################\n")

    @staticmethod
    def promptUser():
        print("Would you like to get one?")
        print("1. Yes")
        print("2. No")

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
        print("4. Give medicine")

    @classmethod
    def showStatus(cls):
        cls.character.updateStatus()
        if cls.character.isDead():
            Menu.promptUser()
            numberInput = int(input())
            if numberInput == 1:
                Menu.createTamagochi()
            else:
                print("Sorry to hear that...")
                exit()
        print(cls.character.getSick())

        #     print("Your tamagotchi is sick!")
        # print(datetime)
        cls.character.showStatus()

    @classmethod
    def feedFood(cls, number):
        selectedFood = cls.food.get(number)
        cls.character.giveFood(selectedFood)
        print("Great! Your tamagochi is happier than before!")

    @classmethod
    def giveMedicine(cls):
        cls.character.giveMedicine()
        print("Your tamagotchi recovered")

    @classmethod
    def play(cls):
        playInput = random.randint(0, 1)
        cls.character.play(playInput)
        print("Your tamagotchi seems happy!")


Menu.welcome()
Menu.promptUser()
numberInput = int(input())
if numberInput == 1:
    Menu.createTamagochi()
else:
    print("Sorry to hear that...")
    exit()
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
    elif optionInput == 3:
        Menu.play()
    elif optionInput == 4:
        Menu.giveMedicine()
    else:
        print("Invalid Input! Try again!")
