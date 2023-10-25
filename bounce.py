class Vehicle:
    def __init__(self, brand, name, color, capacity, plate_number):
        self._brand = brand
        self._name = name
        self._color = color
        self._capacity = capacity
        self._plate_number = plate_number
        self._is_running = False

    def drive(self):
        print(f"{self._name} is driving!")

    def drift(self):
        print(f"{self._name} is drifting!")

    def carry_cargo(self):
        print(f"{self._name} is carrying cargo!")

    def start(self):
        self._is_running = True

    def stop(self):
        self._is_running = False

    def is_running(self):
        return self._is_running

    def get_brand(self):
        return self._brand

    def set_brand(self, brand):
        self._brand = brand

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color

    def get_capacity(self):
        return self._capacity

    def set_capacity(self, capacity):
        self._capacity = capacity

    def get_plate_number(self):
        return self._plate_number

    def set_plate_number(self, plate_number):
        self._plate_number = plate_number

class Bus(Vehicle):
    def carry_cargo(self):
        print(f"{self._name} is carrying passengers in a bus!")

class Truck(Vehicle):
    def carry_cargo(self):
        print(f"{self._name} is carrying goods in a truck!")


car = Vehicle("Toyota", "Sedan", "Blue", 4, "ABC123")
bus = Bus("Mercedes", "Bus", "Yellow", 40, "XYZ789")
truck = Truck("Ford", "Truck", "Red", 1000, "DEF456")

car.drive()
car.start()
print(f"Is the car running? {car.is_running()}")
car.stop()
print(f"Is the car running? {car.is_running()}")
car.drift()
car.set_color("Green")
print(f"Car color: {car.get_color()}")

bus.carry_cargo()
bus.drive()
bus.drift()
print(f"Bus brand: {bus.get_brand()}")

truck.carry_cargo()
truck.drive()
truck.drift()
print(f"Truck capacity: {truck.get_capacity()}")
