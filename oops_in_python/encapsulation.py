class car:
    def __init__(self,__brand,model):
        self.__brand=__brand
        self.model=model

    def get_brand(self):#getter should always start wtih get_
        return self.__brand + "!"#__ lagane se attribute private ho jata hai 
    
class ElectricCar(car):
    def __init__(self,__brand, model,battery_size):
        super().__init__(__brand,model)
        self.battery_size=battery_size

my_car = ElectricCar("Tesla","Model S","85kWh")
# print(my_car.__brand)
print(my_car.get_brand())
