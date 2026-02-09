#Exercise 1
#Create a class Rectangle with attributes width and height that as a method get_area() that returns the area 
#That has a method get perimeter() that returns de perimeter 
#Validate that none of the values is negative and if it is that returns a exception with a message accordingly 

class Rectangle():

    def __init__(self):
        self.width = 0

        self.height = 0

    

    def get_area(self,width,height):

        area = float(width) * float(height)

        return area

    def get_perimeter(self,width,height):

        two_side_width = float(width) * 2

        two_side_height = float(height) * 2

        perimeter = two_side_width + two_side_height

        return perimeter


width = input("Please type the width of the rectangle: ")

height = input("Please type the hight of the rectangle: ")


if width.isdigit() == False:
    while width.isdigit() == False:
        print("The number can not be less than 0 or have letters please try again:")
        width = input("Please type the width of the rectangle: ")
        if width.isdigit() == True and float(width) >= 0:
            break


if height.isdigit() == False:
    while height.isdigit() == False:
        print("The number can not be less than 0 or have letters please try again:")
        height = input("Please type the height of the rectangle: ")
        if height.isdigit() == True and float(height) >= 0:
            break


rectangle = Rectangle()

area = rectangle.get_area(width,height)

perimeter = rectangle.get_perimeter(width,height)

print("------------------------------------------------")
print(f"The area of the rectangle is {area}")
print("------------------------------------------------")
print(f"The perimeter of the rectangle is {perimeter}")
print("------------------------------------------------")