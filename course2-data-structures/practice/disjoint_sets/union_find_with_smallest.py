class UnionFindWithSmallest:

    def __init__(self, n):
        if n <= 0:
            raise ValueError('n must be > 0.')

        self.smallest = [ 0 ] * n

    def __str__(self):
        return str(self.smallest)

    def __repr__(self):
        return str(self.smallest)

    def make_set(self, x):
        if x < 0 or x >= len(self.smallest):
            raise ValueError("x must be within the set's range.")

        self.smallest[x] = x

    def find(self, x):
        if x < 0 or x >= len(self.smallest):
            raise ValueError("x must be within the set's range.")

        return self.smallest[x]

    def union(self, x, y):
        if x < 0 or x >= len(self.smallest):
            raise ValueError("x must be within the set's range.")
        if y < 0 or y >= len(self.smallest):
            raise ValueError("y must be within the set's range.")

        x_id = self.find(x)
        y_id = self.find(y)

        if x_id == y_id:
            return

        min_id = min(x_id, y_id)
        ids = [ x_id, y_id ]
        for k in range(0, len(self.smallest)):
            if self.smallest[k] in ids:
                self.smallest[k] = min_id
