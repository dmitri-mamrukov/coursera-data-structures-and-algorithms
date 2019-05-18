#!/usr/bin/python3

from collections import namedtuple
import math
from enum import Enum
import sys

CellSimplified = namedtuple('Cell', 'cost operation')
Cell = namedtuple('Cell', 'cost operations')

class Operation(Enum):
    multiply_by_two = 1
    multiply_by_three = 2
    add_one = 3

def _check_args(n):
    assert(1 <= n)

def _get_sequence_helper(n, info, sequence):
    if n == 1:
        return

    operation = info[n].operation
    k = n
    if operation == Operation.multiply_by_three:
        v = k // 3
        sequence.append(v)
        _get_sequence_helper(v, info, sequence)
    elif operation == Operation.multiply_by_two:
        v = k // 2
        sequence.append(v)
        _get_sequence_helper(v, info, sequence)
    elif operation == Operation.add_one:
        v = k - 1
        sequence.append(v)
        _get_sequence_helper(v, info, sequence)

def _get_sequence(n, info):
    sequence = [ n ]
    _get_sequence_helper(n, info, sequence)

    return sequence

def optimal_sequence_simplified(n):
    """We are given a primitive calculator that can perform the following
    three operations with the current number x: multiply x by 2, multiply x
    by 3, or add 1 to x. Our goal is, given a positive integer n, to find the
    minimum number of operations needed to obtain the number n, starting from
    the number 1.
    """
    _check_args(n)

    info = [ CellSimplified(0, None) ] * (n + 1)

    for i in range(1, n + 1):
        min_cost = None
        operation = None

        if i % 3 == 0 and i // 3 >= 0:
            cell = info[i // 3]
            if min_cost == None or cell.cost < min_cost:
                min_cost = cell.cost
                operation = Operation.multiply_by_three
        if i % 2 == 0 and i // 2 >= 0:
            cell = info[i // 2]
            if min_cost == None or cell.cost < min_cost:
                min_cost = cell.cost
                operation = Operation.multiply_by_two
        if i - 1 >= 0:
            cell = info[i - 1]
            if min_cost == None or cell.cost < min_cost:
                min_cost = cell.cost
                operation = Operation.add_one

        info[i] = CellSimplified(min_cost + 1, operation)

    sequence = _get_sequence(n, info)

    return list(reversed(sequence))

def _get_sequences_and_operations_helper(n, info, sequences, sequence,
    operations_list, actions):
    if n == 1:
        sequences.append(list(reversed(sequence)))
        operations_list.append(list(reversed(actions)))

        return

    for i in range(0, len(info[n].operations)):
        operations = info[n].operations
        k = n
        a = list(actions)
        a.append(operations[i].name)
        if operations[i] == Operation.multiply_by_three:
            v = k // 3
            s = list(sequence)
            s.append(v)
            _get_sequences_and_operations_helper(v, info,
                sequences, s, operations_list, a)
        elif operations[i] == Operation.multiply_by_two:
            v = k // 2
            s = list(sequence)
            s.append(v)
            _get_sequences_and_operations_helper(v, info,
                sequences, s, operations_list, a)
        elif operations[i] == Operation.add_one:
            v = k - 1
            s = list(sequence)
            s.append(v)
            _get_sequences_and_operations_helper(v, info,
                sequences, s, operations_list, a)

def _get_sequences_and_operations(n, info, sequences, operations_list):
    sequence = [ n ]
    operations = []
    _get_sequences_and_operations_helper(n, info, sequences, sequence,
        operations_list, operations)

def optimal_sequence(n):
    """We are given a primitive calculator that can perform the following
    three operations with the current number x: multiply x by 2, multiply x
    by 3, or add 1 to x. Our goal is, given a positive integer n, to find the
    minimum number of operations needed to obtain the number n, starting from
    the number 1.
    """
    _check_args(n)

    info = [ Cell(0, []) ] * (n + 1)

    for i in range(1, n + 1):
        min_cost = None
        multiply_by_three_cost = None
        multiply_by_two_cost = None
        add_one_cost = None

        if i % 3 == 0 and i // 3 >= 0:
            cell = info[i // 3]
            if min_cost == None or cell.cost <= min_cost:
                multiply_by_three_cost = cell.cost
                min_cost = multiply_by_three_cost
        if i % 2 == 0 and i // 2 >= 0:
            cell = info[i // 2]
            if min_cost == None or cell.cost <= min_cost:
                multiply_by_two_cost = cell.cost
                min_cost = multiply_by_two_cost
        if i - 1 >= 0:
            cell = info[i - 1]
            if min_cost == None or cell.cost <= min_cost:
                add_one_cost = cell.cost
                min_cost = add_one_cost

        operations = []
        if min_cost == multiply_by_three_cost:
            operations.append(Operation.multiply_by_three)
        if min_cost == multiply_by_two_cost:
            operations.append(Operation.multiply_by_two)
        if min_cost == add_one_cost:
            operations.append(Operation.add_one)
        info[i] = Cell(min_cost + 1, operations)

    sequences = []
    operations_list = []

    _get_sequences_and_operations(n, info, sequences, operations_list)

    return (sequences, operations_list)

def optimal_sequence_greedy_approach(n):
    """This seemingly correct algorithm is in fact incorrect.
    Hence in this case moving from n to min{n / 3, n / 2, n − 1} is not safe.
    """
    _check_args(n)

    sequence = []

    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1

    return list(reversed(sequence))

if __name__ == "__main__":
    input = sys.stdin.read()
    n = int(input)

    sequence = optimal_sequence_simplified(n)

    print(len(sequence) - 1)
    for x in sequence:
        print(x, end = ' ')
    print()
