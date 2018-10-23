# Assignment 6 part 7
import random
def how_many(dic):
    nbofitems = 0
    for (i,j) in dic.items():
        if isinstance(j,list):
            nbofitems += len(j)
        else:
            nbofitems +=1
            
    return nbofitems

def biggest(d):
    variable = d.values()
    best = max(variable, key = len)
    key = []
    for k in d:
        if len(d[k]) == len(best):
           
           key.append(k) 
    random.shuffle(key)
    return key[0]
def dstats(d):
    x = biggest(d)
    return (how_many(d),len(d[x]))

animals = { 'a': ['horse'], 'b': ['baboon'], 'c': ['giraffe']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
print(dstats(animals))

