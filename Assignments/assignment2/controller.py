""" This module runs the sequence of instructions for the program to function"""
from wallet import Wallet
from prompt import Prompt


class Controller:
    """
    This class deals with all the user interactions
    """

    def __init__(self):
        """ Initializes the Controller class """
        self._wallet = None

    def run(self):
        """
        Runs the program
        """
        Prompt.welcome()
        if Prompt.will_start():
            self._wallet = Wallet()
            print("\nSuccessfully created wallet")
            while True:
                option_input = Prompt.display_options()
                self.give_options(option_input)

    def add_card(self, card_type):
        """
        Calls the add_method inside the wallet with the retrieved input from the user
        """
        try:
            if card_type == 1:
                self.create_credit_card()
            elif card_type == 2:
                self.create_membership_card()
            elif card_type == 3:
                self.create_gift_card()
            elif card_type == 4:
                self.create_business_card()
            elif card_type == 5:
                self.create_debit_card()
            else:
                raise InvalidOptionError("Select from the given options!")
        except InvalidOptionError as e:
            print(e)
            self.add_card()
        else:
            print("Successfully added")

    def search_card(self, id_input):
        """
        Calls the search method inside the wallet with the retrieved input from the user
        """
        try:
            if not self._wallet.cards_list:
                raise EmptyWalletError(
                    "There are no cards to search in your wallet!")
        except EmptyWalletError as e:
            print(e)
        else:
            if not self._wallet.search(id_input):
                print("Cannot find id!")

    def delete_card(self, id_input):
        """
        Calls the delete method inside the wallet with the retrieved input from the user
        """
        try:
            if not self._wallet.cards_list:
                raise EmptyWalletError(
                    "There are no cards to delete in your wallet!")
        except EmptyWalletError as e:
            print(e)
        else:
            if self._wallet.delete(id_input):
                print("Successfully deleted")
            else:
                print("The ID you looked for is invalid")

    def export_card(self):
        """
        Calls the export method inside the wallet with the retrieved input from the user
        """
        try:
            if not self._wallet.cards_list:
                raise EmptyWalletError(
                    "There are no cards to export in your wallet!")
        except EmptyWalletError as e:
            print(e)
        else:
            self._wallet.export()
            print("Successfully exported")

    def check_cards(self):
        """
        Calls the display_all_cards method inside the wallet with the retrieved input from the user
        """
        try:
            if not self._wallet.cards_list:
                raise EmptyWalletError(
                    "There are no cards to display in your wallet!")
        except EmptyWalletError as e:
            print(e)
        else:
            self._wallet.display_all_cards()

    def create_credit_card(self):
        """
        Forwards the credit card information being added by the user to the wallet
        """
        try:
            name_input = input("What is the name of the card?\n")
            account_number_input = int(input("What is the account number\n"))
            security_code_input = int(input("What is the security code?\n"))
            expiry_date_input = int(input("When is the expiry date?\n"))
        except ValueError:
            print("There was an invalid value")
            self.create_credit_card()
        else:
            self._wallet.add_credit_card(
                [name_input, account_number_input, security_code_input, expiry_date_input])

    def create_membership_card(self):
        """
        Forwards the membership information being added by the user to the wallet
        """
        try:
            name_input = input("What is the name of the card?\n")
            organization_input = input("What is the organization?\n")
            membership_input = input("What is the membership number?\n")
            expiry_date_input = int(input("When is the expiry date?\n"))
        except ValueError:
            print("There was an invalid value")
            self.create_membership_card()
        else:
            self._wallet.add_membership_card(
                [name_input, organization_input, membership_input, expiry_date_input])

    def create_business_card(self):
        """
        Forwards the business information being added by the user to the wallet
        """
        try:
            name_input = input("Who's business card is it?\n")
            company_input = input("What is the name of the company?\n")
            email_address_input = input("What is the email address?\n")
        except ValueError:
            print("There was an invalid value")
            self.create_business_card()
        else:
            self._wallet.add_business_card(
                [name_input, company_input, email_address_input])

    def create_gift_card(self):
        """
        Forwards the giftcard information being added by the user to the wallet
        """
        try:
            name_input = input("What is the name of the card?\n")
            amount_input = int(input("What is the amount?\n"))
            code_input = input("What is the code?\n")
        except ValueError:
            print("There was an invalid value")
            self.create_gift_card()
        else:
            self._wallet.add_gift_card(
                [name_input, amount_input, code_input])

    def create_debit_card(self):
        """
        Forwards the debitcard information being added by the user to the wallet
        """
        try:
            name_input = input("What is the name of the card?\n")
            account_number_input = int(input("What is the account number\n"))
            security_code_input = int(input("What is the security code?\n"))
            expiry_date_input = int(input("What is the expiry_date"))
        except ValueError:
            print("There was an invalid value")
            self.create_debit_card()
        else:
            self._wallet.add_debit_card(
                [name_input, account_number_input, security_code_input, expiry_date_input])

    def give_options(self, option_input):
        """
        Displays the options for the users to select
        """
        try:
            if option_input == 1:
                card_type = Prompt.prompt_card_type()
                self.add_card(card_type)
            elif option_input == 2:
                id_input = Prompt.prompt_id()
                self.search_card(id_input)
            elif option_input == 3:
                id_input = Prompt.prompt_id()
                self.delete_card(id_input)
            elif option_input == 4:
                self.export_card()
            elif option_input == 5:
                self.check_cards()
            elif option_input == 6:
                print("See you next time")
                exit()
            else:
                raise ValueError
        except ValueError:
            print("Select from within the provided options!")


class EmptyWalletError(Exception):
    """
    An error called when the user tries to do something with an empty wallet
    """

    def __init__(self, name):
        """
        Initializes the error
        :param name: a string
        """
        super().__init__(name)


class InvalidOptionError(Exception):
    """
    An error called when the user tried to select an option that is not displayed
    """

    def __init__(self, name):
        """
        Initializes the error
        :param name: a string
        """
        super().__init__(name)
