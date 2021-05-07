'''
This program contains my solution for the hackerrank problem on sets
Problem statement - https://www.hackerrank.com/challenges/symmetric-difference/problem
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT

from sys import stdin,stdout

def getInputs():
    return list(map(int,stdin.readline().strip().split()))

M = int(input())
my_arr1 = set(getInputs())
N = int(input())
my_arr2 = set(getInputs())

diff = my_arr2.union(my_arr1) - my_arr2.intersection(my_arr1)
diff = sorted(list(diff))
print(*diff,sep = '\n')
##########################
#print("\n".join(map(str,diff))) ### Can also print it using this statement