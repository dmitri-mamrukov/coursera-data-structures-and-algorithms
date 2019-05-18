#!/usr/bin/python3

import sys

def __merge(a, b):
    result = [ 0 ] * (len(a) + len(b))

    i = 0
    while(len(a) > 0 and len(b) > 0):
        if (a[0] <= b[0]):
            result[i] = a[0]
            del a[0]
        else:
            result[i] = b[0]
            del b[0]
        i += 1

    for k in a:
        result[i] = k
        i += 1
    for k in b:
        result[i] = k
        i += 1

    return result

def solve(data):
    """Sorts the array of data.
    """
    n = len(data)
    if n <= 1:
        return data

    mid = n // 2
    left = solve(data[:mid])
    right = solve(data[mid:])

    return __merge(left, right)

if __name__ == '__main__':
    data = list(map(int, input().split()))

    print(solve(data))
