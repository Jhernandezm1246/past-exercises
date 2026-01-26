
from menu import menu_system
from actions import new_student_info, all_students_information, all_students_average_scores, top_three_students_average_scores
from data import students_data_export, student_data_import

def main():

    print("----------------------------------------------")
    print("Welcome to the Student Control System program")
    print("----------------------------------------------")

    student_records = []
    
    system_start = str(input("Would you like to start the program (Y/N): ").upper())


    if system_start == "Y" or system_start == "N":

        while system_start == "Y":

            menu_number_selected = menu_system()
            
            all_students_information(menu_number_selected,student_records)

            students_data_export(menu_number_selected,student_records)

            imported_student_record = student_records.append(student_data_import(menu_number_selected))

            student_records.append(imported_student_record)

            new_record = new_student_info(menu_number_selected)

            student_records.append(new_record)

            all_students_average_scores(menu_number_selected,student_records)

            top_three_students_average_scores(menu_number_selected,student_records)

    else:
        print("Incorrect Value please make sure only to select Y or N")
        system_start = str(input("Would you like to start the program (Y/N): ").upper())

        while system_start == "Y":

            menu_number_selected = menu_system()
            
            all_students_information(menu_number_selected,student_records)

            students_data_export(menu_number_selected,student_records)

            imported_student_record = student_records.append(student_data_import(menu_number_selected))

            student_records.append(imported_student_record)

            new_record = new_student_info(menu_number_selected)

            student_records.append(new_record)

            all_students_average_scores(menu_number_selected,student_records)

            top_three_students_average_scores(menu_number_selected,student_records)
main()