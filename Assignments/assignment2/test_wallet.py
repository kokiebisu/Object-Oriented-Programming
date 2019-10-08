from unittest import TestCase
from controller import Controller, EmptyWalletError


class TestWallet(TestCase):
    def test_empty_delete(self):
        self.controller = Controller()
        self.assertRaises(EmptyWalletError, self.controller.delete_card())
