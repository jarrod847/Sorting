import random
mSort = list(range(1, 11))
random.shuffle(mSort)
Arr2 = list(range(11, 21))
random.shuffle(Arr2)
# TO-DO: complete the helpe function below to merge 2 sorted arrays


def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # TO-DO
    L = 0
    R = 0
    for i in range(0, elements):
        if L >= len(arrA):
            merged_arr[i] = arrB[R]
            R += 1
        elif R >= len(arrB):
            merged_arr[i] = arrA[L]
            L += 1
        elif arrA[L] < arrB[R]:
            merged_arr[i] = arrA[L]
            L += 1
        else:
            merged_arr[i] = arrB[R]
            R += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    # TO-DO
    if len(arr) > 1:
        mid = len(arr) // 2
        Left = arr[:mid]
        Right = arr[mid:]

        ms1 = merge_sort(Left)
        ms2 = merge_sort(Right)
        # two halves
        return merge(ms1, ms2)
    else:
        if(len(arr) <= 1):
            return arr

    return arr


print(f"merge sort after", merge_sort(mSort), )

# STRETCH: implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
