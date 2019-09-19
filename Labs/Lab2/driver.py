from library import Library
from book import Book


def generating_books():
    book1 = Book("Hamlet", "1", "Shakespeare", 4)
    book2 = Book("Justic", "3", "Marc Adams", 2)
    Library.add_book(book1)
    Library.add_book(book2)


def prompt():
    print("What is your option?")
    print("1: Display all books")
    print("2: Return a book")
    print("3: Checkout a book")


def retrieve_call_number():
    print("What is the call number of the book?")
    user_input = input()
    return user_input


def main():
    flag = True
    # populate some books
    generating_books()

    while flag:
        prompt()
        option_input = int(input())

        if option_input == 1:
            Library.display_available_books()
        elif option_input == 2:
            call_number = retrieve_call_number()
            Library.return_book(call_number)
        elif option_input == 3:
            call_number = retrieve_call_number()
            Library.check_out_book(call_number)

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
