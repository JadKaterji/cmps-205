# Assignment 6 part 4

def flatten(lst):
    if lst == []:
        return lst
    elif isinstance(lst[0], list):
        return flatten(lst[0]) + flatten(lst[1 : len(lst)])
    else:
        return [lst[0]] + flatten(lst[1 : len(lst)])




def different(t):
    entries = flatten(t)        #flattens the list of lists, which constructs one list containing all elements of the table given
    distinct_elements = []
    for i in range(len(entries)):
        for j in distinct_elements:
            if entries[i] != distinct_elements:
                distinct_elements.append(entries[i])
    return(distinct_elements)
print(different([[32,12,52,63],[32,64,67,52],[64,64,17,34],[34,17,76,98]]))

