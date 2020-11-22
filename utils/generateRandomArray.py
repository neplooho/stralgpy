from .generateOrderedArray import generate_ordered_array
import random
import time


# todo: pass optional argument for timestamp
def generate_shuffled_array(x):
    array = generate_ordered_array(x)
    random.seed(time.time())
    random.shuffle(array)
    array.accesses = 0
    return array
