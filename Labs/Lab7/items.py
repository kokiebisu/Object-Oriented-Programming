from abc import ABC, abstractstaticmethod


class LibraryItem(ABC):
    """
    The Abstracted class for specific objects Journal, Dvd, Book
    """

    def __init__(self, name, call_number, num_copies):
        """
        Initializes the created instance
        :param name: a string
        :param call_number: a string
        :param num_copies: an int
        """
        self._name = name
        self._call_number = call_number
        self._num_copies = num_copies

    def check_availability(self):
        """
        Checks if the item is available in the catalogue or not
        :return: a boolean
        """
        return self._num_copies == 0

    @staticmethod
    def create():
        """
        A method that returns the user input received for common attributes: name, call_number, num_copies
        :return: a list of inputs from user
        """
        print("What is the name?")
        name_input = input()
        print("What is the call number?")
        call_number_input = input()
        print("How many number of copies?")
        num_copies_input = int(input())
        return [name_input, call_number_input, num_copies_input]


class Journal(LibraryItem):
    def __init__(self, name, call_number, num_copies, issue_number, publisher):
        """
        Initializes the instance created for Journal
        :param name: a string
        :param call_number: a string
        :param num_copies: an int
        :param issue_number: a string
        :param publisher: a string
        """
        super().__init__(name, call_number, num_copies)
        self._issue_number = issue_number
        self._publisher = publisher

    @staticmethod
    def create():
        """
        Prompts user for the name, call number, number of copies, issue number and publisher of the book and creates one
        :return: an instance of journal
        """
        inputs = LibraryItem.create()
        print("What is the issue number?")
        issue_number_input = input()
        print("What is publisher?")
        publisher_input = input()
        return Journal(inputs[0], inputs[1], inputs[2], issue_number_input, publisher_input)

    def __str__(self):
        """
        String representation of the created object
        """
        return f"Journal: {self._name}, Call Number: {self._call_number}, Issue Number: {self._issue_number}, Publisher: {self._publisher}, Number of Copies: {self._num_copies}"


class Dvd(LibraryItem):
    def __init__(self, name, call_number, num_copies, release_date, region_code):
        """
        Initializes the instance for Dvd
        :param name: a string
        :param call_number: a string
        :param num_copies: an int
        :param release_date: a string
        :param region_code: a string
        """
        super().__init__(name, call_number, num_copies)
        self._release_date = release_date
        self._region_code = region_code

    @staticmethod
    def create():
        """
        Prompts the user for necessary input and creates a Dvd object
        :return: an instance of Dvd
        """
        inputs = LibraryItem.create()
        print("When is the release_date?")
        release_date_input = input()
        print("What is region code?")
        region_code_input = input()
        return Dvd(inputs[0], inputs[1],
                   inputs[2], release_date_input, region_code_input)

    def __str__(self):
        return f"DVD: {self._name}, Call Number: {self._call_number}, Release Date: {self._release_date}, Region Code: {self._region_code}, Number of Copies: {self._num_copies}"


class Book(LibraryItem):
    def __init__(self, name, call_number, num_copies, author):
        """
        Initializes the instance of Book
        :param name: a string
        :param call_number: a string
        :param num_copies: an int
        :param author: a string
        """
        super().__init__(name, call_number, num_copies)
        self._author = author

    @staticmethod
    def create():
        """
        Prompts the user for necessary input and craetes a Book object
        :return: an instance of Book
        """
        super().create()
        inputs = LibraryItem.create()
        print("Who is the author?")
        author_input = input()
        return Book(inputs[0], inputs[1],
                    inputs[2], author_input)

    def __str__(self):
        """
        String representation of the created Book object
        :return: a string
        """
        return f"Book: {self._name}, Call Number: {self._call_number}, Number of Copies: {self._num_copies}, Author: {self._author}"
