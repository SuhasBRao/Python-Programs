'''
A program to find sum of digits of a given number
'''
from sys import stdin,stdout

number = int(stdin.readline())
sumx = 0
while number > 0:
    rem = int(number%10)
    sumx += rem
    number = number/10
print(sumx)