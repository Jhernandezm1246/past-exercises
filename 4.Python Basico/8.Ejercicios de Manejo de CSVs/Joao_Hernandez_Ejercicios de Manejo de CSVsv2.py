#Excercise 1
#Create a program that allow yo type x amount of videogames and save it on a CSV file 

import csv

def excercice_1():
    try:
        new_cycle = str(input("Would you like to perform an operation Y/N: "))
        cycle = new_cycle.upper()
        num_games = int(input("Insert the amount of games you would like to add to the file: "))
        
        while cycle == "Y":
            def intro_games(num):
                counter = 0
                game_list = []
                while counter < num:
                    game = str(input("Type the game name: "))
                    gender = str(input("Type the game gender: "))
                    developer = str(input("Type the game developer: "))
                    clasification = str(input("Type the game classification: "))
                    game_dic = {
                        'game': game,
                        'gender': gender,
                        'developer': developer,
                        'clasification': clasification,
                    }
                    game_list.append(game_dic)
                    counter += 1

                    new_cycle = str(input("Would you like to make any adjustment Y/N: "))
                    if new_cycle.upper() == "N":
                        break

                game_headers = ('game', 'gender', 'developer', 'clasification')

                with open("C:\\Users\\jhmba\\Downloads\\Python\\Games.csv", "w", encoding="utf-8") as file:
                    writer = csv.DictWriter(file, game_headers)
                    writer.writeheader()
                    writer.writerows(game_list)

                return new_cycle

            new_cycle = intro_games(num_games)
            cycle = new_cycle

        print("Thanks for using the program")

    except ValueError as error:
        print(f"Error [ValueError]: You tried to enter an incorrect value")

excercice_1()



#Excercise 2
#We will do a variance of the above that saves with tab instead of comma




import csv

def excercice_2():
    try:
        new_cycle = str(input("Would you like to perform an operation Y/N: "))
        cycle = new_cycle.upper()
        num_games = int(input("Insert the amount of games you would like to add to the file: "))
        
        while cycle == "Y":
            def intro_games(num):
                counter = 0
                game_list = []
                while counter < num:
                    game = str(input("Type the game name: "))
                    gender = str(input("Type the game gender: "))
                    developer = str(input("Type the game developer: "))
                    clasification = str(input("Type the game classification: "))
                    game_dic = {
                        'game': game,
                        'gender': gender,
                        'developer': developer,
                        'clasification': clasification,
                    }
                    game_list.append(game_dic)
                    counter += 1

                    new_cycle = str(input("Would you like to make any adjustment Y/N: "))
                    if new_cycle.upper() == "N":
                        break

                game_headers = ('game', 'gender', 'developer', 'clasification')

                with open("C:\\Users\\jhmba\\Downloads\\Python\\Games2.csv", "w" , encoding="utf-8") as file:
                    writer = csv.DictWriter(file, game_headers,delimiter="\t")
                    writer.writeheader()
                    writer.writerows(game_list)

                return new_cycle

            new_cycle = intro_games(num_games)
            cycle = new_cycle

        print("Thanks for using the program")

    except ValueError as error:
        print(f"Error [ValueError]: You tried to enter an incorrect value")

excercice_2()



