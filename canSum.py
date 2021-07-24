'''
The program checks whether the given targetSum can be generated by the
elements of given array.
'''
def canSum(target, arr,ispos = {}):
    if target in ispos:
        return ispos[target]
    if target == 0:
        return True
    if target in arr:
        return True
    else:
        for val in arr:
            nw_targt = target - val
            if nw_targt < 0:
                return False
            
            ispos[target] = canSum(nw_targt,arr,ispos)
        #print(ispos)
        return any(ispos.values())
    
if __name__ =="__main__":
    print(canSum(7,[2,3]))