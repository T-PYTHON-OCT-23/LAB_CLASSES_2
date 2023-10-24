class BankAccount:
    def __init__(self,name:str,initial_balance=0):
        self.account_holder=name
        self.initial_balance=initial_balance

    def deposit(self,amount:int):
        if amount >0:
            self.initial_balance+=amount
            print('The Updated balance is:',self.initial_balance)

    def withdraw(self,amount):
        if amount<=self.initial_balance:
            self.initial_balance-=amount
            print('The Updated balance after withdraw:',self.initial_balance)
        else:
            print('Error the balance is not enough')

    def get_balance(self):
        return self.initial_balance
    
    def get_account_holder(self):
        return self.account_holder

b=BankAccount('Aseel')
b.deposit(5)
b.withdraw(4)
print('The current balance is:',b.get_balance())
print('The account holder name is:',b.get_account_holder())


