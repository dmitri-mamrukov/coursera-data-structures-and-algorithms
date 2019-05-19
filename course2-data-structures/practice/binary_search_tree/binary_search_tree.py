#!/usr/bin/python3

class TreeNode:
    """
    Defines the binary search tree node.
    """

    def __init__(self, key, value, left=None, right=None, parent=None):
        """
        Initializes the node.
        """

        self.key = key
        self.value = value
        self.left_child = left
        self.right_child = right
        self.parent = parent
        self.height = 0

        if self.left_child is not None:
            self.left_child.parent = self
        if self.right_child is not None:
            self.right_child.parent = self

        self.update_heights()

    def __str__(self):
        """
        Returns the string representation.
        """

        return 'key: {}, value: {}'.format(self.key, self.value)

    def __repr__(self):
        """
        Returns the string representation.
        """

        text = ('key: {}, value: {}, parent: [{}], left: [{}], right: [{}], ' +
                'height: {}')
        return text.format(self.key,
                           self.value,
                           str(self.parent),
                           str(self.left_child),
                           str(self.right_child),
                           self.height)

    def __iter__(self):
        """
        Iterates over all the keys in the tree (starting with this node)
        in order.

        Traverses the binary tree in order, using the inorder traversal
        algorithm.

        At first glance you might think that the code is not recursive.
        However, remember that __iter__ overrides the 'for x in' operation
        for iteration, so it really is recursive!
        """

        if self:
            if self.has_left_child():
                for key in self.left_child:
                    yield key

        yield self.key

        if self.has_right_child():
            for key in self.right_child:
                yield key

    def has_left_child(self):
        """
        Returns the truth value that indicates whether the node has a left
        child.
        """

        return self.left_child is not None

    def has_right_child(self):
        """
        Returns the truth value that indicates whether the node has a right
        child.
        """

        return self.right_child is not None

    def is_left_child(self):
        """
        Returns the truth value that indicates whether the node is a left
        child of its parent.
        """

        return self.parent is not None and self.parent.left_child == self

    def is_right_child(self):
        """
        Returns the truth value that indicates whether the node is a right
        child of its parent.
        """

        return self.parent is not None and self.parent.right_child == self

    def is_root(self):
        """
        Returns the truth value that indicates whether the node is the root,
        that is, it has no parent.
        """

        return self.parent is None

    def is_leaf(self):
        """
        Returns the truth value that indicates whether the node is a leaf,
        that is, it has no children.
        """

        return self.right_child is None and self.left_child is None

    def has_any_children(self):
        """
        Returns the truth value that indicates whether the node has either a
        left or right child.
        """

        return self.left_child is not None or self.right_child is not None

    def has_both_children(self):
        """
        Returns the truth value that indicates whether the node has both a
        left or right child.
        """

        return self.left_child is not None and self.right_child is not None

    def replace_node_data(self, key, value, left, right):
        """
        Replaces the node's attributes and updates the parent attribute of its
        left and right children if any.
        """

        self.key = key
        self.value = value
        self.left_child = left
        self.right_child = right
        if self.has_left_child():
            self.left_child.parent = self
        if self.has_right_child():
            self.right_child.parent = self

        self.update_heights()

    def find_min(self):
        """
        Returns the minimum valued key, which is the leftmost child of the tree.

        Note: To be called on a TreeNode object.
        """

        current = self
        while current is not None and current.has_left_child():
            current = current.left_child

        return current

    def find_successor(self):
        """
        Returns the successor of this node.

        If the node has a right child, then the successor is the smallest key
        in the right subtree.

        If the node has no right child and is the left child of its parent,
        then the parent is the successor.

        If the node is the right child of its parent and itself has no right
        child, then the successor to this node is the successor of its parent,
        excluding this node.
        """

        successor = None
        if self.has_right_child():
            successor = self.right_child.find_min()
        else:
            if self.parent is not None:
                if self.is_left_child():
                    successor = self.parent
                else:
                    self.parent.right_child = None
                    successor = self.parent.find_successor()
                    self.parent.right_child = self

        return successor

    def splice_out(self):
        """
        Goes directly to the node we want to splice out and makes the right
        changes.

        If the node is a leaf, then:

            - If it is the parent's left child, then that is deleted.

                B    B
               /  ->
              A

            - If it is the parent's right child, then that is deleted.

              A      A
               \  ->
                B

        If the node has at least one child, then:

            - If it has a left child, then:

                - If it is the parent's left child, then the node's left child
                  becomes that.

                      C      C
                     /      /
                    B   -> A
                   /
                  A

                - If it is the parent's right child, then the node's left child
                  becomes that.

                  A      A
                   \      \
                    C ->   B
                   /
                  B

            - If it has a right child, then:

                - If it is the parent's left child, then the node's right child
                  becomes that.

                    C      C
                   /      /
                  A   -> B
                   \
                    B

                - If it is the parent's right child, then the node's right child
                  becomes that.

                  A        A
                   \        \
                    B   ->   C
                     \
                      C
        """

        if self.is_root():
            return

        if self.is_leaf():
            if self.is_left_child():
                self.parent.left_child = None
            else:
                self.parent.right_child = None

            self.parent.update_heights()
        elif self.has_any_children():
            if self.has_left_child():
                if self.is_left_child():
                    self.parent.left_child = self.left_child
                else:
                    self.parent.right_child = self.left_child
                self.left_child.parent = self.parent

                self.left_child.update_heights()
            else:
                if self.is_left_child():
                    self.parent.left_child = self.right_child
                else:
                    self.parent.right_child = self.right_child
                self.right_child.parent = self.parent

                self.right_child.update_heights()

    def update_heights(self):
        """
        Updates heights from this node toward the root.
        """

        node = self
        while node is not None:
            height = 0
            if node.has_any_children():
                height = (1 + max((node.left_child.height
                                   if node.left_child is not None else 0),
                                  (node.right_child.height
                                   if node.right_child is not None else 0)))
            node.height = height

            node = node.parent

    def balance_factor(self):
        """
        We define the balance factor for a node as the difference between the
        height of the left subtree and the height of the right subtree.

            balance_factor = height(left_sub_tree) - height(right_sub_tree)

        Using the definition for balance factor given above we say that a
        subtree is left-heavy if the balance factor is greater than zero. If
        the balance factor is less than zero then the subtree is right heavy.
        If the balance factor is zero then the tree is perfectly in balance.

        We define a tree to be in balance if the balance factor is -1, 0, or 1.
        """

        if not self.has_any_children():
            return 0
        if self.has_both_children():
            return self.left_child.height - self.right_child.height
        if self.has_left_child():
            return 1 + self.left_child.height
        if self.has_right_child():
            return -(1 + self.right_child.height)

