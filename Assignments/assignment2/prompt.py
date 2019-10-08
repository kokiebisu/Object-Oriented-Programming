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

    # @staticmethod
    # def prompt_credit_card():
    #     """
    #     Asks the user the card information to be stored
    #     :return: a list
    #     """
    #     name_input = input("What is the name of the card?\n")
    #     account_number_input = int(input("What is the account number\n"))
    #     security_code_input = int(input("What is the security code?\n"))
    #     expiry_date_input = input("When is the expiry date?\n")
    #     return [name_input, account_number_input, security_code_input, expiry_date_input]

    # @staticmethod
    # def prompt_debit_card():
    #     """
    #     Asks the user the card information to be stored
    #     :return: a list
    #     """
    #     name_input = input("What is the name of the card?\n")
    #     account_number_input = int(input("What is the account number\n"))
    #     security_code_input = int(input("What is the security code?\n"))
    #     expiry_date_input = input("When is the expiry date?\n")
    #     return [name_input, account_number_input, security_code_input, expiry_date_input]

    # @staticmethod
    # def prompt_business_card():
    #     """
    #     Asks the user the card information to be stored
    #     :return: a list
    #     """
    #     name_input = input("Who's business card is it?\n")
    #     company_input = int(input("What is the name of the company?\n"))
    #     email_address_input = input("What is the email address?\n")
    #     return [name_input, company_input, email_address_input]

    # @staticmethod
    # def prompt_membership_card():
    #     name_input = input("What is the name of the card?\n")
    #     organization_input = input("What is the organization?\n")
    #     membership_input = input("What is the membership number?\n")
    #     expiry_date_input = input("When is the expiry date?\n")
    #     return [name_input, organization_input, membership_input, expiry_date_input]

    # @staticmethod
    # def prompt_gift_card():
    #     name_input = input("What is the name of the card?\n")
    #     amount_input = int(input("What is the amount?\n"))
    #     code_input = input("What is the code?\n")
    #     return [name_input, amount_input, code_input]

    @staticmethod
    def prompt_id():
        """
        Asks the user for the id of the card
        :return: an int
        """
        return int(input("What is the id of the card?\n"))
