def findPair(my_list):
    my_dict = dict()
    for a in range(len(my_list)):
        for b in range(a+1,len(my_list)):
            i=my_list[a]
            j=my_list[b]
            my_sum = i+j
            if my_dict.get(my_sum) !=None:
                return [my_dict.get(my_sum),[i,j]]
            else:
                my_dict[my_sum] = [i,j]
    return []

my_list = [3,4,7,1,12,9]
result = findPair(my_list)
print result