#!/usr/bin/python3

import sys

DEBUG = False

def __check_args(capacity, weights, values):
    assert(0 <= capacity)
    assert(len(weights) == len(values))
    for w in weights:
        assert(0 < w)
    for v in values:
        assert(0 <= v)

def get_optimal_value(capacity, weights, values):
    """Given a set of items and total capacity of a knapsack,
    finds the maximal value of fractions of items that fit
    into the knapsack.

    Greedy Strategy:

    Select f fractions of the maximum value per unit weight that fit the
    capacity and continue on capacity - f. Otherwise, we are done.

    Safety Proof:

    Suppose we have an *optimal* solution of f fractions of items that fill
    the capacity and we can replace a subset of the f fractions with g
    fractions of a higher value per unit weight. The total capacity stays
    the same but we can increase the total value. Contradiction.
    """
    __check_args(capacity, weights, values)

    unit_values = []
    for i in range(0, len(weights)):
        unit_values.append(values[i] / weights[i])

    if DEBUG:
        print('unit values: %s' % unit_values)

    value = 0.
    total_weight = 0
    while total_weight < capacity and len(weights) > 0:
        remaining_capacity = capacity - total_weight

        if DEBUG:
            print('total weight: %s, remaining capacity: %s' %
                (total_weight, remaining_capacity))

        max_unit_value = 0.
        index = 0
        for i in range(0, len(unit_values)):
            if (unit_values[i] > max_unit_value):
                max_unit_value = unit_values[i]
                index = i

        actual_weight = min(weights[index], remaining_capacity)
        total_weight += actual_weight
        value += unit_values[index] * actual_weight

        if DEBUG:
            print('adding weight: %s of unit value %s = %s' %
                (actual_weight, max_unit_value,
                unit_values[index] * actual_weight))

        del weights[index]
        del values[index]
        del unit_values[index]

    if DEBUG:
        print('final: total weight: %s of value %s' %
            (total_weight, value))

    return value

if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, capacity = data[0:2]
    values = data[2:(2 + 2 * n):2]
    weights = data[3:(2 + 2 * n):2]

    optimal_value = get_optimal_value(capacity, weights, values)

    print("{:.10f}".format(optimal_value))
