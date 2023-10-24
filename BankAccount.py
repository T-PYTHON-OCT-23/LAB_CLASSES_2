
class BankAccount:
    
    def __init__(self,name: str, balance: float = 0.0):

        self.name=name
        self.__balance = balance
    
    
    
    def deposit(self,balance):

        self.__balance = balance + self.__balance

        return self.__balance
    
    def withdraw(self,balance):
        if balance > self.__balance:
           raise ValueError("sorry your balance is not enough!!")
        else: 
            self.__balance = self.__balance - balance
            return self.__balance
        
    def get_balance(self):
        return self.__balance
    def get_account_holder(self):
        return self.name
    



