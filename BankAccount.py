class BankAccount():



    def __init__(self , account_holder: str , initial_balance : int  , account_balance:int ) -> None:
        self.account_holder = account_holder
        self.initial_balance = 0
        self.account_balance = account_balance



    def deposit(self , amount:int):
        account_balance = account_balance + amount
        return "updated balance: ", account_balance

    def withdraw(self , amount:int):
        if account_balance > amount:
            raise Exception ("the balance lower ,can't withdraw ")
        account_balance = account_balance - amount

        
    def get_balance(self , account_balance:int):
        return account_balance
    def get_account_holder(self , account_holder:str):
        return account_holder
    

    
