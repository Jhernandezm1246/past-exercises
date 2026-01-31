import csv


def students_data_export(menu_selection,students_group_list):


    if menu_selection == 5:

        

        print(students_group_list)
        flat_list = []
        for item in students_group_list:
            if isinstance(item, dict):
                flat_list.append(item)
            elif isinstance(item, list):
                for subitem in item:
                    if isinstance(subitem, dict):
                        flat_list.append(subitem)
        print(flat_list)

        
        with open("Student_records.csv","w",encoding='utf-8') as file:

            info_for_file = csv.DictWriter(file, fieldnames=["name","section","spanish","english","history","science"])

            info_for_file.writeheader()
            
            info_for_file.writerows(flat_list)



def student_data_import(menu_selection):

    if menu_selection == 6:

        try:

            with open("Student_records.csv","r",encoding='utf-8') as file:

                reader = csv.DictReader(file)

                imported_group_of_students = list(reader)

                print(imported_group_of_students)

                return imported_group_of_students
            
        except FileNotFoundError as error:
            print(f"Error [FileNotFoundError] The file was not found")
            return []
        
    return[]

            
            
