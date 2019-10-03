from wallet import Wallet
from prompt import Prompt


class Controller:
    def __init__(self):
        self.run()

    def run(self):
        Prompt.welcome()
        if Prompt.will_start():
            wallet = Wallet()
            print("\nSuccessfully created wallet")
            option_input = Prompt.display_options()
            if option_input == 1:
                Prompt.prompt_card()
            elif option_input == 2:
                print("2")
            elif option_input == 3:
                print("3")
            elif option_input == 4:
                print("4")
            else:
                print("Invalid input")
