'''
Function to generate prime numbrs less than a given number n
'''
from sys import stdin,stdout
N = int(stdin.readline())

def is_it_prime(num):
    # This function checks if a number is prime or not
    if num < 2:
        return False
    for i in range(2,num):
        if num%i == 0:
            return False
    return True

def generate_prime(n):
    # the funciton genrates prime numbrs less than n
    # using is_it_prime() function defined above
    for i in range(1,n + 1):
        val = is_it_prime(i)
        if val == True:
            stdout.writelines(str(i) + ' ')

generate_prime(N)