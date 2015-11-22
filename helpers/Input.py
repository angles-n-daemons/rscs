# author: brian dillmann
# for rscs

import RPi.GPIO as GPIO

class Input:
	def __init__(self, loc):
		if not isinstance(loc, (int, long)):
			raise Error('Input Location must be an integer')
		
