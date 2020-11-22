from utils import loggable_decorator
import copy


@loggable_decorator
def sorted(arr):
    return list(bubble_sort(copy.copy(arr)))[-1]


def sort(arr):
    return bubble_sort(arr)


def bubble_sort(arr):
    for x in range(len(arr) - 1):
        for y in range(1, len(arr) - x):
            if arr[y - 1] > arr[y]:
                arr.swap(y, y - 1)
                yield arr
