
from menu import menu_system
from actions import new_student_info, all_students_information, all_students_average_scores, top_three_students_average_scores, delete_student, all_students_average_scores_lower_than_sixty
from data import students_data_export, student_data_import

def main():

    print("----------------------------------------------")
    print("Welcome to the Student Control System program")
    print("----------------------------------------------")

    student_records = []
    


    system_start = str(input("Would you like to start the program (Y/N): ").upper()) 

    while system_start != "Y" and system_start != "N": 
        print("Please note that at this moment you should only select Y or N ") 
        system_start = str(input("Would you like to start the program (Y/N): ").upper()) 
        

    
    while system_start == "Y":
        menu_number_selected = menu_system()

        if menu_number_selected == 2:
            all_students_information(menu_number_selected, student_records)
        elif menu_number_selected == 5:
            students_data_export(menu_number_selected, student_records)
        elif menu_number_selected == 6:
            imported_student_record = student_data_import(menu_number_selected)
            if imported_student_record is not None:
                student_records.extend(imported_student_record)
        elif menu_number_selected == 1:
            new_record = new_student_info(menu_number_selected)
            student_records.extend(new_record)
        elif menu_number_selected == 4:
            all_students_average_scores(menu_number_selected, student_records)
        elif menu_number_selected == 3:
            top_three_students_average_scores(menu_number_selected, student_records)
        elif menu_number_selected == 7:
            student_records = delete_student(menu_number_selected, student_records)
        elif menu_number_selected == 8:
            all_students_average_scores_lower_than_sixty(menu_number_selected, student_records)

    system_start = str(input("Would you like to continue (Y/N): ").upper())

main()