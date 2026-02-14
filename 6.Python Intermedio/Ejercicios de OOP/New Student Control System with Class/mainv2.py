
from menuv2 import menu_system
from actionsv2 import Class_Room, Student, new_student_info
from datav2 import students_data_export, student_data_import

def main():

    print("----------------------------------------------")
    print("Welcome to the Student Control System program")
    print("----------------------------------------------")

    student_records = []
    

    class_room = Class_Room()

    system_start = str(input("Would you like to start the program (Y/N): ").upper()) 

    while system_start != "Y" and system_start != "N": 
        print("Please note that at this moment you should only select Y or N ") 
        system_start = str(input("Would you like to start the program (Y/N): ").upper()) 
        


    
    while system_start == "Y":
        menu_number_selected = menu_system()

        if menu_number_selected == 2:
            class_room.all_student_information(menu_number_selected)

        elif menu_number_selected == 1:
            
            new_student_info(menu_number_selected,class_room)
        
        elif menu_number_selected == 3:
            class_room.top_three_students_average_scores(menu_number_selected)

        elif menu_number_selected == 4:
            class_room.all_students_average_scores(menu_number_selected)


        elif menu_number_selected == 5:
            students_data_export(menu_number_selected,class_room)
            
        elif menu_number_selected == 6:
            student_data_import(menu_number_selected,class_room)
        
        elif menu_number_selected == 7:
            class_room.delete_student(menu_number_selected)

        elif menu_number_selected == 8:
            class_room.all_students_average_scores_lower_than_sixty(menu_number_selected)

    system_start = str(input("Would you like to continue (Y/N): ").upper())

main()