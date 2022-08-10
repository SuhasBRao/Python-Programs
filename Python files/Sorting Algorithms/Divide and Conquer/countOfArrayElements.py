'''
Program to count the number of Elements in an array using D&C strategy.
This is similary to SumOfArrayElements.py but here we count the number 
of elements in array.
'''

from sys import stdin

def readInput():
    return list(map(int, stdin.readline().split()))

def countNumberOfElements(anArray):
    if anArray == []:
        return 0
    
    return 1 + countNumberOfElements(anArray[1:])
    

# {
# Driver Code starts
if __name__ == "__main__":
    # write your code here
    anArray = readInput()
    
    print(countNumberOfElements(anArray))

# } Driver Code ends