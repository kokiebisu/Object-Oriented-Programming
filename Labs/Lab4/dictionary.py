"""This module interacts with the dictionary"""
from file_handler import FileHandler
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
        """
        Assigns the term and definition previously searched to the dictionary's
        _line attribute
        """
        term = key_pair[0]
        definition = key_pair[1]
        self._line = f"{term}: {definition}"


class Controller:
    def __init__(self, file_path):
        """
        Initializes the Controller class
        """
        self.dictionary = Dictionary(file_path)
        self.run()

    @staticmethod
    def prompt_word():
        """
        Calls the word method of the Prompt class
        :return: a string
        """
        return Prompt.word()

    def get_saved_key_pair(self):
        """
        Calls the get_line method of the dictionary instance
        :return: a string
        """
        return self.dictionary.get_line()

    def search(self, word):
        """
        Calls the query definition method of the created dictionary instance
        :param word: a string
        :return: a string
        """
        definition = self.dictionary.query_definition(word)
        return definition

    def run(self):
        """
        Runs the program
        """
        will_continue = True
        while will_continue:
            option_input = Prompt.options()
            if option_input == 1:
                user_input = self.prompt_word()
                definition = self.search(user_input)
                print(f"{definition}\n")
                will_continue = Prompt.prompt_continue()
            elif option_input == 2:
                FileHandler.write_lines(
                    "./data.txt", self.get_saved_key_pair())
                print("Saved Successfully")
                Prompt.prompt_continue()
            else:
                print("Invalid Input")


class Prompt:
    @staticmethod
    def welcome():
        """
        Greets the users with a warm welcome
        """
        print("Welcome to the dictionary")

    @staticmethod
    def options():
        """
        Displays options to let users interact with the program
        :return: an int
        """
        print("\nWhat would you like to do?"
              "\n1. Search"
              "\n2. Add to textfile"
              )
        option_input = int(input())
        return option_input

    @staticmethod
    def word():
        """
        Prompts the user for the word they want to search
        :return: a string
        """
        print("What is the word? Type 'exitprogram' to quit.")
        word_input = input().lower()
        if word_input == 'exitprogram':
            exit()
        else:
            return word_input

    @staticmethod
    def prompt_file_path():
        """
        Prompts the user for the filepath in which they want to load the dictionary from
        :return: a string
        """
        print("Let us know which file you want to load!")
        file_path = input()
        return file_path

    @staticmethod
    def prompt_continue():
        """
        Prompts the user if they would like to continue using the program
        :return: a boolean
        """
        print("Would you like to continue?"
              "\n 1. Yes"
              "\n 2. No"
              )
        continue_input = int(input())
        if continue_input == 1:
            return True
        elif continue_input == 2:
            return False
        else:
            print("Invalid Input")
