class Stack:

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

    def top(self):
        if len(self._list) == 0:
            raise Exception('The stack is empty.')

        return self._list[-1]

    def push(self, element):
        return self._list.append(element)

    def pop(self):
        if len(self._list) == 0:
            raise Exception('The stack is empty.')

        return self._list.pop(-1)
