#!/usr/bin/python3

import sys

class Cell(object):

    def __init__(self, value, i, j, k):
        self.value = value
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        return ('{%s (%s, %s, %s)}' % +
            (self.value, self.i, self.j, self.k))

    def __repr__(self):
        return ('{%s (%s, %s, %s)}' % +
            (self.value, self.i, self.j, self.k))

def longest_common_sequence_different_matrix(a, b, c):
    """This version stores the solution in matrix[0][0][0]."""
    n = len(a)
    m = len(b)
    l = len(c)

    if 0 in (n, m, l):
        return 0

    matrix = \
            [
                [
                    [
                        0 for _ in range(l + 1)
                    ] for _ in range(m + 1)
                ] for _ in range(n + 1)
            ]

    for i in reversed(range(n + 1)):
        for j in reversed(range(m + 1)):
            for k in reversed(range(l + 1)):
                if i == n or j == m or k == l:
                    continue
                elif a[i] == b[j] == c[k]:
                    matrix[i][j][k] = 1 + matrix[i + 1][j + 1][k + 1]
                else:
                    matrix[i][j][k] = max(matrix[i + 1][j][k],
                        matrix[i][j + 1][k], matrix[i][j][k + 1])

    return matrix[0][0][0]

def longest_common_sequence(a, b, c):
    """In this problem, our goal is to compute the length of a longest
    common subsequence of three sequences.

    TODO: Enhance this implementation to find all possible sequences.
    Take a look at Assignment 4 Primitive Calculator, where I used a
    bread-first reconstruction of solutions.
    """
    n = len(a)
    m = len(b)
    l = len(c)

    if 0 in (n, m, l):
        return (0, [])

    matrix = \
            [
                [
                    [
                        Cell(0, None, None, None)
                        for _ in range(l + 1)
                    ] for _ in range(m + 1)
                ] for _ in range(n + 1)
            ]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for k in range(1, l + 1):
                if a[i - 1] == b[j - 1] == c[k - 1]:
                    matrix[i][j][k].value = \
                        1 + matrix[i - 1][j - 1][k - 1].value
                    matrix[i][j][k].i, matrix[i][j][k].j, matrix[i][j][k].k = \
                        i - 1, j - 1, k - 1
                else:
                    max_val = 0
                    x, y, z = None, None, None
                    if max_val <= matrix[i - 1][j][k].value:
                        max_val = matrix[i - 1][j][k].value
                        x, y, z = i - 1, j, k
                    if max_val <= matrix[i][j - 1][k].value:
                        max_val = matrix[i][j - 1][k].value
                        x, y, z = i, j - 1, k
                    if max_val <= matrix[i][j][k - 1].value:
                        max_val = matrix[i][j][k - 1].value
                        x, y, z = i, j, k - 1

                    matrix[i][j][k].value = max_val
                    if None not in (x, y, 2):
                        matrix[i][j][k].i, matrix[i][j][k].j, \
                            matrix[i][j][k].k = \
                        (matrix[x][y][z].i, matrix[x][y][z].j,
                         matrix[x][y][z].k)

    indices = []
    x, y, z = n, m, l
    while (None not in
        (matrix[x][y][z].i, matrix[x][y][z].j, matrix[x][y][z].k)):
        indices.append(
            (matrix[x][y][z].i, matrix[x][y][z].j,
             matrix[x][y][z].k))
        x, y, z = (matrix[x][y][z].i, matrix[x][y][z].j,
            matrix[x][y][z].k)

    return (matrix[n][m][l].value, indices)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    value, indices = longest_common_sequence(a, b, c)
    print(value)
