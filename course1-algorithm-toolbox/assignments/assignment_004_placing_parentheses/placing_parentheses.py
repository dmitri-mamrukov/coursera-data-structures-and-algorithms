#!/usr/bin/python3

from collections import namedtuple
from enum import Enum

Cell = namedtuple('Cell', 'min max min_k min_kind max_k max_kind')

class MinMaxKind(Enum):
    max_max = 1
    max_min = 2
    min_max = 3
    min_min = 4

def _check_args(text):
    operations = [ '+', '-', '*' ]

    assert(1 <= len(text))
    assert(len(text) % 2 != 0)

    for i in range(0, len(text)):
        if (i % 2 == 0):
            assert(text[i].isdigit())
        else:
            assert(text[i] in operations)

def _get_n(text):
    return 1 + (len(text) - 1) // 2

def _evaluate(a, b, op):
    if a == None:
        return b
    if b == None:
        return a

    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        raise ValueError('Unsupported operation: ' + str(op))

def _min_max(matrix, i, j, text):
    min_val = None
    max_val = None
    min_k = None
    min_kind = None
    max_k = None
    max_kind = None
    for k in range(0, j):
        op = text[2 * k + 1]
        a = _evaluate(matrix[i][k].max, matrix[k + 1][j].max, op)
        b = _evaluate(matrix[i][k].max, matrix[k + 1][j].min, op)
        c = _evaluate(matrix[i][k].min, matrix[k + 1][j].max, op)
        d = _evaluate(matrix[i][k].min, matrix[k + 1][j].min, op)

        new_min_val = None
        new_min_kind = None
        if new_min_val == None or (a != None and a < new_min_val):
            new_min_val = a
            new_min_kind = MinMaxKind.max_max
        if new_min_val == None or (b != None and b < new_min_val):
            new_min_val = b
            new_min_kind = MinMaxKind.max_min
        if new_min_val == None or (c != None and c < new_min_val):
            new_min_val = c
            new_min_kind = MinMaxKind.min_max
        if new_min_val == None or (d != None and d < new_min_val):
            new_min_val = d
            new_min_kind = MinMaxKind.min_min
        if new_min_val != None:
            if min_val == None or min_val > new_min_val:
                min_val = new_min_val
                min_kind = new_min_kind
                min_k = k

        new_max_val = None
        new_max_kind = None
        if new_max_val == None or (a != None and a > new_max_val):
            new_max_val = a
            new_max_kind = MinMaxKind.max_max
        if new_max_val == None or (b != None and b > new_max_val):
            new_max_val = b
            new_max_kind = MinMaxKind.max_min
        if new_max_val == None or (c != None and c > new_max_val):
            new_max_val = c
            new_max_kind = MinMaxKind.min_max
        if new_max_val == None or (d != None and d > new_max_val):
            new_max_val = d
            new_max_kind = MinMaxKind.min_min
        if new_max_val != None:
            if max_val == None or max_val < new_max_val:
                max_val = new_max_val
                max_kind = new_max_kind
                max_k = k

    return (min_val, max_val, min_k, min_kind, max_k, max_kind)

def get_min_max(text):
    """In this problem, our goal is to add parentheses to a given arithmetic
    expression to return its minimum and maximum values.
    """
    _check_args(text)

    n = _get_n(text)

    matrix = [ [ Cell(None, None, None, None, None, None) ] * n
        for i in range(0, n) ]

    for i in range(0, n):
        operand_index = 2 * i
        matrix[i][i] = matrix[i][i]._replace(min = int(text[operand_index]))
        matrix[i][i] = matrix[i][i]._replace(max = int(text[operand_index]))

    for s in range(0, n):
        for i in range(0, n - s):
            j = i + s
            min_val, max_val, min_k, min_kind, max_k, max_kind = \
                _min_max(matrix, i, j, text)
            if min_val != None:
                matrix[i][j] = matrix[i][j]._replace(min = min_val)
                matrix[i][j] = matrix[i][j]._replace(min_k = min_k)
                matrix[i][j] = matrix[i][j]._replace(min_kind = min_kind)
            if max_val != None:
                matrix[i][j] = matrix[i][j]._replace(max = max_val)
                matrix[i][j] = matrix[i][j]._replace(max_k = max_k)
                matrix[i][j] = matrix[i][j]._replace(max_kind = max_kind)

    return (matrix[0][n - 1].min, matrix[0][n - 1].max,
        _get_min_solution(matrix, 0, n - 1, text),
        _get_max_solution(matrix, 0, n - 1, text))

def _get_min_solution(matrix, i, j, text):
    if i == j:
        return '(' + text[2 * i] + ')'
    if i + 1 == j:
        op1 = text[2 * i]
        op = text[2 * i + 1]
        op2 = text[2 * j]

        return '(' + op1 + op + op2 + ')'

    k = matrix[i][j].min_k
    op = text[2 * k + 1]
    if matrix[i][j].min_kind == MinMaxKind.max_max:
        return ('(' + _get_max_solution(matrix, i, k, text) +
            op +
            _get_max_solution(matrix, k + 1, j, text) + ')')
    elif matrix[i][j].min_kind == MinMaxKind.max_min:
        return ('(' + _get_max_solution(matrix, i, k, text) +
            op +
            _get_min_solution(matrix, k + 1, j, text) + ')')
    elif matrix[i][j].min_kind == MinMaxKind.min_max:
        return ('(' + _get_min_solution(matrix, i, k, text) +
            op +
            _get_max_solution(matrix, k + 1, j, text) + ')')
    elif matrix[i][j].min_kind == MinMaxKind.min_min:
        return ('(' + _get_min_solution(matrix, i, k, text) +
            op +
            _get_min_solution(matrix, k + 1, j, text) + ')')

def _get_max_solution(matrix, i, j, text):
    if i == j:
        return '(' + text[2 * i] + ')'
    if i + 1 == j:
        op1 = text[2 * i]
        op = text[2 * i + 1]
        op2 = text[2 * j]

        return '(' + op1 + op + op2 + ')'

    k = matrix[i][j].max_k
    op = text[2 * k + 1]
    if matrix[i][j].max_kind == MinMaxKind.max_max:
        return ('(' + _get_max_solution(matrix, i, k, text) +
            op +
            _get_max_solution(matrix, k + 1, j, text) + ')')
    elif matrix[i][j].max_kind == MinMaxKind.max_min:
        return ('(' + _get_max_solution(matrix, i, k, text) +
            op +
            _get_min_solution(matrix, k + 1, j, text) + ')')
    elif matrix[i][j].max_kind == MinMaxKind.min_max:
        return ('(' + _get_min_solution(matrix, i, k, text) +
            op +
            _get_max_solution(matrix, k + 1, j, text) + ')')
    elif matrix[i][j].max_kind == MinMaxKind.min_min:
        return ('(' + _get_min_solution(matrix, i, k, text) +
            op +
            _get_min_solution(matrix, k + 1, j, text) + ')')

if __name__ == "__main__":
    input = input()
    min_val, max_val, min_solution, max_solution = get_min_max(input)
    print(max_val)
