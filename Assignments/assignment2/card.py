""" This module deals with information about the Card class """


class Card:
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
        return f"ID: {self._id} Name: {self.name} "


class ExpiryCard(Card):
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
        return super().__str__() + f"Expiry Date: {self._expiry_date} "


class CreditCard(ExpiryCard):
    """
    This class holds the attributes of the Credit Card instance which is the subclass of the ExpiryCard class
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

    def __str__(self):
        """
        A String representation of the instance
        :return: a string
        """
        return super().__str__() + f"Account_number: {self._account_number}, Security code: {self._security_code}"


class MemberShipCard(ExpiryCard):
    """
    This class holds the attributes of the Membership Card instance which is the subclass of the ExpiryCard class
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

    def __str__(self):
        """
        A String representation of the instance
        :return: a string
        """
        return super().__str__() + f"Organization: {self._organization}, Membership Number: {self._membership_number}"


class GiftCard(Card):
    """
    This class holds the attributes of the Gift Card instance which is the subclass of the Card class
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

    def __str__(self):
        """
        A String representation of the instance
        :return: a string
        """
        return super().__str__() + f"Amount: {self._amount}, Code: {self._code}"
