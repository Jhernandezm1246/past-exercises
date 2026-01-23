#Excercise 1
#Create a algorithm that uses print to show your full name age, favorite color and favorite meal


full_name = str(input("Type your full name: " ))
age = int(input("Type your age: " ))
favorite_color = str(input("Type your favorite color: " ))
favorite_meal = str(input("Type your favorite meal: " ))


print(f"My name is {full_name}")
print(f"I am {age} years old")
print(f"My favorite color is {favorite_color}")
print(f"My favorite meal is {favorite_meal}")


#Excercise 2
#Create an algorithm that shows your how old you will be in 10 year 

age = int(input("Type your age: " ))

new_age = age + 10

print(f"I am {age} years old and will be {new_age} in 10 year ")


#Excercise 3
# Create an algorithm that defines an amount of meters and the your the amount in centimeters 

meters = int(input("Please add the amount of meters you like to know the value on centimeters and we will calculate for you: "))

centimeters = meters * 100

print(f"Please note that {meters} meters in centimeters is {centimeters}")