from library import Library, Catalogue
from book import Book


def generating_item():
    Catalogue.add_item()


def prompt():
    print("What is your option?")
    print("1: Display all items")
    print("2: Return a item")
    print("3: Checkout a item")
    print("4: Add new Item")


def retrieve_item_type():
    print("What type of item is it?")
    print("1. Book")
    print("2. Journal")
    print("3. DVD")
    item_input = int(input())
    if item_input == 1:
        return "Book"
    elif item_input == 2:
        return "Journal"
    else:
        return "DVD"


def retrieve_identification_code(item_input):
    if item_input == "Book":
        print("What is the call number?")
        return input()
    elif item_input == "Journal":
        print("What is the Issue Number?")
        return input()
    elif item_input == "Dvd":
        print("What is the Region Code?")
        return input()
    else:
        print("Invalid input")


def main():
    flag = True

    generating_item()

    while flag:
        prompt()
        option_input = int(input())
        itemType = retrieve_item_type()
        if option_input == 1:
            Library.display_available_items()
        elif option_input == 2:
            identification = retrieve_identification_code(itemType)
            Library.return_item(identification, itemType)
        elif option_input == 3:
            identification = retrieve_identification_code(itemType)
            Library.check_out_item(identification)
        elif option_input == 4:
            generating_item()
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
