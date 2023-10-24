from BankAccount import BankAccount

account1=BankAccount("abdullah")
account1.deposit(10000)
print(account1.get_balance())
account1.withdraw(5000)
print(account1.get_account_holder(),account1.get_balance())
