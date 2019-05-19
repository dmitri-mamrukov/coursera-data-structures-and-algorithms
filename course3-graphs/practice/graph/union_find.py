class Node:

    def __init__ (self, value):
        self.value = value
        self.parent = None
        self.rank = None

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return '[{}, parent={}, rank={}]'.format(self.value,
                                                 self.parent,
                                                 self.rank)

    def __lt__(self, other):
        if other is None or not isinstance(other, Node):
            return False

        return self.value < other.value

    def __eq__(self, other):
        if other is None or not isinstance(other, Node):
            return False

        return self.value == other.value

    def __gt__(self, other):
        if other is None or not isinstance(other, Node):
            return False

        return self.value > other.value

class UnionFind:

    def make_set(self, x):
        """
        Makes a set containing only a given element (a singleton).
        """

        x.parent = x
        x.rank = 0

    def union(self, x, y):
        """
        Combines two trees into one by attaching the root of one to the root
        of the other.
        """

        x_root = self.find(x)
        y_root = self.find(y)

        if x_root.rank > y_root.rank:
            y_root.parent = x_root
        elif x_root.rank < y_root.rank:
            x_root.parent = y_root
        elif x_root != y_root:
            # x and y are not in the same set, so merge them
            y_root.parent = x_root
            x_root.rank = x_root.rank + 1

    def find(self, x):
        """
        Follows parent nodes until it reaches the root.

        Applies path compression.
        """

        if x.parent == None:
            raise ValueError('{} not in the set.'.format(x))

        if x.parent == x:
            return x
        else:
            x.parent = self.find(x.parent)

            return x.parent
