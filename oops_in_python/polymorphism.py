class car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def full_name(self):
        return f"{self.brand} {self.model} "
    def fuel_type(self):
        return "Petrol"
    
class ElectricCar(car):
    def __init__(self,brand, model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size
    def fuel_type(self):
        return "Electrical"
    
my_car =car("Mercedes","Class A")
my_tesla = ElectricCar("Tesla","Model S","85kWh")
print(my_car.brand)
print(my_car.model)
print(my_car.fuel_type())
print(my_tesla.battery_size)
print(my_tesla.full_name())
print(my_tesla.fuel_type())

