import sys

from SQLProcessor import SQLProcessor
from SQLInputConvertor import dataConvertor
from SQLCreateMindmap import createMindmap



def main():

	processor = SQLProcessor(sys.argv[1])

	standardInput = dataConvertor(processor.getResult())

	print standardInput

	createMindmap(standardInput)


if __name__=='__main__':
	main()