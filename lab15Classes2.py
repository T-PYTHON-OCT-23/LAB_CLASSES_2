class BankAccount:
    def __init__(self,account_holder:str,initial_balanc = 0) :
        self.account_holder = account_holder
        self.initial_balanc = initial_balanc

    def deposit(self,amount:int):
        #amount = int(input("Enter amount to be deposited: "))
        if amount > 0 :
          self.initial_balanc += amount
          print("\n Amount Deposited:", amount)
      

    def withdraw(self,amount:int):
        #amount = int(input("Enter amount to be withdrawn: "))
        if self.initial_balanc >= amount:
            self.initial_balanc -= amount
            print("\n You Withdrew:", amount)
        else:
            print("\n The balance is not enough ")

    def get_balance(self):
        return self.initial_balanc

    def get_account_holde(self):
        return self.account_holder
    
user = BankAccount("sarah")  
user.deposit(1)
user.withdraw (6)  
print("\n The current balance is:",user.get_balance())
print('\n The account holder name is:',user.get_account_holde())
'''
user.deposit(50)
user.withdraw (25)  
print("The current balance is:",user.get_balance())
print('The account holder name is:',user.get_account_holde())

user.deposit(1)
user.withdraw (1)  
print("The current balance is:",user.get_balance())
print('The account holder name is:',user.get_account_holde())'''