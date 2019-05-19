#!/usr/bin/python3

from collections import namedtuple
import sys
import threading

NodeInfo = namedtuple('NodeInfo', 'index parent')

class TreeHeight:
    def init(self, n, parents):
        self.n = n
        self.parents = parents

    def _compute_height_helper(self, info, root_index):
        if root_index not in info:
            return 0

        max_height = 0

        children = info[root_index]
        for c in children:
            height = self._compute_height_helper(info, c)
            if max_height < height:
                max_height = height

        return 1 + max_height

    def compute_height(self):
        info = {}
        for i in range(self.n):
            key = self.parents[i]
            if key not in info:
                info[key] = []
            info[key].append(i)

        root_index = -1

        return self._compute_height_helper(info, root_index)

    def _binary_search(self, data, key, compare):
        """Finds the first index of the key in the array if any.
        Otherwise, the returns -1 (the item is not found).

        In case of duplicates, the leftmost duplicate's index is considered
        to be the first index of the duplicates.
        """
        low = 0
        high = len(data) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if compare(data[mid], key) == 0:
                if mid - 1 >= low and compare(data[mid - 1], key) == 0:
                    high = mid - 1
                else:
                    return mid
            elif compare(data[mid], key) == 1:
                high = mid - 1
            else:
                low = mid + 1

        return -1

    def _compare_node_infos(self, data, key):
        if data.parent < key:
            return -1
        elif data.parent == key:
            return 0
        else:
            return 1

    def _compute_height_helper_still_slow(self, info, root_index):
        if root_index == -1:
            return 0

        max_height = 0

        child_index = self._binary_search(info, info[root_index].index,
            self._compare_node_infos)
        if child_index != -1:
            sibling_index = child_index
            while (sibling_index < len(info) and
                info[child_index].parent == info[sibling_index].parent):
                height = self._compute_height_helper_still_slow(info,
                    sibling_index)
                if max_height < height:
                    max_height = height
                sibling_index += 1

        return 1 + max_height

    def compute_height_still_slow(self):
        info = []
        for i in range(self.n):
            info.append(NodeInfo(i, self.parents[i]))
        info = sorted(info, key = lambda x: x.parent)

        root_index = self._binary_search(info, -1, self._compare_node_infos)

        return self._compute_height_helper_still_slow(info, root_index)

    def compute_height_slow(self):
        max_height = 0
        for vertex in range(self.n):
            height = 0
            i = vertex
            while i != -1:
                height += 1
                i = self.parents[i]
            max_height = max(max_height, height)

        return max_height

def _check_input(n, parents):
    assert(n == len(parents))

    root_count = 0
    node_count = 0
    for p in parents:
        if p == -1:
            root_count += 1
        else:
            assert(0 <= p)
            node_count += 1

    assert(1 == root_count)
    assert(n == 1 + node_count)

def process(n, parents):
    """You are given a description of a rooted tree. Your task is to compute
    and output its height. Recall that the height of a (rooted) tree is the
    maximum depth of a node, or the maximum distance from a leaf to the root.
    You are given an arbitrary tree, not necessarily a binary tree.

    Input Format: The first line contains the number of vertices n. The second
    line contains n integer numbers from −1 to n − 1 — parents of vertices.
    If the i-th one of them (0 ≤ i ≤ n − 1) is −1, vertex i is the root,
    otherwise it’s a 0-based index of the parent of i-th vertex. It is
    guaranteed that there is exactly one root. It is guaranteed that the
    input represents a tree.

    Example Input:

    5
    4 -1  4  1  1

    Explanation:

    The input means that there are 5 nodes with numbers from 0 to 4, node 0 is
    a child of node 4, node 1 is the root, node 2 is a child of node 4, node 3
    is a child of node 1, and node 4 is a child of node 1. To see this, let us
    write numbers of nodes from 0 to 4 in one line and the numbers given in
    the input in the second line underneath:

    Indices: 0  1  2  3  4
    Nodes:   4 -1  4  1  1

    Now we can see that the node number 1 is the root, because −1 corresponds
    to it in the second line. Also, we know that the nodes number 3 and number
    4 are children of the root node 1. Also, we know that the nodes number 0
    and number 2 are children of the node 4.

            1
           / \
          3   4
             / \
            0   2

    The height of this tree is 3, because the number of vertices on the path
    from root 1 to leaf 2 is 3.

    Example Input:

    5
    -1  0  4  0  3

    Explanation:

    Indices:  0  1  2  3  4
    Nodes:   -1  0  4  0  3

    The input means that there are 5 nodes with numbers from 0 to 4, node 0 is
    the root, node 1 is a child of node 0, node 2 is a child of node 4,
    node 3 is a child of node 0, and node 4 is a child of node 3.

            0
           / \
          1   3
              |
              4
              |
              2

    The height of this tree is 4, because the number of vertices on the path
    from root 0 to leaf 2 is 4.

    Note: The tree is not necessarily binary.
    """
    _check_input(n, parents)

    tree = TreeHeight()
    tree.init(n, parents)

    return tree.compute_height()

def main():
    n = int(sys.stdin.readline())
    parents = list(map(int, sys.stdin.readline().split()))
    print(process(n, parents))

if __name__ == '__main__':
    """Instructor Michael Levin: Not only those three lines are critical for
    everything to work correctly, but also creating and starting a Thread
    object and calling your solution function inside it, because you set the
    stack size for threading, not for the whole program.
    """
    sys.setrecursionlimit(10**7) # max depth of recursion
    threading.stack_size(2**25)  # a new thread will get a stack of such a size
    threading.Thread(target = main).start()
