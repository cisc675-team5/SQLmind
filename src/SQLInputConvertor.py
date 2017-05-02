def dataConvertor(sqlFunctions):
	result=[]
	parent=[]
	child=[]
	result.append(parent)
	result.append(child)
	for function in sqlFunctions:
		parent.append(function[0])
		child.append(function[1])
	return result