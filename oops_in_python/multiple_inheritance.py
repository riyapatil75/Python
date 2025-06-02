class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

class Battery:
    def battery_info(self):
        return "This is battery"
    
class Engine:
    def engine_info(self):
        return "This is Engine"
    
class ElectricCarTwo(Battery,Engine,Car):
    pass

my_tesla= ElectricCarTwo("Tesla","Model S")
print(my_tesla.engine_info())
print(my_tesla.battery_info())
print(my_tesla.model)
        
    