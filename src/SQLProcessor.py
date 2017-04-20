import sys
import re
from sets import Set


class SQLProcessor:



	def __init__(self,sqlFileName):
		self.__dict__ = {}
		self.__Store = []
		self.__result = Set()
		self.__functions = Set()
		self.__processSQLFile(sqlFileName)
		self.__resultList = []
		#print "original set:"
		#print self.__result
		self.__removeInvalidNode()
		#print "purified set:"
		#print self.__resultList




	def __processInnerfunction(self,ends): #extract the function name if it's in a block
		if len(ends)==0:
			return
		for e in ends:
			self.__processBlock(e)




	def __processBlock(self,block): #extract function name in block
		if len(block)<2:
			return
		for i in range(0,len(block)):
			if block[i]=='(':
				self.__result.add(tuple([self.__Store[-1],block[:i]]))
				self.__Store.append(block[:i])
				self.__processInnerfunction(block[i+1:-1].split(','))
				self.__Store.pop()
				return




	def __processLine(self,line): #split line by operators or semicolon
		blocks=filter(None, re.split("[ \-\+\=\/\;]+", line))
		if len(blocks)==0:
			return
		if blocks[0]=='FUNCTION' or blocks[0]=='function':
			self.__Store.append(blocks[1])
			return
		for block in blocks:
			self.__processBlock(block)




	def __processSQLfunction(self,function): #split function by '\n'
		lines = function.split('\n')
		for line in lines:
			if len(line)>0:
				self.__processLine(line)




	def __processSQLFile(self,sqlFileName): #read in the file and split the file by 'CREATE'
		fd = open(sqlFileName, 'r')
		sqlFile = fd.read()
		fd.close()
		sqlFuntions = re.split('CREATE',sqlFile)
		self.__extractDefinedSQLFunction(sqlFuntions)
		for function in sqlFuntions:
			self.__processSQLfunction(function)




	def __extractDefinedSQLFunction(self,sqlFunctions):
		for function in sqlFunctions:
			self.__getNameOfFunction(function)




	def __getNameOfFunction(self,function):
		lines = function.split('\n')
		if len(lines)>0:
			line = lines[0]
			blocks=filter(None, re.split("[ \-\+\=\/\;]+", line))
			if len(blocks)>0:
				self.__functions.add(blocks[1])
		#print "selfdefined function names:"
		#print self.__functions


	def __removeInvalidNode(self):
		for e in self.__result:
			parent = e[0]
			child = e[1]			
			if (parent in self.__functions) and (child in self.__functions):
				self.__resultList.append(e)



	def getResult(self):
		return self.__resultList

