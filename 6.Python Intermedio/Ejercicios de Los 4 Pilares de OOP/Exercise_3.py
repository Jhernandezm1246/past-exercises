#Exercise 3
#Investigate the multiple inheritance for python and create an example 

#This is what I came from after checking about this topic 

class A():
    def hello(self):
        print("A")


class B(A):
    def hello(self):
        print("B")

class C(A):
    def hello(self):
        print("C")



class D(B,C):
    pass



#While investigating about this there was a terminology that came across MRO 
#Method Resolution order 

print(D.mro())

#Being this said the multiple heritage works in order to add different classes to a new class being able to provide different methods 
#There are things to have into consideration as the MRO since python will first do a left to right search and in scenarios like the one above will print the first one with the method found
