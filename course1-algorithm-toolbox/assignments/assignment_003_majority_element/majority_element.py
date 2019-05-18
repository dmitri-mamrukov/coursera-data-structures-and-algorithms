#!/usr/bin/python3

import math
import sys

DEBUG = False

def __get_frequency(data, left, right, element):
    if element == None:
        return 0

    count = 0
    for i in range(left, right):
        if data[i] == element:
            count += 1

    return count

def __get_majority_element(data, left, right):
    """An element of a sequence of length n is called a majority element
    if it appears in the sequence strictly more than n / 2 times.

    The goal in this code problem is to check whether an input sequence
    contains a majority element.

    Hint:

    This problem can be solved by the divide-and-conquer algorithm in time
    O(n log n). Indeed, if a sequence of length n contains a majority
    element, then the same element is also a majority element for one of
    its halves. Thus, to solve this problem you first split a given sequence
    into halves and make two recursive calls. Do you see how to combine
    the results of two recursive calls?

    Approach:

    Classical divide and conquer: split A into two subsets, A1 and A2.
    If A has a majority element v, v must also be a majority element of
    A1 or A2 or both.

    The equivalent contra-positive restatement is immediate: (If v is <= half
    in each, it is <= half in the total.) If both parts have the same majority
    element, it is automatically the majority element for A.

    If both parts have the same majority, we return it.

    If one of the parts has a majority element, count the number of repetitions
    of that element in both parts (in O(n) time) to see if it is a majority
    element.

    If both parts have different majorities, you may need to do this count
    for each of the two candidates, still O(n).

    This splitting can be done recursively. The base case is when n = 1. A
    recurrence relation is T(n) = 2 T(n / 2) + O(n), so T(n) is O(n log n)
    by the Master Theorem.
    """
    if DEBUG:
        print('__get_majority_element: left = %s, right = %s' % (left, right))

    if left == right:
        return None
    if left + 1 == right:
        return data[left]

    mid = (right + left) // 2
    majority_element1 = __get_majority_element(data, left, mid)
    majority_element2 = __get_majority_element(data, mid, right)

    if DEBUG:
        print('majority_element1 = %s, majority_element2 = %s'
              % (majority_element1, majority_element2))

    if majority_element1 == majority_element2:
        return majority_element1

    majority_element1_count = __get_frequency(data, left, right,
        majority_element1)
    majority_element2_count = __get_frequency(data, left, right,
        majority_element2)

    if DEBUG:
        print('majority_element1_count = %s, majority_element2_count = %s'
              % (majority_element1_count, majority_element2_count))

    count = (right - left) // 2
    if majority_element1_count > count:
        return majority_element1
    elif majority_element2_count > count:
        return majority_element2
    else:
        return None

def solve(data):

    return __get_majority_element(data, 0, len(data))

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = list(map(int, input.split()))

    result = solve(data)

    if DEBUG:
        print('majority element: %s' % result)

    if result == None:
        print(0)
    else:
        print(1)
