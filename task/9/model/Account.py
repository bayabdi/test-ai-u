from .Transaction import Transaction


class Account:
    def __init__(self, account_type, interest_rate=0):
        self.balance = 0
        self.transactions = []
        self.account_type = account_type
        self.interest_rate = interest_rate

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(Transaction(amount, "Deposit"))
            print(f"Успешно зачислили ${amount} на ваш счет {self.account_type}.")
                
        else:
            print("Неверная сумма депозита.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transactions.append(Transaction(amount, "Withdrawal"))
            print(f"Успешно сняли ${amount} с вашего счета {self.account_type}.")
        else:
            print("Неверная сумма вывода или недостаточное количество средств.")

    def get_balance(self):
        return self.balance

    def calculate_interest(self):
        if self.account_type == "Savings":
            interest = self.balance * self.interest_rate
            self.balance += interest
            self.transactions.append(Transaction(interest, "Interest"))
            print(f"Проценты в размере ${interest}, начисляемые на ваш сберегательный счет.")

    def get_transaction_history(self):
        return self.transactions