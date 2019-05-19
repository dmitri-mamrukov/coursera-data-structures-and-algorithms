class TreeNode:

    def __init__(self, key, parent = None):
        self._parent = parent
        self._key = key
        self._left = None
        self._right = None

    def __str__(self):
        return str(self.key)

    def __repr__(self):
        return ('[key=' + str(self.key) + ', parent=' +
            str(self.parent) + ', left=' + str(self.left) +
            ', right=' + str(self.right) + ']')

    def _height(self, node, height):
        if node.left == None and node.right == None:
            return height

        height += 1
        left_child_height = height
        if node.left != None:
            left_child_height = self._height(node.left, height)
        right_child_height = height
        if node.right != None:
            right_child_height = self._height(node.right, height)

        return max(left_child_height, right_child_height)

    def _size(self, node, size):
        if node.left == None and node.right == None:
            return size

        if node.left != None:
            size += self._size(node.left, 1)
        if node.right != None:
            size += self._size(node.right, 1)

        return size

    @property
    def parent(self):
        return self._parent

    @property
    def key(self):
        return self._key

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right

    @property
    def height(self):
        return self._height(self, 0)

    @property
    def size(self):
        return self._size(self, 1)

    def set_left(self, key):
        node = TreeNode(key, self)
        self._left = node

        return node

    def set_right(self, key):
        node = TreeNode(key, self)
        self._right = node

        return node

    def depth_first_traverse(self, visitor):
        visitor(self)

        if self.left == None and self.right == None:
            return

        if self.left != None:
            self.left.depth_first_traverse(visitor)
        if self.right != None:
            self.right.depth_first_traverse(visitor)

    def depth_first_traverse_iterative(self, visitor):
        stack = []
        stack.append(self)
        while len(stack) > 0:
            node = stack.pop(0)
            visitor(node)
            if node.right != None:
                stack.insert(0, node.right)
            if node.left != None:
                stack.insert(0, node.left)

    def breadth_first_traverse(self, visitor):
        queue = []
        queue.append(self)
        while len(queue) > 0:
            node = queue.pop(0)
            visitor(node)
            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)

    def in_order_traverse(self, visitor):
        if self == None:
            return

        if self.left != None:
            self.left.in_order_traverse(visitor)

        visitor(self)

        if self.right != None:
            self.right.in_order_traverse(visitor)

    def pre_order_traverse(self, visitor):
        if self == None:
            return

        visitor(self)

        if self.left != None:
            self.left.pre_order_traverse(visitor)

        if self.right != None:
            self.right.pre_order_traverse(visitor)

    def post_order_traverse(self, visitor):
        if self == None:
            return

        if self.left != None:
            self.left.post_order_traverse(visitor)

        if self.right != None:
            self.right.post_order_traverse(visitor)

        visitor(self)

    def depth_first_traverse_gen(self):
        yield self

        queue = []
        if self.left != None:
            queue.append(self.left)
        if self.right != None:
            queue.append(self.right)
        while queue:
            yield queue[0]
            expansion = []
            if queue[0].left != None:
                expansion.append(queue[0].left)
            if queue[0].right != None:
                expansion.append(queue[0].right)
            queue = expansion + queue[1:]

    def breadth_first_traverse_gen(self):
        yield self

        queue = []
        if self.left != None:
            queue.append(self.left)
        if self.right != None:
            queue.append(self.right)
        while queue:
            yield queue[0]
            expansion = []
            if queue[0].left != None:
                expansion.append(queue[0].left)
            if queue[0].right != None:
                expansion.append(queue[0].right)
            queue = queue[1:] + expansion

    def _display(self, depth):
        if depth == 0:
            print(self)
        else:
            print(' ' * depth, self)

        if self.left != None:
            self.left._display(depth + 1)
        if self.right != None:
            self.right._display(depth + 1)

    def display(self):
        self._display(0)
