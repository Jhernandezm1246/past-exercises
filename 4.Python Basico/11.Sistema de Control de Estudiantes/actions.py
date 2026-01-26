def new_student_info(selection):

    new_group_of_students = []

    if selection == 1 or selection == 2 or selection == 3 or selection == 4 or selection == 5 or selection == 6:

        if selection == 1:

            counter = 0 

            number_of_new_students = int(input("Type the number of new students information you like to add: "))

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
                

    elif selection.isdigit() != True:
        print("Please note that you should not add text only the numbers on the list")
        

    else:
        print("Incorrect Selection please make sure you are using one of the options above")



def all_students_information(selection,students_records):

    if selection == 2:

    
        for student in students_records:
            if student != None:
                """print(f"{student}\n")"""
                for record in student:
                    print(f"Name : {record["name"]}, section : {record["section"]}")

                
def top_three_students_average_scores(selection,students_records):

    if selection == 3:

        top_average_scores = []

        for student in students_records:
            if student != None:
                for record in student:
                    science = int(record["science"])
                    spanish = int(record["spanish"])
                    english = int(record["english"])
                    history = int(record["history"])
                    total_scores = science + spanish + english + history 

                    average_scores = total_scores / 4

                    student_avg_score = {"name":record["name"],"avg" : average_scores}
                    
                    top_average_scores.append(student_avg_score)

                
                initial_num = 0
                student_top_three_scores = []
                counter = 0
                    

                while counter < 3:
                    for score in top_average_scores:
                        for avg in score:
                            if score["avg"] > initial_num:
                                max_value_one = score["avg"]
                    for score in top_average_scores:
                        for avg in score:       
                            if score["avg"] > initial_num and score["avg"] < max_value_one:
                                max_value_two = score["avg"]
                    for score in top_average_scores:
                        for avg in score:        
                            if score["avg"] > initial_num and score["avg"] < max_value_one and score["avg"] < max_value_two:
                                max_value_three = score["avg"]
                    counter += 1
                                
                    print(f"Name : {score["name"]}, avg {max_value_one}")
                    print(f"Name : {score["name"]}, avg {max_value_two}")
                    print(f"Name : {score["name"]}, avg {max_value_three}")
                    



                
                    """if score not in student_top_three_scores:
                        student_top_three_scores.append(score)
                elif score["avg"] > student_top_three_scores[0] and score["avg"] < max_value_one:
                    max_value_two = score["avg"]
                    student_top_three_scores.append(score)
                    if score not in student_top_three_scores:
                        student_top_three_scores.append(score)
                elif score["avg"] > student_top_three_scores[1] and score["avg"] < max_value_one and score["avg"] < max_value_two:
                    max_value_three = score["avg"]
                    student_top_three_scores.append(score)
                    if score not in student_top_three_scores:
                        student_top_three_scores.append(score)
                            

                for score_top_three in student_top_three_scores:
                    print(f"Name : {score_top_three["name"]}, avg {score_top_three["avg"]}")
                    
                print(f"Name : {record["name"]}, avg {max_value_one}")
                print(f"Name : {record["name"]}, avg {max_value_two}")
                print(f"Name : {record["name"]}, avg {max_value_three}")"""
                                    


def all_students_average_scores(selection,students_records):

    if selection == 4:

    
        for student in students_records:
            if student != None:
                for record in student:
                    science = int(record["science"])
                    spanish = int(record["spanish"])
                    english = int(record["english"])
                    history = int(record["history"])
                    total_scores = science + spanish + english + history 

                    average_scores = total_scores / 4

                    print(f"Name : {record["name"]}, section : {record["section"]}, average_score {average_scores}")
