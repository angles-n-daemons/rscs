# author: brian dillmann
# for rcsc

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

class Output:
	def __init__(self, loc, invert = False):
		if not isinstance(loc, (int, long)):	
			raise TypeError('Output Location must be an integer')

		GPIO.setup(loc, GPIO.OUT)
		self.loc = loc
		self.invert = invert
 
	def on(self):
		msg = GPIO.HIGH if not self.invert else GPIO.LOW
		GPIO.output(self.loc, msg)

	def off(self):
		msg = GPIO.LOW if not self.invert else GPIO.HIGH
		GPIO.output(self.loc, msg)	
