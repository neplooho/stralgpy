from utils import loggable_decorator
import copy


@loggable_decorator
def sorted(arr):
    return list(selection_sort(copy.copy(arr)))[-1]


def sort(arr):
    return selection_sort(arr)


def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr.swap(min_idx, i)
        yield arr
