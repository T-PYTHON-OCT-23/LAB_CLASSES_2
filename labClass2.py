class BankAccount:
    def __init__(self , account_holder , initial_balance = 0):
        self.account_holder = account_holder
        self.initial_balance = initial_balance

    def deposit(self, amount ):
        if amount > 0:
            self.initial_balance += amount
        return self.initial_balance
    
    def withdraw(self, amount):
        if amount > 0 and amount < self.initial_balance:
            self.initial_balance -= amount
            return self.initial_balance
        else:
            print("Pleas Enter valid number and less than balance!!")
    
    def get_balance(self):
        return self.initial_balance
    
    def get_account_holder(self):
        return self.account_holder
    

client1 = BankAccount("Ebtesam" , 500)
client2 = BankAccount("Majed" , 550)
client3 = BankAccount("Danah" , 600)

print(f"client1 information\nname is: {client1.get_account_holder()} \nbalanc is: {client1.get_balance()}")
print(f"clien1 processors\ndeposit is: {client1.deposit(10)}\nwithdraw is: {client1.withdraw(5)}\n")

print(f"client2 information\nname is: {client2.get_account_holder()} \nbalanc is: {client2.get_balance()}")
print(f"clien2 processors\ndeposit is: {client2.deposit(5)}\nwithdraw is: {client2.withdraw(10)}\n")

print(f"client3 information\nname is: {client3.get_account_holder()} \nbalanc is: {client3.get_balance()}")
print(f"clien3 processors\ndeposit is: {client3.deposit(15)}\nwithdraw is: {client3.withdraw(20)}\n")          
