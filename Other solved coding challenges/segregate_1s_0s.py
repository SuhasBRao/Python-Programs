n = int(input())
arr = list(map(int,input().split()))
zrs = []
ones = []
for ele in arr:
    if ele == 0: zrs.append(ele)
    if ele == 1: ones.append(ele)
#print(*[zrs + ones])
arr = zrs+ones
for i in arr:
    print(i,end=' ')