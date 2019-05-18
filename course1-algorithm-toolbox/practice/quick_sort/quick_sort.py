#!/usr/bin/python3

import sys

def __partition(data, first, last):
   pivot_value = data[first]

   left_mark = first + 1
   right_mark = last

   done = False
   while not done:
       while left_mark <= right_mark and data[left_mark] <= pivot_value:
           left_mark = left_mark + 1

       while data[right_mark] >= pivot_value and right_mark >= left_mark:
           right_mark = right_mark - 1

       if right_mark < left_mark:
           done = True
       else:
           data[left_mark], data[right_mark] = \
               data[right_mark], data[left_mark]

   data[first], data[right_mark] = data[right_mark], data[first]

   return right_mark

def __solve(data, first, last):
   if first < last:
       split_point = __partition(data, first, last)
       __solve(data, first, split_point - 1)
       __solve(data, split_point + 1, last)

def solve(data):
    """Sorts the array of data.

    Quick Sort uses divide and conquer to gain the same advantages as
    the merge sort, while not using additional storage. As a trade off,
    however, it is possible that the list may not be divided in half.
    When this happens, we will see that performance is diminished.

    Quick Sort first selects a value, which is called the pivot value.
    Although there are many different ways to choose the pivot value,
    we will simply use the first item in the list. The role of the pivot
    value is to assist with splitting the list. The actual position where
    the pivot value belongs in the final sorted list, commonly called
    the split point, will be used to divide the list for subsequent calls
    to the quick sort.

    The partition process will happen next. It will find the split point
    and at the same time move other items to the appropriate side of the
    list, either less than or greater than the pivot value.

    Partitioning begins by locating two position markers — let’s call them
    left_mark and right_mark — at the beginning and end of the remaining
    items in the list (positions 1 and n). The goal of the partition process
    is to move items that are on the wrong side with respect to the pivot
    value while also converging on the split point.

    We begin by incrementing left_mark until we locate a value that is greater
    than the pivot value. We then decrement right_mark until we find a value
    that is less than the pivot value. At this point we have discovered
    two items that are out of place with respect to the eventual split point.
    Now we can exchange these two items and then repeat the process again.

    At the point where right_mark becomes less than left_mark, we stop.
    The position of right_mark is now the split point. The pivot value can be
    exchanged with the contents of the split point and the pivot value is now
    in place. In addition, all the items to the left of the split point are
    less than the pivot value, and all the items to the right of the split
    point are greater than the pivot value. The list can now be divided at
    the split point and the quick sort can be invoked recursively on the two
    halves.
    """
    __solve(data, 0, len(data) - 1)

if __name__ == '__main__':
    data = list(map(int, input().split()))

    solve(data)
    print(data)
