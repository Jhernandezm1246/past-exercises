#Exercise 2
#Create an abstract class User with the following abstract methods 
#get role()
#has permission(permission)
#Then create a inherit class AdminUser RegularUser
#each of those need to implement their methods 
#For example AdminUser  has permission and regular user has read only


from abc import ABC, abstractmethod

class User(ABC):

    @abstractmethod
    def get_role(self):
        pass
    
    @abstractmethod
    def has_permission(self):
        pass


class AdminUser(User):

    def get_role(self):
        return print("Admin")

    def has_permission(self,permission):
        
        if permission == "Delete":
            return print("True")

        elif permission == "Create":
            return print("True")

        elif permission == "Update":
            return print("True")
        
        elif permission == "Read":
            return print("True")

class RegularUser(User):

    def get_role(self):
        return print("Regular User")

    def has_permission(self,permission):
        
        if permission == "Delete":
            return print("False")

        elif permission == "Create":
            return print("False")

        elif permission == "Update":
            return print("False")
        
        elif permission == "Read":
            return print("True")

user_one = AdminUser()

user_two = RegularUser()



user_one.has_permission("Delete")
user_two.has_permission("Delete")