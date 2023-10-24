import Vehicle
class Bus():

    def __init__(self , brand:str, name:str ,color:str ,capacity:str ,plate_number:int , length:int):
        super().__init__(brand, name ,color ,capacity ,plate_number )
        self.length=length

    #overriding
    def carry_cargo(self , name):
        print(f"the {name} is carrying cargo and big !!")



bus=Bus("Toyota" , "Toyota Tundra" , "white" , 12000 , 222 , 233)

print(bus)
#print(bus.get_brand() , bus.get_name() , bus.get_color() , bus.get_capacity() , bus.get_plate_number() , bus.length())