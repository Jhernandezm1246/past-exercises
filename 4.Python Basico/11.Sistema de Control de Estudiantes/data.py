import csv


def students_data_export(menu_selection,students_group_list):


    if menu_selection == 5:


        with open("Student_records.csv","a",encoding='utf-8') as file:

            if file == FileNotFoundError:

                file.write(students_group_list)

            else:
                print("This file already exist")



def student_data_import(menu_selection):

    if menu_selection == 6:

        imported_group_of_students = []

        try:

            with open("Student_records.csv","r",encoding='utf-8') as file:

                reader = csv.DictReader(file)

                for student in reader:
                    imported_group_of_students.append(student)
                    
                
                return imported_group_of_students
        except FileNotFoundError as error:
            print(f"Error [FileNotFoundError] The file was not found")
            
