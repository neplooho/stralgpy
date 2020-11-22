from utils import loggable_decorator
import copy


@loggable_decorator
def sorted(arr):
    return list(cocktail_shaker(copy.copy(arr)))[-1]


def sort(arr):
    return cocktail_shaker(arr)


def cocktail_shaker(arr):
    i = 0
    j = len(arr)
    while i < j:
        for x in range(i + 1, j):
            if arr[x - 1] > arr[x]:
                arr.swap(x, x - 1)
                yield arr
        j -= 1
        for y in range(j - 1, i, -1):
            if arr[y - 1] > arr[y]:
                arr.swap(y, y - 1)
                yield arr
        i += 1
