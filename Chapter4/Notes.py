# divide-and-conquer:
# recursive algorithm
# figure out the base case
# reduce the problem and get to the base case

# quicksort:
# faster than selection sort
# steps:
# 1. select a pivot (may or may not be the middle element)
# 2. partition the array into two sub-arrays: elements lesser than the pivot and those greater than the pivot
# 3. call quicksort recursively on the two sub-arrays
# run time: 
# average/best case - O(n log n)
# worst case - O(n^2)
# performance depends on the chosen pivot

# merge sort:
# steps:
# 1. recursively dividing the array into half until reaching the base case
# 2. compare and merge the array
# run time: O(n log n) for best, average and worst case

# ***quicksort is faster than merge sort (constant in Big O for merge sort is larger)
# ***constant in Big O almost never matters for simple search vs binary search as O(n) < O(log n)