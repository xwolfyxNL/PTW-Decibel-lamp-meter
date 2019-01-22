""""This module setups and intializes the connected microphones.
After it's initialised it starts recording on both the microphones and calculates both the RMS trough a decibel formula.
These values will be stored in a temporary list that after a certain interval returns the average decibel"""

# Imports
import time
import os
import pyaudio
import audioop
import numpy as np

# Initialize audio channel for both the microphones
pa = pyaudio.PyAudio()

# Print microphone device id's in case of a initialisation error
info = pa.get_host_api_info_by_index(0)
numdevices = info.get('deviceCount')
for i in range(0, numdevices):
    if (pa.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
        print "Input Device id ", i, " - ", pa.get_device_info_by_host_api_device_index(0, i).get('name')

# Initialize microphone 1
stream1 = pa.open(format=pyaudio.paInt16,
                  channels=1,
                  rate=48000,
                  input=True,
                  frames_per_buffer=128,
                  input_device_index=2)  # input_device_index specifies the device number of the microphone

# Initialize microphone 2
stream2 = pa.open(format=pyaudio.paInt16,
                  channels=1,
                  rate=48000,
                  input=True,
                  frames_per_buffer=128,
                  input_device_index=3)  # input_device_index specifies the device number of the microphone

### Start the microphone listening
os.system('clear') # Clear screen
def dbValue():
    dbList = [] # dB list
    
    # Microphone 1 data
    for index in range(1000):
        data = stream1.read(128, exception_on_overflow=False)
        rms = audioop.rms(data,2) # Fetch the RMS value from the microphone
        dbList.append((20*np.log(rms))) # dB calculation formula

    # Microphone 2 data
    for index in range(1000):
        data = stream2.read(128, exception_on_overflow=False)
        rms = audioop.rms(data,2) # Fetch the RMS value from the microphone
        dbList.append((20*np.log(rms))) # dB calculation formula
    value = int(sum(dbList)/len(dbList)) # Calculate average dB based on the RMS
    return value # Return the average dB value