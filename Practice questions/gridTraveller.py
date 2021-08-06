'''
Implements a grid traveller problem to move from 0*0 to m-1*n-1 
in a grid where the user can move either right or down
'''
def gT(m,n, memo = {}):
    if m == 0 or n == 0:
        return 0
    if m == 1 and n == 1:
        return 1
    if (m,n) in memo:
        return memo[(m,n)]
    else:
        memo[(m,n)] = gT(m-1, n) + gT(n-1,m)
    return memo[(m,n)]

m,n = list(map(int,input().split()))
print(gT(m,n))