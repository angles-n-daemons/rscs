# author: brian dillmann
# for rscs
from context import DeviceManager
import unittest
import RPi.GPIO as GPIO

class device_manager_test(unittest.TestCase):

	def setUp(self):
		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)
	
	def test_not_found_errors(self):
		m = DeviceManager()

		with self.assertRaises(KeyError):
			m.read('blahdevice')

		with self.assertRaises(KeyError):
			m.turnOn('randomdevice')

		with self.assertRaises(KeyError):
			m.turnOff('randomDevice')

	def test_input_exists(self):
		m = DeviceManager()

		m.addSimpleInput('device name', 18)

		with self.assertRaises(KeyError):
			m.addSimpleInput('device name', 18)
		with self.assertRaises(KeyError):
			m.addTimer('device name')
		with self.assertRaises(KeyError):
			m.addAnalogInput('device name', 18)

	def test_output_exists(self):
		m = DeviceManager()

		m.addOutput('device name', 2)
		
		with self.assertRaises(KeyError):
			m.addOutput('device name', 2)

	def test_simple_input(self):
		m = DeviceManager()
		
		m.addSimpleInput('device', 18)
		x = m.read('device')
		m.addSimpleInput('device 2', 18, True)
		y = m.read('device 2')
		
		self.assertNotEqual(x, y)

	def test_analog_input(self):
		m = DeviceManager()

		m.addAnalogInput('analog input', 18)
		x = m.read('analog input')
		self.assertNotEqual(x, 0)

	def test_timer(self):
		m = DeviceManager()

		m.addTimer('timer', 's')
		m.addTimer('timer 2', 'ms')
		
		import time
		time.sleep(1)

		x = m.read('timer')
		y = m.read('timer 2')

		self.assertGreater(y, x)		

if __name__ == 'main':
	unittest.main()
