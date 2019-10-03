import abc


class Card(ABC):
    def __init__(self, name, category, **kwargs):
        self.name = name

    @abc.abstractmethod
    def get_input(self):
        pass


class CreditCard(Card):
    def __init__(self, account_number, security_code, **kwargs):
        self._account_number = account_number
        self._security_code = security_code
        super().__init__(**kwargs)

    @staticmethod
    def get_input():

    def __str__(self):
        return f"Name: {self.name}, Account_number: {self._account_number}, Security code: {self._security_code}"


# class CardType(Enum):
#     CREDIT_CARD = 'Credit Card'
