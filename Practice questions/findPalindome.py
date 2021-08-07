'''
For gien positive number num, identify the palindrome
formed by performing the following operations;-
- Add 'num' and its reverse.
- check if the sum is palindrome or not. if not, add
the sum and its reverse and repeat the proces until a palindrome is 
obtained.

Input 1:
124
Output 1:
545

input 2:
4
output 2:
8
'''
n = int(input())

def findPalindrome(n):
    sm = str(n + int((str(n)[::-1])))
    if sm == sm[::-1]:
        return sm
    else:
        return findPalindrome(int(sm))
print(findPalindrome(n))