class BinarySearchTree:
    """
    Defines the binary search tree.
    """

    def __init__(self):
        """
        Initializes the tree.
        """

        self.root = None
        self._size = 0

        self._node_type = TreeNode

    def __str__(self):
        """
        Returns the string representation.
        """

        return 'root: [{}], size: {}'.format(self.root, self._size)

    def __repr__(self):
        """
        Returns the string representation.
        """

        if self.root is None:
            return 'None'

        nodes = [ self.root ]

        texts = []
        while len(nodes) > 0:
            node = nodes.pop()

            texts.append('[{}]'.format(repr(node)))

            if node.left_child is not None:
                nodes.append(node.left_child)
            if node.right_child is not None:
                nodes.append(node.right_child)

        return '{}, nodes: '.format(str(self)) + ', '.join(texts)

    def __len__(self):
        """
        Returns the tree's size.
        """

        return self._size

    def __getitem__(self, key):
        """
        Returns the node associated with the key if any.
        """

        return self.get(key)

    def __setitem__(self, k, v):
        """
        Adds the item to the tree.
        """

        self.put(k, v)

    def __delitem__(self, key):
        """
        Deletes the node associated with the key.
        """

        self.delete(key)

    def __contains__(self, key):
        """
        Returns the truth value that indicates whether the node associated with
        the key is in the tree.
        """

        if self._get(key, self.root):
            return True
        else:
            return False

    def __iter__(self):
        """
        Returns the tree's iterator.
        """

        return self.root.__iter__()

    def _get(self, key, current_node):
        """
        Returns the node associated with the key.

        If not found, returns None.
        """

        if current_node is None:
            return None
        elif current_node.key == key:
            return current_node
        elif key < current_node.key:
            return self._get(key, current_node.left_child)
        else:
            return self._get(key, current_node.right_child)

    def _do_update(self, node):
        node.update_heights()

    def _put(self, key, value, current_node):
        """
        Inserts the node associated with the key.

        Returns the truth value that indicates whether the key is duplicate.
        """

        if key == current_node.key:
            current_node.replace_node_data(key,
                                           value,
                                           current_node.left_child,
                                           current_node.right_child)
            return True
        elif key < current_node.key:
            if current_node.has_left_child():
                return self._put(key, value, current_node.left_child)
            else:
                current_node.left_child = self._node_type(key,
                                                          value,
                                                          parent=current_node)

                current_node.left_child._height = current_node.height + 1
                self._do_update(current_node)

                return False
        else:
            if current_node.has_right_child():
                return self._put(key, value, current_node.right_child)
            else:
                current_node.right_child = self._node_type(key,
                                                           value,
                                                           parent=current_node)
                current_node.right_child._height = current_node.height + 1
                self._do_update(current_node)

                return False

    def _remove(self, current_node):
        """
        Once we’ve found the node containing the key we want to delete, there
        are three cases that we must consider:

            - The node to be deleted has no children.
            - The node to be deleted has only one child.
            - The node to be deleted has two children.
        """

        if current_node.is_leaf():
            if current_node == current_node.parent.left_child:
                current_node.parent.left_child = None
            else:
                current_node.parent.right_child = None

            self._do_update(current_node.parent)
        elif current_node.has_both_children():
            successor = current_node.find_successor()
            # splicing out already takes care of the height update
            successor.splice_out()
            current_node.key = successor.key
            current_node.value = successor.value
        else:
            if current_node.has_left_child():
                if current_node.is_left_child():
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.left_child

                    self._do_update(current_node.left_child)
                elif current_node.is_right_child():
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.left_child

                    self._do_update(current_node.left_child)
                else:
                    # data replacing already takes care of the height update
                    current_node.replace_node_data(
                                            current_node.left_child.key,
                                            current_node.left_child.value,
                                            current_node.left_child.left_child,
                                            current_node.left_child.right_child)
            else:
                if current_node.is_left_child():
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.right_child

                    self._do_update(current_node.right_child)
                elif current_node.is_right_child():
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.right_child

                    self._do_update(current_node.right_child)
                else:
                    # data replacing already takes care of the height update
                    current_node.replace_node_data(
                                           current_node.right_child.key,
                                           current_node.right_child.value,
                                           current_node.right_child.left_child,
                                           current_node.right_child.right_child)

    @property
    def size(self):
        """
        Returns the tree's size.
        """

        return self._size

    def get(self, key):
        """
        Returns the node associated with the key if any.

        If not found, returns None.
        """

        if self.root is not None:
            result = self._get(key, self.root)
            if result:
                return result.value
            else:
                return None
        else:
            return None

    def put(self, key, value):
        """
        Inserts the node associated with the key.

        Correctly handles insertion of a duplicate key.

        It is important to handle duplicate keys properly. Otherwise, a
        duplicate key will create a new node with the same key value in the
        right subtree of the node having the original key. The result of this
        is that the node with the new key will never be found during a search.

        So, to handle the insertion of a duplicate key, the value associated
        with the new key replaces the old value.
        """

        is_duplicate = False

        if self.root is not None:
            is_duplicate = self._put(key, value, self.root)
        else:
            self.root = self._node_type(key, value)

        if not is_duplicate:
            self._size = self.size + 1

    def delete(self, key):
        """
        Deletes the node containing the key if any. Otherwise, raises a
        KeyError.
        """

        if self._size > 1:
            node_to_remove = self._get(key, self.root)
            if node_to_remove is not None:
                self._remove(node_to_remove)
                self._size = self.size - 1
            else:
                raise KeyError('The key not in the tree.')
        elif self._size == 1 and self.root.key == key:
            self.root = None
            self._size = self._size - 1
        else:
            raise KeyError('The key not in the tree.')

