from abc import ABC, abstractstaticmethod


class LibraryItem(ABC):
    def __init__(self, name, call_number, num_copies):
        self._name = name
        self._call_number = call_number
        self._num_copies = num_copies

    def check_availability(self):
        return self._num_copies == 0

    @staticmethod
    @abstractstaticmethod
    def create():
        pass


class Journal(LibraryItem):
    def __init__(self, name, call_number, num_copies, issue_number, publisher):
        super().__init__(name, call_number, num_copies)
        self._issue_number = issue_number
        self._publisher = publisher

    @staticmethod
    def create():
        print("What is the name?")
        name_input = input()
        print("What is the call number?")
        call_number_input = input()
        print("How many number of copies?")
        num_copies_input = int(input())
        print("What is the issue number?")
        issue_number_input = input()
        print("What is publisher?")
        publisher_input = input()
        return Journal(name_input, call_number_input, num_copies_input, issue_number_input, publisher_input)

    def __str__(self):
        return f"Journal: {self._name}, Call Number: {self._call_number}, Issue Number: {self._issue_number}, Publisher: {self._publisher}, Number of Copies: {self._num_copies}"


class Dvd(LibraryItem):
    def __init__(self, name, call_number, num_copies, release_date, region_code):
        super().__init__(name, call_number, num_copies)
        self._release_date = release_date
        self._region_code = region_code

    @staticmethod
    def create():
        print("What is the name?")
        name_input = input()
        print("What is the call number?")
        call_number_input = input()
        print("How many number of copies?")
        num_copies_input = input()
        print("When is the release_date?")
        release_date_input = input()
        print("What is region code?")
        region_code_input = input()
        return Dvd(name_input, call_number_input,
                      num_copies_input, release_date_input, region_code_input)

    def __str__(self):
        return f"DVD: {self._name}, Call Number: {self._call_number}, Release Date: {self._release_date}, Region Code: {self._region_code}, Number of Copies: {self._num_copies}"


class Book(LibraryItem):
    def __init__(self, name, call_number, num_copies, author):
        super().__init__(name, call_number, num_copies)
        self._author = author

    @staticmethod
    def create():
        print("What is the name?")
        name_input = input()
        print("What is the call number?")
        call_number_input = input()
        print("How many number of copies?")
        num_copies_input = input()
        print("When is the author?")
        author_input = input()
        return Book(name_input, call_number_input,
                      num_copies_input, author_input)

    def __str__(self):
        return f"Book: {self._name}, Call Number: {self._call_number}, Number of Copies: {self._num_copies}, Author: {self._author}"
