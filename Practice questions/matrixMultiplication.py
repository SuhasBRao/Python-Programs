'''
N matrices have to be multiplied M0, M1, M2, ...Mn-1. 
Write a function to compute the minimum number of 
multiplications needed to multiply the chain.


Input Format:

A number in the first line indicating the total number of matrices (N)

Next N lines has row and column count of each matrix separated by a space.

Output Format:

The minimum number of multiplications to compute the chain multiplication
'''
n = int(input())
arr = []
for i in range(n):
	arr.append(list(map(int,input().split())))

#print(arr)
def calc(arr):
	#print(arr)
	if len(arr) == 1:
		return 0
	else:
		vals = arr[0][1]*arr[1][1]*arr[0][0]
		nw_ele = [arr[0][0],arr[1][1]]
		
		arr.pop(1)
		
		arr[0] = nw_ele
		
		return vals + calc(arr)
print(calc(arr))

 