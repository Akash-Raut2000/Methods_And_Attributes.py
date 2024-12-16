class Car:

    wheel = 4
    def __init__(self,name,brand):
        self.name=name
        self.brand=brand

    def discription(self):
        return f"This is my car and the car name is {self.name}, and its brand is {self.brand}"

car1=Car("Fortuner", "Toyota")
car2=Car("G-Wagon", "Mercedies")

print(car1.discription())
print(car2.discription())

print(Car.wheel)