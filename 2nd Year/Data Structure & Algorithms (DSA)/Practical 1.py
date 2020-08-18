from math import floor

def binary_search(Array, Search_Term):
    n = len(Array)
    L = 0
    R = n-1
    
    while L <= R:
        mid = floor((L+R)/2)
        if Array[mid] < Search_Term:
            L = mid + 1
        elif Array[mid] > Search_Term:
            R = mid - 1
        else:
            return mid
    return -1

x = int(input("Number of elements:"))
myList = []
for a in range(x):
    number = int(input("Enter Element: "))
    myList.append(number)
print("Elements in List :", myList)

element=int(input("Element to be searched:"))
index = binary_search(myList, element)
if index >= 0:
    print( "Element " + str(element) + " is found at index %d" %(index))
    print( "Element " + str(element) + " is found at position %d" %(index+1))
else:
    print("Search element not found")
    