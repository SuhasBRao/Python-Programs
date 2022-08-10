'''
Function to generate prime numbrs less than a given number n.
'''
from sys import stdin,stdout
from math import sqrt
N = int(stdin.readline())

def is_it_prime(num):
    # This function checks if a number is prime or not
    # has O(n) complexity.
    if num < 2:
        return False
    for i in range(2,num):
        if num%i == 0:
            return False
    return True

def is_prime(num):
    # This function checks if a number is prime or not
    # This has O(sqrt(n)) complexity.
    if num < 2:
        return False
    for item in range(2,int(sqrt(num))):
        if num % item == 0:
            return False 
    return True

def generate_prime(n):
    # the funciton genrates prime numbrs less than n
    # using is_it_prime() function defined above
    for i in range(1,n + 1):
        val = is_it_prime(i)
        val_1 = is_prime(i)
        if (val == True) and (val_1 == True):
            stdout.writelines(str(i) + ' ')
            stdout.writelines(str(i) + ' ')
            print()

generate_prime(N)