#User function Template for python3

def isSubset( a1, a2, n, m):
    b_map = dict()
    for i in range(0,n):
        b_map[a1[i]] =1
    
    for i in range(0,m):
        if a2[i] not in b_map.keys():
            return False
    return True
    


#{ 
#  Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m = sz[0], sz[1]
        a1 = [int(x) for x in input().strip().split()]
        a2 = [int(x) for x in input().strip().split()]
        
        print(isSubset( a1, a2, n, m))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends