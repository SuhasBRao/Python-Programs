# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
from sys import stdin

def getInputs():
    return list(map(int, stdin.readline().strip().split()))
    

def cartesian_product(A,B):
    result = sorted(list(product(A,B)))
    for pair in result:
        print(pair, end=' ')

# {
# Driver Code starts
if __name__ == "__main__":
    # write your code here
    A = getInputs()
    B = getInputs()
    cartesian_product(A,B)

# } Driver Code ends