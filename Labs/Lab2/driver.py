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
    # populate some books
    generating_books()

    # prompt choices
    prompt()

    option_input = int(input())

    if option_input == 1:
        Library.display_available_books()
    elif option_input == 2:
        call_number = retrieve_call_number()
        # Return book
    elif option_input == 3:
        call_number = retrieve_call_number()
        # Checkout book


if __name__ == '__main__':
    main()
