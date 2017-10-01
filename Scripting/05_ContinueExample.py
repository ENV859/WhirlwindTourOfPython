#BreakExample.py

# This example evaluates a list 10 randomly generated numbers, calculating the
#  square root of each. The break statement is used to catch numbers less than
#  zero, as an error would ensue. 

randomNumbers = [81, 8, -17, 2, 9, 0, 9, 4, 16, 64]
   
# Loop through each day in the tuple of days
for x in randomNumbers:
    # Evaluate the value
    if x < 0:
        print x , "is not a positive number"
        continue
    print "The square root of ",x, "is", x ** 0.5 

# Dedent lines run after the loop completes
print "Finished processing"