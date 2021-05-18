from sys import stdin,stdout
def getInputs():
    return list((map(int,stdin.readline().strip().split())))

def get_strings():
    return stdin.readline().strip()

N,M = getInputs()
arr = []
my_str = ''
#lambda x : x.isalpahnum()

#print(arr)

for i in range(N):
    #for j in range(M):
    tmp = input()
    #print(tmp)
    
    temp = [x for x in tmp]
    arr.append(temp)

print(arr)
temp = ''
for i in range(M):
    for j in range(N):
#        print(j,i)
        #print(arr[j][i])
        item = arr[j][i]
        temp = temp + item
        item = (' ',item)[item.isalnum()]
        
        my_str = ((my_str, my_str + item)[item.isalnum() or item == ' '])

print(my_str)
print(temp)
