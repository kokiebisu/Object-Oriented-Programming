"""This module runs the program"""
from prompt import Prompt
from controller import Controller


def main():
    """
    Starts the program
    """
    Prompt.welcome()
    filepath = "./data.json" #Prompt.prompt_file_path()
    Controller(filepath)


if __name__ == '__main__':
    main()
