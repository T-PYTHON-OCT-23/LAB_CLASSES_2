from classes2 import BankAccount


BankAccount1 = BankAccount("Abdullah Fahd", 1800.0)

print("Account Holder:", BankAccount1.get_account_holder())
print("Balance:", BankAccount1.get_balance())


BankAccount1.deposit(300.0)    
print("After deposit:", BankAccount1.get_balance())

BankAccount1.withdraw(150.0)
print("After withdrawal:", BankAccount1.get_balance())

BankAccount1.set_balance(1500.0)
print("After setting a new balance:", BankAccount1.get_balance())

BankAccount1.set_account_holder("Saad")
print("After changing the account holder:",BankAccount1.get_account_holder())




