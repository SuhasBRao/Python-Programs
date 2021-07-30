#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrCount function below.
def substrCount(n, s):
    
    noSpecialString = n
    no = lambda i: n - i - 1
    if s==s[::-1]:
        temp = [no(i) for i in range(n-1)]
        noSpecialString += sum(temp)
        #print(noSpecialString)
    else:
        isSpecial = lambda i: 1 if (s[i] == s[i+1]) or (s[i]== s[i+2]) else 0
        
        #temp = [1 for i in range(n-1) if isSpecial(i)]
        lst = [i for i in range(n-2)]
        #print(lst)
        temp = list(map(isSpecial,lst))
        
        noSpecialString += sum(temp)
        #print(temp)
        #noSpecialString += 1 if s[-2] == s[-1] else noSpecialString
        #print(sum(temp))
    '''
    for i in range(n-1):
        
            cur = s[i]
            try:
                if s[i+1] and s[i+2]:
                    if cur == s[i+1]: noSpecialString +=1
                    elif cur== s[i+2]: noSpecialString += 1
            except:
                if s[i+1] and cur==s[i+1]: noSpecialString +=1
            
    '''
    
   
    
    return noSpecialString   
    #print(noSpecialString)
    #pass
    

if __name__ == '__main__':
    n = int(input())

    s = input()

    result = substrCount(n, s)
    print(result)
    