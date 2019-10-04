"""This module interacts with the dictionary"""
from file_handler import FileHandler, FileExtensions
import difflib
from pathlib import Path


class Dictionary:
    """
    This class contains the attributes of a dictionary with means to access it.
    """

    def __init__(self, filepath):
        """
        Initializes the instance of the Dictionary class
        """
        self._data = {}
        self._terms = []
        self._line = None
        self.load_dictionary(filepath)

    def get_line(self):
        """
        Gets the previous term and definition that was being searched
        :return: a string
        """
        return self._line

    def load_dictionary(self, filepath):
        """
        Loads data from file if it is valid
        """
        file_extension = Path(filepath).suffix
        try:
            self._data, self._terms = FileHandler.load_data(
                filepath, file_extension)
        except TypeError:
            print("OOPS! Cannot return the list!")
            exit()

    def query_definition(self, word):
        """
        Retrieves the definition of the given word
        :return: a string
        """
        try:
            if word in self._terms:
                for key, item in self._data.items():
                    if word == key:
                        definition = ''.join(self._data[key])
                        word_and_definition = [word, definition]
                        self.save(word_and_definition)
                        return definition
            else:
                raise WordNotFoundError(word, self._terms)
        except WordNotFoundError as e:
            return e

    def save(self, key_pair):
        """
        Assigns the term and definition previously searched to the dictionary's
        _line attribute
        """
        term = key_pair[0]
        definition = key_pair[1]
        self._line = f"{term}: {definition}"


class WordNotFoundError(Exception):
    """
    This exception should be raised if the user attempts to read a file that is not a .json or .txt file
    """

    def __init__(self, word, terms):
        self.incorrect_word = word
        phrase = self.get_close_match(word, terms)
        super().__init__(phrase)

    def get_close_match(self, word, terms):
        close_word = difflib.get_close_matches(word, terms)
        close_word_string = ', '.join(close_word)
        if ',' in close_word_string:
            return f"Can't find {self.incorrect_word}. Did you mean? {close_word_string}"
        else:
            return f"Sorry, I have no idea what you are looking for..."

