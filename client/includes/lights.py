### Control the lights with the dB value parameters from the database and the recorded dB from the 2 microphones

# Prints the name and the values of the loaded profile
print ("Loaded profile information:\nName: " + profilename + "\ndB min: " + str(dbmin) + "\ndB max: " + str(dbmax) + "\n")

# Lights
while True:
    
    result = dbValue() # Fetch the average dB value from the readAudio() function
    if result < dbmin: # If the result is smaller then the dbmin value, then turn the light to green
		GPIO.output(GREEN, 1)
		GPIO.output(YELLOW, 0)
		GPIO.output(RED, 0)
		print("Level Green\ndB: " + str(result) + "\n") # Print the level green and the dB value
    if result > dbmin and result < dbmax: # If the result is bigger then the dbmin value and smaller then the dbmax value, then turn the light to yellow
		GPIO.output(GREEN, 0)
		GPIO.output(YELLOW, 1)
		GPIO.output(RED, 0)
		print("Level Yellow\ndB: " + str(result) + "\n") # Print the level yellow and the dB value
    if result > dbmax: # If the result is bigger then the dbmax value, then turn the light to red
		GPIO.output(GREEN, 0)
		GPIO.output(YELLOW, 0)
		GPIO.output(RED, 1)
		print("Niveau Red\ndB: " + str(result) + "\n") # Print the level red and the dB value