#!/usr/bin/python3

import sys

def __merge(data, left, mid, right):
    data_left = data[left:mid]
    data_right = data[mid:right]
    l, r = 0, 0
    for k in range(left, right):
        if (r >= len(data_right) or
            (l < len(data_left) and data_left[l] < data_right[r])):
            data[k] = data_left[l]
            l += 1
        else:
            data[k] = data_right[r]
            r += 1

def __solve(data, left, right):
    if right - left <= 1:
        return

    mid = (left + right) // 2
    __solve(data, left, mid)
    __solve(data, mid, right)
    __merge(data, left, mid, right)

def solve(data):
    """Sorts the array of data.
    """
    __solve(data, 0, len(data))

if __name__ == '__main__':
    data = list(map(int, input().split()))

    solve(data)
    print(data)
