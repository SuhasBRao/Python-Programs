
import math
import os
import random
import re
import sys

#
# Complete the 'designerPdfViewer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h
#  2. STRING word
#

def designerPdfViewer(h, word):
    # Write your code here
    mylist = ['a','b','c','d','e','f','g','h','i',
              'j','k','l','m','n','o','p','q','r',
              's','t','u','v','w','x','y','z']
    
    letterHeights = dict(zip(mylist,h))
    
    tallest = max([letterHeights[x] for x in word])
    return tallest*len(word)
    
    pass

if __name__ == '__main__':
    
    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    print(result)