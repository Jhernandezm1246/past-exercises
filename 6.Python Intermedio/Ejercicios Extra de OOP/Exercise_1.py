#Exercise 1
#Create a class Rectangle with attributes width and height that as a method get_area() that returns the area 
#That has a method get perimeter() that returns de perimeter 
#Validate that none of the values is negative and if it is that returns a exception with a message accordingly 

class Rectangle():

    def __init__(self,width,height):
        self.width = width

        self.height = height

        if self.width.isdigit() == False:
            while self.width.isdigit() == False:
                print("The number can not be less than 0 or have letters please try again:")
                self.width = input("Please type the width of the rectangle: ")
                if self.width.isdigit() == True and float(self.width) >= 0:
                    break


        if self.height.isdigit() == False:
            while self.height.isdigit() == False:
                print("The number can not be less than 0 or have letters please try again:")
                self.height = input("Please type the height of the rectangle: ")
                if self.height.isdigit() == True and float(self.height) >= 0:
                    break

    

    def get_area(self):

        area = float(self.width) * float(self.height)

        return area

    def get_perimeter(self):

        two_side_width = float(self.width) * 2

        two_side_height = float(self.height) * 2

        perimeter = two_side_width + two_side_height

        return perimeter


width = input("Please type the width of the rectangle: ")

height = input("Please type the hight of the rectangle: ")





rectangle = Rectangle(width,height)

area = rectangle.get_area()

perimeter = rectangle.get_perimeter()

print("------------------------------------------------")
print(f"The area of the rectangle is {area}")
print("------------------------------------------------")
print(f"The perimeter of the rectangle is {perimeter}")
print("------------------------------------------------")