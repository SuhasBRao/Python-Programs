'''
The below program implements brute force algorithms for string matching.
A sequce of charater will be given in TEXT with size n.
and another sequence PATTERN with size m, will be given.
The task is to find PATTERN in TEXT.
Although python has inbuilt function .find to find a substring 
in a given string we will use brute force approch to find the substring.
'''
from sys import stdin,stdout

def getInts():
    return stdin.readline().strip()

def find_Pattern(text,pattern):

    m = len(pattern)
    count = 0
    for item1 in text:
        for item2 in pattern:            
            if item1 == item2:
                count += 1

        if count == m:
            return text.index(item1)
        if count  < 1:
            count = 0
    return -1

text = getInts()
pattern = getInts()

result_indx = find_Pattern(text,pattern)
print(f'The pattern starts at the index {result_indx}')