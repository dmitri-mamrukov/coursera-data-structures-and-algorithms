#!/usr/bin/python3

import sys

def solve(data):
    """Sorts the array of data.
    """
    for i in range(len(data) - 1, 0, -1):
        for j in range(0, i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]

if __name__ == '__main__':
    data = list(map(int, input().split()))

    solve(data)
    print(data)
