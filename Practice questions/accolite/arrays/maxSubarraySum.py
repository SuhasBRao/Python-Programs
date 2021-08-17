arr = list(map(int,input().split()))
#print(maxSubarray(arr, len(arr) - 1))

global_max = 0
local_max = 0
memo ={}
for i in range(len(arr)):
    local_max = max(arr[i], arr[i] + local_max)
    global_max = max(global_max, local_max)

print(global_max)