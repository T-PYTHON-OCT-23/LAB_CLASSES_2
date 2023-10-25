from bank_account import BankAccount

acouunt1 = BankAccount("Oudy",1000) 
print(acouunt1.deposit(300))
print(acouunt1.withdraw(400))
print(acouunt1.get_balance())
print(acouunt1.get_account_holder())