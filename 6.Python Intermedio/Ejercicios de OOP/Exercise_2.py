#Exercise 2
#Create a class Bus
#One attribute max passengers
#One method to add passengers one by one that accepts an instance person and should only let add passengers if the bus has not reach its limit, if so show an error saying buss is full

import random

def exercise_two():


    #Menu block 
    system_start = str(input("Would you like to start the program (Y/N): ").upper())

    while system_start != "Y" and system_start != "N": 
        print("Please note that at this moment you should only select Y or N ") 
        system_start = str(input("Would you like to start the program (Y/N): ").upper()) 


    def menu():
        print("-------------------------")
        print("Bus Menu")
        print("1.Add a passenger: ")
        print("2.Remove a passenger: ")
        print("3.Show all passengers: ")
        print("-------------------------")

        #Selection block with validation of number
        selection = input("Type the option that you like: ")
        try:
            selection = int(selection)

        except ValueError as error:
            while selection.isdigit() == False:
                print("Please only type numbers no letters or words")
                selection = input("Type the option that you like: ")
                if selection.isdigit():
                    selection = int(selection)
                    print(selection)
                    break
        return selection


    #Block for new entry name, age
    def ask_person():


        while True:
            name = input("Type the name of the passenger: ")
            if any(letter.isdigit() for letter in name):
                print("Only letter are accepted in the name")
                
                    
                
            age = input("Type the age of the passenger: ")
            while age.isdigit() == False:
                print("Please only type numbers no letters or words")
                age = input("Type the age of the passenger: ")
                if age.isdigit():
                    age = int(age)
                    break
            break


        return name, age


    #Class person
    class Person:

        def __init__(self,name,age):
            self.name = name
            self.age = age

    #Bus Class this will have different methods within that will show new passengers getting in the bus or getting out
    class Bus:
        
        def __init__(self):

            self.bus_passengers = []
            self.max_passengers = 3
        

        def add_passenger(self,new_person):

            

            if len(self.bus_passengers) < self.max_passengers:
                self.bus_passengers.append(new_person)
            
            if len(self.bus_passengers) < self.max_passengers:
                total_in_bus = self.max_passengers - len(self.bus_passengers)
                print(f"There are still {total_in_bus} spots available")

            else:
                print("Bus is full")

        def passenger_takeoff(self):

            print("Which passenger you like to takeoff: ")
            while True:
                name = input("Type the name of the passenger: ")
                if any(letter.isdigit() for letter in name):
                    print("Only letter are accepted in the name")
                    
                        
                    
                age = input("Type the age of the passenger: ")
                while age.isdigit() == False:
                    print("Please only type numbers no letters or words")
                    age = input("Type the age of the passenger: ")
                    if age.isdigit():
                        age = int(age)
                        break
                break

            for passenger in self.bus_passengers:
                if passenger.name == name and passenger.age == age:
                    self.bus_passengers.remove(passenger)

        
        def show_passengers(self):


            for passenger in self.bus_passengers:
                print(f"Passenger name: {passenger.name} age: {passenger.age}")


    # logic behind the selection 
    Bus = Bus()

    

    while system_start =="Y":

        selection = menu()

        if selection == 1:

            name, age = ask_person()

            new_person = Person(name, age)

            Bus.add_passenger(new_person)
        
        elif selection == 2:

            Bus.passenger_takeoff()

        elif selection == 3:

            Bus.show_passengers()
            

        system_start = str(input("Would you like to continue (Y/N): ").upper())


exercise_two()