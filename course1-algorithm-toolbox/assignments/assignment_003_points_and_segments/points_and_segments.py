#!/usr/bin/python3

import sys

def _check_args_count_segments(starts, ends, points):
    assert(len(starts) == len(ends))

def _partition(data, left, right):
   pivot_value = data[left]

   j = left

   for i in range(left + 1, right + 1):
       if data[i] <= pivot_value:
           j += 1
           data[i], data[j] = data[j], data[i]

   data[left], data[j] = data[j], data[left]

   return j

def _quick_sort(data, left, right):
    while left < right:
        split_point = _partition(data, left, right)
        if (split_point - left) < (right - split_point):
            _quick_sort(data, left, split_point - 1)
            left = split_point + 1
        else:
            _quick_sort(data, split_point + 1, right)
            right = split_point - 1

def quick_sort(data):
    """Sorts the array of data.
    """
    _quick_sort(data, 0, len(data) - 1)

def _binary_search(data, key, rightmost_duplicates):
    """Finds the first index of the key in the array if any.
    Otherwise, the lowest index of the first value that is less
    than the key is returned.

    The rightmost_duplicates argument affects the handling of duplicates.

     - If rightmost_duplicates is True, then the rightmost duplicate's index
       is considered to be the first index of duplicates.
     - If rightmost_duplicates is False, then the leftmost duplicate's
       index is considered to be the first index of duplicates.
    """
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if data[mid] == key:
            if (rightmost_duplicates and
                mid + 1 <= high and data[mid + 1] == key):
                    low = mid + 1
            elif (not rightmost_duplicates and
                  mid - 1 >= low and data[mid - 1] == key):
                    high = mid - 1
            else:
                return mid
        elif key < data[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return low - 1

def fast_count_segments(starts, ends, points):
    """In this problem you are given a set of points on a line and a set of
    segments on a line. The goal is to compute, for each point, the number
    of segments that contain this point.

    This version uses the segment tree data structure.
    """
    _check_args_count_segments(starts, ends, points)
    counts = [ 0 ] * len(points)

    if len(points) == 0 or len(starts) == 0:
        return counts

    starts.sort()
    ends.sort()

    for i, p in enumerate(points):
        s = _binary_search(starts, p, True)
        if s == -1:
            continue
        e = _binary_search(ends, p, False)
        if e == -1:
            counts[i] += s + 1
        elif s == e and starts[s] <= p <= ends[e]:
            counts[i] += 1
        elif s != e:
            if starts[s] <= p <= ends[e]:
                counts[i] += abs(e - s) + 1
            else:
                counts[i] += abs(e - s)

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
