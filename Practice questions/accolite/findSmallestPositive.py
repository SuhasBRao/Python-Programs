def segregate(arr, size):
    j = 0
    for i in range(size):
        if (arr[i] <= 0):
            arr[i], arr[j] = arr[j], arr[i]
            j += 1 # increment count of non-positive integers
    return j

def findMissingPositive(arr, size):
     
    # Mark arr[i] as visited by
    # making arr[arr[i] - 1] negative.
    # Note that 1 is subtracted
    # because index start
    # from 0 and positive numbers start from 1
    for i in range(size):
        if (abs(arr[i]) - 1 < size and arr[abs(arr[i]) - 1] > 0):
            arr[abs(arr[i]) - 1] = -arr[abs(arr[i]) - 1]
             
    # Return the first index value at which is positive
    for i in range(size):
        if (arr[i] > 0):
             
            # 1 is added because indexes start from 0
            return i + 1
    return size + 1

def findMissing(arr, size):
     
    # First separate positive and negative numbers
    shift = segregate(arr, size)
     
    # Shift the array and call findMissingPositive for
    # positive part
    return findMissingPositive(arr[shift:], size - shift)

arr = list(map(int, input().split()))
print(findMissing(arr,len(arr)))
