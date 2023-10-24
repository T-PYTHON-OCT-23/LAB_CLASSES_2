from lab_classes_2 import BankAccount

client = BankAccount("Sufana", 1234)
print(client.account_holder, client.balance)

print(client.deposit(100))
print(client.withdraw(2000))

print(client.get_balance())
print(client.get_account_holder())

