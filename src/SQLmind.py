import sys

from SQLProcessor import SQLProcessor


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


def main():
	processor = SQLProcessor(sys.argv[1])
	#print processor.getResult()
	print dataConvertor(processor.getResult())


if __name__=='__main__':
	main()