class BankAccount:
    
    def __init__(self, account_holder: str, initial_balance: float = 0.0):
        self._account_holder = account_holder
        self._balance = initial_balance

    def withdraw(self, amount):
        if amount > 0:
            if self._balance >= amount:
                self._balance -= amount
                return self._balance
    
            else:
                print("Insufficient funds.")
        else:
            print("Invalid withdrawal amount")
        return self._balance
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            
        else:
            print("Invalid deposit amount")    

    def get_balance(self):
        return self._balance
    
    def set_balance(self, new_balance):
        if new_balance >= 0:
            self._balance = new_balance

        else:
            print("Invalid balance value.")


    def get_account_holder(self):
        return self._account_holder

    def set_account_holder(self, new_holder):
        self._account_holder = new_holder
    

    



