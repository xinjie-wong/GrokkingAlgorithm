# details:
# requires a sorted list
# returns the position of the item if found
# returns None if the item doesn't exist
# utilises low, middle and high index
# run time = O(log n)

def binary_search(arr, item):
    arr.sort()    # sort the data in the array
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
lst = [1, 9, 3, 7, 4]
print(binary_search(lst, 7))

    
