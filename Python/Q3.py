#Q3
def listToset(listIn):
    mySet = []
    for num in listIn:
        if num not in mySet:
            mySet.append(num)
    
    return mySet

myList = [12,23,43,3,2,2,3,1,2,3,3,2]

mySet = listToset(myList)

print(mySet)
