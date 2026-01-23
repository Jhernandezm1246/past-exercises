#Exercise 1
#Create a program that opens a .csv file with the information of video games
# Read each line with csv.reader()
#Show the content on screen on a legible format 

import csv

def exercise_one():


    def csv_reader():
        
        with open("Games.csv","r") as file:

            reader = csv.DictReader(file)
            
            for value in reader:
                for key , value in value.items():
                    print(f"{key} : {value} ")
            
            

    csv_reader()


exercise_one()



#Exercise 2
#Create a program that opens a .csv file with the information of video games
# Request the user for a classification  
#show all games that have that classification 

import csv

def exercise_two():

    try:
        classification = str(input("Please type the classification and we will give you the list of games (E, E10+, T, M, AO): ").upper())

    except ValueError as error:
        print(f"Error [ValueError] Please note at this point you should only add one of the following (E, E10+, T, M, AO)")

    def csv_reader(classification):

        with open("Games.csv","r") as file:

            reader = csv.DictReader(file)
            
            
            for lines in reader:
                for key , value in lines.items():
                    if classification == value:
                        print(lines)


    csv_reader(classification)



exercise_two()


#Exercise 3
#Create a program that opens a .csv file with the information of video games
# Show how many games are for each gender


import csv

def exercise_three():


    def csv_reader():
        
        gender_group = {}

        with open("Games.csv","r") as file:

            reader = csv.DictReader(file)
            
            for value in reader:
                
                gender = value["gender"]

                if gender not in gender_group:
                        gender_group[gender] = {"count":0}
                gender_group[gender]["count"] += 1    
            
            print("Game gender found: ")
            for gen , count in gender_group.items():
                for counts in count.values():
                    print(f"{gen} : {counts}")
                
            

    csv_reader()



exercise_three()


#Exercise 4
#Create a program that opens a .csv file with the information of video games
# Show how many games are developed by a developer 


import csv

def exercise_four():

    try:
        developer = str(input("Please type the Developer and we will give you the list of games: ").upper())

    except ValueError as error:
        print(f"Error [ValueError] Error")

        
    def csv_reader(developer):

        with open("Games.csv","r") as file:

            reader = csv.DictReader(file)
            
            print(f"Games developed by {developer}: ")
            for lines in reader:
                for key , value in lines.items():
                    if developer == value.upper():
                        print(f"{lines["game"]} (Classification {lines["classification"]} Gender: {lines["gender"]})")

    csv_reader(developer)



exercise_four()
