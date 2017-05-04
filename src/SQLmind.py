import sys

from SQLProcessor import SQLProcessor
from SQLCreateMindmap import createMindmap
from SQLInputConvertor import dataConvertor



def main():

	processor = SQLProcessor(sys.argv[1])

	standardInput = dataConvertor(processor.getResult())
	printF(standardInput)
	createMindmap(standardInput)


#def printF(output):
#	for o in output:
#		for i in o:
#			print i.function,i


if __name__=='__main__':
	main()