def mergeArrays(L1,L2):
    L3 = []
    i=0
    j=0
    while (i<len(L1) or j<len(L2)): 
        if i<len(L1) and j<len(L2):
            if L1[i]<L2[j]:
                L3.append(L1[i])
                i=i+1
            elif L2[j]<L1[i]:
                L3.append(L2[j])
                j=j+1
            else:
                L3.append(L1[i])
                i=i+1
        elif i==len(L1):
            L3.append(L2[j])
            j=j+1
        elif j==len(L2):
            L3.append(L1[i])
            i=i+1
    return L3

arr1 = [1,3,4,5]  
arr2 = [2,6,7,8]
print (mergeArrays(arr1,arr2))
