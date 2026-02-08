import csv

from actionsv2 import Class_Room, Student


def students_data_export(menu_selection,class_room):


    if menu_selection == 5:

        

        
        flat_list = []
        for student in class_room.new_group_of_students:
            flat_list.append({"name":student.name, 
                                "section":student.section, 
                                "science_score":student.science_score, 
                                "spanish_score":student.spanish_score, 
                                "english_score":student.english_score, 
                                "history_score":student.history_score})

        print(flat_list)

        
        with open("Student_records.csv","w",encoding='utf-8',newline='') as file:

            info_for_file = csv.DictWriter(file, fieldnames=["name", "section", "science_score", "spanish_score", "english_score", "history_score"])

            info_for_file.writeheader()
            
            info_for_file.writerows(flat_list)



def student_data_import(menu_selection,class_room):

    if menu_selection == 6:

        try:

            with open("Student_records.csv","r",encoding='utf-8') as file:

                reader = csv.DictReader(file)

                imported_group_of_students = list(reader)

                print(imported_group_of_students)
                
                if imported_group_of_students is not None:
                    for student in imported_group_of_students:
                        student_name = student["name"]
                        student_section = student["section"]
                        student_science_score = float(student["science_score"])
                        student_spanish_score = float(student["spanish_score"])
                        student_english_score = float(student["english_score"])
                        student_history_score = float(student["history_score"])

                        new_student_object_for_class = Student(student_name, student_section, student_science_score, student_spanish_score, student_english_score, student_history_score)

                        class_room.add_student(new_student_object_for_class)


            
        except FileNotFoundError as error:
            print(f"Error [FileNotFoundError] The file was not found")
            return []
        
    return[]

            
            
