#!/usr/bin/python3

def __check_args(n):
    assert(0 <= n)

def get_fibonacci_last_digit(n):
    """Computing the last digit of Fi is easy: it is just the last digit of
    the sum of the last digits of Fi−1 and Fi−2:

    Fi mod 10 = (Fi−1 + Fi−2) mod 10
    """
    __check_args(n)

    a, b = 0, 1

    for i in range(0, n):
        a, b = b, (a + b) % 10

    return a

if __name__ == '__main__':
    n = int(input())

    print(get_fibonacci_last_digit(n))
