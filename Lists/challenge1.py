def removeEven(myList):
    newL = []
    for i in myList:
        if i%2 !=0:
            newL.append(i)
    return newL

myList = [1,2,3,4,5,8,7,9]
print (removeEven(myList))