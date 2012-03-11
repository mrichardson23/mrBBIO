#!/usr/bin/python
from mrbbio import *

def setup():
	pinMode("P8.12", OUTPUT)
	pinMode("P8.14", OUTPUT)
	pinMode("P8.16", OUTPUT)
	pinMode("P8.18", OUTPUT)
	pinMode("P8.20", OUTPUT)
	pinMode("P8.8", OUTPUT)

def loop():
	digitalWrite("P8.12", HIGH)
	digitalWrite("P8.14", HIGH)
	digitalWrite("P8.16", HIGH)
	digitalWrite("P8.18", HIGH)
	digitalWrite("P8.20", HIGH)
	digitalWrite("P8.8", LOW)
	delay(1000)
	digitalWrite("P8.12", LOW)
	digitalWrite("P8.14", LOW)
	digitalWrite("P8.16", LOW)
	digitalWrite("P8.18", LOW)
	digitalWrite("P8.20", LOW)
	delay(1000)
	
run(setup, loop)
