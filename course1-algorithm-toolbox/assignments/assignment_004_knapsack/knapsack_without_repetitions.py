from collections import namedtuple

import sys

Cell = namedtuple('Cell', 'value row column index')

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

    rows = capacity + 1
    columns = len(weights) + 1
    matrix = [[ Cell(0, None, None, None) ] * columns for i in range(0, rows)]

    for i in range(1, columns):
        for w in range(1, rows):
            matrix[w][i] = matrix[w][i]._replace(
                value = matrix[w][i - 1].value)
            matrix[w][i] = matrix[w][i]._replace(
                row = matrix[w][i - 1].row)
            matrix[w][i] = matrix[w][i]._replace(
                column = matrix[w][i - 1].column)
            matrix[w][i] = matrix[w][i]._replace(
                index = matrix[w][i - 1].index)

            item_index = i - 1
            if weights[item_index] <= w:
                v = (matrix[w - weights[item_index]][i - 1].value +
                    values[item_index])
                if v > matrix[w][i].value:
                    matrix[w][i] = matrix[w][i]._replace(value = v)
                    matrix[w][i] = matrix[w][i]._replace(index = item_index)
                    matrix[w][i] = matrix[w][i]._replace(
                        row = w - weights[item_index])
                    matrix[w][i] = matrix[w][i]._replace(column = i - 1)

    items = []
    w = capacity
    i = columns - 1
    while matrix[w][i].index != None:
        items.append(matrix[w][i].index)
        w, i = matrix[w][i].row, matrix[w][i].column

    return (matrix[capacity][len(weights)].value, items)
