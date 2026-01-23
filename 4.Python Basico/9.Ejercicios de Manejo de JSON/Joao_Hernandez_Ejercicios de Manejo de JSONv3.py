

import json


def excercice_1():
    try:

        def read_json():
           with open(".\\pokemon.json", "r") as file:

                data = json.load(file)
                print(data)


        def new_data():
           with open(".\\pokemon.json", "r") as file:

                data = json.load(file)

           new_cycle = str(input("Would you like to add a new pokemon: (Y/N) "))
           cycle = new_cycle.upper()

           if cycle == "Y":
                pokemon_name = str(input("Enter the pokemon name: "))
                pokemon_type = str(input("Enter the pokemon type: "))
                pokemon_hp = int(input("Enter the pokemon HP: "))
                pokemon_attk = int(input("Enter the pokemon Attack: "))
                pokemon_dffens = int(input("Enter the pokemon Defense: "))
                pokemon_sp_attk = int(input("Enter the pokemon SP.Attack: "))
                pokemon_sp_dffens = int(input("Enter the pokemon SP.Defense: "))
                pokemon_speed = int(input("Enter the pokemon Speed: "))

                data.append({
                    "name": {"english": pokemon_name},
                    "type": [pokemon_type],
                    "base": {
                        "HP": pokemon_hp,
                        "Attack": pokemon_attk,
                        "Defense": pokemon_dffens,
                        "Sp. Attack": pokemon_sp_attk,
                        "Sp. Defense": pokemon_sp_dffens,
                        "Speed": pokemon_speed
                    }
                })

                with open("C:\\Users\\jhmba\\Downloads\\Python\\pokemon.json", "w") as file:
                    json.dump(data, file, indent= 4)

           else:
                print("Thanks for using the program")
            
           print(data)



        def append_to_json():
                


    except ValueError as error:
        print(f"Error [ValueError]: You tried to enter an incorrect value")

    read_json()


excercice_1()