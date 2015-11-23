from context import Input 
import unittest
import RPi.GPIO as GPIO

class test_simple_input(unittest.TestCase):

	def setUp(self):
		self.in_pin = 2
		GPIO.setmode(GPIO.BCM)

	def test_init_errs(self):
		# try to initialize input with illegal location 
		with self.assertRaises(TypeError):
			input = Input('a')

		with self.assertRaises(ValueError):
			# try to initialize a port that is a legal GPIO input
			input = Input(500)

	def test_read(self):
		input = Input(22)
		x = input.read() 

if __name__ == 'main':
	unittest.main()
