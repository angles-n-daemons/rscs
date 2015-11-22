from context import TimeInput 
import unittest
import time

class test_simple_output(unittest.TestCase):

	def test_start_on_init(self):
		input = TimeInput()
		t = input.read()
		self.assertGreater(t, 0)

	def test_seconds_interval(self):
		input1 = TimeInput()
		input2 = TimeInput('s')
		time.sleep(10)
		t1 = input1.read()
		t2 = input2.read()
		self.assertGreater(t1, 9)
		self.assertGreater(t2, 9)
		self.assertLess(t1, 11)
		self.assertLess(t2, 11)

	def test_reset(self):
		input = TimeInput('s')
		time.sleep(5)
		t = input.read()
		self.assertGreater(t, 4)
		input.start_time()
		t = input.read()
		self.assertLess(t, 1)

	def test_millis(self):
		input = TimeInput('ms')
		time.sleep(1)
		t = input.read()
		self.assertGreater(t, 900)
		self.assertLess(t, 1100)

	def test_mins(self):
		input = TimeInput('m')
		time.sleep(3)
		t = input.read()
		self.assertLess(t, 1)

if __name__ == 'main':
	unittest.main()
