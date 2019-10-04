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
        file_path = input().strip()
        if file_path:
            raise ValueError("Must have something!")
        return file_path

    @staticmethod
    def prompt_save():
        """
        Prompts the user if they would like to continue using the program
        :return: a boolean
        """
        print("Would you like to save?"
              "\n 1. Yes"
              "\n 2. No"
              )
        save_input = int(input())
        if save_input == 1:
            return True
        elif save_input == 2:
            return False
        else:
            raise ValueError("Must be either 1 or 2")
