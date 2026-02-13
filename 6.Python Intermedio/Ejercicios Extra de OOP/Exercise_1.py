#Exercise 1
#Create a class Rectangle with attributes width and height that as a method get_area() that returns the area 
#That has a method get perimeter() that returns de perimeter 
#Validate that none of the values is negative and if it is that returns a exception with a message accordingly 

class Rectangle():

    def __init__(self):
        
        while True:

            try:

                self.width = float(input("Please type the width of the rectangle: "))

                if self.width > 0:
                    break

                else:
                    
                    print(f"The number can not be less than 0  please try again:")

            except ValueError as error:

                print(f"Error [ValueError] The number can not have letters please try again:")

        while True:

            try:

                self.height = float(input("Please type the height of the rectangle: "))

                if self.height > 0:
                    break

                else:
                    
                    print(f"The number can not be less than 0  please try again:")
            except ValueError as error:

                print(f"Error [ValueError] The number can not have letters please try again:")

    

    def get_area(self):

        area = float(self.width) * float(self.height)

        return area

    def get_perimeter(self):

        two_side_width = float(self.width) * 2

        two_side_height = float(self.height) * 2

        perimeter = two_side_width + two_side_height

        return perimeter



rectangle = Rectangle()

area = rectangle.get_area()

perimeter = rectangle.get_perimeter()

print("------------------------------------------------")
print(f"The area of the rectangle is {area}")
print("------------------------------------------------")
print(f"The perimeter of the rectangle is {perimeter}")
print("------------------------------------------------")