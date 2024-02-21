# going through the list and select the most/least then add it to a new list
# run time: 
# O(n^2)


# to sort from greatest to smallest
def findSmallest(arr):
    smallest = arr[0]
    smallestIndex = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallestIndex = i

    return smallestIndex

def selectionSortAsc(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    
    return newArr

# to sort from smallest to greatest
def findGreatest(arr):
    greatest = arr[0]
    greatestIndex = 0

    for i in range(1, len(arr)):
        if arr[i] > greatest:
            greatest = arr[i]
            greatestIndex = i

    return greatestIndex
    
def selectionSortDesc(arr):
    newArr = []
    for i in range(len(arr)):
        greatest = findGreatest(arr)
        newArr.append(arr.pop(greatest))
    
    return newArr


# tester
arr = [1,6,2,7,3,8]
print('Ascending: ', selectionSortAsc(arr))
Arr = [1,6,2,7,3,8]
print('Descending: ', selectionSortDesc(Arr))
