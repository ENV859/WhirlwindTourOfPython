#ForLoopExample.py

# This example uses a for loop to iterate through each item in 
# the "fruit" list, updating the value of the "fruit" variable and 
# executing whatever lines are indented under the for statement

#Create a list of fruit
fruitList = ("apples","oranges","kiwi","grapes","blueberries") 

# Loop through each item in the tuple and execute
# each line that is indented under the for loop
for fruit in fruitList:
    print "I like to eat " + fruit

# Dedented lines are run after the loop completes
print "\nI like ice cream too..."
