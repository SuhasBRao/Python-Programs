from itertools import permutations
from sys import stdin

def getInputs():
    # pass
    return list(stdin.readline().split())

def find_permutations(s, r):
    # pass
    result = list(permutations(s, r))
    for p in result:
        print(''.join(p))

# {
# Driver Code starts
if __name__ == "__main__":
    # write your code here
    input_str, r = getInputs()
    
    find_permutations(input_str, int(r))
    

# } Driver Code ends