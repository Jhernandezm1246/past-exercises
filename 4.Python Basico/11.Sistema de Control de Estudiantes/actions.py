def new_student_info(selection):

    new_group_of_students = []


    if selection == 1:

        


        number_of_new_students = input("Type the number of new students information you like to add: ")


        if number_of_new_students.isdigit() == False:
            while number_of_new_students.isdigit() == False:
                print("Please only type numbers no letters or words")
                number_of_new_students = input("Type the number of new students information you like to add: ")
                if number_of_new_students.isdigit():
                    break
        
        number_of_new_students = int(number_of_new_students)

        counter = 0 

        while counter < number_of_new_students:

            while True:

                student_name = input("Type the student name: ")

                if any(letter.isdigit() for letter in student_name):
                    print("The name should only include characters no numbers")
                    continue

                else:
                    break


            student_section = str(input("Type the student section: "))

            #Spanish


            while True:
                student_spanish_score = input("Type the student spanish score: ")

                try:
                    student_spanish_score = float(student_spanish_score)

                except ValueError as error:
                    print(f"Error [ValueError] Input should only be numbers")
                    print("Please try again")
                    continue

                if student_spanish_score < 0 or student_spanish_score > 100:
                    print(f"Error [ValueError] The Score can not be higher than 100 or lower than 0")
                    print("Please try again")
                    continue
                    

                if student_spanish_score >= 0 and student_spanish_score <= 100 :
                    break



            #English

            while True:
                student_english_score = input("Type the student spanish score: ")

                try:
                    student_english_score = float(student_english_score)

                except ValueError as error:
                    print(f"Error [ValueError] Input should only be numbers")
                    print("Please try again")
                    continue
                
                if student_english_score < 0 or student_english_score > 100:
                    print(f"Error [ValueError] The Score can not be higher than 100 or lower than 0")
                    print("Please try again")
                    continue
                    

                if student_english_score >= 0 and student_english_score <= 100 :
                    break
            #History


            while True:
                student_history_score = input("Type the student spanish score: ")

                try:
                    student_history_score = float(student_history_score)

                except ValueError as error:
                    print(f"Error [ValueError] Input should only be numbers")
                    print("Please try again")
                    continue
                
                if student_history_score < 0 or student_history_score > 100:
                    print(f"Error [ValueError] The Score can not be higher than 100 or lower than 0")
                    print("Please try again")
                    continue
                    

                if student_history_score >= 0 and student_history_score <= 100 :
                    break

            #Science

            while True:
                student_science_score = input("Type the student spanish score: ")

                try:
                    student_science_score = float(student_science_score)

                except ValueError as error:
                    print(f"Error [ValueError] Input should only be numbers")
                    print("Please try again")
                    continue
                
                if student_science_score < 0 or student_science_score > 100:
                    print(f"Error [ValueError] The Score can not be higher than 100 or lower than 0")
                    print("Please try again")
                    continue
                    

                if student_science_score >= 0 and student_science_score <= 100 :
                    break

            new_student = {"name" : student_name,
                            "section" : student_section,
                            "spanish" : float(student_spanish_score),
                            "english" : float(student_english_score),
                            "history" : float(student_history_score),
                            "science" : float(student_science_score)}
            
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

        

        total_score_science = 0
        total_counter_science = 0
        total_score_spanish = 0
        total_counter_spanish = 0
        total_score_english = 0
        total_counter_english = 0
        total_score_history = 0
        total_counter_history = 0

    
        for student in students_records:

            science = float(student["science"])
            spanish = float(student["spanish"])
            english = float(student["english"])
            history = float(student["history"])
            

            if science :
                total_score_science += science
                total_counter_science += 1

            if spanish :
                total_score_spanish += spanish
                total_counter_spanish += 1

            if english :
                total_score_english += english
                total_counter_english += 1

            if history :
                total_score_history += history
                total_counter_history += 1


        final_score_all_students = total_score_science + total_score_spanish + total_score_english + total_score_history
        final_count_all_students = total_counter_science + total_counter_spanish + total_counter_english + total_counter_history

        average_scores = final_score_all_students / final_count_all_students

        
        print(f"Sum of all Student scores {final_score_all_students}")
        print(f"Sum of all Student amount of scores {final_count_all_students}")
        print(f"Total students average_score {average_scores}")


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

            if science < 60 or spanish < 60 or english < 60 or history < 60:
                print(f"{student}")

