"""#Exercise 1 
#Create a program that iterates and prints the valoes of both lists with the same size at the same time 

first_list = ["Hay", "en", "que", "iteracion", "indices", "muy"]
second_list = ["casos", "los", "la", "por", "es", "util"]

#This was the first way I try to resolve the excercise 

for word in(first_list):
    for words in (second_list):

        print(f"{first_list[0]} {second_list[0]}")
        print(f"{first_list[1]} {second_list[1]}")
        print(f"{first_list[2]} {second_list[2]}")
        print(f"{first_list[3]} {second_list[3]}")
        print(f"{first_list[4]} {second_list[4]}")
        print(f"{first_list[5]} {second_list[5]}")

#Then I went back to the material to find a more eficient way to do it this is what I made

for index in range(0,len(first_list)):
    word = first_list[index]
    words = second_list[index]
    print(f"{word} {words}")

"""

#Excercise 2
#Crete a string that can iterate and print a string letter by letter form right to left 

my_string = "Pizza con piña"
inverted_string = ""

for index in range(len(my_string)-1,-1,-1):
    inverted_string = my_string[index]
    print(f"{inverted_string}")

"""
#Excercise 3
#Create a program that changes the first and last number of a list, This should work with lists of any size 

my_list = [4, 3, 6, 1, 7]

print(f"Original list {my_list}")

deleted_num_two = my_list.pop()
deleted_num = my_list.pop(0)

my_list.insert(0,deleted_num_two)
my_list.append(deleted_num)


print(f"New list {my_list}")
print(f"First number moved {deleted_num}")
print(f"Last number moved {deleted_num_two}")



#Excercise 4
# Create a origran thar removes all the inpair numbers of a list 

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new_list =[]


for num in my_list:
    if num % 2 ==0:
        new_list.append(num)

print(new_list)



#Excercise 5
#Create a program that requests an user 10 numbers and at the end shows the numebrs that the user type in and then the hightst number 

print("The system will request 10 different numbers and then will show them up and show you the highest one")

counter = 0 
new_list = []


while counter < 10:
    num = int(input("Type a number: "))
    new_list.append(num)
    counter += 1

max_value = new_list[0]

for max_num in new_list:
    if max_num > max_value:
        max_value = max_num
        
print(f"The max number is {max_value}") 
print(new_list)

"""