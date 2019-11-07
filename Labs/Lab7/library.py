from items import JournalFactory, BookFactory, DvdFactory
import difflib


class Library:
    def __init__(self, catalogue):
        self.catalogue = catalogue

    def return_item(self):
        call_number_input = input("What is the call number? ")
        self.catalogue.increment_num_copies(call_number_input)

    def check_out_item(self):
        call_number_input = input("What is the call number? ")
        self.catalogue.decrement_num_copies(call_number_input)

    def display_available_items(self):
        for key, value in self.catalogue.items.items():
            print(f"Call Number: {key}, {value}")

    def find_items(self):
        name_input = input("What is the name? ")
        self.catalogue.search(name_input)

    def generate_item(self):
        item = LibraryItemGenerator.retrieve_common_attributes()
        self.catalogue.add_item(item)


class LibraryItemGenerator:
    @staticmethod
    def retrieve_common_attributes():
        print("Which type of item do you want to create?")
        print("1. Book")
        print("2. Journal")
        print("3. DVD")
        user_input = int(input())
        if user_input == 1:
            return BookFactory.create_item()
        elif user_input == 2:
            return JournalFactory.create_item()
        elif user_input == 3:
            return DvdFactory.create_item()
        else:
            print("Invalid Input")

    @staticmethod
    def get_common_information():
        call_number = input("What is the Call Number? ")
        title = input("What is the title?  ")
        num_copies = int(input("How many copies are there? "))
        bundle = [call_number, title, num_copies]
        return bundle

    @staticmethod
    def create_book():
        call_number, title, num_copies = LibraryItemGenerator.get_common_information()
        author = input("Who is the Author? ")
        return Book(call_number=call_number, name=title, num_copies=num_copies, author=author)

    @staticmethod
    def create_journal():
        call_number, title, num_copies = LibraryItemGenerator.get_common_information()
        publisher = input("Who is the publisher? ")
        issue_number = input("What is the issue number? ")
        return Journal(call_number=call_number, name=title, num_copies=num_copies, publisher=publisher, issue_number=issue_number)

    @staticmethod
    def create_dvd():
        call_number, title, num_copies = LibraryItemGenerator.get_common_information()
        release_date = input("When is the release date? ")
        region_code = input("What is the region code? ")
        return Dvd(call_number=call_number, name=title, num_copies=num_copies, release_date=release_date, region_code=region_code)


class Catalogue:

    def __init__(self):
        self.item_dict = {}

    @property
    def items(self):
        return self.item_dict

    def search(self, name_input):
        name_dict = {key: value._name for key, value in self.item_dict.items()}
        try:
            print(self.item_dict[name_input])
        except KeyError:
            similar_words = difflib.get_close_matches(
                name_input, name_dict.values())
            print(f"Nothing Found. Did you mean {similar_words}?")

    def check_if_exists(self, call_number):
        if call_number in self.item_dict.keys():
            return True

    def add_item(self, item):
        if self.check_if_exists(item._call_number):
            pass
        else:
            self.item_dict[item._call_number] = item

    def remove_book(self, call_number):
        if self.item_dict.search(call_number):
            del self.item_dict[call_number]

    def increment_num_copies(self, call_number_input):
        if call_number_input in self.item_dict.keys():
            self.item_dict[call_number_input]._num_copies += 1
        else:
            similar_words = difflib.get_close_matches(
                call_number_input, self.item_dict.keys())
            print(f"Nothing Found. Did you mean {similar_words}?")

    def decrement_num_copies(self, call_number_input):
        if call_number_input in self.item_dict.keys():
            self.item_dict[call_number_input]._num_copies -= 1
        else:
            similar_words = difflib.get_close_matches(
                call_number_input, self.item_dict.keys())
            print(f"Nothing Found. Did you mean {similar_words}?")
