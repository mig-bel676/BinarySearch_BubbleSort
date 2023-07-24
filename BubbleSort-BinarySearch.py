
def bubble_Sort(array):
    n = len(array)
    for i in range(n-1):
        for j in range(n-i-1):
            # Left to Right
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

def binary_Search(array, target):
    lower = 0
    upper = len(array)
    while lower <= upper:
        mid = (lower + upper) // 2
        if array[mid] == target:
            return mid 
        elif array[mid] < target:
            lower = mid + 1
        else:
            upper = mid - 1
    return None


my_List = [34, 4, 56, 77, 1, 23, 87, 6]
bubble_Sort(my_List)
print(my_List)

target = int(input("What number are you looking for: "))
index = binary_Search(my_List, target)

if index == None:
    print(f"{target} is not in list")
else:
    print(f"{target} is at index: {index}")