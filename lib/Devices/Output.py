# author: brian dillmann
# for rcsc

import RPi.GPIO as GPIO

class Output:
	def __init__(self, name, loc, invert = False):
		if not isinstance(loc, (int, long)):	
			raise TypeError('Output Location must be an integer')
		if not name.replace(' ', '').isalnum():
                        raise ValueError('Device names must only contain letters, numbers and spaces')
		GPIO.setup(loc, GPIO.OUT)
		self.name = name
		self.loc = loc
		self.invert = invert
 
	def on(self):
		msg = GPIO.HIGH if not self.invert else GPIO.LOW
		GPIO.output(self.loc, msg)

	def off(self):
		msg = GPIO.LOW if not self.invert else GPIO.HIGH
		GPIO.output(self.loc, msg)	
