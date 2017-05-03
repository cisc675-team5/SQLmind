from sets import Set

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

def removeDupilicates(parentNodes):
	parent=Set()
	for node in parentNodes:
		parent.add(node)
	return list(parent)

