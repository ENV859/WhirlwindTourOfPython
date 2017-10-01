#WriteDataExample.py

# This script demonstrates how a file object is used to both write to a new text file and
#  append to an existing text file.In it we will read the contents of the EnoNearDurham.txt 
#  file and write selected data records to the output file.

# First, create some variables. "dataFileName" will point to the EnoNearDurham.txt file, 
#  and "outputFileName" will that will contain the name of the file we will create.
dataFileName = "S://Scripting2//EnoNearDurham.txt" 
outputFileName = "S://Scripting2//SelectedNWISRecords.txt"

# Next, open the data file and read its contents into a list object. This is similar
#  to the previous tutorial, but here we read the entire contents into a single list
dataFileObj = open(dataFileName, 'r')  ## Opens the data file as read only
lineList = dataFileObj.readlines()     ## Creates a list of lines from the data file
dataFileObj.close()                    ## We have our list, so we can close the file
print len(lineList), " lines read in"  ## This is a quick statement to show how many lines were read

# Here, we create a file object in 'w' or write mode. This step creates a new file at
#  the location specified. IF A FILE EXISTS ALREADY THIS WILL OVERWRITE IT!
newFileObj = open(outputFileName,'w')

# Next, we loop through the lines in the dataList. If it's a comment, we'll skip it.
#  Otherwise, we'll split the items in the line into a list.
for dataLine in lineList:
    # If the line is a comment, skip further processing and go to the next line
    if dataLine[:4] <> "USGS":
        continue
    # Parse the data line and look at the discharge value. Write only records below 6 cfs
    lineData = dataLine.split("\t")  ## Creates a list from the lineData string of items separated by a tab (\t)
    cfs = float(lineData[4])         ## Converts discharge, the 5th item in this list, from a string to a float
    if cfs >= 6.0:                   ## Checks whether the discharge is greater than 6.0
        newFileObj.write(dataLine)   ## If it is, only then write it to the out file
newFileObj.close() 