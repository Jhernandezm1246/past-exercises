#Exercise 1 
#Create a decorator that prints 2 parameters and returns the function that is being decorated 




def decorator(function):

    def wrapper(*args,**kwargs):
        print("Executing", function.__name__)
        return function(*args,**kwargs)
    
    return wrapper

@decorator
def sum_two_numbers(a,b):
    return a + b 

print(sum_two_numbers(10,50))