from mekk.xmind import XMindDocument

def constructTreeMap(root,parents,children,distingushParentList):
	#first level
	Current=[]
	Next=[]
	flagList=[0]*len(parents)

	for node in distingushParentList:
		Current.append(root.add_subtopic(node))

	#use BFS to build the tree
	while not Finshed(flagList):
		for i in xrange(0,len(parents)):
			for node in Current:
				if parents[i]==node.get_title():
					Next.append(node.add_subtopic(children[i]))
					#has been set
					flagList[i]=1

		Current=Next
		Next=[]
		


def Finshed(flagList):
	for e in flagList:
		if e==0:
			return False
	return True


