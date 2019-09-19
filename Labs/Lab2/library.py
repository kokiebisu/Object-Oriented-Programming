from book import Book
from journal import Journal
from dvd import Dvd
import difflib


class Library:
    """This cl"""
    def return_item(identification, item_type):
        if Catalogue.search(identification) and item_type == "Book":
            Catalogue.item_list[identification].num_copies += 1
            print("Thank you for returning the book")
        elif Catalogue.search(identification) and item_type == "Journal":
            Catalogue.item_list[identification].num_copies += 1
            print("Thank you for returning the Journal")
        elif Catalogue.search(identification) and item_type == "Dvd":
            Catalogue.item_list[identification].num_copies += 1
            print("Thank you for returning the Dvd")
        else:
            similar_words = difflib.get_close_matches(identification, Catalogue.item_list)
            print("Nothing Found. Did you mean {}".format(similar_words))

    @staticmethod
    def check_out_item(identification):
        if Catalogue.search(identification):
            Catalogue.item_list[identification].num_copies -= 1
            print("Please return your book by due date")
        else:
            similar_words = difflib.get_close_matches(identification, Catalogue.item_list)
            print("Nothing Found. Did you mean {}".format(similar_words))

    @staticmethod
    def display_available_items():
        for i in Catalogue.item_list:
            print(Catalogue.item_list[i])

    @staticmethod
    def find_items(title):
        for i in Catalogue.item_list:
            if Catalogue.item_list[i].title == title:
                return Catalogue.item_list[i].title
        else:
            similar_words = difflib.get_close_matches(
                title, Catalogue.item_list)
            print("Nothing Found. Did you mean {}".format(similar_words))


class LibraryItemGenerator:
    @staticmethod
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

    @staticmethod
    def add_item():
        created_item = LibraryItemGenerator.prompt()
        Catalogue.add_to_list(created_item)
