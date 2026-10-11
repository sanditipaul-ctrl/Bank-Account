class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def show_balance(self):
        print(f"Account: {self.name}")
        print(f"Balance: {self.balance}")