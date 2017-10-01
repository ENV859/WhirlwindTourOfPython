#RangeFunctionExample.py

# This example demonstrates the range function for generating 
# a sequence of values that can be used in a for loop.

pi = 3.1415

for r in range(0,100,20):
    area = (r ** 2) * pi
    print "The area of a circle with radius ", r, "is ", area