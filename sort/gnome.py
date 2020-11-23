from utils import loggable_decorator
import copy


# Probably some day I will gather all algorithms brief description in one place
@loggable_decorator
def sorted(arr):
    return list(gnome_sort(copy.copy(arr)))[-1]


def sort(arr):
    return gnome_sort(arr)


# This one tries to behave like a nice one insertion sort, it also pushes elements by one to
# their best position at this moment
# But it's slower that insertion because it doesn't remember where it took that element from
# To return back it has to loop back to it (do many += 1) while insertion sort just jumps into the
# position of last taken element
def gnome_sort(arr):
    index = 0
    while index < len(arr):
        if index == 0:
            index += 1
        if arr[index] < arr[index - 1]:
            arr.swap(index, index - 1)
            yield arr
            index -= 1
        else:
            index += 1
    yield arr
