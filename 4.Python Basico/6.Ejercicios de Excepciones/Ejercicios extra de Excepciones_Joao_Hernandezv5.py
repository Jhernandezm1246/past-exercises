#Exercise 1 

#Request the user his name, rise ValueError if the number has a number 
#THen as for the user age and capture value error if not a number 
#If everything is ok please print Hello name your age is age 



def exercise_one():



    def name_and_age():

        
        name = str(input("Please type your name: "))

            
        if name.isdigit() == True:
            raise ValueError ("The name can not be a number or have numbers")


        
        try:
            age = int(input("Type your age: "))

        except ValueError as error:
            print(f"Error [ValueError] The age can not be a word or have decimals")

        
        if name.isdigit() == False and age > 0:

            return print(f"Hello {name}, your age is {age}")
        
        else:
            return print("The values are incorrect")

    name_and_age()

exercise_one()



#Exercise 2 

#Create a function to convert into int  
#Receive a list of strings and try to convert the using int 
#use try-except to capture the ValueError
#If one of the elements can not be converted print "We can not convert [element]"

def exercise_two():

    try:
        selection = str(input("Would you like to start the program (Y/N)").upper())

    except ValueError as error:
        print(f"Error [ValueError] Please note that at this step the only accepted options are Y or N")


    def new_list(selection):


        new_list = []

        counter = 0 

        if selection == "Y":

            try:

                records  = int(input("Type the number of records you like to add to the list: "))

            except ValueError as error: 
                print(f"Error [ValueError] Please note at this point you should only add numbers")

            while counter < records:

                new_value = input("Type the values you like to add to the list: ")

                new_list.append(new_value)

                counter += 1
        
            return new_list

        else:

            print("Thanks for using the program")
            return new_list
        
    

    list_to_program = []

    list_to_program.extend(new_list(selection))


    def convert_to_int(list):


        for num in list:

            try:

                new_num = int(num)

                print("Result")

                print(f"\"{num}\" converted to {new_num}")

            except ValueError as error:
                print(f"Error [ValueError] We could not convert {num}")


    convert_to_int(list_to_program)
            


exercise_two()




#Exercise 3 

#Create a function to sum values
#Receive a list of strings and try to convert them to float
#use try-except to capture the ValueError
#If one of the elements can not be converted print "We can not convert [element]"


def exercise_three():

    try:
        selection = str(input("Would you like to start the program (Y/N)").upper())

    except ValueError as error:
        print(f"Error [ValueError] Please note that at this step the only accepted options are Y or N")


    def new_list(selection):


        new_list = []

        counter = 0 

        if selection == "Y":

            try:

                records  = int(input("Type the number of records you like to add to the list: "))

            except ValueError as error: 
                print(f"Error [ValueError] Please note at this point you should only add numbers")

            while counter < records:

                new_value = input("Type the values you like to add to the list: ")

                new_list.append(new_value)

                counter += 1

        
            return new_list

        else:

            print("Thanks for using the program")
            return new_list
        
    

    list_to_program = []

    list_to_program.extend(new_list(selection))


    def convert_to_int(list):

        total = 0

        for num in list:

            try:

                new_num = float(num)

                print("Result")

                print(f"{new_num} added correctly")

                total += new_num



            except ValueError as error:
                print(f"Error [ValueError] Invalid element {num}")

        
        print(f"Total sum of numbers is {total} ")

            


    convert_to_int(list_to_program)
            


exercise_three()