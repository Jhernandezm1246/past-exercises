#Exercise 1
#Create a class Employee with the following requisites 
#Private Attributes _name, _salary
#Use @property and @<attribute>.setter to
#Show name and salary
#Validate that salary is never a negative number 
#Create a method promote that increase the salary in a defined percentage 

class Employee():

    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name_value):
        if any(char.isdigit() for char in name_value):
            raise ValueError("Name can not have numbers")
        self._name = name_value

    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self,salary_value):

        if salary_value < 0:
            raise ValueError("Salary can not be lower than 0")
        self._salary = salary_value

    def promote(self,increase):

        salary_increase_percentage = increase / 100

        salary_increase = self._salary * salary_increase_percentage


        self._salary = self._salary + salary_increase

        return self._salary
    

new_employee = Employee()

new_employee.name = "Jhon Marston"
new_employee.salary = 500000

new_employee.promote(10)

        
print(new_employee.salary)