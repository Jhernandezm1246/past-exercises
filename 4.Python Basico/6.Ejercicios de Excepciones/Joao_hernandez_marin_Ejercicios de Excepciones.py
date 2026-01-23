def excercice_1():
    global num
    global cycle
    try:

        new_cycle = str(input("Would you like to perform an operation Y/N: "))
        cycle = new_cycle.upper()
        print("Matematic calculator next your will see the options that the calculator will offer your")
        num = int(input("Select the first number for the operations: "))

        while cycle == "Y":
            
            print("1: Sum")
            print("2: Deduct")
            print("3: Multiply")
            print("4: Divide")
            print("5: Clean")


            selection = int(input("Type a number from 1 to 5 based on the options shown before: "))


            def calculator(selection):
                global num
                global cycle
                try:
                    
                    if selection == 1:
                        new_num = int(input("Type the number you like to sum: "))
                        sumatory = num + new_num
                        num = sumatory
                        print(f"The result of the sum of both numbers is {sumatory}")
                        cycle = str(input("Would you like to continue Y/N: "))

                    elif selection == 2:
                        new_num = int(input("Type the number you like to deduct: "))
                        deduct = num - new_num
                        num = deduct
                        print(f"The result of the deduction of numbers is {deduct}")
                        cycle = str(input("Would you like to continue Y/N: "))

                    elif selection == 3:
                        new_num = int(input("Type the number you like to multiply: "))
                        multiply = num * new_num
                        num = multiply
                        print(f"The result of the multiplication of both numbers is {multiply}")
                        cycle = str(input("Would you like to continue Y/N: "))

                    elif selection == 4:
                        try:
                            new_num = int(input("Type the number you like to division: "))
                            division = num / new_num
                            num = division
                            print(f"The result of the division of both numbers is {division}")
                            cycle = str(input("Would you like to continue Y/N: "))

                        except ZeroDivisionError as error:
                            print(f"Error [ZeroDivisionError]: You try dividing {num} by 0. Details:{error}")
                    elif selection == 5:
                        num = 0
                        cycle = str(input("Would you like to continue Y/N: "))

                except TypeError as error:
                    print(f"Error [TyperError]: You tried to enter a string and should only add numbers from 1 to 5")

            calculator(selection)

    except TypeError as error:
                print(f"Error [TyperError]: You tried to enter a string and should only add numbers from 1 to 5")




excercice_1() 