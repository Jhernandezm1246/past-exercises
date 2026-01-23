#Exercise 1
#Create a program that opens a JSON document 
#Read the JSON document and run the list of Pokemon n console their name, type or any other attribute 

import json


def exercise_one():


    def poke_info_specific_stats():

        with open("pokemon.json", "r") as file:
            data = json.load(file)
            for pokemon in data:


                print(f"Name : {pokemon["name"]["english"]} , Type : {pokemon["type"][0]} , Attack : {pokemon["base"]["Attack"]}")

    poke_info_specific_stats()


exercise_one()


#Exercise 2
#Create a program that opens a JSON document 
#Read the JSON document and ask the user for an specific type and print all pokemon with that type

def exercise_two():


    def poke_info_specific_type():

        with open("pokemon.json", "r") as file:
            data = json.load(file)

            try:
                type_selection = str(input("Please write the Type of pokemon you like to look for (Water - Fire - Grass - Electric, etc): ").upper())

            except ValueError as error:
                print(f"Error [ValueError] Please select only the available types")

            print("The pokemon with this type are: ")
            for pokemon in data:
                if type_selection == pokemon["type"][0].upper():

                    print(f"Name : {pokemon["name"]["english"]}")

    poke_info_specific_type()


exercise_two()



#Exercise 3
#Create a program that opens a JSON document 
#Read the JSON document and show the main statistics for each of them

def exercise_three():


    def poke_info_main_stats():

        with open("pokemon.json", "r") as file:
            data = json.load(file)
            for pokemon in data:


                print(f"Name : {pokemon["name"]["english"]} \n Attack : {pokemon["base"]["Attack"]} \n Defense : {pokemon["base"]["Defense"]} \n Speed : {pokemon["base"]["Speed"]}")

    poke_info_main_stats()


exercise_three()


#Exercise 4
#Create a program that opens a JSON document 
#Read the JSON document and group pokemon by type and the provide a average of their level


def exercise_four():


    def poke_info_level_average():

        with open("pokemon.json", "r") as file:
            data = json.load(file)

            poke_type_avg_group = {}

            
            for pokemon in data:
                

                type_group = pokemon["type"][0].upper()
                poke_level = pokemon["base"]["level"]

                if type_group not in poke_type_avg_group:
                    poke_type_avg_group[type_group] = {"count" : 0,"total" : 0}

                poke_type_avg_group[type_group]["count"] += 1
                poke_type_avg_group[type_group]["total"] += poke_level
                

            for data , value in poke_type_avg_group.items():
                
                print(f"Type : {data} - The average level is: {value["total"]/value["count"]}")
                

            
            
    poke_info_level_average()

exercise_four()