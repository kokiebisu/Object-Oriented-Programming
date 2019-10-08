""" This module interacts with the cards """
from datetime import datetime
from card import Card


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

    def delete(self, id_):
        """
        Deletes the card based on the id given by the user
        :param id_: an int
        """
        for card in self._cards_list:
            if card.id == id_:
                print(f"id: {card.id}")
                index = self._cards_list.index(card)
                print(f"index: {index}")
                self._cards_list.pop(index)
        for card in self._cards_list:
            if self._cards_list.index(card) >= index:
                card.id -= 1
        if not self._cards_list:
            Card.card_id = 0

        return True

    def search(self, id_):
        """
        Prints the card information based on the id given by the user
        :param id_: an int
        """
        for card in self._cards_list:
            if card.id == id_:
                print(card)

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
        return len(self._cards_list)

    @property
    def cards_list(self):
        return self._cards_list
