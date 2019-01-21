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