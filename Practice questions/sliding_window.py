'''
Sliding window Problem
'''
arr = list(map(int,input().split()))
k = int(input())
for i in range(len(arr)-k +1):
    #print(i)
    #print(arr[i:i+k])
    max_in_range = max(arr[i:i+k])
    print(max_in_range,end=' ')

#8 5 10 7 9 4 15 12 90 13