from collections import namedtuple

import sys

Cell = namedtuple('Cell', 'value index')

def _check_args(capacity, weights, values):
    assert(0 <= capacity)
    assert(len(weights) == len(values))
    for w in weights:
        assert(0 <= w)
    for v in values:
        assert(0 <= v)

def optimal_value(capacity, weights, values):
    _check_args(capacity, weights, values)

    if len(weights) == 0:
        return (0, [])

    size = capacity + 1
    matrix = [ Cell(0, None) ] * size
    for w in range(0, size):
        for i in range(0, len(weights)):
            if weights[i] <= w:
                v = matrix[w - weights[i]].value + values[i]
                if v > matrix[w].value:
                    matrix[w] = matrix[w]._replace(value = v)
                    matrix[w] = matrix[w]._replace(index = i)

    items = []
    w = capacity
    while matrix[w].index != None:
        items.append(matrix[w].index)
        w -= weights[matrix[w].index]

    return (matrix[capacity].value, items)
