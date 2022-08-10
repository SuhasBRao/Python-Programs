name = input()
identifier = int(input())

n = 26

indx = ord(name) - 97

cnt = 0

while cnt < identifier:
    indx += 1
    cnt += 1
   
indx = indx%n
    
if name.islower():
    # print(arr[indx])
    print(chr(indx + 97))
else:
    # print(arr[indx].upper())
    print(chr(indx + 97).upper())