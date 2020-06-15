def linear_search(arr, target):
    # Your code here
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    
    floor = 0
    ceiling = len(arr) - 1

    while ceiling - floor > 1:
        midpoint = (ceiling - floor) // 2 + floor
        if target == arr[midpoint]:
            return midpoint
        elif target < arr[midpoint]:
            ceiling = midpoint
        elif target > arr[midpoint]:
            floor = midpoint
    

    return -1  # not found
