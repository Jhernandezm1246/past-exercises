#Exercise 1 

#Request the user his name, rise ValueError if the number has a number 
#THen as for the user age and capture value error if not a number 
#If everything is ok please print Hello name your age is age 



def exercise_one():



    def name_and_age():

        
        name = str(input("Please type your name: "))

            
        if name.isdigit() == True:
            raise ValueError ("The name can not be a number or have numbers")

        age = 0
        
        age = int(input("Type your age: "))
        
        if name.isdigit() == False and age > 0:

            return print(f"Hello {name}, your age is {age}")
        
        else:
            return print("The values are incorrect")
    try:

        name_and_age()

    except ValueError as error:
        print(f"Error [ValueError] One or more values are incorrect")

exercise_one()



#Exercise 2 

#Create a function to convert into int  
#Receive a list of strings and try to convert the using int 
#use try-except to capture the ValueError
#If one of the elements can not be converted print "We can not convert [element]"

def exercise_two():

    
    selection = str(input("Would you like to start the program (Y/N)").upper())

    
    def new_group_for_conversion_int(selection):


        new_group = []

        if selection == "Y":

            records  = int(input("Type the number of records you like to add to the list: "))
            
            if str(records).isdigit():
                counter = 0

                while counter < records:

                    new_value = input("Type the values you like to add to the list: ")

                    new_group.append(new_value)

                    counter += 1
            
                return new_group

            else:
                print(" Please note at this point you should only add numbers")
                return new_group

        else:

            print("Thanks for using the program")
            return new_group
        
    

    group_to_program = []

    try:

        group_to_program.extend(new_group_for_conversion_int(selection))

    except ValueError as error: 
        print(f"Error [ValueError] Please note at this point you should only add numbers")



    def str_conversion_to_int(group):

        print("Result")

        for num in group:

            try:
                new_num = int(num)
                print(f"\"{num}\" converted to {new_num}")

            except ValueError as error:
                print(f"Error [ValueError] We could not convert {num}")


    str_conversion_to_int(group_to_program)
            


exercise_two()




#Exercise 3 

#Create a function to sum values
#Receive a list of strings and try to convert them to float
#use try-except to capture the ValueError
#If one of the elements can not be converted print "We can not convert [element]"


def exercise_three():

    
    selection = str(input("Would you like to start the program (Y/N)").upper())

    def new_group_for_conversion_float(selection):


        new_group = []

        if selection == "Y":

            records  = int(input("Type the number of records you like to add to the list: "))
            
            if str(records).isdigit():
                counter = 0

                while counter < records:

                    new_value = input("Type the values you like to add to the list: ")

                    new_group.append(new_value)

                    counter += 1
            
                return new_group

            else:
                print(" Please note at this point you should only add numbers")
                return new_group

        else:

            print("Thanks for using the program")
            return new_group
        
    

    group_to_program = []

    try:

        group_to_program.extend(new_group_for_conversion_float(selection))

    except ValueError as error: 
        print(f"Error [ValueError] Please note at this point you should only add numbers")



    def str_conversion_to_float(list):

        total = 0

        for num in list:

            try:
                number_converted_flt = float(num)

                print("Result")

                print(f"{number_converted_flt} added correctly")

                total += number_converted_flt

            except ValueError as error:
                print(f"Error [ValueError] Invalid element {num}")
        
        print(f"Total sum of numbers is {total} ")
            
    str_conversion_to_float(group_to_program)
            


exercise_three()

