from context import Output
import unittest
import RPi.GPIO as GPIO

class test_simple_output(unittest.TestCase):

	def setUp(self):
		self.out_pin = 2
		GPIO.setmode(GPIO.BCM)

	def test_init_errs(self):
		# try to initialize output with illegal location 
		with self.assertRaises(TypeError):
			output = Output('out', 'a')

		with self.assertRaises(ValueError):
			# try to initialize a port that is a legal GPIO output
			output = Output('out', 500)

	def test_using(self):
		output = Output('out', self.out_pin)
		output.on()
		self.assertTrue(GPIO.input(self.out_pin))
		output.off()
		self.assertFalse(GPIO.input(self.out_pin))
		GPIO.cleanup()

	def test_invert(self):
		output = Output('out', self.out_pin, True)
		output.on()
		self.assertFalse(GPIO.input(self.out_pin))
		output.off()
		self.assertTrue(GPIO.input(self.out_pin))
		GPIO.cleanup()

if __name__ == 'main':
	unittest.main()
