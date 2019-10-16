from unittest import TestCase
from controller import Controller, EmptyWalletError, InvalidOptionError
from wallet import Wallet
from card import CreditCard, DebitCard, GiftCard, MemberShipCard, BusinessCard


class TestController(TestCase):
    def test_wallet_add_credit_card(self):
        self.controller = Controller()
        self.controller._wallet = Wallet()
        card = CreditCard(name="Visa", account_number="10001", security_code="101", expiry_date="2019-10-01")
        self.controller._wallet.add(card)
        self.assertEqual(len(self.controller._wallet), 1)

    def test_wallet_add_debit_card(self):
        self.controller = Controller()
        self.controller._wallet = Wallet()
        card = DebitCard(name="MasterCard", account_number="10001", security_code="101", expiry_date="2019-10-01")
        self.controller._wallet.add(card)
        self.assertEqual(len(self.controller._wallet), 1)

    def test_wallet_add_gift_card(self):
        self.controller = Controller()
        self.controller._wallet = Wallet()
        card = GiftCard(name="Itunes", amount=30.0, code="234SDAF3")
        self.controller._wallet.add(card)
        self.assertEqual(len(self.controller._wallet), 1)

    def test_wallet_add_membership_card(self):
        self.controller = Controller()
        self.controller._wallet = Wallet()
        card = MemberShipCard(name="Gym", organization="Actos", membership_number="3248930284", expiry_date="2019-10-01")
        self.controller._wallet.add(card)
        self.assertEqual(len(self.controller._wallet), 1)

    def test_wallet_add_business_card(self):
        self.controller = Controller()
        self.controller._wallet = Wallet()
        card = BusinessCard(name="Ken", company="BCIT", email_address="kokiebisu@gmail.com")
        self.controller._wallet.add(card)
        self.assertEqual(len(self.controller._wallet), 1)

    def test_wallet_delete(self):
        self.controller = Controller()
        self.controller._wallet = Wallet()
        card = CreditCard(name="Visa", account_number="10001", security_code="101", expiry_date="2019-10-01")
        self.controller._wallet.add(card)
        self.controller.delete_card(card._id)
        self.assertTrue(not self.controller._wallet._cards_list)

    def test_invalid_number_option(self):
        self.controller = Controller()
        self.assertRaises(InvalidOptionError, self.controller.give_options(7))

    def test_invalid_type_option(self):
        self.controller = Controller()
        self.assertRaises(InvalidOptionError, self.controller.give_options("string"))

    def test_empty_wallet_delete(self):
        self.controller = Controller()
        self.controller._wallet = Wallet()
        index = 0
        self.assertRaises(EmptyWalletError, self.controller.delete_card(index))

    def test_empty_wallet_search(self):
        self.controller = Controller()
        self.controller._wallet = Wallet()
        self.assertRaises(EmptyWalletError, self.controller.search_card(0))

    def test_empty_wallet_export(self):
        self.controller = Controller()
        self.controller._wallet = Wallet()
        self.assertRaises(EmptyWalletError, self.controller.export_card())
