#!/usr/bin/python3

import io
import sys

class BaseSplayTree:
    """
    Splay tree implementation.

    A splay tree is a self-adjusting binary search tree with the additional
    property that recently accessed elements are quick to access again. It
    performs basic operations such as insertion, look-up and removal in
    O(log n) amortized time. For many sequences of non-random operations,
    splay trees perform better than other search trees, even when the specific
    pattern of the sequence is unknown. The splay tree was invented by
    Daniel Sleator and Robert Tarjan in 1985.

    All normal operations on a binary search tree are combined with one basic
    operation, called splaying. Splaying the tree for a certain element
    rearranges the tree so that the element is placed at the root of the tree.

    One way to do this is to first perform a standard binary tree search for
    the element in question, and then use tree rotations in a specific fashion
    to bring the element to the top.

    Alternatively, a top-down algorithm can combine the search and the tree
    reorganization into a single phase.
    """

    class Vertex:
        """
        Defines a vertex of a splay tree.
        """

        def __init__(self, key, left, right, parent):
            self.key, self.left, self.right, self.parent = \
                                                      (key, left, right, parent)

        def __str__(self):
            return str(self.key)

        def __repr__(self):
            return '[key: {}, left: {}, right: {}, parent: {}]'. \
                               format(self.key, str(self.left), str(self.right),
                                      str(self.parent))

    def __init__(self):
        pass

    def _update(self, v):
        if v is None:
            return

        self._update_augmented_properties(v)

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

    def find(self, root, key):
        """
        Searches for the given key in the tree with the given root and calls
        the splay function for the deepest visited node after that.

        Returns a pair of the result and the new root.

        If found, the result is a pointer to the node with the given key.
        Otherwise, the result is a pointer to the node with the smallest
        bigger key (the next value in the order).

        If the key is bigger than all keys in the tree, then result is None.
        """

        v = root
        last = root
        next = None
        while v is not None:
            if v.key >= key and (next is None or v.key < next.key):
                next = v

            last = v

            if v.key == key:
                break
            if v.key < key:
                v = v.right
            else:
                v = v.left

        root = self.splay(last)

        return (next, root)

    def split(self, root, key):
        """
        Given a tree and an element x, returns two new trees: one containing
        all elements less than or equal to x and the other containing all
        elements greater than x. This can be done in the following way:

        - Splay x. Now it is in the root so the tree to its left contains
          all elements smaller than x and the tree to its right contains
          all element larger than x.
        - Split the right subtree from the rest of the tree.
        """

        result, root = self.find(root, key)

        if result is None:
            return (root, None)

        right = self.splay(result)
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

class SumSplayTree(BaseSplayTree):

    class Vertex(BaseSplayTree.Vertex):
        """
        Defines a vertex of a splay tree.
        """

        def __init__(self, key, sum, left, right, parent):
            super(SumSplayTree.Vertex, self).__init__(key, left, right, parent)
            self.sum = sum

        def __repr__(self):
            return '[key: {}, sum: {}, left: {}, right: {}, parent: {}]'. \
                format(self.key, self.sum, str(self.left), str(self.right),
                str(self.parent))

    def __init__(self):
        pass

    def _update_augmented_properties(self, v):
        v.sum = (v.key + (v.left.sum if v.left is not None else 0) +
            (v.right.sum if v.right is not None else 0))

class Set:
    """
    Implements a data structure that stores a set S of integers with the
    following allowed operations:

        - add(i) — add integer i into the set S (if it was there already,
          the set doesn’t change).
        - del(i) — remove integer i from the set S (if there was no such
          element, nothing happens).
        - find(i) — check whether i is in the set S or not.
        - sum(l, r) — output the sum of all elements v in S such that l ≤ v ≤ r.
    """

    def __init__(self):
        self._tree = SumSplayTree()
        self._root = None

    def insert(self, x):
        """
        Inserts integer i into the set S (if it was there already, the
        set doesn’t change).
        """

        left, right = self._tree.split(self._root, x)

        new_vertex = None
        if right is None or right.key != x:
            new_vertex = self._tree.Vertex(x, x, None, None, None)

        new_left = self._tree.merge(left, new_vertex)
        self._root = self._tree.merge(new_left, right)

    def erase(self, x):
        """
        Removes integer i from the set S (if there was no such element,
        nothing happens).
        """

        if not self.search(x):
            return

        self._tree.splay(self._root)

        self._root = self._tree.merge(self._root.left, self._root.right)
        if self._root is not None:
            self._root.parent = None

    def search(self, x):
        """
        Checks whether i is in the set S or not.
        """

        result, self._root = self._tree.find(self._root, x)
        if result is None or result.key != x:
            return False

        return True

    def sum(self, start, end):
        """
        Outputs the sum of all elements v in S such that l ≤ v ≤ r.
        """

        if end < start:
            raise ValueError('start must <= end.')

        left, middle = self._tree.split(self._root, start)
        middle, right = self._tree.split(middle, end + 1)
        answer = 0

        if middle is None:
            answer = 0
            self._root = self._tree.merge(left, right)
        else:
            answer = middle.sum
            new_left = self._tree.merge(left, middle)
            self._root = self._tree.merge(new_left, right)

        return answer

class Solver:
    """
    Your goal is to implement a data structure to store a set of integers and
    quickly compute range sums.
    """

    MODULO = 1000000001

    def __init__(self):
        if __name__ == '__main__':
            input_stream = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
            self.input_processor = input_stream

    def _input(self):
        return self.input_processor.readline().strip()

    def _output(self, text):
        print(text)

    def solve(self):
        n = int(self._input())

        set = Set()
        last_sum_result = 0
        for i in range(n):
            line = self._input().split()
            if line[0] == '+':
                x = int(line[1])
                set.insert((x + last_sum_result) % Solver.MODULO)
            elif line[0] == '-':
                x = int(line[1])
                set.erase((x + last_sum_result) % Solver.MODULO)
            elif line[0] == '?':
                x = int(line[1])
                result = set.search((x + last_sum_result) % Solver.MODULO)
                self._output('Found' if result else 'Not found')
            elif line[0] == 's':
                l = int(line[1])
                r = int(line[2])
                result = set.sum((l + last_sum_result) % Solver.MODULO,
                                 (r + last_sum_result) % Solver.MODULO)
                self._output(str(result))

                last_sum_result = result % Solver.MODULO

if __name__ == '__main__':
    Solver().solve()
