#!/usr/bin/python3

import sys

def _check_args_count_segments(starts, ends, points):
    assert(len(starts) == len(ends))

def _check_args_quick_sort(data1, data2):
    assert(len(data1) == len(data2))

def _check_args_sort_segments(data1, data2):
    assert(len(data1) == len(data2))

def _find_segments(starts, point):
    low = 0
    high = len(starts) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if starts[mid] <= point:
            low = mid + 1
        else:
            high = mid - 1

    return low - 1

def _count_segments(starts, ends, left, right, point):

    if left >= right:
        return 0

    mid = (right - left) // 2
    if starts[mid] <= point <= ends[mid]:
        return (_count_segments(starts, ends, left, mid - 1, point) +
            _count_segments(starts, ends, mid + 1, right, point) + 1)
    else:
        return (_count_segments(starts, ends, left, mid - 1, point) +
            _count_segments(starts, ends, mid + 1, right, point))

def _less_than(a, b):
    return a < b

def _greater_than(a, b):
    return a > b

def _partition_on_two_lists(data1, data2, left, right, compare_function):
   pivot_value = data1[left]

   j = left

   for i in range(left + 1, right + 1):
       if compare_function(data1[i], pivot_value):
           j += 1
           data1[i], data1[j] = data1[j], data1[i]
           data2[i], data2[j] = data2[j], data2[i]

   data1[left], data1[j] = data1[j], data1[left]
   data2[left], data2[j] = data2[j], data2[left]

   return j

def _quick_sort_on_two_lists(data1, data2, left, right, compare_function):
   if left >= right:
       return

   split_point = _partition_on_two_lists(data1, data2, left, right,
        compare_function)
   _quick_sort_on_two_lists(data1, data2, left, split_point - 1,
        compare_function)
   _quick_sort_on_two_lists(data1, data2, split_point + 1, right,
        compare_function)

def quick_sort_on_two_lists(data1, data2, compare_function):
    """Sorts the corresponding arrays of data. These arrays are of the same
    length n and data1[i] is associated with data2[i] for every i between 0
    and n. So the sorting will sort data1 according to its contents and
    correspondingly re-arrange indices of data2.
    """
    _check_args_quick_sort(data1, data2)

    _quick_sort_on_two_lists(data1, data2, 0, len(data1) - 1, compare_function)

def sort_segments(starts, ends):
    _check_args_sort_segments(starts, ends)

    # sort segments by starts
    _quick_sort_on_two_lists(starts, ends, 0, len(starts) - 1, _less_than)

    # sort segments by lengths as determined by ends
    i, j = 0, 0
    for j in range(1, len(starts)):
        if starts[i] < starts[j]:
            _quick_sort_on_two_lists(ends, starts, i, j - 1, _less_than)
            i = j
    if i != j:
        _quick_sort_on_two_lists(ends, starts, i, j, _less_than)

def fast_count_segments_slow(starts, ends, points):
    """In this problem you are given a set of points on a line and a set of
    segments on a line. The goal is to compute, for each point, the number
    of segments that contain this point.

    If you sort the list by starting value, and then again (for the same
    starting value) by length, you end up with the roots of an efficient
    algorithm.

    - Sort the list by starting value.
    - For the same starting value, sort by length in the ascending order.

    Then, when you need the number of line segments that overlap a given
    point p:

    for a given value p
        find the points in the list with starting value <= p
        (use the binary search, which is fast)

        for each starting value, start with the longest length
            if it spans the point of interest, increment the counter
            if not, go to the next smaller start value
            keep going until you have reached the smallest starting value

    It's not perfect, but a lot better than searching through millions of
    points. Although the initial sort will take some time, obviously.
    But you only need to do it once.
    """
    _check_args_count_segments(starts, ends, points)

    counts = [ 0 ] * len(points)

    sort_segments(starts, ends)
    if len(starts) > 0:
        for i, p in enumerate(points):
            pos = _find_segments(starts, p)
            k = pos if pos != -1 else 0
            while k >= 0:
                if starts[k] <= p <= ends[k]:
                    counts[i] += 1
                k -= 1

    return counts

def naive_count_segments(starts, ends, points):
    _check_args_count_segments(starts, ends, points)

    counts = [ 0 ] * len(points)

    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                counts[i] += 1

    return counts

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]

    counts = fast_count_segments(starts, ends, points)

    for x in counts:
        print(x, end = ' ')
    print()
