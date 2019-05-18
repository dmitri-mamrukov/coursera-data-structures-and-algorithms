#!/usr/bin/python3

import sys

def _partition(data, left, right):
   pivot_value = data[left]

   j = left

   for i in range(left + 1, right + 1):
       if data[i] <= pivot_value:
           j += 1
           data[i], data[j] = data[j], data[i]

   data[left], data[j] = data[j], data[left]

   return j

def _solve(data, left, right):
    """If, for example, the length of the first part is shorter, then we
    make a recursive call to this part. And instead of making the recursive
    call for the second part, we just update the value of left.

    In the other case, when the right part is shorter, we make the recursive
    call for this part. And instead of making the recursive call for this
    part, we just update the value of right.

    So overall this gives us an implementation of the Quick Sort algorithm,
    which uses in the worst case an additional logarithmic space.
    """
    while left < right:
        split_point = _partition(data, left, right)
        if (split_point - left) < (right - split_point):
            _solve(data, left, split_point - 1)
            left = split_point + 1
        else:
            _solve(data, split_point + 1, right)
            right = split_point - 1

def solve(data):
    """Sorts the array of data.
    """
    _solve(data, 0, len(data) - 1)

if __name__ == '__main__':
    data = list(map(int, input().split()))

    solve(data)
    print(data)
