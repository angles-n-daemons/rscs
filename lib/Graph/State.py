# author: brian dillmann
# for rscs

class State:
	def __init__(self, name):
		if not isinstance(name, basestring):
			raise TypeError('State name must be a string')

		if not len(name):
			raise ValueError('Cannot create State with empty name')

		self.name = name
		self.transitions = []
		self.outputs = {}

	def addOutputVal(self, deviceName, val):
		self.outputs[deviceName] = bool(val)

	def addTransition(self, transition):
		self.transitions.push(transition)
