class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            print("Insufficient funds. Withdrawal not allowed.")
            return self.balance

    def get_balance(self):
        return self.balance

    def get_account_holder(self):
        return self.account_holder


account = BankAccount("muhamed", 1000)
print(f"Account holder: {account.get_account_holder()}")
print(f"Initial balance: {account.get_balance()}")

account.deposit(500)
print(f"New balance after deposit: {account.get_balance()}")

account.withdraw(300)
print(f"New balance after withdrawal: {account.get_balance()}")

account.withdraw(1500)  

