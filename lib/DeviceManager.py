# author: brian dillmann
# for rscs
from Devices.Input import Input
from Devices.Timer import Timer
from Devices.AnalogInput import AnalogInput
from Devices.Output import Output

class DeviceManager:
	def __init__(self):
		self.inputs = {}
		self.outputs = {}

	def addSimpleInput(self, name, location, invert = False):
		if name in self.inputs:
			raise KeyError('Cannot create device with name %s because input with that name already exists' % name)
		self.inputs[name] = Input(name, location, invert)

	def addTimer(self, name, interval = 's'):
		if name in self.inputs:
			raise KeyError('Cannot create device with name %s because input with that name already exists' % name)
		self.inputs[name] = Timer(name, interval)

	def addAnalogInput(self, name, location):
		if name in self.inputs:
			raise KeyError('Cannot create device with name %s because input with that name already exists' % name)
		self.inputs[name] = AnalogInput(name, location)

	def addOutput(self, name, location, invert = False):
		if name in self.outputs:
			raise KeyError('Cannot create device with name %s because output with that name already exists' % name)
		self.outputs[name] = Output(name, location, invert)

	def read(self, name):
		if not name in self.inputs:
			raise KeyError('Cannot find input with name %s, unable to read' % name)
		return self.inputs[name].read()

	def turnOn(self, name):
		if not name in self.outputs:
			raise KeyError('Cannot find output with name %s, unable to turn on' % name)
		self.outputs[name].on()

	def turnOff(self, name):
		if not name in self.outputs:
			raise KeyError('Cannot find output with name %s, unable to turn off' % name)
		self.outputs[name].off()
