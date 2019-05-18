#!/usr/bin/python3

import sys

def __partition(data, left, right):
   pivot_value = data[left]

   j = left

   for i in range(left + 1, right + 1):
       if data[i] <= pivot_value:
           j += 1
           data[i], data[j] = data[j], data[i]

   data[left], data[j] = data[j], data[left]

   return j

def __solve(data, left, right):
   while left < right:
       split_point = __partition(data, left, right)
       __solve(data, left, split_point - 1)
       left = split_point + 1

def solve(data):
    """Sorts the array of data.
    """
    __solve(data, 0, len(data) - 1)

if __name__ == '__main__':
    data = list(map(int, input().split()))

    solve(data)
    print(data)
