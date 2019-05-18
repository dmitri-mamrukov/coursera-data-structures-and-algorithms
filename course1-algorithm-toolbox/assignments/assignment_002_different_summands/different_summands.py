#!/usr/bin/python3

import sys

DEBUG = False

def __check_args(n):
    assert(1 <= n)

def optimal_summands(n):
    """This is an example of a problem where a subproblem of the
    corresponding greedy algorithm is slightly distinct from the
    initial problem.

    The goal of this problem is to represent a given positive integer n
    as a sum of as many pairwise distinct positive integers as possible.
    That is, to find the maximum k such that n can be written as
    a1 + a2 + ... + ak where a1, ..., ak are positive integers and
    ai ≠ aj for all 1 ≤ i < j ≤ k.

    Greedy Strategy:

    To find an algorithm for this problem, you may want to play a little bit
    with small numbers. Assume, for example, that we want to represent 8 as
    a sum of as many pairwise distinct summands as possible. Well, it is
    natural to try to use 1 as the first summand, right? Then, the remaining
    problem is to represent 7 as a sum of the maximum number of pairwise
    distinct positive integers none of which is equal to 1. We then take
    2 and are left with the following problem: represent 5 as a sum of
    distinct positive integers each of which is at least 3. Clearly, we cannot
    use two summands in this case (do you see why?). Overall, this gives us
    the following optimal representation: 8 = 1 + 2 + 5.

    Safety Proof:

    In general, our subproblem is the following: given integers k and l,
    where l ≤ k, represent k as a sum of as many pairwise distinct integers
    each of which is at least l as possible. If k ≤ 2l, then the answer is
    clearly k. Otherwise, it is safe to use l as one of the summands.
    """
    __check_args(n)

    summands = []

    l = 1
    k = n
    while l <= k:
        if k <= 2 * l:
            summands.append(k)
            break
        else:
            summands.append(l)

        k -= l
        l += 1

    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)

    summands = optimal_summands(n)

    print(len(summands))
    for x in summands:
        print(x, end = ' ')
    print()
