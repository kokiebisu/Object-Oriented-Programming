from tamagochi import Tamagochi
import random


class Menu:
    """
    A controller for the users to interact with the game. Users will be able to perform
    actions to the tamagotchi and take care of it by calling this class.
    """

    # Foods that the user can give to their tamagotchi
    food = {1: "Apple", 2: "Orange", 3: "Kiwi"}

    # The type of tamagotchi that will be spawned
    character = []

    @staticmethod
    def welcome():
        """
        Greets the user with a warm welcome
        """
        print("\n#####################\n")
        print("Welcome to Tamagochi\n")
        print("#######################\n")

    @staticmethod
    def prompt_user():
        """
        Asks the user if they want to create their own new tamagotchi
        """
        print("Would you like to get one?")
        print("1. Yes")
        print("2. No\n")

    @classmethod
    def create_tamagochi(cls):
        """
        Creates a tamagotchi of random type.
        """
        print("\nCreating Tamagochi...\n")
        # time.sleep(3)
        cls.character = Tamagochi.spawn()
        cls.character.born()

    @classmethod
    def show_options(cls):
        """
        Prompts the user what would they like to do with their tamaagotchi
        """
        print("What would you like to do?")
        print("1. Check the status")
        print("2. Feed your tamagotchi")
        print("3. Play with your tamagotchi")
        print("4. Give medicine\n")

    @classmethod
    def show_status(cls):
        """
        Shows the user the current status of the tamagotchi. If their tamagotchi died or got sic, it will be
        notified.
        """
        cls.character.update_status()
        if cls.character.is_dead():
            Menu.prompt_user()
            number_input = int(input())
            if number_input == 1:
                Menu.create_tamagochi()
            else:
                print("Sorry to hear that...")
                exit()
        if cls.character.is_sick():
            print("Your tamagotchi is sick!")

        cls.character.show_status()

    @classmethod
    def feed_food(cls, number):
        """
        Feeds food to the tamagotchi
        :param number: an int
        """
        selected_food = cls.food.get(number)
        cls.character.give_food(selected_food)
        print("\nGreat! Your tamagochi is happier than before!\n")

    @classmethod
    def give_medicine(cls):
        """
        Gives medicine to the tamagotchi
        """
        cls.character.give_medicine()
        print("\nYour tamagotchi recovered\n")

    @classmethod
    def play(cls):
        """
        Plays with the tamagotchi. Method of playing will be randomized.
        """
        play_input = random.randint(0, 2)
        cls.character.play(play_input)
        print("Your tamagotchi seems happy!\n")
