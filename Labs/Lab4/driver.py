from controller import Controller
from prompt import Prompt

def main():
    """
    Starts the program
    """
    Prompt.welcome()
    filepath = Prompt.prompt_file_path()
    Controller(filepath)


if __name__ == '__main__':
    main()
