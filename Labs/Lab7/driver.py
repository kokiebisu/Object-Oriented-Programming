from library import Library, Catalogue


def generating_item(catalogue):
    """
    Creates the item which will be added to the catalogue
    :param catalogue: an instance of catalogue
    """
    catalogue.add_item()


def prompt():
    """
    Asks the usr what actions they want to take
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
    generating_item(catalogue)

    while flag:
        prompt()
        option_input = int(input())
        if option_input == 1:
            Library.display_available_items(catalogue)
        elif option_input == 2:
            Library.return_item(catalogue)
        elif option_input == 3:
            Library.check_out_item(catalogue)
        elif option_input == 4:
            generating_item(catalogue)
        elif option_input == 5:
            Library.find_items(catalogue)
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
