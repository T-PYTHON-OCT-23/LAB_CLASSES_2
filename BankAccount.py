class BankAccount:
    def __init__(self,account_holder:str="null", balance:float=0.0 ):
        self.__account_holder=account_holder
        self.__balance=balance
        
    def deposit(self, amount:float):
        if type(float(amount))==float and amount>0.0:
            self.__balance+=amount
        else:
            raise ValueError("you should enter a number that is more than 0")
    
    def withdraw(self, amount:float):
        if type(float(amount))==float and amount>0.0:
            if amount<=self.__balance:
                self.__balance-=amount
            else:
                raise Exception("You have no sufficient funds!")
        else:
            raise ValueError("you should enter a number that is more than 0")
    
    def get_balance(self):
        return self.__balance
    
    def get_account_holder(self):
        return self.__account_holder
    