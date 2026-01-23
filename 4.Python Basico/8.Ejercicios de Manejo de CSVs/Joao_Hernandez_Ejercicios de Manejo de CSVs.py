#Excercise 1
#Create a program that allow yo type x amount of videogames and save it on a CSV file 

import csv


def excercice_1():

    try:

        num_games = int(input("Insert the amount of games you like to add to the file: "))
        

        def intro_games(cycle):
            counter = 0
            game_list = []
            while counter < cycle:
                
                game = str(input("Type the game name: "))
                gender = str(input("Type the game gender: "))
                developer = str(input("Type the game developer: "))
                clasification = str(input("Type the game clasification: "))
                game_dic = {
                'game':game,
                'gender':gender,
                'developer':developer,
                'clasification':clasification,
                }
                game_list.append(game_dic)
                counter += 1


            game_headers = (
                'game',
                'gender',
                'developer',
                'clasification',
                )

            with open("C:\\Users\\jhmba\\Downloads\\Python\\Games.txt", "w" , encoding="utf-8") as file:
                writer = csv.DictWriter(file, game_headers)
                writer.writeheader()
                writer.writerows(game_list)



    
        intro_games(num_games)


    except ValueError as error:
        print(f"Error [ValueError]: You tried to enter an incorrect value")

    

excercice_1()


#Excercise 1
#We will do a variance of the above that saves with tab instead of comma

import csv


def excercice_2():

    try:

        num_games = int(input("Insert the amount of games you like to add to the file: "))
        

        def intro_games(cycle):
            counter = 0
            game_list = []
            while counter < cycle:
                
                game = str(input("Type the game name: "))
                gender = str(input("Type the game gender: "))
                developer = str(input("Type the game developer: "))
                clasification = str(input("Type the game clasification: "))
                game_dic = {
                'game':game,
                'gender':gender,
                'developer':developer,
                'clasification':clasification,
                }
                game_list.append(game_dic)
                counter += 1


            game_headers = (
                'game',
                'gender',
                'developer',
                'clasification',
                )

            with open("C:\\Users\\jhmba\\Downloads\\Python\\Games2.txt", "w" , encoding="utf-8") as file:
                writer = csv.DictWriter(file, game_headers,delimiter="\t")
                writer.writeheader()
                writer.writerows(game_list)



    
        intro_games(num_games)


    except ValueError as error:
        print(f"Error [ValueError]: You tried to enter an incorrect value")

    

excercice_2()