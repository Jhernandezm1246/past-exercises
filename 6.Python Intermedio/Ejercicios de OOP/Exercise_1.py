#Exercise 1
#Create a class Circle
#One attribute radius 
#One method to get area and returns its area 

import math

def exercise_one():

    class Circle:

        radios = 0


        def get_area(self,radius):

            pi = float(math.pi)



            radius = float(radius) * float(radius)

            area = pi * radius

            return print(f"The area of the circle is: {area}")




    while True:
        radius = input("Please type the radius for your circle calculation: ")

        if any(char.isdigit() for char in radius):

            

            break

        else:
            print(f"Error [ValueError] Please type only numbers")
            continue

        

    circle_calculation = Circle()

    circle_calculation.get_area(radius)

exercise_one()


