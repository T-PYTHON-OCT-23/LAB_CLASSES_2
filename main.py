from BankAccount import BankAccount
#------------------------------------TESTING------------------------------------

acc_holder1=BankAccount("Ahmed",15000.00)
acc_holder2=BankAccount("Khalid")
acc_holders=[acc_holder1,acc_holder2]


acc_holder1.withdraw(5000.0)
acc_holder2.deposit(900)
for i in acc_holders:
    print(i.get_account_holder(),"is Account holder name and",i.get_balance(),"is his balance")
    
