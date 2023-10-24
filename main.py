class BankAccount:
    def __init__(self,account_holder,balance=0):
        self.__account_holder = account_holder
        self.__balance = balance

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def get_balance(self):
        return self.__balance
    
    def get_account_holder(self):
        return self.__account_holder
    
    
# Path: main.py

account1 = BankAccount("John Doe", 1000)
account2 = BankAccount("Bader")
account3 = BankAccount("Ahmad", 5000)

print(account1.get_account_holder())
print(account2.get_account_holder())
print(account3.get_account_holder())
print(account1.get_balance())
print(account2.get_balance())
print(account3.get_balance())