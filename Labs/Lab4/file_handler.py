"""This module is responsible with deals with everything concerning files outside of the program"""
from enum import Enum
from pathlib import Path
import json


class FileHandler:

    """
    This class identifies the type of file and respond respectively based on it.
    """

    @staticmethod
    def load_data(path, file_extension):
        """
        Checks the file extension and reading the file accordingly
        :return: a list
        """
        if not Path(path).exists():
            raise InvalidFileTypeError
        if file_extension == FileExtensions.JSON.value:
            try:
                with open(f"{path}") as read_file:
                    data = json.load(read_file)
            except FileNotFoundError:
                print("OOPS! File was not found!")
            else:
                terms = []
                for term, _ in data.items():
                    terms.append(term)
                return [data, terms]

        elif file_extension == FileExtensions.TEXT.value:
            with open(f"{path}", encoding='utf-8') as read_file:
                data = read_file.read()
                terms = []
                for term, _ in data.items():
                    terms.append(term)
                return [data, terms]
        else:
            # add invalid exception
            print("not valid")

    @staticmethod
    def write_lines(path, line):
        """
        Writes the given lines to a Text file
        """
        with open(f"{path}", "a+") as write_file:
            write_file.write(f"{line}\n")


class FileExtensions(Enum):
    """
    A class that holds two enum types that represent file extensions
    """
    JSON = ".json"
    TEXT = ".txt"


class InvalidFileTypeError(Exception):
    """
    This exception should be raised if the user attempts to read a file that is not a .json or .txt file
    """

    def __init__(self, name):
        super().__init__(f"{name} does not have an extension that is valid!")
