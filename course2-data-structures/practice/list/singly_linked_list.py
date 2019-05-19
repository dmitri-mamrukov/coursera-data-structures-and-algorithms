class Sing1yLinkedListNode:

    def __init__(self, key, next = None):
        self._key = key
        self._next = next

    def __str__(self):
        return str(self._key)

    def __repr__(self):
        return ('[key=' + str(self._key) + ', next=' + str(self._next) + ']')

    @property
    def key(self):
        return self._key

    @property
    def next(self):
        return self._next

class Sing1yLinkedList:

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __str__(self):
        return ('[head=' + str(self._head) + ', tail=' + str(self._tail) +
            ', size=' + str(self._size) + ']')

    def __repr__(self):
        return ('[head=' + str(self._head) + ', tail=' + str(self._tail) +
            ', size=' + str(self._size) + ']')

    def _check_node_is_in_list(self, node):
        curr = self._head
        while curr != None:
            if curr == node:
                break
            curr = curr.next
        if curr == None:
            raise ValueError('The node is not in the list.')

    @property
    def size(self):
        return self._size

    @property
    def top_front(self):
        return self._head

    @property
    def top_back(self):
        return self._tail

    def empty(self):
        return self._size == 0

    def push_front(self, key):
        node = Sing1yLinkedListNode(key)
        node._next = self._head
        self._head = node

        if self._tail == None:
            self._tail = self._head

        self._size += 1

        return node

    def pop_front(self):
        if self._head == None:
            raise Exception('The list is empty.')

        node = self._head
        self._head = self._head.next

        if self._head == None:
            self._tail = None

        self._size -= 1

        return node

    def push_back(self, key):
        node = Sing1yLinkedListNode(key)
        node._next = None

        if self._tail == None:
            self._tail = node
            self._head = self._tail
        else:
            self._tail._next = node
            self._tail = node

        self._size += 1

        return node

    def pop_back(self):
        if self._head == None:
            raise Exception('The list is empty.')

        node = None

        if self._head == self._tail:
            node = self._head

            self._tail = None
            self._head = None
        else:
            curr = self._head
            while curr.next.next != None:
                curr = curr.next

            node = curr.next

            curr._next = None
            self._tail = curr

        self._size -= 1

        return node

    def add_after(self, node, key):
        if node == None:
            raise ValueError('The node cannot be None.')

        self._check_node_is_in_list(node)

        new_node = Sing1yLinkedListNode(key)
        new_node._next = node.next
        node._next = new_node

        if self._tail == node:
            self._tail = new_node

        self._size += 1

        return new_node

    def add_before(self, node, key):
        if node == None:
            raise ValueError('The node cannot be None.')

        self._check_node_is_in_list(node)

        prev, curr = None, self._head
        while curr != None:
            if curr == node:
                break
            prev = curr
            curr = curr.next

        new_node = Sing1yLinkedListNode(key)
        new_node._next = node

        if self._head == node:
            self._head = new_node
        else:
            prev._next = new_node

        self._size += 1

        return new_node

    def find(self, key):
        curr = self._head
        while curr != None:
            if curr.key == key:
                return curr
            curr = curr.next

        return None

    def erase(self, key):
        prev, curr = None, self._head
        while curr != None:
            if curr.key == key:
                if prev == None:
                    self._head = curr.next
                    if self._head == None:
                        self._tail = None
                else:
                    prev._next = curr.next
                    if prev._next == None:
                        self._tail = prev

                self._size -= 1

                return curr

            prev = curr
            curr = curr.next

        raise ValueError('The key is not in the list.')
