#!/usr/bin/python3

import io
import sys

class RopeSplayTree:
    """
    Splay tree based rope implementation.
    """

    class Vertex:
        """
        Defines a vertex of a splay tree.
        """

        def __init__(self, key, sum, left, right, parent):
            self.key, self.left, self.right, self.parent = \
                                                      (key, left, right, parent)
            # the number of nodes below this one (including itself)
            self.sum = sum

        def __str__(self):
            return str(self.key)

        def __repr__(self):
            return '[key: {}, sum: {}, left: {}, right: {}, parent: {}]'. \
                     format(self.key, self.sum, str(self.left), str(self.right),
                            str(self.parent))

    def _update(self, v):
        if v is None:
            return

        v.sum = (1 + (v.left.sum if v.left is not None else 0) +
            (v.right.sum if v.right is not None else 0))

        if v.left is not None:
            v.left.parent = v
        if v.right is not None:
            v.right.parent = v

    def _small_rotation(self, v):
        # zig step
        parent = v.parent
        if parent is None:
            return

        grandparent = v.parent.parent
        if parent.left == v:
            m = v.right
            v.right = parent
            parent.left = m
        else:
            m = v.left
            v.left = parent
            parent.right = m

        self._update(parent)
        self._update(v)

        v.parent = grandparent
        if grandparent is not None:
            if grandparent.left == parent:
                grandparent.left = v
            else:
                grandparent.right = v

    def _big_rotation(self, v):
        if v.parent.left == v and v.parent.parent.left == v.parent:
            # zig-zig step
            self._small_rotation(v.parent)
            self._small_rotation(v)
        elif v.parent.right == v and v.parent.parent.right == v.parent:
            # zig-zig step
            self._small_rotation(v.parent)
            self._small_rotation(v)
        else:
            # zig-zag step
            self._small_rotation(v)
            self._small_rotation(v)

    def splay(self, v):
        """
        Performs a splay of the given vertex and makes it the new root.

        Theory:

        When a node x is accessed, a splay operation is performed on x to move
        it to the root. To perform a splay operation we carry out a sequence of
        splay steps, each of which moves x closer to the root. By performing a
        splay operation on the node of interest after every access, the
        recently accessed nodes are kept near the root and the tree remains
        roughly balanced, so that we achieve the desired amortized time bounds.

        Each particular step depends on three factors:

            - x is the left or right child of its parent node p,

            - p is the root, and

            - p is the left or right child of its parent, g (the grandparent
              of x).

        Zig step: this step is done when p is the root. The tree is rotated on
        the edge between x and p.

        Zig-zig step: this step is done when p is not the root and x and
        p are either both right children or are both left children. The tree
        is rotated on the edge joining p with its parent g, then rotated on
        the edge joining x with p.

        Zig-zag step: this step is done when p is not the root and x is a
        right child and p is a left child or vice versa. The tree is rotated
        on the edge between p and x, and then rotated on the resulting edge
        between x and g.
        """

        if v is None:
            return None

        while v.parent is not None:
            if v.parent.parent is None:
                self._small_rotation(v)
                break

            self._big_rotation(v)

        return v

    def find(self, root, number_of_nodes_on_left):
        """
        Searches for the node which has 'number_of_nodes_on_left' nodes
        in the left side (including the node itself) in the tree with the
        given root and calls the splay function for the deepest visited node
        after that.

        If found, returns a pointer to that node.

        Otherwise, returns None.
        """

        v = root
        while v is not None:
            sum = v.left.sum if v.left is not None else 0

            if number_of_nodes_on_left == sum + 1:
                break
            if number_of_nodes_on_left < sum + 1:
                v = v.left
            elif number_of_nodes_on_left > sum + 1:
                v = v.right
                number_of_nodes_on_left -= sum + 1

        root = self.splay(v)

        return root

    def split(self, root, number_of_nodes_on_left):
        """
        Given a tree and an element x, returns two new trees: one containing
        all elements less than or equal to x and the other containing all
        elements greater than x. This can be done in the following way:

        - Splay x. Now it is in the root so the tree to its left contains
          all elements smaller than x and the tree to its right contains
          all element larger than x.
        - Split the right subtree from the rest of the tree.
        """

        right = self.find(root, number_of_nodes_on_left)

        if right is None:
            return (root, None)

        left = right.left
        right.left = None

        if left is not None:
          left.parent = None

        self._update(left)
        self._update(right)

        return (left, right)

    def merge(self, left, right):
        """
        Given two trees S and T such that all elements of S are smaller than
        the elements of T, the following steps can be used to join them to a
        single tree:

        - Splay the largest item in S. Now this item is in the root of S and
          has a null right child.
        - Set the right child of the new root to T.
        """

        if left is None:
            return right
        if right is None:
            return left

        while right.left is not None:
            right = right.left

        right = self.splay(right)
        right.left = left

        self._update(right)

        return right

class Rope():

    def __init__(self, string):
        self._string = string
        self._tree = RopeSplayTree()
        self._root = None

        for ch in string:
            next = RopeSplayTree.Vertex(ch, 1, None, None, None)
            self._root = self._tree.merge(self._root, next)

    def _insert(self, root, pos, substring_node):
        left, right = self._tree.split(root, pos)
        merged = self._tree.merge(left, substring_node)
        root = self._tree.merge(merged, right)

        return root

    def _traverse_in_order(self, root):
        text = ''

        if root is None:
            return text

        stack = []
        node = root
        while node is not None:
            stack.append(node)
            node = node.left

        while len(stack) > 0:
            node = stack.pop()
            text += node.key
            node = node.right
            while node is not None:
                stack.append(node)
                node = node.left

        return text

    def result(self):
        return self._traverse_in_order(self._root)

    def process(self, i, j, k):
        if i > j:
            i, j = j, i

        left, middle = self._tree.split(self._root, i + 1)
        middle, right = self._tree.split(middle, j - i + 2)
        self._root = self._tree.merge(left, right)
        self._root = self._insert(self._root, k + 1, middle)

class Solver:
    """
    You are given a string S and you have to process n queries. Each query is
    described by three integers i, j, k and means to cut substring S[i..j]
    (i and j are 0-based) from the string and then insert it after the k-th
    symbol of the remaining string (if the symbols are numbered from 1).
    If k = 0, S[i..j] is inserted in the beginning.
    """

    def __init__(self):
        if __name__ == '__main__':
            input_stream = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
            self.input_processor = input_stream

    def _input(self):
        return self.input_processor.readline().strip()

    def _output(self, text):
        print(text)

    def solve(self):
        text = self._input()
        n = int(self._input())

        rope = Rope(text)
        for _ in range(n):
            i, j, k = map(int, self._input().split())
            rope.process(i, j, k)

        self._output(rope.result())

if __name__ == '__main__':
    Solver().solve()
