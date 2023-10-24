from Bonus_lab_class import Vehicle
from Bonus_lab_class import Bus 
from Bonus_lab_class import Truck
print("---Types of Vehicles---")
vehicle1 = Vehicle("Porsche","Taycan","Pink", 71, "2023A")
print(vehicle1._brand, vehicle1._name, vehicle1._color, vehicle1._capacity, vehicle1._plate_number)

vehicle2 = Vehicle("Range Rover", "SUV","Black", 90 , "2020B")
print(vehicle2._brand, vehicle2._name, vehicle2._color, vehicle2._capacity, vehicle2._plate_number)

vehicle3 = Bus("Toyota","Hiace","White", 100 , "200AC")
print(vehicle3._brand, vehicle3._name, vehicle3._color, vehicle3._capacity, vehicle3._plate_number)

vehicle4 = Truck("CAT","CT660","White", 110 , "198KM")
print(vehicle4._brand, vehicle4._name, vehicle4._color, vehicle4._capacity, vehicle4._plate_number)
print("-"*20)
print(vehicle3.drive())
print(vehicle4.carry_cargo())
#Note:I don't know why he prints (None)