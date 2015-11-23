# author: brian dillmann
# for rscs

import RPi.GPIO as GPIO

class Input:
	def __init__(self, loc, invert = False):
		if not isinstance(loc, (int, long)):
			raise TypeError('Input Location must be an integer')

		GPIO.setup(loc, GPIO.IN)
		self.loc = loc
		self.invert = invert

	def read(self):
		msg = GPIO.input(self.loc)
		# logical xor on invert to see whether to invert
		msg = msg ^ self.invert 

