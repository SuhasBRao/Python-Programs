'''
Given two strings, find out the minimum 
number of operations required to convert 
string 1 to string 2. The operations allowed 
are Insert/Delete/Replace a character.

Sample Input:

string 1: hello

string 2: hllo

Sample Output:

1

'''
a = input()
target = input()
def minOpr(a,target,n,m):
	if n<0 or m<0:
		return 0
	if a == target: return 0
	if a == '': return m
	if target == '': return n
	if a[n] == target[m]: return minOpr(a,target,n-1,m-1)
	return 1 + min(minOpr(a,target,n,m-1), minOpr(a,target,n-1,m), 
				   minOpr(a,target,n-1,m-1))

print(minOpr(a,target,len(a) - 1, len(target) -1))