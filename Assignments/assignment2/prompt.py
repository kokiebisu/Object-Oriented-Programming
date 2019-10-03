class Prompt:
    @staticmethod
    def welcome():
        print(
            "\nWelcome to the wallet"
        )

    @staticmethod
    def will_start():
        print(
            "\nWould you like to create a new wallet?"
        )
        return input().lower() == "yes"

    @staticmethod
    def display_options():
        print(
            "\nWhat do you want to do?"
            "\n1. Add Card"
            "\n2. Search Card"
            "\n3. Delete Card"
            "\n4. Export Data"
        )
        return int(input())

    @staticmethod
    def prompt_card_type():
        print(
            "\nWhat type of card is it?"
            "\n1. Credit Card"
        )
        category_input = int(input())

    def prompt_credit_card():

        # @staticmethod
        # def options():
