# funtions go here

# checks input is a number that is more then zero
from turtle import width


def num_check (question):



    valid = False
    while not valid:

        error = "Please enter a number that is more then zero"

        try:

            response = float(input(question))

            if response > 0:
                return response
            
            else:
                print(error)
                print()
        
        except ValueError:
            print(error)



# Main Routine goes here
width = num_check("Width: ")
height = num_check("Height: ")
print()
print("Width", width)
print("Height", height)
print()