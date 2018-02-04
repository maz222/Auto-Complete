from Trie import Trie

class Driver:
	def __init__(self):
		self.trieDict = {}

	def addString(self, string, stringWeight=0):
		trie = self.trieDict.get(string[0])
		if trie == None:
			if len(string) == 1:
				trie = Trie(string,True,stringWeight)
			else:
				trie = Trie(string[0])
		if len(string) > 1:
			trie.addValues(string, stringWeight)
		self.trieDict[string[0]] = trie

	def deleteString(self, string):
		trie = self.trieDict.get(string[0])
		#not found!
		if trie == None:
			return
		node = trie.search(string, False)
		if node == None:
			return
		#if the given string is a substring within the tree (EG:"Ad" in "Adventure")
		if len(node.children.keys()) > 0:
			#change the last node to be non-terminal
			node.isEnd = False
			node.weight = 0
		else:
			#delete all nodes associated with the string
			if len(string) > 1:
				#if the string was the only string in the trie
				if len(trie.headNode.children.keys()) == 1:
					#delete the trie
					self.trieDict.pop(string[0])
				else:
					trie.headNode.children.pop(string[1])
			else:
				#delete the entire trie as it is only one char
				self.trieDict.pop(string[0])

	#get the corresponding *last* node of a string (eg: "Appl[e]")
	def searchNode(self, input):
		trie = self.trieDict.get(input[0])
		#no first char match
		if trie == None:
			return None
		node = trie.search(input)
		return node

	#get all possible strings
	def search(self, input, isWeighted=False):
		trie = self.trieDict.get(input[0])
		#no first char match
		if trie == None:
			return None
		node = trie.search(input)
		results = trie.extractFromNode(node,input[:len(input)-2])
		if isWeighted:
			return sorted(results, key=lambda x:x[1], reverse=True)
		return results

	#add to the current weight of a string
	def addWeight(self, targetString, weight):
		node = self.searchNode(targetString)
		if node == None:
			return
		node.weight += weight

	#set the current weight of a string
	def setWeight(self, targetString, weight):
		node = self.searchNode(targetString)
		if node == None:
			return
		node.weight = weight

		
	def __str__(self):
		out = ""
		if len(self.trieDict.keys()) == 0:
			return "Empty!"
		for trieKey in sorted(self.trieDict.keys()):
			out += trieKey + ":\n" + str(self.trieDict[trieKey]) + "\n"
		return out