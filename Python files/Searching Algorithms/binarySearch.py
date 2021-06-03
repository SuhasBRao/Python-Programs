"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    """Your code goes here."""
    frst_indx = 0
    last_indx = len(input_array) - 1
    mid_indx = (frst_indx + last_indx)//2
    val_indx = -1
    
    while frst_indx <= last_indx:
        if value > input_array[mid_indx]:
            frst_indx = mid_indx + 1
            
        if value < input_array[mid_indx]:
            last_indx = mid_indx - 1
        
        if value == input_array[mid_indx]:
            
            val_indx = mid_indx
            break
            
        mid_indx = (frst_indx + last_indx)//2
        #print(mid_indx)
        #print('\n')

    return val_indx    


test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))