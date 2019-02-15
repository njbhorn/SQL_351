myList = ["apple", "banana", "cherry"]
myTuple = ("banana", "cherry", "apple")
mySet = {"banana", "cherry", "apple"}
myDict = {
    "breakfast" : "banana",
    "lunch" :  "cherry",
    "dinner" : "apple"
    }
myDict2 = {
    10 : "banana",
    20 :  "cherry",
    30 : "apple"
    }
myList.append("orange")
if "apple" in myList:
    print ("Yes Apple in List!")
for x in myList:
    print (x)
print (myTuple[1])
mySet.add("Orange")
print (mySet)
print (myDict)
print (myDict["breakfast"])
print ( myDict2[30])
for fruit in myDict2 :
    print(fruit, myDict2[fruit])
for fruit in myDict2.values() :
    print(fruit)
for fruit in myDict2.items() :
    print(fruit)
myDict2[40] = "grape"
for x in myDict2.items():
    print (x)
