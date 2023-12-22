from .Account import Account
from .CreditAccount import CreditAccount


class Customer:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def create_account(self, account_type, interest_rate=0):
        if account_type == "Credit":
            account = CreditAccount(account_type, interest_rate)
        else:
            account = Account(account_type, interest_rate)
        self.accounts.append(account)
        print(f"Новая учетная запись {account_type} создана для {self.name}.")

    def get_accounts(self):
        return self.accounts
