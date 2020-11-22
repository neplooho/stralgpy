from utils import loggable_decorator
import copy


@loggable_decorator
def sorted(arr):
    return list(insertion_sort(copy.copy(arr)))[-1]


def sort(arr):
    return insertion_sort(arr)


def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr.swap(j, j - 1)
            j -= 1
            yield arr
