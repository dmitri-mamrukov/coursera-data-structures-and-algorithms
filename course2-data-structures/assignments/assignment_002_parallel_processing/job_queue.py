#!/usr/bin/python3

from enum import Enum
import heapq

class HeapMode(Enum):
    min = 0
    max = 1

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

    def _has_greater_priority(self, x, y):
        if self.mode == HeapMode.min:
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
                self._heap_list[right_child]):
                return left_child
            else:
                return right_child

    def _sift_down(self, i):
        while self._left_child(i) < self.size:
            priority_child = self._priority_child(i)

            if self._has_greater_priority(
                self._heap_list[priority_child],
                self._heap_list[i]):
                self._heap_list[i], self._heap_list[priority_child] = \
                    self._heap_list[priority_child], self._heap_list[i]

            i = priority_child

    def _sift_up(self, i):
        while self._parent(i) >= 0:
            parent = self._parent(i)

            if self._has_greater_priority(
                self._heap_list[i],
                self._heap_list[parent]):
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

        old_item = (self._heap_list[i][0], self._heap_list[i][1])
        new_item = (p, self._heap_list[i][1])
        self._heap_list[i] = new_item
        if self._has_greater_priority(new_item, old_item):
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

class Solver:

    @staticmethod
    def assign_jobs(assigned_workers, start_times, n, jobs):
        heap = []
        for i in range(n):
            heap.append((0, i))
        heapq.heapify(heap)

        for i in range(len(jobs)):
            next_worker = heap[0]

            assigned_workers[i] = next_worker[1]
            start_times[i] = next_worker[0]

            heapq.heapreplace(heap, (next_worker[0] + jobs[i], next_worker[1]))

    @staticmethod
    def assign_jobs_still_bit_slow(assigned_workers, start_times, n, jobs):
        heap = BinHeap(HeapMode.min)
        items = []
        for i in range(n):
            items.append((0, i))
        heap.build(items)

        for i in range(len(jobs)):
            next_worker = heap._heap_list[0]

            assigned_workers[i] = next_worker[1]
            start_times[i] = next_worker[0]

            heap.change_priority(0, next_worker[0] + jobs[i])

    @staticmethod
    def assign_jobs_still_slow(assigned_workers, start_times, n, jobs):
        heap = BinHeap(HeapMode.min)
        items = []
        for i in range(n):
            items.append((0, i))
        heap.build(items)

        for i in range(len(jobs)):
            next_worker = heap._heap_list[0]
            next_worker_index = 0
            for j in range(1, heap.size):
                if (heap._heap_list[j][0] == next_worker[0] and
                    heap._heap_list[j][1] < next_worker[1]):
                    next_worker = heap._heap_list[j]
                    next_worker_index = j

            assigned_workers[i] = next_worker[1]
            start_times[i] = next_worker[0]

            heap.change_priority(next_worker_index,
                next_worker[0] + jobs[i])

    @staticmethod
    def assign_jobs_slow(assigned_workers, start_times, n, jobs):
        next_free_time = [ 0 ] * n

        for i in range(len(jobs)):
            next_worker = 0
            for j in range(n):
                if next_free_time[j] < next_free_time[next_worker]:
                    next_worker = j

            assigned_workers[i] = next_worker
            start_times[i] = next_free_time[next_worker]

            next_free_time[next_worker] += jobs[i]

class JobQueue:

    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert m == len(self.jobs)

    def write_response(self):
        for i in range(len(self.jobs)):
            print(self.assigned_workers[i], self.start_times[i])

    def assign_jobs(self):
        self.assigned_workers = [ None ] * len(self.jobs)
        self.start_times = [ None ] * len(self.jobs)

        Solver.assign_jobs(self.assigned_workers, self.start_times,
            self.num_workers, self.jobs)

    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()
