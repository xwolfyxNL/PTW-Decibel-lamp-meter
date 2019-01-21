# Imports
import time
import os
import pyaudio
import audioop
import numpy as np

# Initialize audio channel for both the microphones
pa = pyaudio.PyAudio()

# Print microphone device id's incase of initialisation error
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