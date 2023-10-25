class BankAccount:
    def __init__(self,account_holder:str,initial_balance:int =0) -> None:
        self.__account_holder =account_holder
        self.__initial_balance = initial_balance 
        
    
    def set_account_holder(self,account_holder ):
        self.__account_holder =account_holder
        
    def get_account_holder(self):
        return self.__account_holder
    
    def set_initial_balance(self,amount:int):
        if type(amount) != int:
            raise ValueError("Please only integer values")
        
        self.__initial_balance = self.__initial_balance + amount 
        
    def get_balance(self):
        return self.__initial_balance
    
    def withdraw(self,amount:int):
            if type(amount) != int :
                raise ValueError("Please only integer values")
            elif amount > self.__initial_balance :
                return "You don't have enough, you have "+ self.__initial_balance
            self.__initial_balance = self.__initial_balance - amount
            return f"The transaction was completed successfully and is in your account {self.__initial_balance}" 
        
        
    def deposit(self, amount:int):
            if type(amount) != int :
                raise ValueError("Please only integer values")
            self.__initial_balance = self.__initial_balance + amount
            return f"The transaction was completed successfully and is in your account {self.__initial_balance}" 
        
        
        
        