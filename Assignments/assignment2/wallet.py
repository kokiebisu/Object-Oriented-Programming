""" This module interacts with the cards """
from datetime import datetime
from card import Card, CreditCard, DebitCard, BusinessCard, MemberShipCard, GiftCard


class Wallet:
    """
    A Wallet that holds a list of cards. It can perform tasks on the cards you hold.
    """

    def __init__(self):
        """
        Initializes the Wallet class.
        """
        self._cards_list = []

    def add(self, card):
        """
        Adds a card given by the user to the wallet
        :param card: a Card object
        """
        self._cards_list.append(card)
        self.reassign_id()

    def delete(self, id_):
        """
        Deletes the card based on the id given by the user
        :param id_: an int
        """
        temp = [card for card in self._cards_list if card.id != id_]
        if temp == self._cards_list:
            return False
        else:
            self._cards_list = temp
            self.reassign_id()
            if not self._cards_list:
                Card.card_id = 0
            return True

    def search(self, id_):
        """
        Prints the card information based on the id given by the user
        :param id_: an int
        """
        try:
            for card in self._cards_list:
                if card.id == id_:
                    print(card)
                    return True
            return False
        except ValueError:
            print("Invalid Value! Must be a integer!")

    def display_all_cards(self):
        """
        Displays all the cards you have stored in your wallet
        """
        for card in self._cards_list:
            print(card)

    def export(self):
        """
        Exports the card you hold into a text file
        """
        date_time = datetime.now().strftime("%m%d%Y_%H%M")
        with open(f"./Wallet_Export_{date_time}.txt", 'w') as write_file:
            for item in self._cards_list:
                write_file.write("%s\n" % item)

    def __len__(self):
        """
        Returns the size of the list of cards the wallet holds
        :return: an int
        """
        return len(self._cards_list)

    @property
    def cards_list(self):
        """
        Gets the list of cards the wallet instance holds
        :return: a list
        """
        return self._cards_list

    def add_credit_card(self, card_inputs):
        """
        Adds a credit card from the given inputs
        :return: a CreditCard object
        """
        name_input, account_number_input, security_code_input, expiry_date_input = card_inputs
        self.add(CreditCard(
            name=name_input, account_number=account_number_input, security_code=security_code_input, expiry_date=expiry_date_input))

    def add_debit_card(self, card_inputs):
        """
        Adds a debit card from the given inputs
        :return: a DebitCard object
        """
        name_input, account_number_input, security_code_input, expiry_date_input = card_inputs
        self.add(DebitCard(
            name=name_input, account_number=account_number_input, security_code=security_code_input, expiry_date=expiry_date_input))

    def add_membership_card(self, card_inputs):
        """
        Adds a membership card from the given inputs
        :return: a MembershipCard object
        """
        name_input, organization_number_input, membership_input, expiry_date_input = card_inputs
        self.add(MemberShipCard(
            name=name_input, organization=organization_number_input, membership_number=membership_input, expiry_date=expiry_date_input))

    def add_business_card(self, card_inputs):
        """
        Adds a business card from the given inputs
        :return: a BusinessCard object
        """
        name_input, company_input, email_address_input = card_inputs
        self.add(BusinessCard(
            name=name_input, company=company_input, email_address=email_address_input))

    def add_gift_card(self, card_inputs):
        """
        Adds a gift card from the given inputs
        :return: a GiftCard object
        """
        name_input, amount_input, code_input = card_inputs
        self.add(GiftCard(
            name=name_input, amount=amount_input, code=code_input))

    def reassign_id(self):
        """
        Reassigns the id based on the order of the updated card list
        """
        number = 0
        for card in self._cards_list:
            card._id = number
            number += 1
