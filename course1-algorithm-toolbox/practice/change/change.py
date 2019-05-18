#!/usr/bin/python3

import sys

def change(money, coins):
    """The goal in this problem is to find the minimum number of coins needed
    to make a change.

    Note: The algorithm also tells if the money can be fully changed.
    """

    if money == 0 or len(coins) == 0:
        return []

    changes = (money + 1) * [ None ]
    change_coins = (money + 1) * [ None ]
    changes[0] = 0

    for m in range(1, money + 1):
        coin_index = None
        min = None
        for c in range(0, len(coins)):
            if coins[c] <= m:
                val = changes[m - coins[c]]
                if val == None:
                    # m - coins[c] cannot be fully changed
                    continue
                n = val + 1
                if min == None or n < min:
                    min = n
                    coin_index = c

        changes[m] = min
        change_coins[m] = coin_index

    answer = []
    m = money
    while m > 0:
        if change_coins[m] == None:
            # the money cannot be fully changed
            answer.clear()
            break
        coin = coins[change_coins[m]]
        answer.append(coin)
        m = m - coin

    return answer

if __name__ == '__main__':
    coins = list(map(int, input().split()))
    money = int(input())

    print(change(money, coins))
