#ReadDataExample.py
#
# This example illustrates the use of the file object tor ead in data from a 
# text file, extract lines of text, and print them to the screen

# Set the gageDataFile to point to the text file containing the data
#  Note: if no path is specified, Python will look for the file in the same
#  folder as the script. If the file is in a different location, you can
#  specify the entire path, e.g. "S://Scripting2//EnoNearDurham.txt" 
gageDataFile = "EnoNearDurham.txt"

# Create a file object by opening the file -- in read only ('r') mode
fileObj = open(gageDataFile,'r')

# Read the first line, setting its contents into the "lineString" variable, then print it 
lineString = fileObj.readline()
print lineString

# Or, use a while loop to read each line sequentially and print to the screen
while lineString:
    if lineString[0] == "U":            ## All data lines begin with the letter 'U'
        print lineString,           
    lineString = fileObj.readline()

# Send a note that that all lines have now been read and printed to the screen
print "Finished!"

#Be sure to close the fileObject so that other applications can access it
fileObj.close()