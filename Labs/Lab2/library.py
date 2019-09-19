from book import Book


class Library:

    book_list = {}

    @classmethod
    def return_book(cls, call_number):
        if Library.search(call_number):
            cls.book_list[call_number].num_copies += 1

    @classmethod
    def check_out(cls, call_number):
        if Library.search(call_number):
            cls.book_list[call_number].num_copies -= 1

    @classmethod
    def display_available_books(cls):
        # print out the list of books available
        for i in cls.book_list:
            print(cls.book_list[i])

    @classmethod
    def search(cls, call_number):
        for i in cls.book_list:
            if cls.book_list[i].call_number == call_number:
                return True
            else:
                print("Invalid Search")

    @classmethod
    def find_books(cls, call_number):
        # Haven't figured out yet
        for i in cls.book_list:
            if cls.book_list[i].call_number == call_number:
                return cls.book_list[i].title
        else:
            print("Invalid Call Number")

    @classmethod
    def add_book(cls, book):
        call_number = book.call_number
        # check if it is in booklist
        if Library.search(call_number):
            pass
        else:
            cls.book_list[call_number] = book

    @classmethod
    def remove_book(cls, call_number):
        if Library.search(call_number):
            del cls.book_list[call_number]


newBook = Book("title", "call_number", "author", "num_copies")
anotherBook = Book("title2", "call_number2", "author", "num_copies")
Library.add_book(newBook)
Library.add_book(anotherBook)
Library.remove_book("call_number")
print("-------")
Library.display_available_books()
