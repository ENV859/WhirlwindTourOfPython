#WhileLoopExample.py

# This example demonstrates how a while loop is used. Here, we
# calculate the area of several circle with a radius 'r'. We loop
# through gradually larger values of r until the area of the circle
# exceeds 1000.

pi = 3.1415
r = 1
area = (r ** 2) * pi

while area < 1000:
    print r, area          # Indentation indicates what's run in the loop
    r = r + 1              # The variable that gets evaluated must change in the
    area = (r ** 2) * pi   # loop otherwise you'll create an infinite loop!

print "The while loop is done"  # Dedented lines run after the loop completes