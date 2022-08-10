arr = list(input().split())
occ = []
for i in arr:
    if i not in occ:
        occ.append(i)
        print(i, arr.count(i))
#print(*list(set(arr)))    