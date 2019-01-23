def findSymmetric(my_list):

    dictionary = dict()
    result = []

    for i in range(len(my_list)):
        first = my_list[i][0]
        second = my_list[i][1]
        #print first
        #print second

        if (first in dictionary.keys()) and (second not in dictionary.keys()):
            dictionary[first].append(second)
            continue

        value = dictionary.get(second)
        if value==None:
            pass

        elif first in value:
            value = first
        else:
            value = value[0]

        if (value != None and value == first):
            result.append([second,first])
            result.append([first,second])
            continue

        elif (value != None):
            #print ("hi")
            dictionary[second].append(first)
            continue
        elif value == None:
            m=[second]
            dictionary[first] = m
            #print dictionary
            continue

    #print dictionary
    #print dictionary.keys()
    #print result
    return result

my_list=[[1,2], [1,3], [3,1], [2,1], [2,3], [3,4],[5,9],[4,3], [3,2], [9,5]]
#findSymmetric(my_list)
symmetric = findSymmetric(my_list)
print symmetric