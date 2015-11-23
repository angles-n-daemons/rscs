# author: brian dillmann
# for rscs

# this might be a useless class - dont give af
class Transition:
	def __init__(self, destinationStateName, condition, evaluator):
		self.destination = destinationStateName
		self.condition = condition
		self.evaluator = evaluator

	def evaluate(self):
		return self.evaluator.evaluate(self.condition)
