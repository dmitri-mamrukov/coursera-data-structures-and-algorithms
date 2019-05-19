#!/usr/bin/python3

class MinBinHeap:

    def __init__(self):
        self._size = 0
        self._heap_list = []

    def __str__(self):
        return str(self._heap_list)

    def __repr__(self):
        return ('[size=' + str(self.size) +
            ', list=' + str(self._heap_list) + ']')

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

    def _min_child(self, i):
        if self._right_child(i) >= self.size:
            return self._left_child(i)
        else:
            left_child = self._left_child(i)
            right_child = self._right_child(i)
            if self._heap_list[left_child] < self._heap_list[right_child]:
                return left_child
            else:
                return right_child

    def _sift_down(self, i):
        while self._left_child(i) < self.size:
            min_child = self._min_child(i)

            if self._heap_list[i] > self._heap_list[min_child]:
                self._heap_list[i], self._heap_list[min_child] = \
                    self._heap_list[min_child], self._heap_list[i]

            i = min_child

    def _sift_down_and_gen_swaps(self, i, swaps):
        while self._left_child(i) < self.size:
            min_child = self._min_child(i)

            if self._heap_list[i] > self._heap_list[min_child]:
                self._heap_list[i], self._heap_list[min_child] = \
                    self._heap_list[min_child], self._heap_list[i]
                swaps.append((i, min_child))

            i = min_child

    def _sift_up(self, i):
        while self._parent(i) >= 0:
            parent = self._parent(i)

            if self._heap_list[i] < self._heap_list[parent]:
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

    def build_and_gen_swaps(self, list):
        self._size = len(list)
        self._heap_list = list

        swaps = []
        i = self._parent(self.size - 1)
        while i >= 0:
            self._sift_down_and_gen_swaps(i, swaps)
            i -= 1

        return swaps

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

        old_priority = self._heap_list[i]
        self._heap_list[i] = p
        if p > old_priority:
            self._sift_down(i)
        else:
            self._sift_up(i)

class HeapBuilder:

    def __init__(self):
        self._swaps = []
        self._data = []

    def read_data(self):
        n = int(input())
        self._data = [ int(s) for s in input().split() ]
        assert n == len(self._data)

    def write_response(self):
        print(len(self._swaps))
        for swap in self._swaps:
            print(swap[0], swap[1])

    def generate_swaps(self):
        """
        The first step of the HeapSort algorithm is to create a heap from the
        array you want to sort. By the way, did you know that algorithms
        based on Heaps are widely used for external sort, when you need to
        sort huge files that dont fit into memory of a computer?

        Your task is to implement this first step and convert a given array
        of integers into a heap. You will do that by applying a certain number
        of swaps to the array. Swap is an operation which exchanges elements
        ai and aj of the array a for some i and j. You will need to convert
        the array into a heap using only O(n) swaps, as was described in the
        lectures. Note that you will need to use a min-heap instead of a
        max-heap in this problem.
        """
        heap = MinBinHeap()
        self._swaps = heap.build_and_gen_swaps(self._data)

    def generate_swaps_slow(self):
        # The following naive implementation just sorts
        # the given sequence using the selection sort algorithm
        # and saves the resulting sequence of swaps.
        #
        # This turns the given array into a heap,
        # but in the worst case gives a quadratic number of swaps.
        #
        # TODO: Replace by a more efficient implementation.
        for i in range(len(self._data)):
            for j in range(i + 1, len(self._data)):
                if self._data[i] > self._data[j]:
                    self._swaps.append((i, j))
                    self._data[i], self._data[j] = self._data[j], self._data[i]

    def solve(self):
        self.read_data()
        self.generate_swaps()
        self.write_response()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.solve()
