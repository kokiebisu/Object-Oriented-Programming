"""This module runs the program"""
from dictionary import Dictionary, Controller, Prompt


def main():
    """
    Starts the program
    """
    Prompt.welcome()
    filepath = Prompt.prompt_file_path()
    Controller(filepath)


if __name__ == '__main__':
    main()
