class BankAccount:
    
    def __init__(self, account_holder: str, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                return self.balance
            else:
                print("Insufficient funds. Cannot withdraw more than the current balance")
        else:
            print("Invalid withdrawal amount")
        return self.balance

    def get_balance(self):
        return self.balance

    def get_account_holder(self):
        return self.account_holder
    



