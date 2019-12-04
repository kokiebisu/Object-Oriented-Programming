""" A module that deals with Unit Tests of the DeEncryptor module"""
from unittest import TestCase
from question_1 import DeEncryptor


class TestDeEncryptor(TestCase):
    """
    Class that tests the DeEncryptor class
    """
    def test_convert_to_string_value_string_in_list(self):
        """
        Tests the case when a non-integer value was in the sequence of integers
        """
        encrypt = DeEncryptor()
        self.assertRaises(TypeError, encrypt.convert_to_string(["string"]))

    def test_convert_to_string_value_negative_value_in_list(self):
        """
        Tests the case when a negative value was in the sequence of integers
        """
        encrypt = DeEncryptor()
        self.assertRaises(ValueError, encrypt.convert_to_string([-1]))

    def test_convert_to_string_value_with_positive_value_in_list(self):
        """
        Tests the case when a negative value was in the sequence of integers
        """
        encrypt = DeEncryptor()
        self.assertEqual("H", encrypt.convert_to_string([72]))
