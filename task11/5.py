#5.write a program to perform searching activity using linear and binary search.


def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

# Binary Search
def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Main Program
arr = list(map(int, input("Enter elements: ").split()))
key = int(input("Enter element to search: "))

print("Linear Search:", linear_search(arr, key))

arr.sort()
print("Sorted List:", arr)
print("Binary Search:", binary_search(arr, key))

