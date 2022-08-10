arr = list(map(int,input()))

while len(arr) != 1:
    val = str(sum(arr))
    arr = list(map(int,val))

print(arr[0])