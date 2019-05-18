#!/usr/bin/python3

import sys

def solve(data):
    """Sorts the array of data.
    """
    for i in range(1, len(data)):
        value = data[i]
        position = i
        while position > 0 and data[position - 1] > value:
            data[position] = data[position - 1]
            position -= 1

        data[position] = value

if __name__ == '__main__':
    data = list(map(int, input().split()))

    solve(data)
    print(data)
