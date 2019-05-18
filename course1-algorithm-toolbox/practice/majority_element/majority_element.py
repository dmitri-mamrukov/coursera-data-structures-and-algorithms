#!/usr/bin/python3

import math
import sys

DEBUG = False

def __get_majority_element(data, tiebreaker = None):
    """An element of a sequence of length n is called a majority element
    if it appears in the sequence strictly more than n / 2 times.

    Returns the majority element of sequence data or tiebreaker if exactly
    half of the elements in data are tiebreaker or None otherwise.

    Approach:

    The invariant needed for the solution is:

    Proposition P: Given a list L of n > 0 items, and a tiebreaker item, T,
    which may be None. A majority element is one that is a majority in L or
    is T if exactly half of L matches T. If there is a majority for (L, T)
    then there is the same majority for (L1, T1) where

    - L1 is formed by arbitrarily partitioning L into pairs, and including an
      element from each pair where the two elements are the same.
    - T1 is the odd unpaired element of L if n is odd, and T1 is T is n
      is even.

    The tiebreaker is not a part of the original problem (when T = None), but
    it can be a part of sub-problems. The tiebreaker can be thought to get a
    positive contribution to the vote, but less than one full vote. This is
    enough to break a tie, but not enough to overturn a majority with at least
    one extra vote.

    Proof:

    Assume there is a majority element M. Let m be the number of copies of M
    and u be the count of everything else, and e be the excess, m - u.
    Then having a direct majority element means e > 0. For the recursion you
    need to allow something more like the Senate with a tiebreaker vote T, so
    the more general requirements would be

    (e > 0) or (e == 0 and M == T)

    Throwing out unmatched pairs will decrease u at least as much as m, and
    hence not decrease e, so it will not invalidate the majority element.

    Consider two cases:

    1. If n is odd, the tiebreaker is irrelevant, since there will never be
       a tie. Since unmatched pairs are also tossed, it is enough to consider
       the L1 pairs and the odd extra element from L. The odd extra element
       does serve as a tiebreaker with the L1 pairs, since each pair gets
       essentially 2 votes, and the odd element only makes a difference if
       the vote exactly matches in L1, so the same majority will be found
       for (L1, T1).
    2. If n is even, e must be even. Then (e >= 0 and M == T) or (e >= 2).
       At the next level the numbers are halved, leaving (e >= 0 and M == T)
       or (e >=1), still implying M is the majority element.

    Algorithm:

    Note that the base case is when n is 0. At that point the majority element
    is the tiebreaker (which may be None).

    The implication in proposition P indicates that at each level there is
    at most one candidate for majority element, delivered from the base case
    or the next lower case down. The algorithm only needs to confirm that the
    one candidate from the recursive call is actually in the majority, or else
    there is no majority element.

    The initial call to the function is with tiebreaker = None, so any
    majority comes from an actual majority in the list.

    The non-recursive work is O(n) in traversing the list to make pairs before
    the recursive step and then O(n) again after the recursion to count
    proposed majority elements. This direct work is O(n), so the recurrence
    relation is T(n) = T(n / 2) + O(n), resulting in T(n) = O(n), by applying
    the Master Theorem.
    """
    n = len(data)

    if n == 0:
        return tiebreaker

    if n % 2 == 1:
        # the last element has no pair
        tiebreaker = data[-1]

    pairs = []
    for i in range(0, n - 1, 2):
        if data[i] == data[i + 1]:
            pairs.append(data[i])

    major = __get_majority_element(pairs, tiebreaker)
    if major is None:
        return None

    count_of_majors = data.count(major)
    if (2 * count_of_majors > n or
        (2 * count_of_majors == n and major == tiebreaker)):
        return major

    return None

def get_majority_element(data):
    return __get_majority_element(data)

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = list(map(int, input.split()))

    result = get_majority_element(data)

    if DEBUG:
        print('majority element: %s' % result)

    if result != None:
        print(1)
    else:
        print(0)
