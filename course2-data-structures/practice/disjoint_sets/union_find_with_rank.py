class UnionFindWithRank:

    def __init__(self, n):
        if n <= 0:
            raise ValueError('n must be > 0.')

        self.parent = [ 0 ] * n
        self.rank = [ 0 ] * n

    def __str__(self):
        return '[parent=' + str(self.parent) + ', rank=' + str(self.rank) + ']'

    def __repr__(self):
        return '[parent=' + str(self.parent) + ', rank=' + str(self.rank) + ']'

    def make_set(self, x):
        if x < 0 or x >= len(self.parent):
            raise ValueError("x must be within the set's range.")

        self.parent[x] = x
        self.rank[x] = 0

    def union(self, x, y):
        if x < 0 or x >= len(self.parent):
            raise ValueError("x must be within the set's range.")
        if y < 0 or y >= len(self.parent):
            raise ValueError("y must be within the set's range.")

        x_id = self.find(x)
        y_id = self.find(y)

        if x_id == y_id:
            return
        elif self.rank[x_id] > self.rank[y_id]:
            self.parent[y_id] = x_id
        else:
            self.parent[x_id] = y_id
            if self.rank[x_id] == self.rank[y_id]:
                self.rank[y_id] = self.rank[y_id] + 1

    def find(self, x):
        if x < 0 or x >= len(self.parent):
            raise ValueError("x must be within the set's range.")

        while x != self.parent[x]:
            x = self.parent[x]

        return x
