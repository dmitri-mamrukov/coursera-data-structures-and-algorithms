#!/usr/bin/python3

import sys

def solve(data, key):
    """Finds the first index of the key in the array if any.
    Otherwise, the lowest index of the first value that is greater
    than the key is returned.
    """
    data.sort()

    low = 0
    high = len(data) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if data[mid] == key:
            if mid - 1 >= low and data[mid - 1] == key:
                high = mid - 1
            else:
                return mid
        elif key < data[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return low

if __name__ == '__main__':
    data = list(map(int, input().split()))
    key = int(input())

    print(solve(data, key))
