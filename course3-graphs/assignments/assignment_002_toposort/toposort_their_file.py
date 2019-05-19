#!/usr/bin/python3

import sys

def dfs(adj, used, order, x):
    used.add(x)

    for neighbor in adj[x]:
        if neighbor not in used:
            dfs(adj, used, order, neighbor)

    order.insert(0, x)

def toposort(adj):
    used = set()
    order = []

    for x in range(len(adj)):
        if x not in used:
            dfs(adj, used, order, x)

    return order

    order = toposort(adj)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]

    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)

    order = toposort(adj)

    for x in order:
        print(x + 1, end=' ')
    print()
