class FunctionLine:
	def __init__(self,function,line):
		self.function=function
		self.line=line
	
	def __hash__(self):
		return hash(tuple([self.function,self.line]))

	def __eq__(self, other):
		if isinstance(other, self.__class__):
			return self.__dict__ == other.__dict__
		else:
			return False

	def __ne__(self, other):
		return not self.__eq__(other)
