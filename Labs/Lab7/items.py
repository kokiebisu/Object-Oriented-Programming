import abc


class LibraryItem(abc.ABC):
    """
    The Abstracted class for specific objects Journal, Dvd, Book
    """

    @abc.abstractmethod
    def __init__(self, name: str, call_number: int, num_copies: int) -> None:
        """
        Initializes the created instance
        :param name: a string
        :param call_number: an int
        :param num_copies: an int
        """
        self._name = name
        self._call_number = call_number
        self._num_copies = num_copies

    def check_availability(self) -> bool:
        """
        Checks if the item is available in the catalogue or not
        :return: a boolean
        """
        return self._num_copies == 0

    def __str__(self):
        return f"Name: {self._name}, Call Number: {self._call_number}, Number of Copies: {self._num_copies}"


class Journal(LibraryItem):
    def __init__(self, issue_number: int, publisher: str, **kwargs) -> None:
        """
        Initializes the instance created for Journal
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
        return f"Category: {self.__class__.__name__}, {super().__str__()}, Issue Number: {self._issue_number}, Publisher: {self._publisher}"


class Dvd(LibraryItem):
    def __init__(self, release_date: str, region_code: str, **kwargs) -> None:
        """
        Initializes the instance for Dvd
        :param release_date: a string
        :param region_code: a string
        """
        self._release_date = release_date
        self._region_code = region_code
        super().__init__(**kwargs)

    def __str__(self):
        return f"Category: {self.__class__.__name__}, {super().__str__()}, Release Date: {self._release_date}, Region Code: {self._region_code}"


class Book(LibraryItem):
    def __init__(self, author: str, **kwargs) -> None:
        """
        Initializes the instance of Book
        :param author: a string
        """
        self._author = author
        super().__init__(**kwargs)

    def __str__(self):
        """
        String representation of the created Book object
        :return: a string
        """
        return f"Category: {self.__class__.__name__}, {super().__str__()}, Author: {self._author}"


class LibraryItemFactory(abc.ABC):
    @abc.abstractmethod
    def create_item(self) -> LibraryItem:
        pass


class BookFactory(LibraryItemFactory):
    def create_item(self) -> LibraryItem:
        name_input = input("What is the name? ")
        call_number_input = int(input("What is the call number? "))
        num_copies_input = int(input("How many number of copies are there? "))
        author_input = input("Who is the author? ")
        return Book(name=name_input, call_number=call_number_input, num_copies=num_copies_input, author=author_input)


class JournalFactory(LibraryItemFactory):
    def create_item(self) -> LibraryItem:
        name_input = input("What is the name? ")
        call_number_input = int(input("What is the call number? "))
        num_copies_input = int(input("How many number of copies are there? "))
        issue_number_input = int(input("What is the issue number? "))
        publisher_input = int(input("Who is the publisher? "))
        return Journal(name=name_input, call_number=call_number_input, num_copies=num_copies_input, issue_number=issue_number_input, publisher=publisher_input)


class DvdFactory(LibraryItemFactory):
    def create_item(self, name, call_number, num_copies, release_date, region_code) -> LibraryItem:
        name_input = input("What is the name? ")
        call_number_input = int(input("What is the call number? "))
        num_copies_input = int(input("How many number of copies are there? "))
        release_date_input = input("When is the release date? ")
        region_code_input = input("What is the region code? ")
        return Dvd(name=name_input, call_number=call_number_input, num_copies=num_copies_input, release_date=release_date_input, region_code=region_code_input)
