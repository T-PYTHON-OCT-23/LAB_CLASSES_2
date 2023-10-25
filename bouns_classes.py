class Vehicle: 
    def __init__(self, brand:str, name:str ,color: str, capacity: str,plat_number :str): 
        self.__brand=brand 
        self.__name = name
        self.__color = color 
        self.__capacity = capacity
        self.__plat_number = plat_number 
    def drive(self):  
        a= f"the {self.get_name()} is driving!" 
        return a
    def drift(self):  
        b= f"the vehicle {self.get_name ()} is drifting!"
        return b
    def carry_cargo (self): 
        c=f"the vehicle {self.get_name()} is carrying cargo!!"
        return c
    def set_brand(self, brand:str): 
        if type(brand) is not str:
            raise ValueError("please only string value")
        self.brand= brand 
    def get_brand(self): 
        return self.brand 
    def set_name(self, name): 
        if type(name) is not str: 
            raise ValueError("please only string value") 
        self.__name=name 
    def get_name(self):  
        return self.__name  
    def set_color(self, color:str): 
        if type(color) is not str:
            raise ValueError("please only string value") 
            self.__color=color 
    def get_color(self):  
        return self.__color
    def set_capacity(self, capacity): 
        self.__capacity=capacity 
    def get_capacity(self): 
        return self.__capacity 
    def set_plat_num(self,plat_number): 
        self._plat__number=plat_number 
    def get_plat_num(self): 
        return self.__plat_number 
class Bus (Vehicle):
    def __init(self, brand: str, name:str, color: str, capacity:str ,plat_number:str): 
        super().init_(brand, name ,color, capacity, plat_number) 
    def drive(self):
        return f"Most drivers like  driving a {self.get_name()} :" 
    def drift(self):     
        return f"The possibility of the 48 {self.get_name()} drifting is very low"
class Truck (Vehicle):
    def _init(self, brand: str, name:str ,color: str, capacity: str ,plat_number:str): 
        super().init_(brand, name  , color, capacity,plat_number) 
    def carry_cargo(self): 
        return f"One of the best Trucks of transporting goods is {self.get_name()} ." 
vehicle1=Vehicle("Toyota", "Hilux", "white","4 seter","111 aaa") 
bus1=Bus("SML","Tipper", "black","40 set","222 bbb") 
truck1=Truck("Hyundi","car transporter", "red" ,"10 cars","333 ccc") 
print(vehicle1.drive()) 
print(vehicle1.drift()) 
print(bus1.drive()) 
print(bus1.drift()) 
print(truck1.carry_cargo())      