'''
Consecutive four:
Given a m x n matrix inmatrix of positive integers, 
print an integer outnum based on the below logic.



•Identify all possible sets in inmatrix 
that contain at least four consecutive elements 
of the same value val, either horizontally, vertically, or diagonally

•If only one set of consecutive 
elements is identified, store the 
value val in outnum

•If more than one set of consecutive 
elements is identified, find the smallest 
value and store it in outnum

•If no set of four consecutive elements of 
the same value is identified either 
horizontally, vertically, or diagonally, print-1



Assumption:

•m and n wille be greater than 3

Input format:

First line will contain number of rows m of inmatrix

The next m lines will contain the elements of inmatrix. Each line will have n elements separated by space.

Read the input from the standard input stream.

Output format:

Print outnum to the standard output stream.

Example 1

Sample input:

5        

0 1 6 8 8 9

5 6 1 6 8 9

6 5 6 1 1 9

1 6 6 1 1 9

6 3 3 3 3 9



Sample output:

1

Explanation:

Following elements are present consecutively at least four 
times: Element 3 horizontally in the 5th row. 
Element 1 diagonally starting from the 2nd column in the first row. 
Element 6 diagonally starting from the 4th column in the second row.
 Element 9 vertically in the 6th column. 
 As element 1 is the smallest value of the four identified 
 sets of consecutive values, the output is 1.


Example 2

Sample input:

5

0 1 6 8 6 0

5 5 2 1 8 2

6 5 6 1 1 9

1 5 6 1 4 0

3 7 3 3 4 0



Sample output:

-1


Explanation:

Here there are no sets of four consecutive elements of the 
same value either horizontally, vertically, or diagonally. 
Hence the output is-1


'''

m = int(input())
arr = []
for i in range(m):
	arr.append(list(map(int,input().split())))
#print(matrix)
result = []
n = len(arr[0])
for i in range(m):
	for j in range(n):
		if j < n-3:
			if arr[i][j] == arr[i][j+1] == arr[i][j+2] == arr[i][j+3]:
				result.append(arr[i][j])
		if i < m-3:
			if arr[i][j] == arr[i+1][j] == arr[i+2][j] == arr[i+3][j]:
				result.append(arr[i][j])
		if i > m-3 and j<n-3:
			if arr[i][j] == arr[i-1][j+1] == arr[i-2][j+2] == arr[i-3][j+3]:
				result.append(arr[i][j])
		if i > m-3 and j > n-3:
			if arr[i][j] == arr[i-1][j-1] == arr[i-2][j-2]== arr[i-3][j-3]:
				result.append(arr[i][j])
if result:
	print(min(result))
else:
	print(-1)