#Exercise 1

# Create a program that ask for a text and a character and the return how many times the character appear in the text 


def exercise_one():


    try:
        word = str(input("Time a word or a text: "))
        letter = str(input("Type the letter you like to count : "))

    except TypeError as error:
        print(f"Error [TypeError] Please note at this point you should only type letters no numbers")

    def char_count(word,letter):

        counter = 0

        for char in word:
            new_char = char
            if char == letter:
                counter += 1

        return print(f"We have found the character {counter} times")


    


    char_count(word,letter)


exercise_one()



#Exercise 2

# Create a function that receives a list of words and a number and return a new list with the words that has more letters than the selected number


def exercise_two():

    list_of_words = ["uno","dos","perro","caballo","aristocrata"]


    try:
        selection = str(input("Would you like to add a new word to the list ? (Y/N): ").upper())
        

    except ValueError as error:
        print(f"Error [ValueError] please note at this point you should not add any number only Y or N")


    def new_cycle(selection):

        new_list = []

        if selection == "Y":

            counter = 0 

            number_of_words = int(input("How many words you like to add: "))

            while counter < number_of_words:

                new_word = str(input("Type the new word: "))

                new_list.append(new_word)

                counter += 1

            return new_list
    
        else:
            print("Thanks no new words will be added")
            return new_list

    list_to_add = new_cycle(selection)

    list_of_words.extend(list_to_add)

    def word_check(list):

        new_list_count = []

        char_num = int(input("Type the number of letters you like to check: "))

        for word in list:
            char = len(word)
            if char == char_num:
                new_list_count.append(word)


        return print(f"The list of words with {char_num} is {new_list_count}")




    word_check(list_of_words)


exercise_two()



#Exercise 3

# Create a function that receives a string and return how many vocals it has 


def exercise_three():

    try:
        string_list = str(input("Please type a phrase or word and the system will give you have many vocals it has: "))


    except ValueError as error:
        print(f"Error [ValueError] Please note at  this point you should only add words no numbers")

    
    def vocal_finder(word):

        counter = 0 

        for vocal in word:
            if vocal == "a" or vocal == "e" or vocal == "i" or vocal == "o" or vocal == "u":

                counter += 1

        
        return print(f"Your string has {counter} vocals")
    
    vocal_finder(string_list)




exercise_three()


