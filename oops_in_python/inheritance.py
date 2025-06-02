class car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        
    def full_name(self):
        return f"{self.brand} {self.model} "
    
class ElectricCar(car):
    def __init__(self,brand, model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size

my_car = ElectricCar("Tesla","Model S","85kWh")
print(my_car.model)
print(my_car.battery_size)
print(my_car.brand)
print(my_car.full_name())

