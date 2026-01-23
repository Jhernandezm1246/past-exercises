

import json


def excercice_1():
    try:

        def read_json():
            json_text = """
            [
                {
                    "name": {
                    "english": "Pikachu"
                    },
                    "type": [
                    "Electric"
                    ],
                    "base": {
                    "HP": 35,
                    "Attack": 55,
                    "Defense": 40,
                    "Sp. Attack": 50,
                    "Sp. Defense": 50,
                    "Speed": 90
                    }
                },
                {
                    "name": {
                    "english": "Charmander"
                    },
                    "type": [
                    "Fire"
                    ],
                    "base": {
                    "HP": 39,
                    "Attack": 52,
                    "Defense": 43,
                    "Sp. Attack": 60,
                    "Sp. Defense": 50,
                    "Speed": 65
                    }
                },
                {
                    "name": {
                    "english": "Squirtle"
                    },
                    "type": [
                    "Water"
                    ],
                    "base": {
                    "HP": 44,
                    "Attack": 48,
                    "Defense": 65,
                    "Sp. Attack": 50,
                    "Sp. Defense": 64,
                    "Speed": 43
                    }
                }
            ]
            """

            data = json.loads(json_text)

            print(data)

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

            else:
                print("Thanks for using the program")
            
            print(data)


    except ValueError as error:
        print(f"Error [ValueError]: You tried to enter an incorrect value")

    read_json()


excercice_1()