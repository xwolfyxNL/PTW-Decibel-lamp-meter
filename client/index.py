# Import all the modules (Database, GPIO, Microphone)
from modules.database import * # Import the database settings and the fetched values
from modules.gpio import * # Import the GPIO settings and the functions
from modules.microphone import * # Import the microphone settings and the functions

# Prints the name and the values of the loaded profile
print ("Loaded profile information:\nName: " + profilename + "\ndB min: " + str(dbmin) + "\ndB max: " + str(
    dbmax) + "\n")

""" This section controls the lights. It fetches the measured dB's and sets a green light if the measured dB's are
    below the minimum threshold, a yellow light if the measured dB's between the minimum and maximum threshold 
    and a red when above the maximum threshold."""
while True:
    result = dbValue()
    if result < dbmin:
        green() # Calls the function for changing the light and printing the message
        print("Level Green\ndB: " + str(result) + "\n")
    elif result > dbmin and result < dbmax:  
        yellow()
        print("Level Yellow\ndB: " + str(result) + "\n")  # Print the level yellow and the dB value
    elif result > dbmax:
        red()
        print("Level Red\ndB: " + str(result) + "\n")  # Print the level red and the dB value