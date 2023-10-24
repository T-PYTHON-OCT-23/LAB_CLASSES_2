class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            print("Withdrawal failed.")
            return self.balance

    def get_balance(self):
        return self.balance

    def get_account_holder(self):
        return self.account_holder

account = BankAccount("Reef", 10000)

print(f"Account holder: {account.get_account_holder()}")
print(f"Initial balance: {account.get_balance()}")

account.deposit(1000)
print(f"Balance after deposit: {account.get_balance()}")

account.withdraw(500)
print(f"Balance after withdrawal: {account.get_balance()}")

account.withdraw(1200)
print(f"Balance after insufficient withdrawal: {account.get_balance()}")