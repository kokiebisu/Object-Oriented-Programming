from enum import Enum
from pathlib import Path
import json


class FileHandler:

    """
    This module is responsible for housing any classes and/or structures that are
    responsible for reading and writing to files. This includes any custom exceptions
    """

    @staticmethod
    def load_data(path, file_extension):
        """
        Checks the file extension and reading the file accordingly
        Responsible for raising any exceptions if they occur
        look up pathlib module to be able to check if the file exists
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
        Precaution: must be appended
        """
        with open(f"{path}", "a+") as write_file:
            write_file.write(f"{line}\n")


class FileExtensions(Enum):
    JSON = ".json"
    TEXT = ".txt"


class InvalidFileTypeError(Exception):
    """
    This exception should be raised if the user attempts to read a file that is not a .json or .txt file
    """

    def __init__(self, balance, amount):
        pass

    # try:
    #     my_bank_account.withdraw(100, 000)
    #
    # except InvalidWithdrawalError as e:
    #     print(e.args[0])
    #
    # else:
    #     print("Withdrawal completed!")
    #
    # finally:
    #     bank_service.close_connection()
