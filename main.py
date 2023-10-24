from bank import BankAccount 

my_account = BankAccount("maram alasmari",1000)
my_account.withdraw(90)
my_account.deposit(100)

b = my_account.get_balance()
c = my_account.get_account_holder()

print(f"Account owner: {c}")
print(f"Account balance: ${b}")
