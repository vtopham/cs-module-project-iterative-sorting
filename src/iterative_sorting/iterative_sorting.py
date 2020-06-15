# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        #Find the index of the smallest in the remaining array
        for j in range(i, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        
        #Now swap the smallest value with the value at cur_index
            #store the value for the swap
        smallest_value = arr[smallest_index]
            #set the former smallest value for the current index value
        arr[smallest_index] = arr[cur_index]
            #now go fill in that saved value at the current index
        arr[cur_index] = smallest_value
        
        

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # RECURSIVE SOLUTION
    # swapped = 0
    # for i in range(0, len(arr) - 1):
    #     #if the one on the left is bigger...
    #     if arr[i] > arr[i + 1]:
    #         #swap!
    #         bigger = arr[i]
    #         arr[i] = arr[i + 1]
    #         arr[i + 1] = bigger
    #         swapped = 1
    # if swapped:
    #     return bubble_sort(arr)
    # else:
    #     return arr

    #ITERATIVE SOLUTION
    swapped = 1
    while swapped:
        swapped = 0
        for i in range(0, len(arr) - 1):
            #if the one on the left is bigger...
            if arr[i] > arr[i + 1]:
                #swap!
                bigger = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = bigger
                swapped = 1
    
    return arr

     
 

'''
STRETCH: implement the Count Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
