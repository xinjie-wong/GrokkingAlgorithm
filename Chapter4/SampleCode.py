# Quicksort

def quicksort(arr):
    if len(arr) < 2:    # base case
        return arr      # nothing to sort
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
    
# tester
arr = [1,7,2,5,3,9,11]
print(quicksort(arr))