# HandlingErrorsExample.py

# This example demonstrates error handling using try-except
#  statements. If an error occurs within the lines indented
#  under the try: statement, Python jumps to the except: statement
#  and exits more gracefully than spewing red text

userNumber = raw_input("Enter a number")

try:   
    # Convert the raw input from string to a number
    x = float(userNumber)

    # Calculate the square root of the number
    sqroot_x = x ** 0.5 

    # Print the result
    print "The square root of ", x, " is ", sqroot_x

except Exception as e:
    print "An error has occurred"
    print e

