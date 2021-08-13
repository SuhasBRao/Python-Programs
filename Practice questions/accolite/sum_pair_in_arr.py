def hasArrayTwoCandidates(arr,x):
		# code here
        s = set()
        for i in range(len(arr)):
            temp = x - arr[i]
            if temp in s:
                return True
            s.add(arr[i])
        return False
        
x = int(input())
arr = list(map(int,input().split()))


print(hasArrayTwoCandidates(arr,x))