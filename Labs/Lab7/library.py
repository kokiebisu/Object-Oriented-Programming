from items import LibraryItemFactory, JournalFactory, BookFactory, DvdFactory
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
        factory = LibraryItemGenerator().register_item()
        self.catalogue.add_item(factory.create_item())


class LibraryItemGenerator:
    def __init__(self):
        self.choice_factory_mapping = {
            1: BookFactory,
            2: JournalFactory,
            3: DvdFactory
        }

    def register_item(self) -> LibraryItemFactory:
        print("Which type of item do you want to create?")
        print("1. Book")
        print("2. Journal")
        print("3. DVD")
        user_input = int(input())
        factory_class = self.choice_factory_mapping.get(user_input, None)
        return factory_class()


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
