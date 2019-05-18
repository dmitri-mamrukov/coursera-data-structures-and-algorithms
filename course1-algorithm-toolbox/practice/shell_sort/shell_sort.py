#!/usr/bin/python3

import sys

DEBUG = False

def gap_insertion_sort(data, start, gap):
    for i in range(start + gap, len(data), gap):
        value = data[i]
        position = i
        while position >= gap and data[position - gap] > value:
            data[position] = data[position - gap]
            position = position - gap

        data[position] = value

def solve(data):
    """Sorts the array of data.

    Shell Sort, sometimes called the “diminishing increment sort”, improves
    on the insertion sort by breaking the original list into a number of
    smaller sublists, each of which is sorted using an insertion sort.
    The unique way that these sublists are chosen is the key to the shell
    sort. Instead of breaking the list into sublists of contiguous items,
    the shell sort uses an increment i, sometimes called the gap, to create
    a sublist by choosing all items that are i items apart.

    Example:

    54 26 93 17 77 31 44 55 20

    This list has nine items. If we use an increment of three, there are
    three sublists, each of which can be sorted by an insertion sort.

    A Shell Sort with Increments of Three:
    --------------------------------------

    *54  26  93 *17  77  31 *44  55  20 - sublist 1
     54 *26  93  17 *77  31  44 *55  20 - sublist 2
     54  26 *93  17  77 *31  44  55 *20 - sublist 3

    After completing these sorts, we get the list shown below.

    A Shell Sort after Sorting Each Sublist:
    ----------------------------------------

    *17  26  93 *44  77  31 *54  55  20 - sublist 1 sorted
     54 *26  93  17 *55  31  44 *77  20 - sublist 2 sorted
     54  26 *20  17  77 *31  44  55 *93 - sublist 3 sorted

    Positionally, the starred elements are ordered as:

    17 26 20 44 55 31 54 77 93.

    Although this list is not completely sorted, something very interesting
    has happened. By sorting the sublists, we have moved the items closer to
    where they actually belong.

    Illustration below shows a final insertion sort using an increment of one;
    in other words, a standard insertion sort. Note that by performing the
    earlier sublist sorts, we have now reduced the total number of shifting
    operations necessary to put the list in its final order. For this case,
    we need only four more shifts to complete the process.

    Shell Sort: A Final Insertion Sort with Increment of 1:
    -------------------------------------------------------

    17 26 20 44 55 31 54 77 93
        ^--
    17 20 26 44 55 31 54 77 93 - 1 shift for 20
             ^------
    17 20 26 31 44 55 54 77 93 - 1 shift for 31
                    ^--
    17 20 26 31 44 54 55 77 93 - 1 shift for 54

    17 20 26 31 44 54 55 77 93 - sorted

    The way in which the increments are chosen is the unique feature
    of the shell sort.

    We use a different set of increments. In this case, we begin with
    n / 2 sublists. On the next pass, n / 4 sublists are sorted.
    Eventually, a single list is sorted with the basic insertion sort.

    Example:

    54 26 93 17 77 31 44 55 20

    Initial Sublists for a Shell Sort:
    ----------------------------------

    *54  26  93  17 *77  31  44  55 *20 - sublist 1
     54 *26  93  17  77 *31  44  55  20 - sublist 2
     54  26 *93  17  77  31 *44  55  20 - sublist 3
     54  26  93 *17  77  31  44 *55  20 - sublist 4
    """
    sublist_count = len(data) // 2
    while sublist_count > 0:
        for start in range(0, sublist_count):
            gap_insertion_sort(data, start, sublist_count)

        if DEBUG:
            print("After increment of size: %s, the list is %s" %
                (sublist_count, data))

        sublist_count = sublist_count // 2

if __name__ == '__main__':
    data = list(map(int, input().split()))

    solve(data)
    print(data)
