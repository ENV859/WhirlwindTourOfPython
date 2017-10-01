#IfExample.py

# This example demonstrates how an 'if' statement is used to
#  control execution of certain commands. It builds off the for
#  loop example, adding a condition so that the message prints
#  only when the fruit is a kiwi or blueberries

#Create a list of fruit
fruitList = ("apples","oranges","kiwi","grapes","blueberries") 

# Loop through each item in the tuple and execute
# each line that is indented under the for loop
for fruit in fruitList:
    if fruit == "kiwi" or fruit == "blueberries":
        print "I like to eat " + fruit


# Dedented lines are run after the loop completes
print "\nI like ice cream too..."