class TreeNode:

    def __init__(self, key, parent = None):
        self._parent = parent
        self._key = key
        self._children = []

    def __str__(self):
        return str(self.key)

    def __repr__(self):
        return ('[key=' + str(self.key) + ', parent=' +
            str(self.parent) + ', children=' + str(self.children) + ']')

    def _height(self, node, height):
        if len(node.children) == 0:
            return height

        height += 1
        max_height = height
        for child in node.children:
            child_height = self._height(child, height)
            if child_height > max_height:
                max_height = child_height

        return max_height

    def _size(self, node, size):
        if len(node.children) == 0:
            return size

        for child in node.children:
            size += self._size(child, 1)

        return size

    @property
    def parent(self):
        return self._parent

    @property
    def key(self):
        return self._key

    @property
    def children(self):
        return self._children

    @property
    def height(self):
        return self._height(self, 0)

    @property
    def size(self):
        return self._size(self, 1)

    def add_child(self, key):
        node = TreeNode(key, self)
        self.children.append(node)

        return node

    def depth_first_traverse(self, visitor):
        visitor(self)

        if len(self.children) == 0:
            return

        for child in self.children:
            child.depth_first_traverse(visitor)

    def depth_first_traverse_iterative(self, visitor):
        stack = []
        stack.append(self)
        while len(stack) > 0:
            node = stack.pop(0)
            visitor(node)
            stack = node.children + stack

    def breadth_first_traverse(self, visitor):
        queue = []
        queue.append(self)
        while len(queue) > 0:
            node = queue.pop(0)
            visitor(node)
            queue = queue + node.children

    def depth_first_traverse_gen(self):
        yield self

        queue = self.children
        while queue:
            yield queue[0]
            expansion = queue[0].children
            queue = expansion + queue[1:]

    def breadth_first_traverse_gen(self):
        yield self

        queue = self.children
        while queue:
            yield queue[0]
            expansion = queue[0].children
            queue = queue[1:] + expansion

    def _display(self, depth):
        if depth == 0:
            print(self)
        else:
            print(' ' * depth, self)

        for child in self.children:
            child._display(depth + 1)

    def display(self):
        self._display(0)
