class UnionFind:

    def make_set(self, x):
        x.parent = x
        x.rank = 0

    def union(self, x, y):
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
        if x.parent == x:
            return x
        else:
            x.parent = self.find(x.parent)

            return x.parent

