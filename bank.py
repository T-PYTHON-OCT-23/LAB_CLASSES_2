# bank account

# 1
class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.initial_balance = initial_balance

# 2
    def deposit(self, amount):
        if amount > 0:
            self.initial_balance += amount
            return self.initial_balance
        else:
            print("Invalid deposit amount")
            return self.initial_balance

# 3
    def withdraw(self, amount):
        if amount > 0:
            if self.initial_balance >= amount:
                self.initial_balance -= amount
                return self.initial_balance
            else:
                print(" Insufficient funds ")
                return self.initial_balance
        else:
            print(" Invalid withdrawal amount ")
            return self.initial_balance

# 4
    def get_balance(self):
        return self.initial_balance

# 5

    def get_account_holder(self):
        return self.account_holder
