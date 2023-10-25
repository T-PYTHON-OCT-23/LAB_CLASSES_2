class Vehicle:

    def __init__(self, brand, name, color , capacity, plate_number):
        self.__brand = brand
        self.__name = name
        self.__color = color
        self.__capacity = capacity
        self.__plate_number = plate_number

    def set_brand(self, brand:str):
        if len(brand) < 3:
            raise NameError("Please provid valid brand")
        self.__brand = brand
    def get_brand(self):
        return self.__brand 

    def set_name(self, name:str):
        if len(name) < 3:
            raise NameError("Please provid valid name")
        self.__name = name
    def get_name(self):
        return self.__name 

    def set_color(self, color:str):
        if len(color) < 3:
            raise NameError("Please provid valid color")
        self.__color = color
    def get_name(self):
        return self.__color
    
    def set_capacity(self, capacity:str):
        if type(capacity) is not int:
            raise ValueError("Please only integer values")
        self.__capacity = capacity
    def get_name(self):
        return self.__capacity 
    
    def set_plate_number(self, plate_number:int):
        if type(plate_number) is not int:
            raise ValueError("Please only integer values")
        self.__plate_number = plate_number
    def get_plate_number(self):
        return self.__plate_number

    def drive(self):
        return f"the {self.__name} is driving!"

    def drift(self):
        return f"the {self.__name} is drifting !!"

    def carry_cargo(self):
        return f"the {self.__name} is carrying cargo !!"
    

class Bus(Vehicle):
     def __init__(self, brand, name, color , capacity, plate_number, passengers):
         super().__init__(brand, name, color, capacity, plate_number)
         self.passengers = passengers

     def drive(self):
        return f"{self.__name} is driving with {self.passengers} passengers!"
     def carry_cargo(self):
        return f"{self.__name} is carrying passengers!"


class Truck(Vehicle):
    def __init__(self, brand, name, color , capacity, plate_number, capacityAmount):
         super().__init__(brand, name, color, capacity, plate_number)
         self.capacityAmount = capacityAmount
        
    def drive(self):
        return f"{self.__name} is driving with a load capacity of {self.capacityAmount} kg!"

    def carry_cargo(self):
        f"{self.__name} is carrying cargo in the truck!"


car = Vehicle("Toyota", "Camry", "Blue", 5, "ABC123")
bus = Bus("GMS", "Sprinter", "White", 20, "XYZ789", 15)
truck = Truck("Volvo", "FH16", "Red", 2, "DEF456", 20000)


print(f"{car.drive()}\n{car.drift()}\n{car.carry_cargo()}")
print(f"{bus.drive()}\n{bus.drift()}\n{bus.carry_cargo()}")
print(f"{truck.drive()}\n{truck.drift()}\n{truck.carry_cargo()}")






