# Exercise 4.1
# Write out the code for the earlier sum function

def sum(arr):
    if len(arr) == 1:   # bass case
        return arr[0]
    else:
        return arr[0] + sum(arr[1:])

arr = [1,7,2,5,4]
print(sum(arr))

"""
Sample Answer:

def sum(arr):
    if arr == []:
        return 0
    return arr[0] + sum(arr[1:])
"""


# Exercise 4.2
# Write a recursive function to count the number of items in a list

def count(arr):
    if len(arr) == 1:   #base case
        return 1
    else:
        return 1 + count(arr[1:])
    
print(count(arr))

"""
Sample Answer:

def count(arr):
    if arr == []:
        return 0
    return 1 + count(arr[1:])
"""

# Exercise 4.3 
# Find the maximum number in a list
maxValue = 0

def maxNum(arr):
    global maxValue
    if len(arr) == 0:
            return maxValue
    else:
        if arr[0] > maxValue:
            maxValue = arr[0]
        return maxNum(arr[1:])

print(maxNum(arr))

"""
Sample Answer:

def max(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub_max = max(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max
"""

# Exercise 4.4
# Remember binary search from chapter 1? It's a divide-and-conquer algorithm, too.
# Can you come out with the base case and recursive case for binary search?

# index = 0

# def binary_search(arr, item):
#     global index
#     if len(arr) == 0:
#         return None
#     else:
#         if arr[0] == item:
#             return index
#         else:
#             index += 1
#             return binary_search(arr[1:], item)
    

# print(binary_search(arr, 7))

"""
second trial:

def binary_search(arr, item):
    if len(arr) == 1:
        return arr[0] if arr[0] == item else None
    mid = len(arr) // 2
    search = binary_search(arr[:mid], item)
    return binary_search(arr[mid:], item) if search == None else search
"""

"""
third trial:

def binary_search(arr, item, l):
    if len(arr) == 0:
        return None

    mid = len(arr) // 2

    if arr[mid] == item:
        return l + mid
    elif arr[mid] < item:
        return binary_search(arr[mid+1:], item, l + mid + 1)    
    else:
        return binary_search(arr[:mid], item, l)
"""

# How long would each of these questions take in Big O notation?

# Exercise 4.5
# Printing the value of each element in an array
# Answer: O(n)

# Exercise 4.6
# Doubling the value of each element in an array
# Answer: O(n)

# Exercise 4.7
# Doubling the value of just the first element in an array
# Answer: O(1)

# Exercise 4.8
# Creating a multiplication table with all the elements in the array.
# So if your array is [2 ,3, 7, 8, 10], you first multiply every element by 2, then multiply every element by 3, then by 7, and so on.
# Answer: O(n^2)



