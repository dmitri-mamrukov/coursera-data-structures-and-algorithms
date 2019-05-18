#!/usr/bin/python3

import sys

def _solve_recursively(data, low, high, key):
    if high < low:
        return -1
    mid = low + (high - low) // 2
    if data[mid] == key:
        return mid
    elif key < data[mid]:
        return _solve_recursively(data, low, mid - 1, key)
    else:
        return _solve_recursively(data, mid + 1, high, key)

def solve_iteratively(data, key):
    """Finds the index of the key in the array if any.
    Otherwise, -1 is returned.
    """
    data.sort()

    low = 0
    high = len(data) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if data[mid] == key:
            return mid
        elif key < data[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1

def solve_recursively(data, key):
    """Finds the index of the key in the array if any.
    Otherwise, -1 is returned.
    """
    data.sort()

    return _solve_recursively(data, 0, len(data) - 1, key)

if __name__ == '__main__':
    data = list(map(int, input().split()))
    key = int(input())

    print(solve_recursively(data, key))
