def menu_system():



    print("----------------------------------------------")
    print("Welcome to the Student Control System Menu")
    print("----------------------------------------------")
    print("Please select an option: ")
    print("----------------------------------------------")
    print("1. Add Student information")
    print("2. Show all students information")
    print("3. Show top 3 best average scores ")
    print("4. Show average scores of all students")
    print("5. Export all current student information to a .csv file")
    print("6. Import data from previously exported file")
    print("7. Delete a student")
    print("8. Students with scores lower than 60")
    print("----------------------------------------------")

    try:
        menu_selection = int(input("Type the option that you like: "))
        if menu_selection == 1 or menu_selection == 2 or menu_selection == 3 or menu_selection == 4 or menu_selection == 5 or menu_selection == 6 or menu_selection == 7 or menu_selection == 8:
            return menu_selection
        
        else:
            print("Please note that you should only type the numbers on the list")
    except ValueError as error:
        print(f"Error [ValueError] Please note that you should only type the numbers on the list")

    
    
