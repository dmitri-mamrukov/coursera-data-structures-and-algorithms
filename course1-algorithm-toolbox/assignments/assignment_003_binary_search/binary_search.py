#!/usr/bin/python3

import sys

def binary_search(data, key):
    """Finds the index of the key in the array if any.
    Otherwise, -1 is returned.
    """
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

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i

    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]

    for x in data[n + 2:]:
        print(binary_search(a, x), end = ' ')
    print()
