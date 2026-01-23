#Excesice 1 
#Experience doing diferen sums betwen diferent types of data and show up the results 

string = str("Hello")
intiger = int(1)
boolean = bool(True)
floats = float(1.5)
lists = [1,2,3,4]

print(string + string)
#print(string + intiger)
#TypeError: can only concatenate str (not "int") to str
#print(string + boolean)
#TypeError: can only concatenate str (not "bool") to str
#print(string + floats)
#TypeError: can only concatenate str (not "float") to str
#print(lists + string)
#TypeError: can only concatenate list (not "str") to list
#print(lists + intiger)
#TypeError: can only concatenate list (not "int") to list
#print(lists + boolean)
#TypeError: can only concatenate list (not "bool") to list
#print(lists + floats)
#TypeError: can only concatenate list (not "float") to list
#print(intiger + string)
#TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(intiger + intiger)
print(intiger + boolean)
print(intiger + floats)
#print(boolean + string)
#TypeError: unsupported operand type(s) for +: 'bool' and 'str'
print(boolean + intiger)
print(boolean + boolean)
print(boolean + floats)
#print(floats + string)
#TypeError: unsupported operand type(s) for +: 'float' and 'str'
print(floats + intiger)
print(floats + boolean)
print(floats + floats)


#Exercise 2 
#Cree un programa que le pida al usuario su nombre, apellido, y edad, y muestre si es un bebé, niño, preadolescente, adolescente, adulto joven, adulto, o adulto mayor.
#Create a program that requests user name, last name and age and show up if its a babe, a kit, a preteen, a teen, a young adolt an adolt or a older adult

name = str(input("Type your name: "))
last_name = str(input("Type your last name: "))
age = int(input("Type your age: "))

if age < 3:
    print(f"Hello {name} {last_name} you are a baby")
elif age < 8:
    print(f"Hello {name} {last_name} you are a kit")
elif age < 15:
    print(f"Hello {name} {last_name} you are a preteen")
elif age < 18:
    print(f"Hello {name} {last_name} you are a teen")
elif age < 30:
    print(f"Hello {name} {last_name} you are a young adult") 
elif age < 50:
    print(f"Hello {name} {last_name} you are a adult ") 
else:
    print(f"Hello {name} {last_name} you are a older adult ") 

#Excercise 3
#Create a program with a secret number form 1 to 10, The program show not close until the user chose the correct number 

import random



num_secret = random.randint(1,10)

while True:

    num_user = int(input("Try to guess the numer that the system holds, Next type your guess from 1 to 10: "))
    if num_user < 1 or num_user > 10:
        print("The number is out of range 1 to 10")


    elif num_user == num_secret:
        print("Congratulations you select the correct number ")
        break

    else:
        print("Incorrect number try again")

        

#Excercise 4
#Create a program that request 3 number to user and show the highest 


print("Next the system will request 3 numbers and will give you the highest: ")

num_one = int(input("Type the first number: "))
num_two = int(input("Type the second number: "))
num_three = int(input("Type the third number: "))

if num_one > num_two and num_one > num_three:
    print(f"The highest number is {num_one}")
elif num_two > num_one and num_two > num_three:
    print(f"The highest number is {num_two}")
elif num_three > num_two and num_three > num_one:
    print(f"The highest number is {num_three}")
elif num_one == num_two and num_one == num_three:
    print("All numbers are the same")
elif num_one == num_two and num_one > num_three:
    print(f"The highest numbers are {num_one} and {num_two} they are the same")
elif num_one == num_three and num_one > num_two:
    print(f"The highest numbers are {num_one} and {num_three} they are the same")
elif num_two == num_three and num_two > num_one:
    print(f"The highest numbers are {num_two} and {num_three} they are the same")
else:
    print("You type an invalid number or text")


#Excercise 5

#Given  the amount of scores that a student has please calculate the amount of average good and bad scores and the total amount 



print("Next you will be requested to input the amount of scores that you like to calculate and the system will let you know which ones were approve and unapprove and the total average for both")
amount_scores = int(input("Type the amount of scores: "))
counter = 1 
counter_good_scores = 0
counter_bad_scores = 0
total_bad_scores = 0
total_good_scores = 0

while counter <= amount_scores:
    score = int(input("Type the score: "))
    if score < 70:
        total_bad_scores = total_bad_scores + score
        counter_bad_scores+= 1
    else:
        total_good_scores = total_good_scores + score
        counter_good_scores += 1
    counter += 1 

average_good_scores = total_good_scores/counter_good_scores
average_bad_scores = total_bad_scores/counter_bad_scores
average_all_scores = (total_bad_scores+total_good_scores)/(counter_bad_scores+counter_good_scores)

print(f"The amount of approved scores is {counter_good_scores} and your average {average_good_scores}")
print(f"The amount of unapproved scores is {counter_bad_scores} and your average {average_bad_scores}")
print(f"The total amount of scores is {amount_scores} and your final score average is {average_all_scores}")


