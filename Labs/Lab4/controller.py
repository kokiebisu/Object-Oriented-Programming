from dictionary import Dictionary
from prompt import Prompt
from file_handler import FileHandler

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
            user_input = self.prompt_word()
            definition = self.search(user_input)
            print(f"{definition}\n")
            will_save = Prompt.prompt_save()
            if will_save:
                FileHandler.write_lines(
                        "./data.txt", self.get_saved_key_pair())
                print("Saved Successfully")

