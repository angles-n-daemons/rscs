# author: brian dillmann
# for rscs
from context import AnalogInput
import unittest
import RPi.GPIO as GPIO

class test_analog_input(unittest.TestCase):

	def setUp(self):
		self.out_pin = 2
		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)

	def test_init(self):
		# try to initialize output with illegal location 
		with self.assertRaises(TypeError):
			analog_input = AnalogInput('a')

		with self.assertRaises(ValueError):
			# try to initialize a port that is a legal GPIO output
			analog_input = AnalogInput(500)
	def test_works(self):
		analog_input = AnalogInput(18)
		x = analog_input.read()
		# sanity check
		print x
		self.assertNotEqual(0, x)

if __name__ == 'main':
	unittest.main()
