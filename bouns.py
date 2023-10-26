class Vehicle:
    def __init__(self, brand, name, color, capacity, plate_number):
        self.__brand = brand
        self.__name = name
        self.__color = color
        self.__capacity = capacity
        self.__plate_number = plate_number

    def drive(self):
        print(self.__name, 'is driving')

    def drift(self):
        print(self.__name, 'is drifting')

    def cargo(self):
        print(self.__name, 'is carrying cargo')

    def get_brand(self):
        return self.__brand

    def get_name(self):
        return self.__name

    def get_color(self):
        return self.__color

    def get_capacity(self):
        return self.__capacity

    def get_plate_number(self):
        return self.__plate_number

class Bus(Vehicle):
    def drift(self):
        print(self.get_name(), 'cannot drift')
    
    def cargo(self):
        print(self.get_name(), 'cannot carry cargo')

    def __init__(self, brand, name, color, capacity, plate_number, pt, direction):
        super().__init__(brand, name, color, capacity, plate_number)
        self.public_transport = pt
        self.direction = direction

class Truck(Vehicle):
    def drift(self):
        print(self.get_name(), 'cannot drift')

    def __init__(self, brand, name, color, capacity, plate_number, cargo_type, cargo_weight):
        super().__init__(brand, name, color, capacity, plate_number)
        self.cargo_type = cargo_type
        self.cargo_weight = cargo_weight

bus1 = Bus('Mercedes', 'Citaro', 'White', 50, '123456', True, 'North')
bus2 = Bus('Mercedes', 'Citaro', 'White', 50, '123456', True, 'South')
truck1 = Truck('Mercedes', 'Actros', 'White', 100, '654321', 'Furniture', 2000)

bus1.drive()
bus1.drift()
bus1.cargo()
print(bus1.get_brand())
print(bus1.get_name())
print(bus1.get_color())
print(bus1.get_capacity())
print(bus1.get_plate_number())
print(bus1.public_transport)
print(bus1.direction)

truck1.drive()
truck1.drift()
print(truck1.get_brand())
print(truck1.get_name())
print(truck1.get_color())
print(truck1.get_capacity())
print(truck1.get_plate_number())
print(truck1.cargo_type)
print(truck1.cargo_weight)
