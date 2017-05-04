import sys
import re
from sets import Set
from SQLDataStructure import FunctionLine


class SQLProcessor:

	def __init__(self,sqlFileName):
		self.__keyWord =''
		self.__dict__ = {}
		self.__Store = []
		self.__result = Set()
		self.__functions = Set()
		self.__functionLineDictionary = {}
		self.__counter = 0
		self.__resultList = []
		self.__finalResult = []

		self.__createDictionary(sqlFileName)
		self.__processSQLFile(sqlFileName)
		self.__removeInvalidNode()
		self.__convertTofunctionLineFormat()



#-----------------------------------------------------------------------------
	def __createDictionary(self,sqlFile):
		fd = open(sqlFile, 'r')
		sqlFile = fd.read()
		fd.close()
		lines = sqlFile.split('\n')
		blocks = lines[0].split()
		self.__keyWord = blocks[0]
		for l in lines:
			blocks = l.split()
			if self.__containKeyWords(blocks):
				self.__functionLineDictionary[blocks[2]] = self.__counter
			self.__counter = self.__counter+1


	def __containKeyWords(self,blocks):
		if len(blocks) == 0:
			return False
		if blocks[0] == self.__keyWord:
			return True
		return False
#-----------------------------------------------------------------------------


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
		sqlFuntions = re.split(self.__keyWord,sqlFile)
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


	def __removeInvalidNode(self):
		for e in self.__result:
			parent = e[0]
			child = e[1]			
			if (parent in self.__functions) and (child in self.__functions):
				self.__resultList.append(e)



	def __convertTofunctionLineFormat(self):
		for i in xrange(0,len(self.__resultList)):
			pfunction = self.__resultList[i][0]
			pline = self.__functionLineDictionary[self.__resultList[i][0]] 
			cfunction = self.__resultList[i][1]
			cline = self.__functionLineDictionary[self.__resultList[i][1]] 
			self.__finalResult.append(tuple([FunctionLine(pfunction,pline),FunctionLine(cfunction,cline)]))


	def getResult(self):
		return self.__finalResult

