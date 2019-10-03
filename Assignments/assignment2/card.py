class Card:
    def __init__(self, name, **kwargs):
        self.name = name


class CreditCard(Card):
    def __init__(self, account_number, security_code, **kwargs):
        self._account_number = account_number
        self._security_code = security_code
        super().__init__(**kwargs)

    def __str__(self):
        return f"Name: {self.name}, Account_number: {self._account_number}, Security code: {self._security_code}"
