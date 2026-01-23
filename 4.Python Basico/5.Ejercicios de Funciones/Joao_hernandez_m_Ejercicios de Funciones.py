#Excercise 1 
#Create 2 functions and print them and that one function calls the other function


def run_excercice_1():


    def first_function():
        return f"Hola"


    def second_function():
        greating = first_function()
        print(f"{greating} Mundo")


    second_function()


run_excercice_1()



#Excercise 2
#Experiment with the scope concept 
#Try accesing a variable define within a function from outside
#Try accesing a global variable from a function and change its value 
def run_excercice_2():


    def forth_function():
        new_variable = "Hello Word"

    #print(f"{new_variable}")
    #NameError: name 'new_variable' is not defined

    other_variable = "Dog"


    def fifth_function():
        global other_variable
        other_variable = "cat"
        return print(other_variable)

    fifth_function()

run_excercice_2()




#Excercise 3
#Create a function that returns the sum of all values from a list 
#The function will have a parameter that will be the list and will retunr the sum 

def run_excercice_3():


    def sum_of_lists(my_list):
        all_numbers = 0
        for num in my_list:
            all_numbers = all_numbers + num
        
        return all_numbers

    new_list = []
    nums_in_list = int(input("Please type how many numbers the list will have: "))

    counter = 0

    while counter < nums_in_list:
        num_for_list = int(input("Insert the number for the list: "))
        new_list.append(num_for_list)
        counter += 1

    new_num = sum_of_lists(new_list)

    print(f"The total sum of all numbers corespond to {new_num}")

run_excercice_3()


#Excercise 4
#Create a function come back to a strig and return it 
def run_excercice_4():


    def string_up_side_down(my_string):
        inverted_string = []
        for index in range(len(my_string)-1,-1,-1):
            inverted_string.append(my_string[index])
            new_string = " ".join(inverted_string)
            

        return new_string

    new_string = str(input("Type a word and we will give it back to you up side down: "))

    up_side_string = string_up_side_down(new_string)

    print(f"Your new word is comming the other way {up_side_string}")

run_excercice_4()



#Excercise 5
#Create a function that prints the number of uppercase and lower cases characters on a string 

def run_excercice_5():


    def char_count(string):
        counter_upper = 0
        counter_lower = 0
        for char in string:
            if char.isupper() : 
                counter_upper += 1

            else:
                counter_lower +=1

        return f"There's {counter_upper} upper cases and {counter_lower} lower cases"


    new_string = str(input("Type a phrase: "))

    count_char = char_count(new_string)

    print(count_char)

run_excercice_5()


#Excercise 6
#Create a function that accepts a string with separate words by a hyphen and terun the same string but in alphabetic order 

def run_excercice_6():


    def alphabetic_list(string):
        new_string = string.split("-")
        sorted_string = sorted(new_string)
        sorted_string = "-".join(sorted_string)
        return sorted_string


    string = str(input("Add a list of words separeted by - and the sytem will give it back sorted: "))

    sorted_list = alphabetic_list(string)

    print(sorted_list)

run_excercice_6()



#Excercise 7
#Create a function that acept a list of numbers and return a list of numbers with only prime numbers 

def run_excercice_7():


    def prime_list_fix(list):
        new_list = []
        for num in list:
            is_prime = True
            if num > 1:
                for i in range(2, num//2 + 1): 
                    if num % i == 0:
                        is_prime = False
                        break
                if is_prime:
                    new_list.append(num)
        return new_list




    counter = 0 
    num_of_list = int(input("Insert the amount of numbers you you like to check: "))
    list_num = []

    while counter < num_of_list:
        new_num = int(input("Insert a new number: "))
        list_num.append(new_num)
        counter +=1

    prime = prime_list_fix(list_num)

    print(f"The primo numbers are: {prime}")


run_excercice_7()

