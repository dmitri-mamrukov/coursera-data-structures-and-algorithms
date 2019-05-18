#!/usr/bin/python3

import sys

DEBUG = False

def __check_args(a, b):
    assert(len(a) == len(b))

def min_dot_product(a, b):
    """The goal is, given two sequences a1, a2, ..., an and
    b1, b2, ..., bn, finds a permutation p of the second sequence
    such that the dot product of a1, a2, ..., an and bp1, bp2, ..., bpn
    is minimum.

    Greedy Strategy:

    Select the maximum from a and the minimum from b. Their product is the
    current minimum. Remove these items from a and b. Continue on subsets.
    Otherwise, we are done.

    Alternatively, we can search for the minimum from a
    and the maximum from b.

    Safety Proof:

    Every time we select the maximum from a and the minimum from b,
    their product is the current minimum. So a sum of minimums is
    guaranteed to be minimal.

    More formally. We claim that it is safe to multiply a maximum element of a
    by a minimum element of b. We illustrate this by a toy example. Assume
    that n = 4 and that a2 = max { a1, a2, a3, a4 } and
    b1 = min { b1, b2, b3, b4 }.

    Consider a candidate solution:

    a1 * b3 + a2 * b4 + a3 * b1 + a4 * b2.

    Here, a2 is multiplied by b4 and b1 is multiplied by a3. Let’s show that
    if we “swap” these two pairs, then the total value can only decrease.
    Indeed, the difference between dot products of these two solutions is
    equal to

    (a1 * b3 + a2 * b4 + a3 * b1 + a4 * b2) −
    (a1 * b3 + a2 * b1 + a3 * b4 + a4 * b2) =

    a2 * b4 + a3 * b1 − a2 * b1 − a3 * b4 = (a2 − a3)(b4 − b1).

    It is non-negative, since a2 ≥ a3 and b4 ≥ b1.
    """
    __check_args(a, b)

    if DEBUG:
        print('a: %s' % a)
        print('b: %s' % b)

    result = 0

    while len(a) > 0:
        max_index = 0
        for i in range(0, len(a)):
            if a[i] > a[max_index]:
                max_index = i

        min_index = 0
        for i in range(0, len(b)):
            if b[i] < b[min_index]:
                min_index = i

        result += a[max_index] * b[min_index]

        if DEBUG:
            print('selecting: %s * %s = %s' %
                (a[max_index], b[min_index], a[max_index] * b[min_index]))

        del a[max_index]
        del b[min_index]

    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]

    print(min_dot_product(a, b))
