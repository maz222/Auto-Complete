from Driver import Driver

testDriver = Driver()

#testing adding strings
print("-adding strings-")
strings = ["apple", "bannana", "carrot", "advertisement", "ball", "condor"]
#strings = ["Ard","Ardvark","Ardva"]
for i in range(len(strings)):
	testDriver.addString(strings[i],i)
print(testDriver)

#testing deleting strings
print("-deleting strings-")
testDriver.deleteString("advertisement")
print(testDriver)

#testing adding / setting weights
print("-changing weights-")
testDriver.addWeight("bannana",5)
print(testDriver.search("bannana"))
testDriver.setWeight("bannana",12)
print(testDriver.search("bannana"))

print("\n-searching-")
#search - results sorted alphabetically (default)
print(testDriver.search("c"))
#search - results sorted by weight
print(testDriver.search("b", True))