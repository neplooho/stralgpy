from utils import loggable_decorator
import random
import copy


@loggable_decorator
def sorted(arr):
    a = copy.copy(arr)
    return list(quick_sort(a, 0, len(a) - 1))[-1]


def sort(arr):
    return quick_sort(arr, 0, len(arr) - 1)


def quick_sort(arr, p, r):
    if p < r:
        pivot = arr[random.randint(p, r)]
        i = p
        j = r
        while i != j:
            if arr[i] >= pivot >= arr[j]:
                arr.swap(i, j)
                yield arr
            elif arr[i] < pivot:
                i += 1
            elif arr[j] >= pivot:
                j -= 1
            else:
                i += 1
                j -= 1
        yield from quick_sort(arr, p, i - 1)
        yield from quick_sort(arr, i, r)
        yield arr
