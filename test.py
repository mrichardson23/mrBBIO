#!/usr/bin/python
from mrbbio import *

def setup():
	pinMode(44, OUTPUT)
	pinMode(26, OUTPUT)
	pinMode(70, INPUT)

def loop():
	digitalWrite(44, HIGH)
	delay(1000)
	digitalWrite(44, LOW)
	delay(1000)

run(setup, loop)
