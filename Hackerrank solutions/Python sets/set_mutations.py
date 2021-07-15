no_elements = int(input())
A = set(map(int,input().split()))
N = int(input())

for i in range(N):
    val, no_el = input().split()
    print(val, no_el)
    temp_set = set(map(int,input().split()))
    if val == 'intersection_update':
        A.intersection_update(temp_set)
        
    elif val == 'update':
        A.update(temp_set)
        
    elif val == 'symmetric_difference_update':
        A.symmetric_difference_update(temp_set)
        
    elif val == 'difference_update':
        A.difference_update(temp_set)

print(sum(A))
    