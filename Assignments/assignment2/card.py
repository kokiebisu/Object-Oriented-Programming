""" This module deals with information about the Card class """
from abc import ABC, abstractstaticmethod


class Card(ABC):
    """
    This class holds the attributes of the Card instance
    """
    card_id = 0

    def __init__(self, name, **kwargs):
        """
        Initializes the Card instance
        :param name: a string
        :param kwargs: keyword arguments
        """
        self.name = name
        self._id = Card.card_id
        Card.card_id += 1

    @abstractstaticmethod
    def get_input():
        """
        Retrieves input to create the card
        """
        pass

    @property
    def id(self):
        """
        Gets the ID of the card
        :return: an int
        """
        return self._id

    def __str__(self):
        """
        String representation of the created instance
        :return: a string
        """
        return f"ID: {self.id} Type: {self.__class__.__name__} Name: {self.name} "


class Expires:
    """
    This class holds the attributes of the Expiry Card which adds a Expiry date atttributes to the card
    """

    def __init__(self, expiry_date, **kwargs):
        """
        Initializes the Expiry Card instance
        :param expiry_date: a string
        :param kwargs: keyword arguments
        """
        self._expiry_date = expiry_date
        super().__init__(**kwargs)

    def __str__(self):
        """
        A String representation of the created instance
        :return: a string
        """
        return super().__str__() + f"Expiry Date: {self._expiry_date} "

    @staticmethod
    def get_input():
        """
        Retrieves the expiry date to create the card
        :return: a string
        """
        return input("When is the expiry date?\n")


class CreditCard(Expires, Card):
    """
    This class holds the attributes of the Credit Card
    """

    def __init__(self, account_number, security_code, **kwargs):
        """
        Initializes the Credit Card instance
        :param account_number: an int
        :param security_code: an int
        :param kwargs: keyword arguments
        """
        self._account_number = account_number
        self._security_code = security_code
        super().__init__(**kwargs)

    @staticmethod
    def get_input():
        """
        Asks the user the card information to be stored
        :return: a list
        """
        name_input = input("What is the name of the card?\n")
        account_number_input = int(input("What is the account number\n"))
        security_code_input = int(input("What is the security code?\n"))
        return [name_input, account_number_input, security_code_input]

    def __str__(self):
        """
        A String representation of the instance
        :return: a string
        """
        return super().__str__() + f"Account_number: {self._account_number}, Security code: {self._security_code}"


class DebitCard(Expires, Card):
    """
    This class holds the attributes of a Debit Card
    """
    def __init__(self, account_number, security_code, **kwargs):
        self._account_number = account_number
        self._security_code = security_code
        super().__init__(**kwargs)

    @staticmethod
    def get_input():
        """
        Asks the user the card information to be stored
        :return: a list
        """
        name_input = input("What is the name of the card?\n")
        account_number_input = int(input("What is the account number\n"))
        security_code_input = int(input("What is the security code?\n"))
        return [name_input, account_number_input, security_code_input]

    def __str__(self):
        """
        A String representation of a created instance
        :return: a string
        """
        return super().__str__() + f"Account_number: {self._account_number}, Security code: {self._security_code}"


class MemberShipCard(Expires, Card):
    """
    This class holds the attributes of a Membership Card
    """

    def __init__(self, organization, membership_number, **kwargs):
        """
        Initializes the Membership Card instance
        :param organization: a string
        :param membership_number: an int
        :param kwargs: keyword arguments
        """
        self._organization = organization
        self._membership_number = membership_number
        super().__init__(**kwargs)

    @staticmethod
    def get_input():
        """
        Retrieves the necessary input to create a Membership Card
        :return: a list
        """
        name_input = input("What is the name of the card?\n")
        organization_input = input("What is the organization?\n")
        membership_input = input("What is the membership number?\n")
        return [name_input, organization_input, membership_input]

    def __str__(self):
        """
        A String representation of the instance
        :return: a string
        """
        return super().__str__() + f"Organization: {self._organization}, Membership Number: {self._membership_number}"


class GiftCard(Card):
    """
    This class holds the attributes of a Gift Card
    """

    def __init__(self, amount, code, **kwargs):
        """
        Initializes the Gift Card instance
        :param amount: an int
        :param code: a string
        :param kwargs: keyword arguments
        """
        self._amount = amount
        self._code = code
        super().__init__(**kwargs)

    @staticmethod
    def get_input():
        """
        Retrieves the necessary input to create a Gift Card
        :return: a list
        """
        name_input = input("What is the name of the card?\n")
        amount_input = int(input("What is the amount?\n"))
        code_input = input("What is the code?\n")
        return [name_input, amount_input, code_input]

    def __str__(self):
        """
        A String representation of the instance
        :return: a string
        """
        return super().__str__() + f"Amount: {self._amount}, Code: {self._code}"


class BusinessCard(Card):
    """
    This class holds the attributes of a Business Card
    """
    def __init__(self, company, email_address, **kwargs):
        """
        Initializes the business card instance
        :param company: a string
        :param email_address: a string
        :param kwargs: keyword arguments
        """
        self._company = company
        self._email_address = email_address
        super().__init__(**kwargs)

    @staticmethod
    def get_input():
        """
        Asks the user the card information to be stored
        :return: a list
        """
        name_input = input("Who's business card is it?\n")
        company_input = input("What is the name of the company?\n")
        email_address_input = input("What is the email address?\n")
        return [name_input, company_input, email_address_input]

    def __str__(self):
        """
        A String representation of the created instance
        :return: a string
        """
        return super().__str__() + f"Company: {self._company}, Email Address: {self._email_address}"
