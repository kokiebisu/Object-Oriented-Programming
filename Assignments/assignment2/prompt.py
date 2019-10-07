""" This module holds all the prompts that will be asked the user """


class Prompt:
    """
    A Prompt class that holds all the messages used to interact with the user
    """

    @staticmethod
    def welcome():
        """
        Welcomes the user
        :return:
        """
        print(
            "\nWelcome to the wallet"
        )

    @staticmethod
    def will_start():
        """
        Asks if the user want to start the program
        :return: a string
        """
        print(
            "\nWould you like to create a new wallet?"
        )
        return input().lower() == "yes"

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
        )
        return int(input())

    @staticmethod
    def prompt_credit_card():
        """
        Asks the user the card information to be stored
        :return: a list
        """
        print("What is the name of the card?")
        name_input = input()
        print("What is account number?")
        account_number_input = int(input())
        print("What is the security code?")
        security_code_input = int(input())
        return [name_input, account_number_input, security_code_input]

    @staticmethod
    def prompt_id():
        """
        Asks the user for the id of the card
        :return: an int
        """
        print("What is the id of the card?")
        return int(input())
