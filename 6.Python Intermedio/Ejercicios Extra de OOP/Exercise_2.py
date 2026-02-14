#Exercise 2
#Create a class animal and two subclass dog and cat 
#Animal most have name and method speak that return "Make a noise"
#Dog should override speak to say guau
#Cat should override speak to sat miau

class Animal():

    def __init__(self,name):

        self.name = name

    def speak(self,speak):
        self.speak = speak 
        return speak
        

class Dog(Animal):
    
    def speak(self):
        
        speak = "Guau"
        return speak

class Cat(Animal):
    def speak(self):
        
        speak = "Miau"
        return speak

    
    


dog = Dog("Firulais")

cat = Cat("Misingo")

print(dog.speak())

print(cat.speak())