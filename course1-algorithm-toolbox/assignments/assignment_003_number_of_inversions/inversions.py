#!/usr/bin/python3

import sys

DEBUG = False

def __merge(a, b, left, mid, right):
    """Merges two sorted lists a and b and returns the number of pairs (b, c)
    such that b ∈ B, c ∈ C, and b > c.

    How to get the number of inversions in the merge process?

    Let i is used for indexing the left sublist and j for the right sublist.
    At any step in the merge process, if a[i] is greater than a[j], then there
    are (mid - i) inversions, because the left and right sublists are sorted,
    so all the remaining elements in left sublist (a[i + 1], a[i + 2], ...,
    a[mid]) will be greater than a[j].
    """
    number_of_inversions = 0

    i = left # the index for the left sublist
    j = mid  # the index for the right sublist
    k = left # the index for the result sublist
    while (i <= mid - 1) and (j < right):
        if a[i] <= a[j]:
            b[k] = a[i]
            k += 1
            i += 1
        else:
            b[k] = a[j]
            k += 1
            j += 1

            number_of_inversions += mid - i

    # copy the remaining elements of the left sublist if any
    while i <= mid - 1:
        b[k] = a[i]
        k += 1
        i += 1
    # copy the remaining elements of the right sublist if any
    while j < right:
        b[k] = a[j]
        k += 1
        j += 1

    # move the merged elements to the original list
    for i in range(left, right):
        a[i] = b[i]

    return number_of_inversions

def __merge_sort(a, b, left, right):
    """An inversion of a sequence a0, a1, ..., an−1 is a pair of indices
    0 ≤ i < j < n such that ai > aj. The number of inversions of a sequence
    in some sense measures how close the sequence is to being sorted. For
    example, a sorted (in non-descending order) sequence contains no
    inversions at all, while in a sequence sorted in descending order
    any two elements constitute an inversion (for a total of
    n (n − 1) / 2 inversions because (n - 1) + (n - 2) + ... + 1 =
    n (n - 1) / 2).

    Returns a sorted array A and the number of inversions in A.
    """
    number_of_inversions = 0

    if right - left <= 1:
        return number_of_inversions

    mid = (left + right) // 2
    number_of_inversions += __merge_sort(a, b, left, mid)
    number_of_inversions += __merge_sort(a, b, mid, right)
    number_of_inversions += __merge(a, b, left, mid, right)

    return number_of_inversions

def merge_sort(a):
    b = len(a) * [0]

    return __merge_sort(a, b, 0, len(a))

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))

    if DEBUG:
        print('before: ' + str(a))

    print(merge_sort(a))

    if DEBUG:
        print('after: ' + str(a))
