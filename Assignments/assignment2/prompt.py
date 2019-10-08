""" This module holds all the prompts that will be asked the user """


class Prompt:
    """
    A Prompt class that holds all the messages used to interact with the user
    """

    @staticmethod
    def welcome():
        """
        Welcomes the user
        """
        print(
            "\nWelcome to the wallet\n"
        )

    @staticmethod
    def will_start():
        """
        Asks if the user want to start the program
        :return: a string
        """
        return input("Would you like to create a new wallet?\n").lower() == "yes"

    @staticmethod
    def display_options():
        """
        Displays the options available with the given wallet
        :return: an int
        """
        print(
            "\nWhat do you want to do?"
            "\n1. Add Card"
            "\n2. Search Card"
            "\n3. Delete Card"
            "\n4. Export Data"
            "\n5. Check All Cards"
            "\n6. Exit the program"
        )
        return int(input())

    @staticmethod
    def prompt_card_type():
        """
        Asks the user the type of card they want to add
        :return: an int
        """
        print(
            "\nWhat type of card is it?"
            "\n1. Credit Card"
            "\n2. Membership Card"
            "\n3. Gift Card"
            "\n4. Business Card"
            "\n5. Debit Card"
        )
        return int(input())

    @staticmethod
    def prompt_id():
        """
        Asks the user for the id of the card
        :return: an int
        """
        return int(input("What is the id of the card?\n"))
