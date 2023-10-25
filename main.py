from bank_account import BankAccount
from vehicle import Vehicle , Bus , Truck

acouunt1 = BankAccount("Oudy",1000) 
print(acouunt1.deposit(300))
print(acouunt1.withdraw(400))
print(acouunt1.get_balance())
print(acouunt1.get_account_holder())
print("")
print("-----class Vehicle----")
vehicle = Vehicle("Nisan","T1","balck","200" , "AAA 001")
bus = Bus("Toyota","T2","white","300" , "AAA 002")
truck = Truck("Mercedes","T3","red","400" , "AAA 003")

print("-----VEHICLE-----")
print(vehicle.drive())
print(vehicle.drift())
print(vehicle.carry_cargo())

print("-----BUS-----")
print(bus.drive())
print(bus.drift())
print(bus.carry_cargo())

print("-----TRUCK-----")
print(truck.drive())
print(truck.drift())
print(truck.carry_cargo())


