class BankAccount:
    def __init__(self , account_holder):
        self.account_holder=account_holder
        self.balance=0
        print("Welcome to your account !")
        
    def deposit(self):
        amount=float(input("Enter amount to be deposited: "))
        self.balance += amount
        print("Amount Deposited: ",amount)
    def withdraw(self):
        amount = float(input("Enter amount to withdraw: "))
        if self.balance>=amount:
            self.balance-=amount
            print("You withdraw: ",amount)
        else:
            print("Insufficient balance ")
    def display(self):
        print(f"{self.account_holder} your Available Balance is : ",self.balance)
# object of class
s = BankAccount('danah')
#calling
s.deposit()
s.withdraw()
s.display()

