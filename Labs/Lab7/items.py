import abc


class LibraryItem(abc.ABC):
    """
    The Abstracted class for specific objects Journal, Dvd, Book
    """

    @abc.abstractmethod
    def __init__(self, name: str, call_number: int) -> None:
        """
        Initializes the created instance
        :param name: a string
        :param call_number: an int
        :param num_copies: an int
        """
        self._name = name
        self._call_number = call_number
        self._num_copies = 1

    @property
    def name(self) -> str:
        """
        Gets the name attribute of the object
        :return: a string
        """
        return self._name

    @property
    def call_number(self) -> int:
        """
        Gets the call number attribute of the object
        :return: an int
        """
        return self._call_number

    @property
    def num_copies(self) -> int:
        """
        Gets the number of copies attribute of the object
        :return:
        """
        return self._num_copies

    def check_availability(self) -> bool:
        """
        Checks if the item is available in the catalogue or not
        :return: a boolean
        """
        return self._num_copies == 0

    def __str__(self) -> str:
        """
        String representation of the created object
        :return: a string
        """
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

    def __str__(self) -> str:
        """
        String representation of the created object
        :return: a string
        """
        return f"Category: {self.__class__.__name__}, {super().__str__()}, Issue Number: {self._issue_number}" \
               f", Publisher: {self._publisher}"


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

    def __str__(self) -> str:
        """
        String representation of the created object
        :return: a string
        """
        return f"Category: {self.__class__.__name__}, {super().__str__()}, Release Date: {self._release_date}" \
               f", Region Code: {self._region_code}"


class Book(LibraryItem):
    def __init__(self, author: str, **kwargs) -> None:
        """
        Initializes the instance of Book
        :param author: a string
        """
        self._author = author
        super().__init__(**kwargs)

    def __str__(self) -> str:
        """
        String representation of the created Book object
        :return: a string
        """
        return f"Category: {self.__class__.__name__}, {super().__str__()}, Author: {self._author}"


class LibraryItemFactory(abc.ABC):
    """
    Abstract Factory that includes the method to create library items
    """
    @abc.abstractmethod
    def create_item(self) -> LibraryItem:
        pass


class BookFactory(LibraryItemFactory):
    def create_item(self) -> LibraryItem:
        """
        Creates a book object from user input
        :return: a book object
        """
        name_input = input("What is the name? ")
        call_number_input = input("What is the call number? ")
        author_input = input("Who is the author? ")
        return Book(name=name_input, call_number=call_number_input, author=author_input)


class JournalFactory(LibraryItemFactory):
    def create_item(self) -> LibraryItem:
        """
        Creates a journal object from user input
        :return: a journal object
        """
        name_input = input("What is the name? ")
        call_number_input = input("What is the call number? ")
        publisher_input = input("Who is the publisher? ")
        try:
            issue_number_input = int(input("What is the issue number? "))
        except ValueError:
            print("Must be int")
            return
        else:
            return Journal(name=name_input, call_number=call_number_input
                           , issue_number=issue_number_input, publisher=publisher_input)


class DvdFactory(LibraryItemFactory):
    def create_item(self) -> LibraryItem:
        """
        Creates a dvd object from user input
        :return: a dvd object
        """
        name_input = input("What is the name? ")
        call_number_input = input("What is the call number? ")
        release_date_input = input("When is the release date? ")
        region_code_input = input("What is the region code? ")
        return Dvd(name=name_input, call_number=call_number_input
                   , release_date=release_date_input, region_code=region_code_input)
