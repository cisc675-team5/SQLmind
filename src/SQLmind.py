import sys

from SQLProcessor import SQLProcessor
from SQLCreateMindmap import createMindmap
from SQLInputConvertor import dataConvertor



def main():

	processor = SQLProcessor(sys.argv[1])

	standardInput = dataConvertor(processor.getResult())

	createMindmap(standardInput)



if __name__=='__main__':
	main()