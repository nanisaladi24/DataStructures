def findSumZero(my_list):
    hMap = dict()
    my_sum = 0

    for i in range(len(my_list)):
        my_sum += my_list[i]
        if my_list[i]==0 or my_sum == 0 or hMap.get(my_sum)!=None:
            return True
        hMap[my_sum] = i
    return False

#my_list = [6,4,-7,2,12,9] #False
my_list = [6,4,-7,3,12,9] #True
print findSumZero(my_list)