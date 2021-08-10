def hcf(a,b):
    small, big = {True:(a,b),False:(b,a)} [a<b]
    rem = big%small
    if rem == 0: return small
    else:return hcf(small,rem)
    
if __name__ =="__main__":

    print(hcf(60,72)) # finds the hcf of the passed arguments