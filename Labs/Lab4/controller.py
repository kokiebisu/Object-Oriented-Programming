from dictionary import Dictionary
from file_handler import FileHandler
from prompt import Prompt


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
        :return:
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
