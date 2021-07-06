import math
import os
import random
import re
import sys
import numpy as np

def add(x,k):
    return x + k

def arrayManipulation(n, queries):

    arr = [0]*n
    
    q = iter(queries)
    Done = False
    for q in queries:
        #print(next(q))
        a, b, k = q
        indxs = iter(range(a - 1,b))
        #print(a,b,k)
        D = False
        while not D:
            try:
                    #print(next(indxs))
                arr[next(indxs)] += k
            except:
                D = True
            
            #print('##########')
        
    return max(arr)

    '''for q in queries:
        a,b,k = q
        x = lambda n: n + k

        #arr[a-1 : b] = map(x,arr[a-1:b])

    print(arr)
    return max(arr)'''


def getINputs(line):
    return list(map(int, line.split()))

if __name__ == '__main__':
    
    #n,m = getINputs()
    queries = []
    '''
    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)
    print(result)
    '''
    with open('inpt.txt', 'r') as file:
        input_lines = [line.strip() for line in file]
    
    #print(input_lines)
    n,m = getINputs(input_lines[0])
    
    for q in input_lines[1:]:
        queries.append(getINputs(q))

    print(len(queries))

    print(arrayManipulation(n,queries)) 
