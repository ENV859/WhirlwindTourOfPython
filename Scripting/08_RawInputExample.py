# RawInputExample.py

# This script demonstrates the use of the raw_input() function
#  for retrieving user input via a simple popup window. The script
#  asks the user for his or her name and date of birth, and then
#  replies with a simple message.

# Ask for the user's name
userName = raw_input("Hi! What's your name?")

# Generate a prompt for the follow up question
promptString = "Hello, "+userName+". How old are you?"

# Get the birth year, using the prompt string created above
userAge = raw_input(promptString)

# Calculate the birth year of the user. All replies using raw_input() are
#  passed as strings, so we would need to convert then to numbers
birthYear = 2012 - int(userAge)

# Send the reply
reply =  "I'm guessing you were born in " + str(birthYear)
raw_input(reply)
