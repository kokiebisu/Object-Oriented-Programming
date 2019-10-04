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
        """Test whether or not the dictionary queries correct definition."""
        data = 'Children word for "father".'
        dictionary = Dictionary('../data.json')
        value = dictionary.query_definition("dad")
        print(value)
        self.assertEquals(value, data)

    def test_not_found_query(self):
        """Test whether or not an invalid word is handled properly."""
        data = "Sorry, I have no idea what you are looking for..."
        dictionary = Dictionary('../data.json')
        value = dictionary.query_definition("c1e2R")
        string = value
        self.assertTrue(string, data)

    def test_dictionary_data_is_loaded(self):
        """Test whether or not the dictionary data is loaded."""
        dictionary = Dictionary('../data.json')
        self.assertTrue(len(dictionary._data) != 0)

    def test_dictionary_words_are_loaded(self):
        """Test whether or not the dictionary words are loaded."""
        dictionary = Dictionary('../data.json')
        self.assertTrue(len(dictionary._data) != 0)
