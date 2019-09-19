from book import Book


class Library:

    def return_book(call_number):
        if search(call_number):
            num_copies += 1

    def check_out(call_number):
        if search(call_number):
            num_copies -= 1

    def display_available_books():
        # print out the list of books available
        for i in book_list:
            print(book_list[i])

    @staticmethod
    def search(call_number):
        for i in book_list:
            if book_list[i].call_number == call_number:
                return True

    def print():
        print("something")


class Catalogue:
    # this booklist
    book_list = {}

    def find_books(call_number):
        # Haven't figured out yet
        if call_number in book_list:
            # do something if found
        else:
            print("Invalid Call Number")

    def add_book(book):
        # check if it is in booklist
        if Library.search(call_number):
            book_list.append()

    def remove_book(call_number):
        # if found in booklist
        Library.search()
        # delete from book_list
