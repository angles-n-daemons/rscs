# author: brian dillmann
# for rscs
import re

class Evaluator:
	# devices should be a DeviceManager Object
	def __init__(self, devices):
		self.devices = devices	

	def evaluate(self, condition):
		try:
			self.checkLegalExpression(condition)
		except:
			raise ValueError(e)

		# extract device name from quotes in condition
		deviceNameExtract = re.findall('"([^"]*)"', condition)
		if not len(deviceNameExtract):
			raise ValueError('Unable to extract device name from condition')
		deviceName = deviceNameExtract[0]

		if not self.devices.hasInput(devicename):
			raise KeyError('Cannot execute conditions. Input by name %s does not exist' % deviceName)

		# remove device name and replace with input value 
		inputVal = self.devices.read(deviceName)
		condition = re.sub(r'"([^"]*)"', inputVal, condition)
		return eval(evalCondition)
		
	def checkLegalExpression(condition)
		rg = r'\"[A-z 0-9 \-_]+\" [!=<>]{1,2} [0-9.]'
		matchObj = re.match(rg, condition)
		if not matchObj:
			raise ValueError('Illegal Condition. Refuse to eval: %s' % condition)

