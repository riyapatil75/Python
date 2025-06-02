#static method ka object bana ke access nhi kr skte
class car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def fuel_type(self):
        return "Petrol or diesel"
     
    @staticmethod
    def general_description():#agar ststic method na hota to agrument me self lagana padta tha
        return "Cars are means of transport"
    
my_car=car("Tata","Nexon")
#print(my_car.general_decription()) #this will give an error
print(car.general_description())