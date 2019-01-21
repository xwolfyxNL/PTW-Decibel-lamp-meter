# Enables the GPIO pins
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

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