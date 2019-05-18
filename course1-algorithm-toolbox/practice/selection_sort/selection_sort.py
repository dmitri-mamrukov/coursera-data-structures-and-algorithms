#!/usr/bin/python3

import sys

def solve_by_min(data):
    """Sorts the array of data.
    """
    for i in range(0, len(data)):
        min_index = i
        for j in range(i + 1, len(data)):
            if data[j] < data[min_index]:
                min_index = j

        data[i], data[min_index] = data[min_index], data[i]

def solve_by_max(data):
    """Sorts the array of data.
    """
    for i in range(len(data) - 1, 0, -1):
        max_index = i
        for j in range(0, i):
            if data[j] > data[max_index]:
                max_index = j

        data[i], data[max_index] = data[max_index], data[i]

if __name__ == '__main__':
    data = list(map(int, input().split()))

    solve_by_min(data)
    print(data)
