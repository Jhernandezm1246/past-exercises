#Exercise 3
#Create a class User that has:
#Attribute date_of_birth
#Has a property of age
#Then create a decorator that for functions that accept a User as parameter and then revise if the user is 18+ and trow an exception if is not 

from datetime import date

class User():

    def __init__(self,date_of_birth):
        self.date_of_birth = date_of_birth

    @property
    def age(self):

        delta = date.today() - self.date_of_birth
        
        return delta.days //365
    


def age_revision(function):

    def wrapper(*args):

        user = args[0]

        if user.age < 18:

            raise Exception("This person is a minor")
        
        return function(*args)
    
    return wrapper




@age_revision
def age_checker(user):
    print("Welcome")




user1 = User(date(1990, 5, 10))


age_checker(user1)

