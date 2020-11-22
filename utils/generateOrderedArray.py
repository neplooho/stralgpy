import numpy as np
from structures import Array


def generate_ordered_array(x, order='ASC'):
    if order == 'ASC':
        return Array(np.array(range(1, x + 1)))
    elif order == 'DESC':
        return Array(np.array(list(reversed(range(1, x + 1)))))
    else:
        raise Exception('order should be either ASC or DESC. The value of order was {}'.format(order))
