# author: brian dillmann
# for rscs
import time

class Timer:
	def __init__(self, interval='s'):
		self.start_time()
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

