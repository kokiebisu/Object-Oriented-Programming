""" This module runs the sequence of instructions for the program to function"""
from wallet import Wallet
from card import CreditCard
from prompt import Prompt


class Controller:
    """
    This class deals with all the user interactions
    """
    def __init__(self):
        """ Initializes the Controller class """
        self._wallet = None
        self.run()

    def run(self):
        """
        Runs the program
        """
        Prompt.welcome()
        if Prompt.will_start():
            self._wallet = Wallet()
            print("\nSuccessfully created wallet")
            while True:
                try:
                    option_input = Prompt.display_options()
                    if option_input == 1:
                        self.add_card()
                    elif option_input == 2:
                        self.search_card()
                    elif option_input == 3:
                        self.delete_card()
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

    def add_card(self):
        """
        Calls the add_method inside the wallet with the retrieved input from the user
        """
        try:
            card_type = Prompt.prompt_card_type()
            if card_type == 1:
                card_information = Prompt.prompt_credit_card()
                name_input, account_number_input, security_code_input = card_information
                card = CreditCard(
                    name=name_input, account_number=account_number_input, security_code=security_code_input)
            else:
                raise ValueError
        except ValueError:
            print("Select from within the option!")
        else:
            self._wallet.add(card)
            print("Successfully added")

    def search_card(self):
        """
        Calls the search method inside the wallet with the retrieved input from the user
        """
        try:
            if not self._wallet.cards_list:
                raise EmptyWalletError("There are no cards to search in your wallet!")
            id_input = Prompt.prompt_id()
            self._wallet.search(id_input)
        except EmptyWalletError as e:
            print(e)

    def delete_card(self):
        """
        Calls the delete method inside the wallet with the retrieved input from the user
        """
        try:
            if not self._wallet.cards_list:
                raise EmptyWalletError("There are no cards to delete in your wallet!")
        except EmptyWalletError as e:
            print(e)
        else:
            id_input = Prompt.prompt_id()
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
                raise EmptyWalletError("There are no cards to export in your wallet!")
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
                raise EmptyWalletError("There are no cards to display in your wallet!")
        except EmptyWalletError as e:
            print(e)
        else:
            self._wallet.display_all_cards()


class EmptyWalletError(Exception):
    """
    An error called when the user tries to do something with an empty wallet
    """
    def __init__(self, name):
        """
        Initializes the wallet
        :param name: a string
        """
        super().__init__(name)
