""""This module setups and initializes the GPIO pins that will be used for connecting the lights.
After the initialization the GPIO pins get turned off in case they were already on.
It also contains three functions for controlling the individual lights"""

# Imports
import RPi.GPIO as GPIO

# Enables the GPIO pins
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# Names GPIO pins for the leds
RED = 3
YELLOW = 5
GREEN = 7

# Setup the GPIO pins
GPIO.setup(RED,GPIO.OUT)
GPIO.setup(YELLOW,GPIO.OUT)
GPIO.setup(GREEN,GPIO.OUT)

# Turn off all the led GPIO pins (in case they were already enabled)
GPIO.output(RED, 0)
GPIO.output(YELLOW, 0)
GPIO.output(GREEN, 0)

# Functions for turning the green, yellow and red light on or off
def green():
        GPIO.output(GREEN, 1)
        GPIO.output(YELLOW, 0)
        GPIO.output(RED, 0)
def yellow():
        GPIO.output(GREEN, 0)
        GPIO.output(YELLOW, 1)
        GPIO.output(RED, 0)
def red():
        GPIO.output(GREEN, 0)
        GPIO.output(YELLOW, 0)
        GPIO.output(RED, 1)