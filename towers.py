# Assignment 6 part 2

def towers(orig,dest,aux,n):
    if n == 1:
        return (orig,dest)
    else:
        return [towers(orig,aux,dest,n-1),towers(orig,dest,aux,1), towers(aux,dest,orig,n-1)]

# In the question, the output will not reach the destination, but instead reach the auxiliary. Here, the destination will be reached.
print(towers('A', 'C', 'B', 3))