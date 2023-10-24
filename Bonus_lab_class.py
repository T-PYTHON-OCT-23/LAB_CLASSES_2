#LAB-CLASSES 2
class Vehicle:
    def __init__(self, brand:str, name:str, color:str, capacity:int, plate_number: str):
        self._brand = brand
        self._name = name
        self._color = color
        self._capacity = capacity
        self._plate_number = plate_number
#brand getter and setter
    def get_brand(self):
        return self._brand
    def set_brand(self, brand):
        self._brand= brand
#name getter and setter
    def get_name(self):
            return self._name
    def set_name(self, name):
        self._name = name
#color getter and setter
    def get_color(self):
            return self._color
    def set_name(self, color):
        self._color = color
#capacity getter and setter
    def get_capacity(self):
            return self._capacity
    def set_capacity(self, capacity):
        self._capacity = capacity
#plate_number getter and setter
    def get_plate_number(self):
            return self._plate_number
    def set_plate_number(self, plate_number):
        self._plate_number = plate_number

    #Methoda
    def drive(self):
        print(f"The {self._name} is driving!")
    
    def drift(self):
        print(f"The {self._name} is drifting!")

    def carry_cargo(self):
        print(f"The {self._name} is carry things from one place to another.")
        
#inheriting from Vehicle
#Bus
class Bus(Vehicle):
    def __init__(self, brand:str, name:str, color:str, capacity:str, plate_number: str):
        super().__init__(brand, name, color,capacity,plate_number)

    def drive(self):
        print(f"The {self._name} is good for school transport.")

#Truck          
class Truck(Vehicle):
    def __init__(self, brand:str, name:str, color:str, capacity:str, plate_number: str):
        super().__init__(brand, name, color,capacity,plate_number)

    def carry_cargo(self):
        print(f"The {self._name} can haul lumber")