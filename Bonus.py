class Vehicle:
    def __init__(self, brand, name, color, capacity, plate_num):
        self.__brand=brand
        self.__name=name
        self.__color=color
        self.__capacity=capacity
        self.__plate_num=plate_num
    def drive(self):
          print(f"the {self.__name} is driving!")

    def drift(self):
        print(f"the {self.__name} is drifting !!")

    def carry_cargo(self):
        print(f"the {self.__name} is carrying cargo !!")

    def brandSet(self, brand):
        self.__brand=brand
        return self.__brand
    
    def brandGet(self):
        return self.__brand
     
    def nameSet(self, name):
        self.__name=name
        return self.__name
    
    def nameGet(self):
        return self.__name
    
    def colorSet(self, color):
        self.__color=color
        return self.__color
    
    def colorGet(self):
        return self.__color

    def capacitySet(self, capacity):
        self.__capacity=capacity
        return self.__capacity
    
    def capacityGet(self):
        return self.__capacity

    def plate_numSet(self, plate_num):
        self.__plate_num=plate_num
        return self.__plate_num
    
    def plate_numGet(self):
        return self.__plate_num

class Bus(Vehicle):
    def __init__(self, brand, name, color, capacity, plate_num, school):
        super().__init__(brand, name, color, capacity, plate_num)
        self.__school=school
        
    def schoolSet(self, school):
        self.__school=school
        return self.__school

    def schoolGet(self):
        return self.__school
    def drift(self):
        print(f"Sorry, {super().nameGet()} cant drift because its a buss!!")

class Truck(Vehicle):
    def __init__(self, brand, name, color, capacity, plate_num, cargo):
        super().__init__(brand, name, color, capacity, plate_num)
        self.__cargo=cargo
    
    def cargoSet(self, cargo):
        self.__cargo=cargo
        return self.__seats_num

    def cargoGet(self):
        return self.__cargo
    def drift(self):
        print(f"Sorry, {super().nameGet()} cant drift because its a Truck!!")


#--------------------------------------------------------

car=Vehicle("totyota", "corola", "red", 4, "abc 5849")
bus=Bus("volvo", "bus506", "yellow", 30, "xyz 9876", "Noor al-islam")
truck=Truck("Merceds", "t-300", "black", 2, "dfg 1736", "Food")

list=[car,bus,truck]

for i in list:
    i.drive()
    i.drift()
    i.carry_cargo()
    print(i.nameGet())
    print(i.brandGet())
    print(i.colorGet())
    print(i.capacityGet())
    print(i.plate_numGet())
    print("--"*30)

