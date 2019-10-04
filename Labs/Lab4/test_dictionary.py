"""
This module is responsible for unit testing the dictionary.py module
"""
import os
from unittest import TestCase
from dictionary import Dictionary
from file_handler import FileHandler


class TestDictionary(TestCase):
    def test_set_up(self):
        """Set up all the needed values for the test."""
        dictionary = Dictionary('../data.json')

    def test_valid_query(self):
        """Tests to see if the the querying the definition is implemented correctly"""
        data = 'Children word for "father".'
        dictionary = Dictionary('../data.json')
        value = dictionary.query_definition("dad")
        print(value)
        self.assertEquals(value, data)

    def test_not_found_query(self):
        """Tests to see if a wrong term queried will give an error"""
        data = "Sorry, I have no idea what you are looking for..."
        dictionary = Dictionary('../data.json')
        value = dictionary.query_definition("c1e2R")
        self.assertTrue(value, data)

    def test_dictionary_data_is_loaded(self):
        """Tests to see if the dictionary is loaded correctly"""
        dictionary = Dictionary('../data.json')
        self.assertTrue(len(dictionary._data) != 0)

    def test_dictionary_words_are_loaded(self):
        """Tests to see if the terms are being loaded correctly"""
        dictionary = Dictionary('../data.json')
        self.assertTrue(len(dictionary._terms) != 0)
