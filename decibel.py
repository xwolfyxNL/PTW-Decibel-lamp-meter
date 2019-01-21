### Imports
import RPi.GPIO as GPIO
import pyaudio
import audioop
import numpy as np
import time
import os
import mysql.connector

### Preparation
# Enables the GPIO pins
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# Connects to the database on the other Raspberry PI
mydb = mysql.connector.connect(
  host="192.168.50.100",
  user="root",
  passwd="root",
  database="LampAppProfiles"
)

# Names GPIO pins for leds
RED = 3
YELLOW = 5
GREEN = 7

# Setup the GPIO pins
GPIO.setup(RED,GPIO.OUT)
GPIO.setup(YELLOW,GPIO.OUT)
GPIO.setup(GREEN,GPIO.OUT)

# Turn off all the led GPIO pins (incase they were already enabled)
GPIO.output(RED, 0)
GPIO.output(YELLOW, 0)
GPIO.output(GREEN, 0)

# Initialize audio channel for both the microphones
pa = pyaudio.PyAudio()

# Print microphone device id's incase of initialisation error
info = pa.get_host_api_info_by_index(0)
numdevices = info.get('deviceCount')
for i in range(0, numdevices):
        if (pa.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
            print "Input Device id ", i, " - ", pa.get_device_info_by_host_api_device_index(0, i).get('name')
            
# Initialize microphone 1
stream1 = pa.open(format = pyaudio.paInt16,
    channels = 1,
    rate = 48000,
    input = True,
    frames_per_buffer = 128,
    input_device_index = 2) # input_device_index specifies the device number of the microphone

# Initialize microphone 2
stream2 = pa.open(format = pyaudio.paInt16,
    channels = 1,
    rate = 48000,
    input = True,
    frames_per_buffer = 128,
    input_device_index = 3) # input_device_index specifies the device number of the microphone

# Fetch dB values from the Mysql database
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM profielen where naam = 'ingesteld'")
data = mycursor.fetchall()
for row in data:
  profilename = str(row[1])
  dbmin = int(row[2])
  dbmax = int(row[3])

### Start the microphone listening
os.system('clear') # Clear screen
def dbValue():
    dbList = [] # dB list
    
    #Microphone 1 data
    for index in range(1000):
        data = stream1.read(128, exception_on_overflow=False)
        rms = audioop.rms(data,2)
        dbList.append((20*np.log(rms)))

    #Microphone 2 data
    for index in range(1000):
        data = stream2.read(128, exception_on_overflow=False)
        rms = audioop.rms(data,2)
        dbList.append((20*np.log(rms)))
    value = int(sum(dbList)/len(dbList)) #calculate average dB based on the RMS
    return value # return the average dB value

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
