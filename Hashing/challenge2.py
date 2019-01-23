def isDisjoint(list1,list2):
    a=set(list1)
    b=set(list2)

    print a
    print b
    print len(a)
    print len(b)

    c = set(list1+list2)
    print c
    print len(c)
    if (len(a)+len(b))==len(c):
        return True
    else:
        return False

list1 = [9,4,7,1,-2,6,5]
#list2 = [7,1,-2] #False
list2 = [11,12,3] #True
m=isDisjoint(list1,list2)
print m