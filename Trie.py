#value - the char/string associated with the node
#isEnd - whether the node is terminal or not
#weight - used to sort results if applicable
class TrieNode:
    def __init__(self, value, isEnd=False, weight=0):
        self.value = value
        self.isEnd = isEnd
        self.children = {}
        self.weight = weight
    
    def getChild(self, value):
        return self.children.get(value)

    def addChild(self, node):
        if self.getChild(node.value) == None:
            self.children[node.value] = node
            return node
        else:
            child = self.getChild(node.value)
            if node.isEnd:
                child.isEnd = True
                child.weight = node.weight
            return child

class Trie:
    def __init__(self, headValue, isEnd=False, weight=0):
        self.headNode = TrieNode(headValue, isEnd, weight)
    
    def addValues(self,values,weight=0):
        walker = self.headNode
        if len(values) == 1:
            walker.isEnd = True
            if weight != 0:
                walker.weight = weight

        for i in range(1,len(values)):
            if i == len(values) - 1:
                walker.addChild(TrieNode(values[i],True,weight))
            else:
                walker.addChild(TrieNode(values[i]))
                walker = walker.getChild(values[i])

    #check whether the input is within the tree 
    #isSubString - whether the input can be contained within the trie as a substring or not 
        #eg: "App"/"Apple" vs "App"/"App"
    #returns either None (not found / not valid) or the final Node (eg: "Appl[e]")
    def search(self,input,isSubString=True):
        walker = self.headNode
        if walker.value != input[0]:
            return None
        for i in range(1, len(input)):
            walker = walker.getChild(input[i])
            #not found at all
            if walker == None:
                return None
        #result is a substring, and not accepted
        if walker.isEnd == False and isSubString == False:
            return None
        return walker

    #used below, DFS
    def dfsNode(self,node,results,prefix):
        #add the nodes value to the current string/path (eg: "App" + "l")
        prefix += node.value
        if node.isEnd:
            #end the current string/path, adds the weight value, and starts a new one
            results.append([prefix,node.weight])
        for childKey in sorted(node.children.keys()):
            self.dfsNode(node.getChild(childKey),results,prefix)
        return

    #gets all possible full strings from a node
        #eg: Trie("Apple", "Apples") "Ap[p]" returns [["Apple",(weight)],["Apples",(weight)]]
    #prefix - a prefix that is added to all of the results 
        #eg: "Ap" + [p] -> "App..."
    def extractFromNode(self, node, prefix=""):
        results = []
        self.dfsNode(node,results,prefix)
        return results

    def __str__(self):
        return str(self.extractFromNode(self.headNode))