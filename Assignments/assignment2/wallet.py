from card import Card, CreditCard


class Wallet():
    def __init__(self):
        self.cards_list = {}

    def add(self, name, card):
        self.cards_list[name] = card
