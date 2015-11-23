# author: brian dillmann
# for rscs

import RPi.GPIO as GPIO

class Input:
	def __init__(self, name, loc, invert = False):
		if not isinstance(loc, (int, long)):
			raise TypeError('Input Location must be an integer')
		if not name.replace(' ', '').isalnum():
                        raise ValueError('Device names must only contain letters, numbers and spaces')
		GPIO.setup(loc, GPIO.IN)
		self.name = name
		self.loc = loc
		self.invert = invert

	def read(self):
		msg = GPIO.input(self.loc)
		# logical xor on invert to see whether to invert
		return msg ^ self.invert 

