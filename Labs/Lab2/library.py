from items import Journal, Dvd, Book
import difflib


class Library:
    @staticmethod
    def return_item(catalogue):
        print("What is the call number?")
        call_number_input = input()
        if catalogue.search(call_number_input):
            for item in catalogue.item_list:
                if catalogue.item_list[item]._call_number == call_number_input:
                    catalogue.item_list[item]._num_copies += 1;
        else:
            similar_words = difflib.get_close_matches(call_number_input, catalogue.item_list)
            print("Nothing Found. Did you mean {}".format(similar_words))



    @staticmethod
    def check_out_item(catalogue):
        print("What is the call number?")
        call_number_input = input()
        if catalogue.search(call_number_input):
            for item in catalogue.item_list:
                if catalogue.item_list[item]._call_number == call_number_input:
                    catalogue.item_list[item]._num_copies -= 1;
        else:
            similar_words = difflib.get_close_matches(call_number_input, catalogue.item_list)
            print("Nothing Found. Did you mean {}".format(similar_words))

    @staticmethod
    def display_available_items(catalogue):
        for i in catalogue.item_list:
            print(catalogue.item_list[i])

    @staticmethod
    def find_items(catalogue):
        print("What is the name?")
        name_input = input()
        if name_input in catalogue.item_list:
            for i in catalogue.item_list:
                if catalogue.item_list[i]._name == name_input:
                    print(catalogue.item_list[i])
        else:
            similar_words = difflib.get_close_matches(name_input, catalogue.item_list)
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
            return Book.create()
        elif user_input == 2:
            return Journal.create()
        elif user_input == 3:
            return Dvd.create()
        else:
            print("Invalid Input")


class Catalogue:

    def __init__(self):
        self.item_list = {}

    def search(self, call_number):
        if call_number in self.item_list:
            return True

    def add_to_list(self, item):
        if self.search(item._call_number):
            pass
        else:
            self.item_list[item._call_number] = item


    def remove_book(self, call_number):
        if Library.search(call_number):
            del self.item_list[call_number]

    def add_item(self):
        created_item = LibraryItemGenerator.prompt()
        self.add_to_list(created_item)
