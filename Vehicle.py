class Vehicle():

    def __init__(self , brand:str, name:str ,color:str ,capacity:int ,plate_number:int ) :
        self.__brand = brand 
        self.__name= name
        self.__color=color
        self.__capacity=capacity
        self.__plate_number=plate_number


    def drive(self , name):
        print(f"the {name} is driving!")
    

    def drift(self , name):
        print(f"the {name} is drifting !!")

    def carry_cargo(self , name):
        print(f"the {name} is carrying cargo !!")



    def set_brand(self , brand):
        self.__brand=brand

    def set_name(self , name):
        self.__name=name

    def set_color(self , color):
        self.__color=color

    def set_capacity(self , capacity):
        self.__capacity=capacity

    def set_plate_number(self , plate_number):
        self.__plate_number=plate_number



    def get_brand(self , brand):
        return self.__brand

    def get_name(self , name):
        return self.__name

    def get_color(self , color):
        return self.__color

    def get_capacity(self , capacity):
        return self.__capacity

    def get_plate_number(self , plate_number):
        return self.__plate_number

