# author: brian dillmann
# for rscs

class Evaluator:
	# devices should be a DeviceManager Object
	def __init__(self, devices):
		self.devices = devices	

	def eval(self, condition):
		toks = condition.split(' ')

		if len(toks) != 3:
			raise ValueError('Condition contains the wrong number of tokens')

		
