'''
This program implements a quick sort(recursive).
'''

def quick_Sort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    left_sub_array = [] # will hold elements less than pivot
    right_sub_array = [] # will hold elements greater than pivot
    
    for ele in arr:
        if ele > pivot: right_sub_array.append(ele)
        elif ele < pivot: left_sub_array.append(ele)
    
    return quick_Sort(left_sub_array) + [pivot] + quick_Sort(right_sub_array)
    
    
if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print(quick_Sort(arr))