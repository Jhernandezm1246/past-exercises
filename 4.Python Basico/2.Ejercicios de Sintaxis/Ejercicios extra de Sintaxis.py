#Excercise 1 
#Create a programn that requests a price of a product and the user can calcula it discount and show the final price 
product_price = int(input("Please add the product price and we will calculate the discount for you: "))

if product_price < 100:
    discount = product_price * 0.02

else:
    discount = product_price *0.1

new_price = product_price - discount

print(f"The product price was {product_price} the discount was {discount} and the price after the discount is {new_price}")

#Excercise 2
#Create a program that request time in seconds to the user and calculate if the time is below or above 10 minutes if it is below show in screen how much seconds will need to reach 10 minutes and if its higher to show Higher or if its equal to show iqual

time_sec = int(input("Please introduce a number in seconds and we let you know if it is below or above 10 minutes: "))

ten_min = 10*60

if time_sec < ten_min:
    missing = ten_min - time_sec
    print(f"Your time is lower to 10 minutes by {missing} seconds")

elif time_sec > ten_min:
    print(f"The time you submither is higher than 10 minutes")

else:
    print("The time you submited is exactly 10 minutes")

#Excercise 3 
#Create a program that request the user to guess a number from 1 to 10 do not close the program until they find the correct number 

import random

user_num = 0 

program_num = random.randint(1,10)

while user_num != program_num:
    user_num = int(input("Type a number to try to guess the secret number between 1 and 10: "))
    if user_num < 1 or user_num > 10:
        print("Incorrect number out of range ")

    elif user_num == program_num:
        print("Congratulations you guess the right number")


#Excercise 4
#Create a program that requests 3 numbers if one of those numbers is 30 or the sum of them is 30 the program show display a corrrect message if not display incorrect

print("The program will request 3 numbers and let you know if one of them is 30 or the 3 of them sum 30")
first = int(input("First Number: "))
second = int(input("Second Number: "))
third = int(input("Third Number: "))

forth = first + second + third

if first  == 30:
    print("One of the numbers is 30")

elif second  == 30:
    print("One of the numbers is 30")

elif third  == 30:
    print("One of the numbers is 30")  

elif forth == 30: 
    print("Correct")

else:
    print("Incorrect")


#Excercise 5
#Create a program that request the temperture in celsius and convert it to fahrenheit and kelvin and show the 3 values 

celcius = float(input("Please type the a temperture on celsius and we will give you back fahrenheit and kelvin: "))

farenheit = (celcius * 9/5) + 32

kelvin = celcius + 273.15

print(f"The value on celcius is {celcius} on farenheit is {farenheit} and on kelvin is {kelvin}")




#Excercise 6
#Request an user to type a number from 1 to 10 and give back the multiplication table from 1 to 12

user_number = int(input("Please type a number from 1 to 10 and we will give you back the multiplication table from 1 to 12: "))

multi_table = [1,2,3,4,5,6,7,8,9,10,11,12]

for num in multi_table:
    multi_num = user_number * num
    print(f"Multiplication table {user_number} x {num} = {multi_num}")

