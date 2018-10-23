# Assginment 6 part 5

# def pascal(n):
#     if n==0:
#         return [1]
#     else:
#         p = pascal(n-1)

#         lst = []
#         lst.append(1)
#         for 

def generate_pascal(n):    
    lst = []
    for i in range(n+1):
        if i == 0:
            lst.append([1])
        else:
            row = [1]
            prevs = lst[i-1]
            for j in range(len(prevs)-1):
                row.append(prevs[j]+prevs[j+1])
            row.append(1)
            lst.append(row)
    return(lst)

def print_triangle(coeffs):
    x = generate_pascal(coeffs)
    for i in x:
        for j in i:
            print(j,end = ' ')
        print()
           

print_triangle(7)
