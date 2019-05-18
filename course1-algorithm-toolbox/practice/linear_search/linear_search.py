#!/usr/bin/python3

import sys

def __solve_recursively(data, low, high, key):
    if high < low:
        return -1
    if data[low] == key:
        return low

    return __solve_recursively(data, low + 1, high, key)

def solve_iteratively(data, key):
    """Finds the index of the key in the array if any.
    Otherwise, -1 is returned.
    """
    for i, v in enumerate(data):
        if v == key:
            return i

    return -1

def solve_recursively(data, key):
    """Finds the index of the key in the array if any.
    Otherwise, -1 is returned.
    """
    return __solve_recursively(data, 0, len(data) - 1, key)

if __name__ == '__main__':
    data = list(map(int, input().split()))
    key = int(input())

    print(solve_recursively(data, key))
