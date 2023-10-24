class BankAccount:
    def __init__(self, account_holder, initial_balance:int=0):
        self.account_holder = account_holder
        self.initial_balance = initial_balance

    def deposit(self , amount:int):
        self.initial_balance += amount
        return self.initial_balance
    
    def withdraw(slef , amount):
        if amount > slef.initial_balance:
            print ("There is not enough money")
        else:
            slef.initial_balance -= amount
            return slef.initial_balance    
    def get_balance(slef):
        return slef.initial_balance
    

    def get_account_holder(slef):
        return slef.account_holder
    
client1 = BankAccount("fares", 200)
client2 = BankAccount("ali" , 600)
client3 = BankAccount("naif", 900)

print(client1.get_account_holder())
print(client2.get_account_holder())
print(client3.get_account_holder())
print(client1.get_balance())
print(client2.get_balance())
print(client3.get_balance())