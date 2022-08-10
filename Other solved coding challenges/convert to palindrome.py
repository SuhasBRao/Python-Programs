
def convertPalindrome(s):
    ori = s
    if s == s[::-1]:
        #print('NULL')
        return 0
    else:
        i = 0
        while True:
            s = ori[i:]

            if i >= len(ori):
                #print(ori[i-1::-1])
                return ori[i-1::-1]
                #break

            if s == s[::-1]:
                indx = len(ori) - len(s)
                #print(ori[indx - 1::-1])
                return len(ori[indx - 1::-1])
                #break

            i += 1

if __name__ == "__main__":
    s = input()

    print(convertPalindrome(s))
    