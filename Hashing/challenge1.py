def isSubset(list1,list2):
    a=set(list1)
    b=set(list2)

    print a
    print b
    print len(a)
    print len(b)

    c = set(list1+list2)
    print c
    print len(c)
    if len(a)==len(c):
        return True
    else:
        return False

list1 = [9,4,7,1,-2,6,5]
list2 = [7,1,-2] #True
#list2 = [7,1,2] #False
m=isSubset(list1,list2)
print m