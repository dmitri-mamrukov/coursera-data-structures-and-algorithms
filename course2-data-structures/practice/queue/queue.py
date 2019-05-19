class Queue:

    def __init__(self):
        self._list = []

    def __str__(self):
        return str(self._list)

    def __repr__(self):
        return str(self._list)

    def empty(self):
        return len(self._list) == 0

    def size(self):
        return len(self._list)

    def enqueue(self, element):
        return self._list.insert(0, element)

    def dequeue(self):
        if len(self._list) == 0:
            raise Exception('The queue is empty.')

        return self._list.pop(-1)
