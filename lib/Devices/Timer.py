# author: brian dillmann
# for rscs
import time

class Timer:
	def __init__(self, name, interval='s'):
		if not name.replace(' ', '').isalnum():
                        raise ValueError('Device names must only contain letters, numbers and spaces')
		self.start_time()
		self.name = name
		if interval == 'ms':
			self.interval = .001
		if interval == 's':
			self.interval = 1
		if interval == 'm':
			self.interval = 60
	
	def start_time(self):
		self.start = time.time()

	def read(self):
		cur = time.time()
		diff = cur - self.start
		return diff / self.interval

