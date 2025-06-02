class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.__model=model
        
    @property #@property ko use krke aisi property ko hide kr skte hai jo ha nhi chahte ki sab use kare
    def model(self):
        return self.__model    
    
my_car=Car("Mercedes","class A")
print(my_car.model) # we cannot use it as a method we can use it as property