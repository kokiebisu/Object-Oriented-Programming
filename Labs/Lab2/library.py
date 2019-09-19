from book import Book
from journal import Journal
from dvd import Dvd


class Library:

    def return_item(identification, itemType):
        if Catalogue.search(identification) and itemType == "Book":
            Catalogue.item_list[identification].num_copies += 1
            print("Thank you for returning the book")
        elif Catalogue.search(identification) and itemType == "Journal":
            Catalogue.item_list[identification].num_copies += 1
            print("Thank you for returning the Journal")
        elif Catalogue.search(identification) and itemType == "Dvd":
            Catalogue.item_list[identification].num_copies += 1
            print("Thank you for returning the Dvd")
        else:
            print("item was not found")

    def check_out_item(call_number):
        if Catalogue.search(call_number):
            Catalogue.item_list[call_number].num_copies -= 1
            print("Please return your book by due date")

    def display_available_items():
        for i in Catalogue.item_list:
            print(Catalogue.item_list[i])

    def find_items(call_number):
        for i in Catalogue.item_list:
            if Catalogue.item_list[i].call_number == call_number:
                return Catalogue.item_list[i].title
        else:
            print("Invalid Call Number")


class LibraryItemGenerator:
    def prompt():
        print("Which type of item do you want to create?")
        print("1. Book")
        print("2. Journal")
        print("3. DVD")
        user_input = int(input())
        if user_input == 1:
            return Book("randomBook", "randomBook", "randomBook", 3)
        elif user_input == 2:
            return Journal("randomJournal", "randomJournal", "randomJournal", 3)
        elif user_input == 3:
            return Dvd("randomDvd", "randomDvd", "randomDvd", 3)
        else:
            print("Invalid Input")


class Catalogue:
    item_list = {}

    @classmethod
    def search(cls, identification):
        if identification in cls.item_list:
            return True

    @classmethod
    def add_to_list(cls, item):
        if isinstance(item, Book):
            identification = item.call_number
        elif isinstance(item, Journal):
            identification = item.issue_number
        else:
            identification = item.region_code

        if cls.search(identification):
            pass
        else:
            cls.item_list[identification] = item

    @classmethod
    def remove_book(cls, call_number):
        if Library.search(call_number):
            del cls.book_list[call_number]

    def add_item():
        created_item = LibraryItemGenerator.prompt()
        Catalogue.add_to_list(created_item)
