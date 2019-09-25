import abc


class BankAccount(abc.ABC):
    def __init__(self, account_number, account_holder, initial_deposit):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0
        self.deposit(initial_deposit)

        @abc.abstractmethod
        def deposit(self, amount):
            pass

    def withdraw(self, amount):
        pass


class SavingsAccount(BankAccount):
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        deduction = 0.05 * amount
        self.balance -= (amount + deduction)


if __name__ == "__main__":
    my_account = BankAccount("92338723", "John Smith", 5000)
    my_account.withdraw(500)
    print(my_account.balance)
