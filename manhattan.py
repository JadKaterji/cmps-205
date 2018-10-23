# Assignment 6 part 6
import random
def manhattan(rows,columns):
    lst = []    
    for i in range(rows):
        lst.append([0]*columns)
    x = rows//2 
    y = columns//2
    for nbofmovements in range(random.randint(0,10)):
        for j in range(random.randint(0,4)):
            if j == 0:
                print('upward')
                lst[x-1][y] += 1
                x -= 1
            elif j == 1:
                print('downward')
                lst[x+1][y] += 1
                x += 1
            elif j == 2:
                print('right')
                lst[x][y+1] += 1
                y += 1
            else:
                print('left')
                lst[x][y-1] += 1
                y -= 1
    for row in lst:
        print(row)
manhattan(5,11)