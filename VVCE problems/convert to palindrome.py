s = input()

ori = s
if s == s[::-1]:
    print('Null')
else:
    i = 0
    while True:
        i += 1
        if s == s[::-1]:
            break
        s = s[i+1:]
        
    print(ori[i-1::-1])