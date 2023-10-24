from BankAccount import BankAccount
client1 = BankAccount("fares", 200)
client2 = BankAccount("ali" , 600)
client3 = BankAccount("naif", 900)

print(client1.get_account_holder())
print(client2.get_account_holder())
print(client3.get_account_holder())
print(client1.get_balance())
print(client2.get_balance())
print(client3.get_balance())