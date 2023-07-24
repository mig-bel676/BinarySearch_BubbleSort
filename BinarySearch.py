# Implementing Binary Search, searching for a value in a data structure more efficiently 
# Basically just a faster way to search
# Ordered array can do binary search but not classic arrays, In python Lists or use numpy arrays

def binary_search(arr, target):
    # Establish Upper and Lower Bounds of the whole array/list
    lowerBound = 0
    higherBound = len(arr)-1
    # This while loop is what keeps checking 
    while lowerBound <= higherBound:
        # Index of Midpoint
        midIndex = (lowerBound + higherBound) // 2
        # if target is greater than mid
        if arr[midIndex] == target:
            return midIndex
        elif arr[midIndex] < target:
            # lower bound increases from the midpoint by 1
            lowerBound = midIndex + 1
        # if target is less than mid
        elif arr[midIndex] > target:
            # higher bound increases from the midpoint by 1
            higherBound = midIndex - 1
    return None

# Implement Bubble Sort for sorting list to ascending  
def bubble_Sort(array):
    n = len(array)
    for i in range(n-1):
        for j in range(n-i-1):
            if array[j] > array[j+1]:
                # Swap
                array[j], array[j+1] = array[j+1], array[j]
                # Or
                # temp = arr[j]
                # arr[j] = arr[j+1]
                # arr[j+1] = temp
   


 # Sorting List       
my_List = [98, 65, 23, 6, 40, 7, 5]
bubble_Sort(my_List)
print(my_List)

# Binary Search on List
target = 65
index = binary_search(my_List, target)

# Output results of Binary Search
if index == None:
    print(f"{target} does not exist in list")
else:
    print(f"{target} at index: {index}")