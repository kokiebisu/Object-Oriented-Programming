from file_handler import FileHandler
import difflib
from pathlib import Path


class Dictionary:
    """
    This module is responsible for housing the dictionary class
    (alongside any custom exceptions that apply to the dictionary) and any driver methods
    that run the program
    """

    def __init__(self, filepath):
        self._data = {}
        self._terms = []
        self._line = None
        self.load_dictionary(filepath)

    def get_line(self):
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
        if word in self._terms:
            for key, item in self._data.items():
                if word == key:
                    definition = ''.join(self._data[key])
                    word_and_definition = [word, definition]
                    self.save(word_and_definition)
                    return definition

        else:
            close_word = difflib.get_close_matches(word, self._terms)
            if isinstance(close_word, list):
                return f"Did you mean from the following? {', '.join(close_word)}"
            else:
                return close_word

    def save(self, key_pair):
        term = key_pair[0]
        definition = key_pair[1]
        self._line = f"{term}: {definition}"
