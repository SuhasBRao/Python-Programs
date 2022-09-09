'''
how the target sum can be generated.
'''
def howSum(target, arr,ispos = {}):
    if target < 0: return None
    if target == 0: return []
    
    shortest_res = None

    for val in arr:
        rem = target -val
        remainder_combination = howSum(rem, arr, ispos)
        #print(remainder_combination)
        if remainder_combination != None:
            remainder_combination.append(val)

            if shortest_res == None or len(remainder_combination)< len(shortest_res):
                shortest_res = remainder_combination
        
        #print(ispos)
    return shortest_res
    
if __name__ =="__main__":
    #print(howSum(120,[3,4,100]))
    print(howSum(9,[3,4,100]))
    print(howSum(20,[3,4,100]))