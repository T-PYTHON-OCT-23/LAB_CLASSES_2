from Lab_classes2 import BankAccount

client1=BankAccount("Mohammed",5000)
client2=BankAccount("ahmad",500)
print(client1.deposit(100))
print(client2.withdraw(200))
print(client1.get_account_holder())
print(client1.get_balance())
print(client2.get_account_holder())
print(client2.get_balance())