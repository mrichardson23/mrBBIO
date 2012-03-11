#!/usr/bin/python
from mrbbio import *

def setup():
	pinMode("P8.12", OUTPUT)
	pinMode("P8.14", OUTPUT)
	pinMode("P8.16", OUTPUT)
	pinMode("P8.18", OUTPUT)
	pinMode("P8.20", OUTPUT)
	pinMode("P8.45", INPUT)

def loop():
	if (digitalRead("P8.45") == HIGH):
		print "Button Pressed at: %d" % millis()
		digitalWrite("P8.12", HIGH)
		digitalWrite("P8.14", HIGH)
		digitalWrite("P8.16", HIGH)
		digitalWrite("P8.18", HIGH)
		digitalWrite("P8.20", HIGH)
		delay(1000)
		digitalWrite("P8.12", LOW)
		digitalWrite("P8.14", LOW)
		digitalWrite("P8.16", LOW)
		digitalWrite("P8.18", LOW)
		digitalWrite("P8.20", LOW)
	delay(10) # don't peg the processor checking pin	
run(setup, loop)
