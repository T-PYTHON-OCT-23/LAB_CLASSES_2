from classes2 import BankAccount


BankAccount1 = BankAccount("Abdullah Fahd", 1500)

print("Account Holder:", BankAccount1.get_account_holder())
print("Balance:", BankAccount1.get_balance())


BankAccount1.deposit(2000)
print("After deposit:", BankAccount1.get_balance())

BankAccount1.withdraw(150)
print("After withdrawal:", BankAccount1.get_balance())

BankAccount1.withdraw(500)
print("After attempted withdrawal:", BankAccount1.get_balance())
