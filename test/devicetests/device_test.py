# author: brian dillmann
# for rscs
from context import Input
from context import Output
from context import Timer
from context import AnalogInput
import unittest

class test_device_simple(unittest.TestCase):

	def test_naming_convention(self):
		import RPi
		RPi.GPIO.setmode(RPi.GPIO.BCM)
		with self.assertRaises(ValueError):
			Input('{', 5)
		with self.assertRaises(ValueError):
			Output('{', 5)
		with self.assertRaises(ValueError):
			AnalogInput('{', 5)
		with self.assertRaises(ValueError):
			Timer('{')

		Input('cannamethis123', 5)
		Output('cannamethis123', 5)
		AnalogInput('cannamethis123', 5)
		Timer('cannamethis123')

if __name__ == 'main':
        unittest.main()

