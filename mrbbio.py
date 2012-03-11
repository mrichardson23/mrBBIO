"""Arduino-like library for Python on BeagleBone"""

import time

HIGH = "HIGH"
LOW = "LOW"
OUTPUT = "OUTPUT"
INPUT = "INPUT"
pinList = [] # needed for unexport()
startTime = time.time() # needed for millis()

def pinMode(pin, direction):
	"""pinMode(pin, direction) opens (exports)  a pin for use and 
	sets the direction"""
	fw = file("/sys/class/gpio/export", "w")
	fw.write("%d" % (pin))
	fw.close()
	fileName = "/sys/class/gpio/gpio%d/direction" % (pin)
	fw = file(fileName, "w")
	if direction == "INPUT":
		fw.write("in")
	else:
		fw.write("out")
	fw.close()
	pinList.append(pin)


def digitalWrite(pin, status):
	"""digitalWrite(pin, status) sets a pin HIGH or LOW"""
	fileName = "/sys/class/gpio/gpio%d/value" % (pin)
	fw = file(fileName, "w")
	if status == "HIGH":
		fw.write("1")
	if status == "LOW":
		fw.write("0")
	fw.close()
	
def digitalRead(pin):
	"""digitalRead(pin) returns HIGH or LOW for a given pin."""
	fileName = "/sys/class/gpio/gpio%d/value" % (pin)
	fw = file(fileName, "r")
	inData = fw.read()
	if inData == "0\n":
		return LOW
	if inData == "1\n":
		return HIGH	
	
def pinUnexport(pin):
	"""pinUnexport(pin) closes a pin in sysfs. This is susally 
	called by cleanup() when a script is exiting."""
	fw = file("/sys/class/gpio/unexport", "w")
	fw.write("%d" % (pin))
	fw.close()

def cleanup():
	for pin in pinList:
		pinUnexport(pin)

def delay(millis):
	"""delay(millis) sleeps the script for a given number of 
	milliseconds"""
	time.sleep(millis/1000)

def millis():
	"""millis() returns an int for the number of milliseconds since 
	the script started."""
	return int((time.time() - startTime) * 1000)


def run(setup, main): # from PyBBIO by Alexander Hiam - ahiam@marlboro.edu - www.alexanderhiam.com https://github.com/alexanderhiam/PyBBIO
  """ The main loop; must be passed a setup and a main function.
      First the setup function will be called once, then the main
      function wil be continuously until a stop signal is raised, 
      e.g. CTRL-C or a call to the stop() function from within the
      main function. """
  try:
    setup()
    while (True):
      main()
  except KeyboardInterrupt:
    # Manual exit signal, clean up and exit happy
    cleanup()
  except Exception, e:
    # Something may have gone wrong, clean up and print exception
    cleanup()
    print e
