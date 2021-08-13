def binSort(self, A, N): 
        #Your code here
        #No need to print the array
        left, right = 0,N -1
        while left<right:
            while left<right and A[left] == 0:
                left += 1
            while left<right and A[right] == 1:
                right -= 1
            if left<right:
                A[left]= 0
                A[right] = 1
                right-= 1
                left+=1
        return A