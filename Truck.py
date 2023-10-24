import Vehicle
class Truck():

    def __init__(self , brand, name ,color ,capacity ,plate_number , higth:int):
        super().__init__(brand, name ,color ,capacity ,plate_number )
        self.higth=higth



    #overriding
    def carry_cargo(self , name):
        print(f"the {name} is carrying cargo and huge !!")


truck=Truck("Toyota" , "Toyota Tundra" , "white" , 12000 , 111 ,160)

print(truck.get_brand() , truck.get_name() , truck.get_color() , truck.get_capacity() , truck.get_plate_number() , truck.hight())
Truck.carry_cargo("Hondai")