#Exercise 2
#Create a decorator that is in charge of the revision of all the parameters on a function and give back an exception if they are not numbers


def decorator(function):

    def wrapper(*args,**kwargs):

        for digit in args:
            try:

                digit = float(digit)

            except ValueError as error:
                print(f"Error [ValueError] Please note that you should only use numbers")

        for digit in args:
            try:

                digit = float(digit)

            except ValueError as error:
                print(f"Error [ValueError] Please note that you should only use numbers")

        return function(*args,**kwargs)
    
    return wrapper


@decorator
def sum_two_numbers(a,b):
    return a + b 

print(sum_two_numbers(60,50))