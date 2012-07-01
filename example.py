#!/usr/bin/python

# mrBBIO Example Code
# 
# By Matt Richardson, July 1, 2012
#
# https://github.com/mrichardson23/mrBBIO
#
# Repeatedly reads if a button is pressed. when it's pressed, it will light
# an LED for one second and print the time (in ms) since the script was
# started.
#
# Circut:
# * An LED is connected to pin 12 on header P8.
# * A button is connected to pin 45 on header P8. Use a pull-down resistor
#   (around 10K ohms) between pin 45 and ground. 3.3v for the other side of
#   the button can be taken from pins 3 or 4 on header P9. Warning: Do not
#   allow 5V to go into the GPIO pins.

# import the functions from the mrbbio module:
from mrbbio import *

def setup(): # this function will run once, on startup
	pinMode("P8.12", OUTPUT) # set up pin 12 on header P8 as an output
	pinMode("P8.45", INPUT) # set up pin 45 on header P8 as an input

def loop(): # this function will run repeatedly, until user hits CTRL+C
	if (digitalRead("P8.45") == HIGH): # was the button pressed? (is 3.3v making it HIGH?) then do:
		print "Button Pressed at: %d" % millis() # print to console, milliseconds since start up
		digitalWrite("P8.12", HIGH) # set pin 12 high, illuminating the LED
		delay(1000) # wait for 1 second
		digitalWrite("P8.12", LOW) # set pin 12 low, turning the LED off
	delay(10) # don't "peg" the processor checking pin

# the line below is required. It passes the functions above into a function that handles
# the overall setup/loop structure of the script. It also handles termination gracefully.
run(setup, loop)
