
#LAB-CLASSES2
class BankAccount:
    def __init__(self, account_holder:str, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance
#1
    def deposit(self,number):
        if number>0:
            self.balance += number
            return self.balance,"---Added successfully---"
            
#2
    def withdraw(self,number):
            if number > self.balance:
                return self.balance,"insufficient funds "
            elif number>0:
                self.balance -= number
                return self.balance,"---Added successfully---"
            else:
                print("Error, faild operation")
#3
    def get_balance(self):
        return "Current account balance:",self.balance
#4
    def get_account_holder(self):
        return "Account holder name:",self.account_holder



