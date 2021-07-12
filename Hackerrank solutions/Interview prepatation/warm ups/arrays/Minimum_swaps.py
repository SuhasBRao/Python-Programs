a = [4,3,1,2]
'''
Solution is copied from discussions
'''
#a = [7, 1, 3, 2, 4, 5, 6]
#3a = [2, 3, 4, 1, 5]
#a = [1, 3, 5, 2, 4, 6, 7]
#nd = dict(zip(a, range(1,len(a) +1)))


def minimumSwaps(arr): 
    #initialize number of swaps as 0 
    swaps = 0
    #create a dictionary which holds value, index pairs of our array
    #[4,3,1,2] --> {4: 1, 3: 2, 1: 3, 2: 4}
    getIndex = dict(zip(arr,range(1,len(arr)+1)))
    for i in range(1,len(arr)+1):
        #swap only if value is not equal to index
        if getIndex[i]!=i: 
            """
            Example of a proper swap when i=1
            {4: 1, 3: 2, 1: 3, 2: 4} --> {4: 3, 3: 2, 1: 1, 2: 4}
            [4,3,1,2] --> [1,3,4,2]
            Full swap is not required i.e. we don't have to set 1:1 or arr[0]=1(i:i or arr[i-1]=i) because we will never use these two values again. Therefore we can keep these two values as it is. And thus our swap looks as follows.
            {4: 1, 3: 2, 1: 3, 2: 4} --> {4: 3, 3: 2, 1: 3, 2: 4}
            [4,3,1,2] --> [4,3,4,2]
            """
            getIndex[arr[i-1]]=getIndex[i]
            arr[getIndex[i]-1]=arr[i-1]

            print(getIndex)
            swaps+=1
    return swaps
    
        

print(minimumSwaps(a))
