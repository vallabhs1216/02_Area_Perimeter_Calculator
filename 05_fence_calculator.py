# functions go here

# checks input is a number more than zero
from turtle import width


def num_check(question):
    valid = False
    while not valid:
        
        error = "Please enter a number that is more than zero"
        
        try:
        
            # ask user to enter a number
            response = float(input(question))
            
            # checks number is more than zero
            if response > 0:
                return response
            
            # outputs error if input is invalid
            else:
                print(error)
                print()
                
        except ValueError:
            print(error)    
    


# Main Routine goes here

# Introduction / Heading print statements

print()
print("**** Fence Cost Calculator *****")
print()

# Start of calculator loop
keep_going = ""
while keep_going == "":

    # call your number checker function three times to get the 
    # width, length and cost_per_m of the fencing
    width = num_check ("Width: ")
    length = num_check ("Length: ")
    cost_per_m = num_check ("Cost_per_m: $")

    # Calulate perimeter (width + length) x 2
    perimeter = (width + length) * 2

    # Calculate the cost of the fencing (perimeter x price / meter)
    cost = (perimeter * cost_per_m)

    # Output the perimeter and cost of the fencing
    print()
    print("Perimeter: {:.2f} units".format(perimeter))
    print("Cost: {:.2f} square units".format(cost))
    print()
    
    keep_going = input("Press <enter> to keep going or any key to quit: ")
    
    print()
    print("-" * 30)
    print()


print()
print("Thanks for using the Fencing cost calculator")