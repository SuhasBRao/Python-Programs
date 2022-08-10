'''
A program to calculate sum of elements of an array using Divide and Conquer (D&C)
Strategy.
A D&C algorithm has two steps,
[1] Find a base case.
[2] Reduce the problem to get near to the base case.
'''
from sys import stdin

def readInput():
    return list(map(int, stdin.readline().split()))

def sumOfElements(anArray):
    # Here the base case is if array is empty then 
    # we return 0 as its sum.
    # Alternatively, we can also check if the array
    # has only one element as base case and return that
    # element as sum
    if anArray == []:
        return 0
    
    return anArray[0] + sumOfElements(anArray[1:])
    

# {
# Driver Code starts
if __name__ == "__main__":
    # write your code here
    anArray = readInput()
    
    #print(anArray)
    
    print(sumOfElements(anArray))

# } Driver Code ends