class AvlTree(BinarySearchTree):
    """
    Defines the AVL balanced binary search tree node.

    Theory:

    An AVL tree implements an abstract data type just like a regular binary
    search tree, the only difference is in how the tree performs. To implement
    our AVL tree we need to keep track of a balance factor for each node in
    the tree. We do this by looking at the heights of the left and right
    subtrees for each node. More formally, we define the balance factor for a
    node as the difference between the height of the left subtree and the
    height of the right subtree.

    balance_factor = height(left_sub_tree) - height(right_sub_tree)

    Using the definition for balance factor given above we say that a subtree
    is left-heavy if the balance factor is greater than zero. If the balance
    factor is less than zero then the subtree is right heavy. If the balance
    factor is zero then the tree is perfectly in balance. For purposes of
    implementing an AVL tree, and gaining the benefit of having a balanced tree
    we will define a tree to be in balance if the balance factor is -1, 0, or 1.
    """

    def _do_update(self, node):
        super(AvlTree, self)._do_update(node)

        if node.balance_factor() > 1 or node.balance_factor() < -1:
            self.rebalance(node)

    def rotate_left(self, rotation_root):
        """
        To perform a left rotation we essentially do the following:

            - Promote the right child to be the root of the subtree.
            - Move the old root to be the left child of the new root.
            - If the new root already had its left child then make it the
              right child of the new left child.
              Note: Since the new root was the right child of the old root,
              the right child of the old root is guaranteed to be empty at
              this point. This allows us to add a new node as the right child
              without any further consideration.

          B               D
         / \             / \
        A   D     -->   B   E
           / \         / \
          C   E       A   C

        B and D are the pivotal nodes and A, C, and E are their subtrees.
        """

        new_root = rotation_root.right_child
        rotation_root.right_child = new_root.left_child

        if new_root.left_child is not None:
            new_root.left_child.parent = rotation_root
        new_root.parent = rotation_root.parent

        if rotation_root.is_root():
            self.root = new_root
        else:
            if rotation_root.is_left_child():
                rotation_root.parent.left_child = new_root
            else:
                rotation_root.parent.right_child = new_root

        new_root.left_child = rotation_root
        rotation_root.parent = new_root

        rotation_root.update_heights()
        new_root.update_heights()

    def rotate_right(self, rotation_root):
        """
        To perform a right rotation we essentially do the following:

            - Promote the left child to be the root of the subtree.
            - Move the old root to be the right child of the new root.
            - If the new root already had its right child then make it the
              left child of the new right child.
              Note: Since the new root was the left child of the old root,
              the left child of the old root is guaranteed to be empty at
              this point. This allows us to add a new node as the left child
              without any further consideration.

            D               B
           / \             / \
          B   E     -->   A   D
         / \                 / \
        A   C               C   E

        D and B are the pivotal nodes and A, C, and E are their subtrees.
        """

        new_root = rotation_root.left_child
        rotation_root.left_child = new_root.right_child

        if new_root.right_child is not None:
            new_root.right_child.parent = rotation_root
        new_root.parent = rotation_root.parent

        if rotation_root.is_root():
            self.root = new_root
        else:
            if rotation_root.is_left_child():
                rotation_root.parent.left_child = new_root
            else:
                rotation_root.parent.right_child = new_root

        new_root.right_child = rotation_root
        rotation_root.parent = new_root

        rotation_root.update_heights()
        new_root.update_heights()

    def rebalance(self, node):
        """
        The node is out of balance, so the tree is re-balanced around it.
        """

        if node.balance_factor() < 0:
            if node.right_child.balance_factor() > 0:
                self.rotate_right(node.right_child)
                self.rotate_left(node)
            else:
                self.rotate_left(node)
        elif node.balance_factor() > 0:
            if node.left_child.balance_factor() < 0:
                self.rotate_left(node.left_child)
                self.rotate_right(node)
            else:
                self.rotate_right(node)
