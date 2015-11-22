# author: brian dillmann
# for rscs

import RPi.GPIO as GPIO, time

class AnalogInput:
	def __init__(self, loc):
		if not isinstance(loc, (int, long)):	
			raise TypeError('Output Location must be an integer')
		self.loc = loc

		GPIO.setup(loc, GPIO.IN)

	def read(self):
		reading = 0
		GPIO.setup(self.loc, GPIO.OUT)
		GPIO.output(self.loc, GPIO.LOW)	
		time.sleep(.1)
		
		GPIO.setup(self.loc, GPIO.IN)	
		while (GPIO.input(self.loc) == GPIO.LOW):
			reading += 1
		return reading


