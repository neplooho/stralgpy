from utils import loggable_decorator
from math import trunc
import copy


@loggable_decorator
def sorted(arr):
    a = copy.copy(arr)
    return list(merge_sort(a, 0, len(a) - 1))[-1]


def sort(arr):
    return merge_sort(arr, 0, len(arr) - 1)


def merge_sort(arr, p, r):
    if p < r:
        q = trunc((p + (r - 1)) / 2)
        yield from merge_sort(arr, p, q)
        yield from merge_sort(arr, q + 1, r)
        yield from merge(arr, p, q, r)
        yield arr


def merge(arr, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    left = [0] * n1
    right = [0] * n2

    for i in range(0, n1):
        left[i] = arr[p + i]

    for j in range(0, n2):
        right[j] = arr[q + 1 + j]

    i = j = 0

    while i < n1 and j < n2:
        if left[i] <= right[j]:
            arr[p] = left[i]
            i += 1
        else:
            arr[p] = right[j]
            j += 1
        p += 1

    while i < n1:
        arr[p] = left[i]
        i += 1
        p += 1
        yield arr
    while j < n2:
        arr[p] = right[j]
        j += 1
        p += 1
        yield arr
