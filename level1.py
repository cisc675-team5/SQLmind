import sys
import re


Vertexes = []
Store = []
sqlFileName = sys.argv[1]



def processInnerfunction(ends): #extract the function name if it's in a block
	global Vertexes
	if len(ends)==0:
		return
	for e in ends:
		processBlock(e)



def processBlock(block): #extract function name in block

	global Vertexes
	global Store 
	if len(block)<2:
		return
	for i in range(0,len(block)):
		if block[i]=='(':
			Vertexes.append(tuple([Store[-1],block[:i]]))
			Store.append(block[:i])
			processInnerfunction(block[i+1:-1].split(','))
			Store.pop();
			return



def processLine(line): #split line by operators or semicolon
	blocks=filter(None, re.split("[ \-\+\=\/\;]+", line))
	if len(blocks)==0:
		return
	if blocks[0]=='FUNCTION' or blocks[0]=='function':
		Store.append(blocks[1])
		return
	for block in blocks:
		processBlock(block)


def processSQLfunction(function): #split function by '\n'
	global Store
	lines = function.split('\n')
	for line in lines:
		if len(line)>0:
			processLine(line)


				
def processSQLFile(sqlFileName): #read in the file and split the file by 'CREATE'
	fd = open(sqlFileName, 'r')
	sqlFile = fd.read()
	fd.close()
	sqlFuntions = re.split('CREATE',sqlFile)
	for function in sqlFuntions:
		processSQLfunction(function)

def main():
	global sqlFileName
	global Vertexes
	processSQLFile(sqlFileName)
	print Vertexes

if __name__ == "__main__":
    main()




