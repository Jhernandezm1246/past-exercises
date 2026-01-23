#Excercise 1
#Create a program that counts how many specific numbers exist on a list, ask the user for the list and the let him know how many times the number selected appears on the list 

my_list = []

num_find = int(input("Please type the number you like to search for in the list: "))
amount_list = int(input("Please type how many numbers you like to add to your list: "))
counter = 0
while counter < amount_list:
    list_num = int(input("Add a number to your list: "))
    counter +=1
    my_list.append(list_num)

count = my_list.count(num_find)

print(f"The number {num_find} appears {count} times in the list ")

#Excercise 2
#Create a program that verify if all number on a list are positive

my_list = []
negative_list = []

amount_list = int(input("Please type how many numbers you like to add to your list: "))
counter = 0
while counter < amount_list:
    list_num = int(input("Add a number to your list: "))
    counter +=1
    my_list.append(list_num)

for num in my_list:
    if num < 0:
        negative_list.append(num)

if len(negative_list) > 0:
    print("Not all numbers are positive")
    print(F" List of all number {my_list}")
    print(F" List of negative numbers {negative_list}")

else:
    print("All numbers are positive")
    print(F" List of all number {my_list}")
    

#Excercise 3
#Create a program that shows the lower number from a list 


my_list = []


amount_list = int(input("Please type how many numbers you like to add to your list: "))
counter = 0
while counter < amount_list:
    list_num = int(input("Add a number to your list: "))
    counter +=1
    my_list.append(list_num)  
    

lower_value = my_list[0]

for low_num in my_list:   
    if low_num < lower_value:
        lower_value = low_num


print(f"The lower number is {lower_value}")


#Excercise 4
#Create a program that receive a list of values and calculate the average the crete a list only with the values above the average 

my_list = []

total_numbers = 0


amount_list = int(input("Please type how many numbers you like to add to your list: "))
counter = 0
while counter < amount_list:
    list_num = int(input("Add a number to your list: "))
    counter +=1
    my_list.append(list_num)  
    total_numbers = total_numbers + list_num


average_num = total_numbers / amount_list

higher_list = []

for num in my_list:
    if num > average_num:
        higher_list.append(num)

print(f"Total list is {my_list}")


print(f"The average is {average_num}")


print(f"This is the list of number that are higher than the average {higher_list}")



#Excercise 5
#Create a program that receive a list of values and calculate the average the crete a list only with the values above the average 

print("Next we will request to type 5 words: ")

four_list = []
all_list = []

counter = 0

while counter < 5:
    word = str(input("Type your word: "))
    all_list.append(word)
    counter += 1

for words in all_list:
    if len(words) > 4:
        four_list.append(words)

print(f"The full list of words that you added was {all_list}")
print(f"The words with more than 4 letters are  {four_list}")