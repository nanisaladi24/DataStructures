def tracePath(map):
    #print map
    #print list(map)
    my_dict = dict(map)
    print my_dict
    src = set(my_dict.keys())
    dest = set(my_dict.values())
    print src
    print dest

    mySrc = src-dest
    mySrc = list(mySrc)[0]
    print mySrc

    myDest = dest-src
    myDest = list(myDest)[0]
    print myDest

    currSrc = mySrc

    result = []
    while(1):
        result.append([currSrc,my_dict.get(currSrc)])
        currSrc = my_dict.get(currSrc)
        if currSrc == myDest:
            break

    return result

map = {
    "NYC": "CHG",
    "BST": "TXS",
    "MSR": "NYC",
    "TXS": "MSR"
}
myRes = tracePath(map)
print myRes
