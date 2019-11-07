from items import LibraryItem, LibraryItemFactory, JournalFactory, BookFactory, DvdFactory
import difflib


class Catalogue:
    def __init__(self) -> None:
        """
        Initializes the catalogue object
        """
        self.item_dict = {}

    @property
    def items(self) -> dict:
        """
        Gets the dictionary attribute of the catalogue object
        :return: a dictionary
        """
        return self.item_dict

    def search(self, name_input: str) -> None:
        """
        Searches through the category to find if there is an item with same name
        :param name_input: a string
        """
        name_dict = {key: value.name for key, value in self.item_dict.items()}
        print("here")
        try:
            print(self.item_dict[name_input])
        except KeyError:
            similar_words = difflib.get_close_matches(
                name_input, name_dict.values())
            print(f"Nothing Found. Did you mean {similar_words}?")

    def check_if_exists(self, call_number: str) -> bool:
        """
        Check if an item exi
        :param call_number: a string
        :return: a bool
        """
        if call_number in self.item_dict.keys():
            return True

    def add_item(self, item: LibraryItem) -> None:
        """
        Adds item to catalogue if it doesn't exist in the catalogue
        :param item: a library item
        """
        if self.check_if_exists(item.call_number):
            pass
        else:
            self.item_dict[item.call_number] = item

    def remove_book(self, call_number: int) -> None:
        """
        Removes the book by call number
        :param call_number: a string
        """
        if self.item_dict.search(call_number):
            del self.item_dict[call_number]

    def increment_num_copies(self, call_number_input: str) -> None:
        """
        Increment the number of copies for specified item
        :param call_number_input: a string
        """
        if call_number_input in self.item_dict.keys():
            self.item_dict[call_number_input].num_copies += 1
        else:
            similar_words = difflib.get_close_matches(
                call_number_input, self.item_dict.keys())
            print(f"Nothing Found. Did you mean {similar_words}?")

    def decrement_num_copies(self, call_number_input: str) -> None:
        """
        Decrement the number of copies for specified item
        :param call_number_input: a string
        """
        if call_number_input in self.item_dict.keys():
            self.item_dict[call_number_input].num_copies -= 1
        else:
            print("not")
            similar_words = difflib.get_close_matches(
                call_number_input, self.item_dict)
            print(f"Nothing Found. Did you mean {similar_words}?")


class Library:
    def __init__(self, catalogue: Catalogue) -> None:
        """
        Initializes the library object
        :param catalogue: a catalogue object
        """
        self.catalogue = catalogue

    def return_item(self) -> None:
        """
        Returns the item to the library
        """
        call_number_input = input("What is the call number? ")
        self.catalogue.increment_num_copies(call_number_input)

    def check_out_item(self) -> None:
        """
        Checks out the item from the library
        """
        call_number_input = input("What is the call number? ")
        self.catalogue.decrement_num_copies(call_number_input)

    def display_available_items(self) -> None:
        """
        Prints all the available items in the library
        """
        for value in self.catalogue.items.values():
            print(f"{value}")

    def find_items(self) -> None:
        """
        Finds the item by the name
        """
        name_input = input("What is the name? ")
        self.catalogue.search(name_input)

    def generate_item(self) -> None:
        """
        Creates the item to be added to the catalogue
        """
        factory = LibraryItemGenerator().register_item()
        self.catalogue.add_item(factory.create_item())


class LibraryItemGenerator:
    def __init__(self) -> None:
        """
        Initializes the library item generator object
        """
        self.choice_factory_mapping = {
            1: BookFactory,
            2: JournalFactory,
            3: DvdFactory
        }

    def register_item(self) -> LibraryItemFactory:
        """
        Checks which kind of item the user wants to create
        :return: a LibraryItemFactory object
        """
        print("Which type of item do you want to create?")
        print("1. Book")
        print("2. Journal")
        print("3. DVD")
        user_input = int(input())
        factory_class = self.choice_factory_mapping.get(user_input, None)
        return factory_class()
