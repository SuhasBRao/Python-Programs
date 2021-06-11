'''
Problem-statement -> https://www.hackerrank.com/challenges/word-order/problem
'''

from collections import OrderedDict
N = int(input())
words = OrderedDict()
unique_inpts = 0
for _ in range(N):
    word_input = input()
    try:
        words[word_input] += 1
    except:
        words[word_input] = 1
        unique_inpts += 1
print(unique_inpts)
print(*words.values())

    