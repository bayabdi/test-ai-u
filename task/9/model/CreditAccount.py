from .Account import Account
from .Transaction import Transaction


class CreditAccount(Account):
    def __init__(self, account_type, interest_rate=0, credit_limit=0):
        super().__init__(account_type, interest_rate)
        self.credit_limit = credit_limit

    def withdraw(self, amount):
        if 0 < amount <= (self.credit_limit + self.balance):
            self.balance -= amount
            self.transactions.append(Transaction(amount, "Withdrawal"))
            print(f"Успешно сняли ${amount} с вашего счета {self.account_type}.")
        else:
            print("Неверная сумма снятия или превышен кредитный лимит.")
