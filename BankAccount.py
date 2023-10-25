class BankAccount:

    def __init__(self, id:int, name:str, initial_balance:int ):
        #Attributes / Properties
        self.id = id
        self.name = name
        self.initial_balance = initial_balance 

    def deposit (self , initial_balance , amount:int):
     
     initial_balance += amount
     return f"you have {initial_balance} Saudi Riyals "


    def withdraw(self , initial_balance , amount):

        if initial_balance > amount:
            updated_balance = initial_balance - amount
            return updated_balance
        else:
            print("sorry! you don't have enough cash")


    def get_balance (self , initial_balance):
        return f" user {self.name} have {self.id}: you're acount have {self.initial_balance}SR"
    
    def get_account_holder(self, name):
        return f"account holder name is: {name}"




