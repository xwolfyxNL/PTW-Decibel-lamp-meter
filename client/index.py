# Load all the files (Imports, Database, GPIO, etc.)

from includes.database import *
from includes.gpio import *
from includes.microphone import *

# Prints the name and the values of the loaded profile
print ("Loaded profile information:\nName: " + profilename + "\ndB min: " + str(dbmin) + "\ndB max: " + str(
    dbmax) + "\n")

# Light control
while True:

    result = dbValue()  # Fetch the average dB value from the readAudio() function
    if result < dbmin:  # If the result is smaller then the dbmin value, then turn the light to green
        green() # Calls the function for changing the light and printing the message
        print("Level Green\ndB: " + str(result) + "\n")  # Print the level green and the dB value
    elif result > dbmin and result < dbmax:  # If the result is bigger then the dbmin value and smaller then the dbmax value, then turn the light to yellow
        yellow()
        print("Level Yellow\ndB: " + str(result) + "\n")  # Print the level yellow and the dB value
    elif result > dbmax:  # If the result is bigger then the dbmax value, then turn the light to red
        red()
        print("Niveau Red\ndB: " + str(result) + "\n")  # Print the level red and the dB value