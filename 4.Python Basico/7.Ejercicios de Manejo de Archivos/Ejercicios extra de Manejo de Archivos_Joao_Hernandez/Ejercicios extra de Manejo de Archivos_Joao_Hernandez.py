#Exercise 1
#Create a program which reads a file line by line and remove the break lines and write the file on one single line 


def exercise_one():


    def single_line():


        single_line = []

        with open("split_lines.txt", "r") as file:
            for line in file.readlines():
                single_line.append(line)
                print(line)
            print(single_line)

        
            string_line = " ".join(single_line)
            clean_string = string_line.replace('\n', '').replace('\r', '')

            print(clean_string)

        
        with open("New_file.txt", "a") as file:
            file.write(clean_string)

    
    single_line()



exercise_one()



#Exercise 2
#Create a program that reads a file and tell you how many words are in it

def exercise_two():


    def count_words():

        new_list = []


        with open("Count_words.txt", "r") as file:
            for line in file.readlines():

                new_list.append(line)
        
        counter = 0

        for word in new_list:
            new_word = word.split()
            for word in new_word:
                counter += 1
                    
            
            print(new_word)

        print(f"This file has {counter} words")

    count_words()



exercise_two()




#Exercise 3
#Create a program that reads a file by line and convert it to upper letters then write it on a new file

def exercise_three():


    def upper_words():


        

        with open("Lower_Words.txt", "r") as file:
            for line in file.readlines():
                with open("New_Upper.txt", "a") as file:
                    file.write(line.upper())
                    print(line)


        
    upper_words()

exercise_three()




#Exercise 4
#Create a program that reads a file by line and convert it to upper letters then write it on a new file


def exercise_four():

    try:
        selection = str(input("Would you like to create a new file? (Y/N)"))

    except ValueError as error:
        print(f"Error [ValueError] Please note at this point you should only type Y or N")


    def new_file(selection):

        if selection == "Y":

            text_line = str(input("Please type a string line: "))

            with open("new_file_text.txt", "x") as file:
                with open("new_file_text.txt", "w") as file:
                    file.write(text_line)
                    print(text_line)

        else:
            print("Thanks for using the program")
            return 0

    new_file(selection)    


exercise_four()