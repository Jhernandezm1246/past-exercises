def new_student_info(selection):

    new_group_of_students = []

    

    if selection == 1:

        counter = 0 


        try:
            number_of_new_students = int(input("Type the number of new students information you like to add: "))

        except ValueError as error:
            print(f"Error [ValueError] Please note at this point only numbers are accepted")


        while counter < number_of_new_students:

            student_name = str(input("Type the student name: "))
            student_section = str(input("Type the student section: "))
            student_spanish_score = float(input("Type the student spanish score: "))
            while student_spanish_score < 0 or student_spanish_score > 100:
                print("The Score can not be higher than 100 or lower than 0")
                print("Please try again")
                student_spanish_score = float(input("Type the student spanish score: "))
            student_english_score = float(input("Type the student english score: "))
            while student_english_score < 0 or student_english_score > 100:
                print("The Score can not be higher than 100 or lower than 0")
                print("Please try again")
                student_english_score = float(input("Type the student spanish score: "))
            student_history_score = float(input("Type the student history score: "))
            while student_history_score < 0 or student_history_score > 100:
                print("The Score can not be higher than 100 or lower than 0")
                print("Please try again")
                student_history_score = float(input("Type the student spanish score: "))
            student_science_score = float(input("Type the student science score: "))
            while student_science_score < 0 or student_science_score > 100:
                print("The Score can not be higher than 100 or lower than 0")
                print("Please try again")
                student_science_score = float(input("Type the student spanish score: "))

            new_student = {"name" : student_name,
                            "section" : student_section,
                            "spanish" : student_spanish_score,
                            "english" : student_english_score,
                            "history" : student_history_score,
                            "science" : student_science_score}
            
            new_group_of_students.append(new_student)
            
            counter += 1

            print(new_group_of_students)

            return new_group_of_students
        




def all_students_information(selection,students_records):

    if selection == 2:

        for student in students_records:
            print(f"Name : {student["name"]}, section : {student["section"]}")


                
def top_three_students_average_scores(selection,students_records):

    if selection == 3:

        top_average_scores = []

        for student in students_records:

            science = float(student["science"])
            spanish = float(student["spanish"])
            english = float(student["english"])
            history = float(student["history"])
            total_scores = science + spanish + english + history 

            average_scores = total_scores / 4

            student_avg_score = {"name":student["name"],"avg" : average_scores}
            
            top_average_scores.append(student_avg_score)

                
        initial_num = 0

        for score in top_average_scores:
            for avg in score:
                if score["avg"] > initial_num:
                    max_value_one = score["avg"]

        new_order = sorted(top_average_scores, key=lambda score: score["avg"], reverse = True)

        counter = 0

        print("The top 3 average scores are: ")
        for student in new_order[:3]:
            print(student)

        

def all_students_average_scores(selection,students_records):

    if selection == 4:

    
        for student in students_records:

            science = float(student["science"])
            spanish = float(student["spanish"])
            english = float(student["english"])
            history = float(student["history"])
            total_scores = science + spanish + english + history 

            average_scores = total_scores / 4

            print(f"Name : {student["name"]}, section : {student["section"]}, average_score {average_scores}")


def delete_student(selection,students_records):


    if selection == 7:

        new_group_of_students = []


        new_group_of_students.extend(students_records)
        print("Type the name and Section of the student you like to remove: ")
        student_name = str(input("Type the student name: ").upper())
        student_section = str(input("Type the student_section: ").upper())

        

        for student in new_group_of_students:
            validation_name = str(student["name"].upper())
            validation_section = str(student["section"].upper())

            if student_name == validation_name and student_section == validation_section:
                print(f"{student["name"]},{student["section"]}")
                delete_validation = str(input("Would you like to delete this user (Y/N): ").upper())

                if delete_validation == "Y":
                    new_group_of_students.remove(student)
                    print("Student deleted as requested")

        return new_group_of_students


def all_students_average_scores_lower_than_sixty(selection,students_records):

    if selection == 8:

    
        for student in students_records:

            science = float(student["science"])
            spanish = float(student["spanish"])
            english = float(student["english"])
            history = float(student["history"])
            total_scores = science + spanish + english + history 

            average_scores = total_scores / 4
            if average_scores < 60:
                print(f"Name : {student["name"]}, section : {student["section"]}, average_score {average_scores}")

