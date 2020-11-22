from utils import loggable_decorator
import numpy as np
import copy


@loggable_decorator
def sorted(arr):
    return list(counting_sort(copy.copy(arr)))[-1]


def sort(arr):
    return counting_sort(arr)


def counting_sort(arr):
    a = np.zeros(len(arr), dtype=int)

    for val in arr:
        a[val - 1] += 1

    for i in range(1, len(a)):
        a[i] = a[i] + a[i - 1]

    for i in range(len(a)):
        if i == 0:
            for asd in range(a[0]):
                arr[asd] = i + 1
                yield arr
        else:
            for asd in range(a[i - 1], a[i]):
                arr[asd] = i + 1
                yield arr
