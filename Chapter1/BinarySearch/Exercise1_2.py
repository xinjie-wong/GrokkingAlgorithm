# Exercise 1.1
# Suppose you have a sorted list of 128 names, and you're searching through it using a binary search.
# What's the maximum number of steps it would take?

# maximum number of steps = log2 128
#                         = log2 2^7
#                         = 7

# Exercise 1.2
# Suppose you double the size of the list.
# What's the maximum number of steps now?

# size = 256
# maximum number of steps = log2 256
#                         = log2 2^8
#                         = 8

def binary_search(arr, item):
    arr.sort()    # sort the data in the array
    print('Sorted list: ', arr)
    low = 0
    high = len(arr) -1

    while low <= high:
        mid = (low + high) // 2   # floor division to return integer as Python 3 will return float in default
        if arr[mid] == item:
            return mid
        elif arr[mid] < item:
            low = mid + 1
        else:
            high = mid - 1
    else:
        return None
    
#testing the binary search function
lst = ['Xin Jie', 'Joseph', 'Annabelle', 'Jane', 'Zoey']
print(binary_search(lst, 'Jane'))  
print(binary_search(lst, 'Zack'))  
