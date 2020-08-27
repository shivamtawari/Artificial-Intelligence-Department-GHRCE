def linear_search(myList,item):
    for i in range(len(myList)):
        if myList[i]==item:
            return i
    return -1

n = int(input("Number of elements:"))
myList = []
for a in range(n):
    number = int(input("Enter Element: "))
    myList.append(number)
print("Elements in List :", myList)

x = int(input("Enter element to be Searched: "))

result = linear_search(myList,x)
if result==-1:
     print("Element not found in the list")
else:
     print( "Element " + str(x) + " is found at index %d" %(result))
     print( "Element " + str(x) + " is found at position %d" %(result+1))