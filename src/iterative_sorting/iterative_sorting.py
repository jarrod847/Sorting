# TO-DO: Complete the selection_sort() function below
import math
import random
arr = list(range(1, 11))
random.shuffle(arr)
print(f'before iterative sort', arr)


def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for t in range(i, len(arr)):
            print(arr)
            if(arr[smallest_index] > arr[t]):
                smallest_index = t
    # TO-DO: swap
        j = arr[cur_index]
        arr[cur_index] = arr[smallest_index]
        arr[smallest_index] = j
    return arr


print(f'after sort', selection_sort(arr))
# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
