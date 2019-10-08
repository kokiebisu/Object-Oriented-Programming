""" This module runs the sequence of instructions for the program to function"""
from wallet import Wallet
from card import CreditCard, ExpiryCard, MemberShipCard, GiftCard, DebitCard, BusinessCard
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
                card = self.create_credit_card()
            elif card_type == 2:
                card = self.create_membership_card()
            elif card_type == 3:
                card = self.create_gift_card()
            elif card_type == 4:
                card = self.create_business_card()
            elif card_type == 5:
                card = self.create_debit_card()
            else:
                raise InvalidOptionError("Select from the given options!")
        except InvalidOptionError as e:
            print(e)
            self.add_card()
        else:
            self._wallet.add(card)
            print("Successfully added")

    def search_card(self, id_input):
        """
        Calls the search method inside the wallet with the retrieved input from the user
        """
        try:
            if not self._wallet.cards_list:
                raise EmptyWalletError(
                    "There are no cards to search in your wallet!")
            self._wallet.search(id_input)
        except EmptyWalletError as e:
            print(e)

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

    @staticmethod
    def create_credit_card():
        """
        Creates a credit card from the given inputs
        :return: a CreditCard object
        """
        name_input, account_number_input, security_code_input = CreditCard.get_input()
        expiry_date_input = ExpiryCard.get_input()
        return CreditCard(
            name=name_input, account_number=account_number_input, security_code=security_code_input, expiry_date=expiry_date_input)

    @staticmethod
    def create_membership_card():
        """
        Creates a membership card from the given inputs
        :return: a MembershipCard object
        """
        name_input, organization_input, membership_input = MemberShipCard.get_input()
        expiry_date_input = ExpiryCard.get_input()
        return MemberShipCard(name=name_input, organization=organization_input, membership_number=membership_input, expiry_date=expiry_date_input)

    @staticmethod
    def create_debit_card():
        """
        Creates a debit card from the given inputs
        :return: a DebitCard object
        """
        name_input, account_number_input, security_code_input = DebitCard.get_input()
        expiry_date_input = ExpiryCard.get_input()
        return DebitCard(name=name_input, account_number=account_number_input, security_code=security_code_input, expiry_date=expiry_date_input)

    @staticmethod
    def create_business_card():
        """
        Creates a business card from the given inputs
        :return: a BusinessCard object
        """
        name_input, company_input, email_address_input = BusinessCard.get_input()
        return BusinessCard(name=name_input, company=company_input, email_address=email_address_input)

    @staticmethod
    def create_gift_card():
        """
        Creates a gift card from the given inputs
        :return: a Gift Card object
        """
        name_input, amount_input, code_input = GiftCard.get_input()
        return GiftCard(name=name_input, amount=amount_input, code=code_input)

    def give_options(self, option_input):
        try:
            if option_input == 1:
                card_type = Prompt.prompt_card_type()
                self.add_card(card_type)
            elif option_input == 2:
                self.search_card()
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
