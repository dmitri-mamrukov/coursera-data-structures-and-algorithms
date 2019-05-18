#!/usr/bin/python3

from collections import namedtuple
from enum import Enum
import sys

class EditOperation(Enum):
    match = 1
    substitute = 2
    insert = 3
    delete = 4

Cell = namedtuple('Cell', 'cost edit')

def edit_distance(word1, word2):
    """Our goal is to find the edit distance between two strings
    x[1...m] and y[1...n].

    The cost of an alignment is the number of columns in which the letters
    differ. And the edit distance between two strings is the cost of their
    best possible alignment.
    """
    # construct a matrix whose last element is the edit distance
    x = [[ 0 ] * (len(word2) + 1) for i in range(0, len(word1) + 1)]

    # initialization of base case values
    for i in range(0, len(word1) + 1):
        x[i][0] = i
    for j in range(0, len(word2) + 1):
        x[0][j] = j

    for i in range (1, len(word1) + 1):
        for j in range(1, len(word2) + 1):
            if word1[i - 1] == word2[j - 1]:
                x[i][j] = x[i - 1][j - 1]
            else:
                x[i][j] = min(x[i][j - 1], x[i - 1][j], x[i - 1][j - 1]) + 1

    return x[i][j]

def _calculate_edit_distance(edits):
    count = 0
    for e in edits:
        if e != 'match':
            count += 1

    return count

def _get_edit(distances, word1, word2):
    moves = []
    i = len(word1)
    j = len(word2)
    while i > 0 and j > 0:
        move = distances[i][j].edit
        moves.append(move.name)
        if move == EditOperation.match or move == EditOperation.substitute:
            i -= 1
            j -= 1
        elif move == EditOperation.insert:
            j -= 1
        elif move == EditOperation.delete:
            i -= 1
        else:
            raise ValueError('Unsupported edit operation.' + str(move))

    for k in range(0, i):
        moves.append(EditOperation.delete.name)
    for k in range(0, j):
        moves.append(EditOperation.insert.name)

    return list(reversed(moves))

def edit_distance_with_traceback(word1, word2):
    """Our goal is to find the edit distance between two strings
    x[1...m] and y[1...n].

    The cost of an alignment is the number of columns in which the letters
    differ. And the edit distance between two strings is the cost of their
    best possible alignment.
    """
    # construct a matrix whose last element is the edit distance
    distances = [[ 0 ] * (len(word2) + 1) for i in range(0, len(word1) + 1)]

    # initialize base case values
    for i in range(0, len(word1) + 1):
        distances[i][0] = Cell(i, EditOperation.delete)
    for j in range(0, len(word2) + 1):
        distances[0][j] = Cell(j, EditOperation.insert)

    for i in range (1, len(word1) + 1):
        for j in range(1, len(word2) + 1):
            cell = None
            if word1[i - 1] == word2[j - 1]:
                cell = Cell(distances[i - 1][j - 1].cost,
                    EditOperation.match)
            else:
                cell = Cell(distances[i - 1][j - 1].cost + 1,
                    EditOperation.substitute)
            deletion_cost = distances[i - 1][j].cost + 1
            if deletion_cost < cell.cost:
                cell = Cell(deletion_cost, EditOperation.delete)
            insertion_cost = distances[i][j - 1].cost + 1
            if insertion_cost < cell.cost:
                cell = Cell(insertion_cost, EditOperation.insert)

            distances[i][j] = cell

    edits = _get_edit(distances, word1, word2)

    return (_calculate_edit_distance(edits), edits)

if __name__ == '__main__':
    x = str(input())
    y = str(input())

    print(edit_distance(x, y))
    print(edit_distance_with_traceback(x, y))
