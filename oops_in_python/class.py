
class Car:
    def __init__(self,brand,model):
        self.brand= brand
        self.model= model

my_car= Car("Toyota","Corolla")
print(my_car.brand)
print(my_car.model)

my_new_car= Car("Toyota","Corolla")
print(my_new_car.model)


# constructor is the ethod in which as soon as the object of the class is created the constructor method will run first, despite anhy number of method present in our class.
#__init__ is the constructor