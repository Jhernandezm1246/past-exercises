#Exercise 2
#Create an abstract from shape that has 
#Abstract methods for calculate perimeter and calculate area 
#Create the following class that inherit circle square and rectangle 
#Each one of those require specific attributes to be able to calculate their area and their perimeter 


from abc import ABC, abstractmethod
import math

def number_validator():

    while True:

        number = input("Please type the number: ")

        try:
            number = float(number)

            if number < 0:
                print("Please note that the number can not be a negative number")

            else:
                return number

        except ValueError as error:
            print(f"Error [ValueError] Please note that the number can only be numbers")
            print("Please try again")

    

class Shape(ABC):

    @abstractmethod
    def calculate_perimeter():
        pass

    @abstractmethod
    def calculate_area():
        pass


class Circle(Shape):

    def calculate_perimeter(self):

        print("Please type the diameter")
        self.diameter = number_validator()

        perimeter = math.pi * self.diameter

        return perimeter
    
    def calculate_area(self):

        print("Please type the radio")
        self.radio = number_validator()

        area = math.pi * self.radio**2

        return area
        
    

class Square(Shape):
        
    
    def calculate_perimeter(self):

        print("Please type the side")
        self.side = number_validator()

        perimeter = self.side * 4 

        return perimeter
    
    def calculate_area(self):

        print("Please type the side")
        self.side = number_validator()

        area = self.side ** 2 

        return area

class Rectangle(Shape):

    
    def calculate_perimeter(self):

        print("Please type the length")
        self.rectangle_length = number_validator()

        print("Please type the width")
        self.rectangle_width = number_validator()

        perimeter = self.rectangle_length * 2 +  self.rectangle_width * 2

        return perimeter
    
    def calculate_area(self):

        print("Please type the length")
        self.rectangle_length = number_validator()

        print("Please type the width")
        self.rectangle_width = number_validator()

        area = self.rectangle_width * self.rectangle_length  

        return area




system_start = input("Would you like to start the system (Y/N): ").upper()

while system_start != "Y" and system_start != "N":
    print("Please note that at this point the only available options are Y and N")
    print("Try again")
    system_start = input("Would you like to start the system (Y/N)").upper()


def sub_menu():

    print("Menu")
    print("-------------------------")
    print("1.Calculate Perimeter")
    print("2.Calculate Area")


    print("-------------------------")

    sub_menu_list = [1,2]

    return sub_menu_list

def main_menu():
    print("-------------------------")
    print("Menu")
    print("-------------------------")
    print("1.Circle_Calculations")
    print("2.Square_Calculations")
    print("3.Rectangle_Calculations")
    print("-------------------------")

    main_menu_list = [1,2,3]

    return main_menu_list



def menu_selection(menu_list):

    while True:

        menu_number = input("Please select one of the options above: ")

        try:
            menu_number = int(menu_number)

            if menu_number not in menu_list:
                print("Invalid Option")

            else:
                return menu_number

        except ValueError as error:
            print(f"Error [ValueError] Please note that only numbers are accepted:")
            print("Please try again")



while system_start == "Y":

    main_menu_list = main_menu()

    option_selected = menu_selection(main_menu_list)
    
    if option_selected == 1:


        circle_calculations = Circle()

        sub_menu_list = sub_menu()

        sub_section_selection  = menu_selection(sub_menu_list)

        if sub_section_selection == 1:
            perimeter = circle_calculations.calculate_perimeter()
            print(f"The perimeter of the circle is {perimeter}")


        elif sub_section_selection == 2:

            area = circle_calculations.calculate_area()
            print(f"The area of the circle is {area}")

    elif option_selected == 2:

        square_calculations = Square()
    
        sub_menu_list = sub_menu()
        
        sub_section_selection  = menu_selection(sub_menu_list)

        if sub_section_selection == 1:
            perimeter = square_calculations.calculate_perimeter()
            print(f"The perimeter of the square is {perimeter}")


        elif sub_section_selection == 2:

            area = square_calculations.calculate_area()
            print(f"The area of the square is {area}")


    elif option_selected == 3:


        rectangle_calculations = Rectangle()

        sub_menu_list = sub_menu()
        
        sub_section_selection  = menu_selection(sub_menu_list)

        if sub_section_selection == 1:
            perimeter = rectangle_calculations.calculate_perimeter()
            print(f"The perimeter of the rectangle is {perimeter}")


        elif sub_section_selection == 2:

            area = rectangle_calculations.calculate_area()
            print(f"The area of the rectangle is {area}")




    system_start = input("Would you like to continue (Y/N)").upper()
