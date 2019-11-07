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


class Journal(LibraryItem):
    def __init__(self, issue_number, publisher, **kwargs):
        """
        Initializes the instance created for Journal
        :param name: a string
        :param call_number: a string
        :param num_copies: an int
        :param issue_number: a string
        :param publisher: a string
        """
        self._issue_number = issue_number
        self._publisher = publisher
        super().__init__(**kwargs)

    def __str__(self):
        """
        String representation of the created object
        """
        return f"Category: {self.__class__.__name__}, Name: {self._name}, Issue Number: {self._issue_number}, Publisher: {self._publisher}, Number of Copies: {self._num_copies}"


class Dvd(LibraryItem):
    def __init__(self, release_date, region_code, **kwargs):
        """
        Initializes the instance for Dvd
        :param name: a string
        :param call_number: a string
        :param num_copies: an int
        :param release_date: a string
        :param region_code: a string
        """
        self._release_date = release_date
        self._region_code = region_code
        super().__init__(**kwargs)

    def __str__(self):
        return f"Category: {self.__class__.__name__}, Name: {self._name}, Release Date: {self._release_date}, Region Code: {self._region_code}, Number of Copies: {self._num_copies}"


class Book(LibraryItem):
    def __init__(self, author, **kwargs):
        """
        Initializes the instance of Book
        :param name: a string
        :param call_number: a string
        :param num_copies: an int
        :param author: a string
        """
        self._author = author
        super().__init__(**kwargs)

    def __str__(self):
        """
        String representation of the created Book object
        :return: a string
        """
        return f"Category: {self.__class__.__name__}, Name: {self._name}, Number of Copies: {self._num_copies}, Author: {self._author}"
