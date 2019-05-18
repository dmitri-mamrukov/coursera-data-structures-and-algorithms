#!/usr/bin/python3

import sys
import random

def __partition3(data, left, right):
    """This function partitions a[] in three parts:

    a) a[left..l - 1] contains all elements smaller than the pivot element
    b) a[l..r] contains all occurrences of the pivot element
    c) a[r + 1..right] contains all elements greater than the pivot element
    """
    l = left
    r = right
    k = left + 1
    pivot_value = data[left]
    while k <= r:
        if data[k] < pivot_value:
            data[l], data[k] = data[k], data[l]
            l += 1
            k += 1
        elif data[k] > pivot_value:
            data[k], data[r] = data[r], data[k]
            r -= 1
        else:
            k += 1

    return (l - 1, r + 1)

def __partition2(data, left, right):
    x = data[left]
    k = left;
    for i in range(left + 1, right + 1):
        if data[i] <= x:
            k += 1
            data[i], data[k] = data[k], data[i]

    data[left], data[k] = data[k], data[left]

    return k

def __randomized_quick_sort(data, left, right):
    if left >= right:
        return

    k = random.randint(left, right)
    data[left], data[k] = data[k], data[left]

    i, j = __partition3(data, left, right)
    __randomized_quick_sort(data, left, i);
    __randomized_quick_sort(data, j, right);

def solve(data):
    __randomized_quick_sort(data, 0, len(data) - 1)

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))

    solve(a)

    for x in a:
        print(x, end = ' ')
    print()
