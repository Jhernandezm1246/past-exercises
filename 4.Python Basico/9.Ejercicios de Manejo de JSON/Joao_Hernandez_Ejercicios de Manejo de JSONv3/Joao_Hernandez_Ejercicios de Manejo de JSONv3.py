

import json


def excercice_1():


    def read_json():
        try:
            with open("pokemon.json", "r") as file:

                data = json.load(file)
                print(data)

        except FileNotFoundError as error:
            print(f"Error [FileNotFoundError]: The file listed in the path was not found")


    read_json()


    try:
        new_cycle = str(input("Would you like to add a new pokemon: (Y/N) "))
        cycle = new_cycle.upper()


    except TypeError as error:
            print(f"Error [TypeError] You selected the incorrect option remember at this point only (Y/N) ")



    def new_data(cycle):
        
        if cycle == "Y":
            pokemon_name = str(input("Enter the pokemon name: "))
            pokemon_type = str(input("Enter the pokemon type: "))
            pokemon_hp = int(input("Enter the pokemon HP: "))
            pokemon_attk = int(input("Enter the pokemon Attack: "))
            pokemon_dffens = int(input("Enter the pokemon Defense: "))
            pokemon_sp_attk = int(input("Enter the pokemon SP.Attack: "))
            pokemon_sp_dffens = int(input("Enter the pokemon SP.Defense: "))
            pokemon_speed = int(input("Enter the pokemon Speed: "))

            return pokemon_name,pokemon_type,pokemon_hp,pokemon_attk,pokemon_dffens,pokemon_sp_attk,pokemon_sp_dffens,pokemon_speed
            

        else:
            print("Thanks for using the program")

        


    def append_to_jason(pokemon_name,pokemon_type,pokemon_hp,pokemon_attk,pokemon_dffens,pokemon_sp_attk,pokemon_sp_dffens,pokemon_speed):
        with open("pokemon.json", "r") as file:

            data = json.load(file)

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

            with open("pokemon.json", "w") as file:
                json.dump(data, file, indent= 4)

        
        print(data)

    
    pokemon_data = new_data(cycle)
    
    append_to_jason(*pokemon_data)

excercice_1()