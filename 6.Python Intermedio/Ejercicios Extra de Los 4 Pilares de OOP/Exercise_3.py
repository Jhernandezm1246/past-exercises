#Exercise 3
#Create a base class Vehicle with attributes _brand and _year 
#add a method get_info() that gives back the description of the vehicle
#then create 2 child classes Car and Motorcycle 
#Each of them has to add their own attribute door or type and override the method get info to get additional information

from abc import ABC, abstractmethod

class Vehicle(ABC):

    def __init__(self,brand,year):
        
        self.brand = brand
        self.year = year


    @abstractmethod
    def get_info(self):

        pass



class Car(Vehicle):


    def __init__(self, brand, year, doors):
        super().__init__(brand, year)
        self.doors = doors


    def get_info(self):
        
        return self.brand , self.year ,  self.doors


class Motorcycle(Vehicle):

    def __init__(self, brand, year, model):
        super().__init__(brand, year)
        self.model = model


    def get_info(self):

        return self.brand , self.year , self.model
    

vehicle_one = Car("Toyota", 2020, 4)

vehicle_two = Motorcycle("Yamaha", 2022, "R9")


print(vehicle_one.get_info())

print(vehicle_two.get_info())