from calssess import BankAccount

account1 = BankAccount("Hazal")
print(BankAccount.get_balance(account1))
BankAccount.deposit(account1,23)
BankAccount.withdraw(account1,20)
balance = BankAccount.get_balance(account1)
print(balance)
account_holder = BankAccount.get_account_holder(account1)
print(account_holder)