from enum import Enum

class HeapMode(Enum):
    min = 0
    max = 1

class HeapItem:

    def __init__(self, priority, datum=None):
        self._priority = priority
        self._datum = datum

    def __str__(self):
        return str(self.datum)

    def __repr__(self):
        return ('[priority=' + str(self.priority) +
            ', datum=' + str(self.datum) + ']')

    def __lt__(self, other):
        if self.priority < other.priority:
            return True
        elif self.priority == other.priority:
            if (self.datum != None and other.datum != None and
                self.datum < other.datum):
                    return True

        return False

    def __eq__(self, other):
        return (self.priority == other.priority and
            self.datum == other.datum)

    def __gt__(self, other):
        if self.priority > other.priority:
            return True
        elif self.priority == other.priority:
            if (self.datum != None and other.datum != None and
                self.datum > other.datum):
                    return True

        return False

    @property
    def priority(self):
        return self._priority

    @property
    def datum(self):
        return self._datum

class BinHeap:

    def __init__(self, mode=HeapMode.min):
        self._mode = mode
        self._size = 0
        self._heap_list = []

    def __str__(self):
        return str(self._heap_list)

    def __repr__(self):
        return ('[mode=' + str(self.mode) + ', size=' + str(self.size) +
            ', list=' + str(self.elements) + ']')

    @property
    def mode(self):
        return self._mode

    @property
    def size(self):
        return self._size

    @property
    def elements(self):
        return self._heap_list

    def _parent(self, i):
        return (i - 1) // 2

    def _left_child(self, i):
        return 2 * i + 1

    def _right_child(self, i):
        return 2 * i + 2

    def _has_greater_priority(self, x, y, mode):
        if mode == HeapMode.min:
            return x < y
        else:
            return x > y

    def _priority_child(self, i):
        if self._right_child(i) >= self.size:
            return self._left_child(i)
        else:
            left_child = self._left_child(i)
            right_child = self._right_child(i)
            if self._has_greater_priority(
                self._heap_list[left_child],
                self._heap_list[right_child],
                self.mode):
                return left_child
            else:
                return right_child

    def _sift_down(self, i):
        while self._left_child(i) < self.size:
            priority_child = self._priority_child(i)

            if self._has_greater_priority(
                self._heap_list[priority_child],
                self._heap_list[i],
                self.mode):
                self._heap_list[i], self._heap_list[priority_child] = \
                    self._heap_list[priority_child], self._heap_list[i]

            i = priority_child

    def _sift_up(self, i):
        while self._parent(i) >= 0:
            parent = self._parent(i)

            if self._has_greater_priority(
                self._heap_list[i],
                self._heap_list[parent],
                self.mode):
                self._heap_list[i], self._heap_list[parent] = \
                    self._heap_list[parent], self._heap_list[i]

            i = parent

    def build(self, list):
        self._size = len(list)
        self._heap_list = list

        i = self._parent(self.size - 1)
        while i >= 0:
            self._sift_down(i)
            i -= 1

    def extract(self):
        min_element = self._heap_list[0]
        self._heap_list[0] = self._heap_list[self.size - 1]
        self._size = self.size - 1
        self._heap_list.pop()
        self._sift_down(0)

        return min_element

    def insert(self, i):
        self._heap_list.append(i)
        self._size = self.size + 1
        self._sift_up(self.size - 1)

    def change_priority(self, i, p):
        if i < 0 or i > self.size:
            raise IndexError()

        old_item = HeapItem(self._heap_list[i].priority,
            self._heap_list[i].datum)
        new_item = HeapItem(p, self._heap_list[i].datum)
        self._heap_list[i]._priority = p
        if self._has_greater_priority(new_item, old_item, self.mode):
            self._sift_up(i)
        else:
            self._sift_down(i)

    def sort_in_place(self, data):
        self.build(data)

        original_size = self.size
        for i in range(1, len(data)):
            self._heap_list[0], self._heap_list[self.size - 1] = \
                self._heap_list[self.size - 1], self._heap_list[0]
            self._size -= 1
            self._sift_down(0)

        self._size = original_size
