#!/usr/bin/python3

import sys

from collections import namedtuple

Cell = namedtuple('Cell', 'value row column index')

def _check_args(capacity, weights, values):
    assert(0 <= capacity)
    assert(len(weights) == len(values))
    for w in weights:
        assert(0 <= w)
    for v in values:
        assert(0 <= v)

def _optimal_value_simplified(capacity, weights, values):
    _check_args(capacity, weights, values)

    if len(weights) == 0:
        return 0

    rows = capacity + 1
    columns = len(weights) + 1
    matrix = [ [ 0 ] * columns for i in range(0, rows) ]

    for i in range(1, columns):
        for w in range(1, rows):
            matrix[w][i] = matrix[w][i - 1]

            item_index = i - 1
            if weights[item_index] <= w:
                v = (matrix[w - weights[item_index]][i - 1] +
                     values[item_index])
                if v > matrix[w][i]:
                    matrix[w][i] = v

    return matrix[capacity][len(weights)]

def _optimal_value(capacity, weights, values):
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

def optimal_weight_simplified(capacity, weights):
    """In this problem, we are given a set of bars of gold and our goal is
    to take as much gold as possible into your bag. There is just one copy
    of each bar and for each bar we can either take it or not (hence
    we cannot take a fraction of a bar).

    Note: For the same units of material, values are equal to weights
    as they are proportional.
    """
    return _optimal_value_simplified(capacity, weights, weights)

def optimal_weight(capacity, weights):
    """In this problem, we are given a set of bars of gold and our goal is
    to take as much gold as possible into your bag. There is just one copy
    of each bar and for each bar we can either take it or not (hence
    we cannot take a fraction of a bar).

    Note: For the same units of material, values are equal to weights
    as they are proportional.
    """
    return _optimal_value(capacity, weights, weights)

def optimal_weight_greedy(capacity, weights):
    result = 0
    for x in w:
        if result + x <= capacity:
            result = result + x

    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    capacity, n, *weights = list(map(int, input.split()))
    value = optimal_weight_simplified(capacity, weights)
    print(value)
