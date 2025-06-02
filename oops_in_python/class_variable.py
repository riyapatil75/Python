class Car:
    total_car = 0

    def __init__(self,brand,model):
        self.brand =brand
        self.model=model
        Car.total_car+=1

Car("Tata","Safari")
Car("Tata","Nexon")
Car("Tata","Nexon")
Car("Tata","Nexon")
Car("Tata","Nexon")
Car("Tata","Nexon")
Car("Tata","Nexon")
Car("Tata","Nexon")
Car("Tata","Nexon")
Car("Tata","Nexon")


print(Car.total_car)