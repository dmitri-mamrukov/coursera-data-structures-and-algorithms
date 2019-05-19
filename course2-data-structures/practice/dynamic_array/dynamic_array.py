class DynamicArray:

    def __init__(self):
        self._size = 0
        self._capacity = 2
        self._array = [ None ] * self._capacity

    def __str__(self):
        return str(self._array)

    def __repr__(self):
        return ('[size=' + str(self._size) + ', capacity=' +
            str(self._capacity) + ', array=' + str(self._array) + ']')

    @property
    def size(self):
        return self._size

    def get(self, i):
        if i < 0 or i >= self._size:
            raise IndexError()

        return self._array[i]

    def set(self, i, value):
        if i < 0 or i >= self._size:
            raise IndexError()

        self._array[i] = value

    def push_back(self, element):
        if self._size == self._capacity:
            new_array = [ None ] * 2 * self._capacity

            for i, v in enumerate(self._array):
                new_array[i] = v

            self._array =  new_array
            self._capacity *= 2

        self._array[self._size] = element

        self._size += 1

    def remove(self, i):
        if i < 0 or i >= self._size:
            raise IndexError()

        element = self._array[i]

        for j in range(i, self._size - 1):
            self._array[j] = self._array[j + 1]
        self._array[self._size - 1] = None

        self._size -= 1

        return element
