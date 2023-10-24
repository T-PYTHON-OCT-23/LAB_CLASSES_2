class BankAccount:
    def __init__(self,account_holder:str,initial_balance:int=0):
        self.account_holder = account_holder
        self.initial_balance = initial_balance
    def deposit(self,amount:int):
        self.initial_balance = amount + self.initial_balance
        return self.initial_balance
    def withdraw(self,amount:int): 
            if amount > self.initial_balance :
                raise Exception("There are sufficient not funds in the account")
            else:
                self.initial_balance-= amount 
                return  self.initial_balance
               
    def get_balance(self):
        current_account=f"This is current account: {self.initial_balance}"
        return current_account
    def get_account_holder(self):
        name=f"This is name of the account: {self.account_holder}"
        return name   



'''    client1=("Mohammed",5000)
    client2=("ahmad",0)
    print(client1.deposit())
    print(client2.withdraw())
    print(client1.get_)'''
