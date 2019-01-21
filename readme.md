# PTW decibel reactive lamp
This project was made as a PTW school project. 

The project uses two microphones to calculate a realtime average decibel. This decibel values is used to control three lights (green, yellow and red). Green indicates a proper dB level, yellow indicates that it's too loud and red indicates that the sound is way too loud.

These values that trigger the certain lights can be controlled from a web panel. This web panel contains default room profiles and also allows the user to create there own. These values are stored in a remote MySQL database.

#### Software dependencies:

##### Server:
- MySQL server
- PHP
- Apache

##### Client:
- MySQL client
- PyAudio
- Numpy
- Audioop

#### Hardware dependencies:
- 2 raspberry pi's
- 1 switch
- 3 UTP cables
- 2 microphones (USB connections as they need to have a sound card build in)

GPIO pins: (this can be changed in the: /client/modules/gpio.py
- Red led = 3
- Yellow led = 5
- Green led = 7

#### Required IP configurations of the raspberry pi's

##### Client IP:
192.168.50.101
netmask 255.255.255.0

##### Server IP:
192.168.50.100
netmask 255.255.255.0

#### File placement on both the raspberry pi's

##### Client side:

Use all the files from the client folder.

Place the py files (except the .asoundrc file) where ever you want, as long as you have read/write permission.

The asound.rc file needs to be placed in the ~/ folder and needs to overwrite the existing one (if it already exists). This will merge multiple microphone sounds cards in to one, as linux can't control multiple sounds cards at the same time.
When that's done reboot the Raspberry PI.

##### Server side:

Use all the files from the server folder.

Place the php files on your apache server. (/var/www/html)

The database.sql needs to be imported in to the database server and the database connection settings need to be changed in the modules/database.php on the server side and the modules/database.py on the client side.

The database.sql contains the database structure and some default profiles.

##### Credits: Stefan, Max, Dorien, Thijs, Lucas
