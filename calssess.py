class BankAccount:
    def __init__(self,name:str,balance:int = 0) -> None:
        self.name = name
        self.__balance = balance

    def initial_balance(self,balance):
        if balance == None:
            balance = 0
        else:
            self.__balance = BankAccount.deposit(balance)
    
    def get_balance(self,balance):
        self.__balance = balance

    def deposit(self,amount):
        self.__balance += amount
        return print(f"total amount after the deposit is {self.__balance}")

    def withdraw(self,amount):
        if amount > self.__balance:
            raise ValueError("You don't have the money in this balance")
        else:
            self.__balance -= amount
            print(f"withdraw successfully. \n you withdraw {amount}\n Total remining is {self.__balance}")

    def get_balance(self):
        return self.__balance

    def get_account_holder(self):
        return self.name
