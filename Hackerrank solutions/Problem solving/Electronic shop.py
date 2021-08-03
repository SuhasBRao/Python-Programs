
import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.
    #

    possible = [x + y for x in keyboards for y in drives]
    within_budget = [x for x in possible if x<=b]
    #print(possible)
    #print(within_budget)
    if within_budget:
        return max(within_budget)
    else:
        return -1
    pass
if __name__ == '__main__':
    
    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    print(moneySpent)