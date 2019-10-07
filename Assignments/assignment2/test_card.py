from unittest import TestCase
from wallet import Wallet
from card import CreditCard, MemberShipCard, GiftCard


class TestCard(TestCase):
    def test_credit_card_setup(self):
        self.wallet = Wallet()
        self.credit = CreditCard(name="Visa", account_number=10001, security_code=101)
        self.membership = MemberShipCard(name="Gym", organization="Ken's Gym", membership_number=1001)
        self.gift = GiftCard(name="Itunes", amount=30, code="SAF8F9SF3")

    def test_add(self):
        pass

    def test_delete(self):
        pass

    def test_search(self):
        pass

    def display_all_cards(self):
        pass

    def export(self):
        pass
