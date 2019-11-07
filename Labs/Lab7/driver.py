from library import Library, Catalogue


def prompt() -> None:
    """
    Asks the user what actions they want to take
    """
    print("What is your option?")
    print("1: Display all items")
    print("2: Return a item")
    print("3: Checkout a item")
    print("4: Add new Item")
    print("5: Find item")


def main():
    """
    Runs the program
    """
    flag = True
    catalogue = Catalogue()
    library = Library(catalogue)
    while flag:
        prompt()
        option_input = int(input())
        if option_input == 1:
            library.display_available_items()
        elif option_input == 2:
            library.return_item()
        elif option_input == 3:
            library.check_out_item()
        elif option_input == 4:
            library.generate_item()
        elif option_input == 5:
            library.find_items()
        else:
            print("Invalid input")

        print("Would you like to continue?")
        print("1. Yes")
        print("2. No")
        continue_input = int(input())
        if continue_input == 1:
            pass
        elif continue_input == 2:
            flag = False
        else:
            print("Invalid Input")


if __name__ == '__main__':
    main()
