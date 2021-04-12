'''
The below program implements brute force algorithms for string matching.
A sequce of charater will be given in TEXT with size n.
and another sequence PATTERN with size m, will be given.
The task is to find PATTERN in TEXT.
'''
from sys import stdin,stdout

def getInts():
    return stdin.readline().strip()

def find_Pattern(text,pattern):
    n = len(text)
    m = len(pattern)

    for i in range(n - m + 1):
        j = 0
        while j < m and pattern[j] == text[i + j]: # the loop checks for the patterns
            #print(pattern[j],text[i+j])
            j = j + 1
        
        if j == m:
            #print('y')
            return i
            
    return -1       # return -1 if the pattern is not found

text = getInts()
pattern = getInts()

result_indx = find_Pattern(text,pattern)
print(f'The pattern starts at the index {result_indx}')