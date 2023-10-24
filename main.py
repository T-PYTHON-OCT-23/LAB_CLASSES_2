from BankAccount import BankAccount
from Bonus import Vehicle,Bus,Truck

account1=BankAccount("abdullah")
account1.deposit(10000)
print(account1.get_balance())
account1.withdraw(5000)
print(account1.get_account_holder(),account1.get_balance())



print("\n---------------Bonus---------------\n")


car1=Vehicle("toyota","Camry","White","4 passengers","A S D D | 4 3 2 5")
bus1=Bus("Nissan","Bus","blue","20 passengers","A S C R | 3 3 2 3")
truck1=Truck("Mercedes","Truck","black","20 tons","h s e d | 6 5 6 3")

car1.drift()
car1.drive()
car1.carry_cargo()

bus1.drive()
bus1.drift()
bus1.carry_cargo()

truck1.drift()
truck1.drive()
truck1.carry_cargo()