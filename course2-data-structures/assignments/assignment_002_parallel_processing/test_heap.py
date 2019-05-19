#!/usr/bin/python3

import unittest

from job_queue import BinHeap, HeapMode

class BinHeapAsMinTestCase(unittest.TestCase):

    def setUp(self):
        self.heap = BinHeap(HeapMode.min)

    def tearDown(self):
        pass

    def test_constructor(self):
        self.assertEqual(0, self.heap.size)
        self.assertEqual([], self.heap.elements)

    def test_str_on_empty_heap(self):
        self.assertEqual('[]', str(self.heap))

    def test_repr_on_empty_heap(self):
        self.assertEqual('[mode=HeapMode.min, size=0, list=[]]',
            repr(self.heap))

    def test_str_on_three_element_heap(self):
        self.heap.build([ (1, 'datum1'), (2, 'datum2'), (3, 'datum3') ])

        self.assertEqual("[(1, 'datum1'), (2, 'datum2'), (3, 'datum3')]",
            str(self.heap))

    def test_repr_on_three_element_heap(self):
        self.heap.build([ (1, 'datum1'), (2, 'datum2'), (3, 'datum3') ])

        self.assertEqual("[mode=HeapMode.min, size=3, " +
            "list=[(1, 'datum1'), (2, 'datum2'), (3, 'datum3')]]",
            repr(self.heap))

    def test_build_on_empty_list(self):
        self.heap.build([])

        self.assertEqual(0, self.heap.size)
        self.assertEqual([], self.heap.elements)

    def test_build_on_one_element_list(self):
        self.heap.build([ (1, 'datum') ])

        self.assertEqual(1, self.heap.size)
        self.assertEqual([ (1, 'datum') ], self.heap.elements)

    def test_build_on_two_element_list_as_1_2(self):
        self.heap.build([ (1, 'datum'), (2, 'datum') ])

        self.assertEqual(2, self.heap.size)
        self.assertEqual([ (1, 'datum'), (2, 'datum') ], self.heap.elements)

    def test_build_on_two_element_list_as_2_1(self):
        self.heap.build([ (2, 'datum'), (1, 'datum') ])

        self.assertEqual(2, self.heap.size)
        self.assertEqual([ (1, 'datum'), (2, 'datum') ], self.heap.elements)

    def test_build_on_three_element_list_as_1_2_3(self):
        self.heap.build([ (1, 'datum'), (2, 'datum'), (3, 'datum') ])

        self.assertEqual(3, self.heap.size)
        self.assertEqual([ (1, 'datum'), (2, 'datum'), (3, 'datum') ],
            self.heap.elements)

    def test_build_on_three_element_list_as_1_3_2(self):
        self.heap.build([ (1, 'datum'), (3, 'datum'), (2, 'datum') ])

        self.assertEqual(3, self.heap.size)
        self.assertEqual([ (1, 'datum'), (3, 'datum'), (2, 'datum') ],
            self.heap.elements)

    def test_build_on_three_element_list_as_2_1_3(self):
        data = [ (2, 'datum'), (1, 'datum'), (3, 'datum') ]

        self.heap.build(data)

        self.assertEqual(3, self.heap.size)
        self.assertEqual([ (1, 'datum'), (2, 'datum'), (3, 'datum') ],
            self.heap.elements)

    def test_build_on_three_element_list_as_2_3_1(self):
        self.heap.build([ (2, 'datum'), (3, 'datum'), (1, 'datum') ])

        self.assertEqual(3, self.heap.size)
        self.assertEqual([ (1, 'datum'), (3, 'datum'), (2, 'datum') ],
            self.heap.elements)

    def test_build_on_three_element_list_as_3_1_2(self):
        self.heap.build([ (3, 'datum'), (1, 'datum'), (2, 'datum') ])

        self.assertEqual(3, self.heap.size)
        self.assertEqual([ (1, 'datum'), (3, 'datum'), (2, 'datum') ],
            self.heap.elements)

    def test_build_on_three_element_list_as_3_2_1(self):
        self.heap.build([ (3, 'datum'), (2, 'datum'), (1, 'datum') ])

        self.assertEqual(3, self.heap.size)
        self.assertEqual([ (1, 'datum'), (2, 'datum'), (3, 'datum') ],
            self.heap.elements)

    def test_build_on_four_element_list(self):
        self.heap.build([ (9, 'datum'), (5, 'datum'), (6, 'datum'),
            (2, 'datum') ])

        self.assertEqual(4, self.heap.size)
        self.assertEqual([ (2, 'datum'), (5, 'datum'), (6, 'datum'),
            (9, 'datum') ], self.heap.elements)

    def test_build_on_five_element_list(self):
        self.heap.build([ (9, 'datum'), (5, 'datum'), (6, 'datum'),
            (2, 'datum'), (3, 'datum') ])

        self.assertEqual(5, self.heap.size)
        self.assertEqual([ (2, 'datum'), (3, 'datum'), (6, 'datum'),
            (5, 'datum'), (9, 'datum') ], self.heap.elements)

    def test_build_on_six_element_list(self):
        self.heap.build([ (9, 'datum'), (5, 'datum'), (6, 'datum'),
            (2, 'datum'), (3, 'datum'), (1, 'datum') ])

        self.assertEqual(6, self.heap.size)
        self.assertEqual([ (1, 'datum'), (2, 'datum'), (6, 'datum'),
            (5, 'datum'), (3, 'datum'), (9, 'datum') ], self.heap.elements)

    def test_build_on_seven_element_list(self):
        self.heap.build([ (9, 'datum'), (5, 'datum'), (6, 'datum'),
            (2, 'datum'), (3, 'datum'), (1, 'datum'), (0, 'datum') ])

        self.assertEqual(7, self.heap.size)
        self.assertEqual([ (0, 'datum'), (2, 'datum'), (1, 'datum'),
            (5, 'datum'), (3, 'datum'), (9, 'datum'), (6, 'datum') ],
            self.heap.elements)

    def test_build_on_seven_element_list_with_duplicates(self):
        self.heap.build([ (9, 'datum'), (5, 'datum'), (2, 'datum'),
            (2, 'datum'), (1, 'datum'), (1, 'datum'), (0, 'datum') ])

        self.assertEqual(7, self.heap.size)
        self.assertEqual([ (0, 'datum'), (1, 'datum'), (1, 'datum'),
            (2, 'datum'), (5, 'datum'), (9, 'datum'), (2, 'datum') ],
            self.heap.elements)

    def test_build_on_seven_duplicate_element_list(self):
        self.heap.build([ (3, 'datum'), (3, 'datum'), (3, 'datum'),
            (3, 'datum'), (3, 'datum'), (3, 'datum'), (3, 'datum') ])

        self.assertEqual(7, self.heap.size)
        self.assertEqual([ (3, 'datum'), (3, 'datum'), (3, 'datum'),
            (3, 'datum'), (3, 'datum'), (3, 'datum'), (3, 'datum') ],
            self.heap.elements)

    def test_extract_on_five_element_list(self):
        self.heap.build([ (9, 'datum'), (5, 'datum'), (6, 'datum'),
            (2, 'datum'), (3, 'datum') ])

        self.assertEqual(5, self.heap.size)
        self.assertEqual([ (2, 'datum'), (3, 'datum'), (6, 'datum'),
            (5, 'datum'), (9, 'datum') ], self.heap.elements)

        min = self.heap.extract()

        self.assertEqual((2, 'datum'), min)
        self.assertEqual(4, self.heap.size)
        self.assertEqual([ (3, 'datum'), (5, 'datum'),
            (6, 'datum'), (9, 'datum') ], self.heap.elements)

        min = self.heap.extract()

        self.assertEqual((3, 'datum'), min)
        self.assertEqual(3, self.heap.size)
        self.assertEqual([ (5, 'datum'), (9, 'datum'), (6, 'datum') ],
            self.heap.elements)

        min = self.heap.extract()

        self.assertEqual((5, 'datum'), min)
        self.assertEqual(2, self.heap.size)
        self.assertEqual([ (6, 'datum'), (9, 'datum') ], self.heap.elements)

        min = self.heap.extract()

        self.assertEqual((6, 'datum'), min)
        self.assertEqual(1, self.heap.size)
        self.assertEqual([ (9, 'datum') ], self.heap.elements)

        min = self.heap.extract()

        self.assertEqual((9, 'datum'), min)
        self.assertEqual(0, self.heap.size)
        self.assertEqual([], self.heap.elements)

    def test_insert_on_empty_list(self):
        self.heap.insert((1, 'datum'))

        self.assertEqual(1, self.heap.size)
        self.assertEqual([ (1, 'datum') ], self.heap.elements)

    def test_insert_on_one_element_list(self):
        self.heap.build([ (2, 'datum') ])

        self.assertEqual(1, self.heap.size)
        self.assertEqual([ (2, 'datum') ], self.heap.elements)

        self.heap.insert((1, 'datum'))

        self.assertEqual(2, self.heap.size)
        self.assertEqual([ (1, 'datum'), (2, 'datum') ], self.heap.elements)

    def test_insert_on_two_element_list(self):
        self.heap.build([ (2, 'datum'), (3, 'datum') ])

        self.assertEqual(2, self.heap.size)
        self.assertEqual([ (2, 'datum'), (3, 'datum') ], self.heap.elements)

        self.heap.insert((1, 'datum'))

        self.assertEqual(3, self.heap.size)
        self.assertEqual([ (1, 'datum'), (3, 'datum'), (2, 'datum') ],
            self.heap.elements)

    def test_insert_on_three_element_list(self):
        self.heap.build([ (2, 'datum'), (3, 'datum'), (4, 'datum') ])

        self.assertEqual(3, self.heap.size)
        self.assertEqual([ (2, 'datum'), (3, 'datum'), (4, 'datum') ],
            self.heap.elements)

        self.heap.insert((1, 'datum'))

        self.assertEqual(4, self.heap.size)
        self.assertEqual([ (1, 'datum'), (2, 'datum'), (4, 'datum'),
            (3, 'datum') ], self.heap.elements)

    def test_insert_on_four_element_list(self):
        self.heap.build([ (2, 'datum'), (3, 'datum'), (4, 'datum'),
            (5, 'datum') ])

        self.assertEqual(4, self.heap.size)
        self.assertEqual([ (2, 'datum'), (3, 'datum'), (4, 'datum'),
            (5, 'datum') ], self.heap.elements)

        self.heap.insert((1, 'datum'))

        self.assertEqual(5, self.heap.size)
        self.assertEqual([ (1, 'datum'), (2, 'datum'), (4, 'datum'),
            (5, 'datum'), (3, 'datum') ], self.heap.elements)

    def test_insert_on_five_element_list(self):
        self.heap.build([ (2, 'datum'), (3, 'datum'), (6, 'datum'),
            (5, 'datum'), (9, 'datum') ])

        self.assertEqual(5, self.heap.size)
        self.assertEqual([ (2, 'datum'), (3, 'datum'), (6, 'datum'),
            (5, 'datum'), (9, 'datum') ], self.heap.elements)

        self.heap.insert((1, 'datum'))

        self.assertEqual(6, self.heap.size)
        self.assertEqual([ (1, 'datum'), (3, 'datum'), (2, 'datum'),
            (5, 'datum'), (9, 'datum'), (6, 'datum') ], self.heap.elements)

    def test_change_priority_on_empty_list(self):
        with self.assertRaisesRegex(IndexError, ''):
            self.heap.change_priority(0, 1)

    def test_change_priority_on_non_empty_list_with_preceeding_index(self):
        self.heap.build([ (9, 'datum'), (5, 'datum'), (6, 'datum'),
            (2, 'datum'), (3, 'datum') ])
        with self.assertRaisesRegex(IndexError, ''):
            self.heap.change_priority(-1, 1)

    def test_change_priority_on_non_empty_list_with_exceeding_index(self):
        self.heap.build([ (9, 'datum'), (5, 'datum'), (6, 'datum'),
            (2, 'datum'), (3, 'datum') ])
        with self.assertRaisesRegex(IndexError, ''):
            self.heap.change_priority(self.heap.size, 1)

    def test_change_priority_on_one_element_list(self):
        self.heap.build([ (9, 'datum') ])

        self.assertEqual(1, self.heap.size)
        self.assertEqual([ (9, 'datum')], self.heap.elements)

        self.heap.change_priority(0, 1)

        self.assertEqual(1, self.heap.size)
        self.assertEqual([ (1, 'datum') ], self.heap.elements)

    def test_change_priority_on_two_element_list_without_sift(self):
        self.heap.build([ (9, 'datum'), (6, 'datum') ])

        self.assertEqual(2, self.heap.size)
        self.assertEqual([ (6, 'datum'), (9, 'datum') ], self.heap.elements)

        self.heap.change_priority(0, 1)

        self.assertEqual(2, self.heap.size)
        self.assertEqual([ (1, 'datum'), (9, 'datum') ], self.heap.elements)

        self.heap.change_priority(1, 2)

        self.assertEqual(2, self.heap.size)
        self.assertEqual([ (1, 'datum'), (2, 'datum') ], self.heap.elements)

    def test_change_priority_on_two_element_list_with_sift_down_up(self):
        self.heap.build([ (9, 'datum'), (6, 'datum') ])

        self.assertEqual(2, self.heap.size)
        self.assertEqual([ (6, 'datum'), (9, 'datum') ], self.heap.elements)

        self.heap.change_priority(0, 10)

        self.assertEqual(2, self.heap.size)
        self.assertEqual([ (9, 'datum'), (10, 'datum') ], self.heap.elements)

        self.heap.change_priority(1, 8)

        self.assertEqual(2, self.heap.size)
        self.assertEqual([ (8, 'datum'), (9, 'datum') ], self.heap.elements)

    def test_change_priority_on_five_element_list_with_sift_down(self):
        self.heap.build([ (3, 'datum'), (4, 'datum'), (5, 'datum'),
            (6, 'datum'), (9, 'datum') ])

        self.assertEqual(5, self.heap.size)
        self.assertEqual([ (3, 'datum'), (4, 'datum'), (5, 'datum'),
            (6, 'datum'), (9, 'datum') ], self.heap.elements)

        self.heap.change_priority(1, 10)

        self.assertEqual(5, self.heap.size)
        self.assertEqual([ (3, 'datum'), (6, 'datum'), (5, 'datum'),
            (10, 'datum'), (9, 'datum') ], self.heap.elements)

    def test_change_priority_on_five_element_list_with_sift_up(self):
        self.heap.build([ (3, 'datum'), (4, 'datum'), (5, 'datum'),
            (6, 'datum'), (9, 'datum') ])

        self.assertEqual(5, self.heap.size)
        self.assertEqual([ (3, 'datum'), (4, 'datum'), (5, 'datum'),
            (6, 'datum'), (9, 'datum') ], self.heap.elements)

        self.heap.change_priority(3, 0)

        self.assertEqual(5, self.heap.size)
        self.assertEqual([ (0, 'datum'), (3, 'datum'), (5, 'datum'),
            (4, 'datum'), (9, 'datum') ], self.heap.elements)

    def test_sort_on_empty_list(self):
        list = []

        self.heap.sort_in_place(list)

        self.assertEqual([], list)
        self.assertEqual(0, self.heap.size)

    def test_sort_on_one_element_list(self):
        list = [ (1, 'datum') ]

        self.heap.sort_in_place(list)

        self.assertEqual([ (1, 'datum') ], list)
        self.assertEqual(1, self.heap.size)

    def test_sort_on_unsorted_two_element_list(self):
        list = [ (1, 'datum'), (2, 'datum') ]

        self.heap.sort_in_place(list)

        self.assertEqual([ (2, 'datum'), (1, 'datum') ], list)
        self.assertEqual(2, self.heap.size)

    def test_sort_on_sorted_two_element_list(self):
        list = [ (2, 'datum'), (1, 'datum') ]

        self.heap.sort_in_place(list)

        self.assertEqual([ (2, 'datum'), (1, 'datum') ], list)
        self.assertEqual(2, self.heap.size)

    def test_sort_on_unsorted_three_element_list(self):
        list = [ (1, 'datum'), (2, 'datum'), (3, 'datum') ]

        self.heap.sort_in_place(list)

        self.assertEqual([ (3, 'datum'), (2, 'datum'), (1, 'datum') ], list)
        self.assertEqual(3, self.heap.size)

    def test_sort_on_sorted_three_element_list(self):
        list = [ (3, 'datum'), (2, 'datum'), (1, 'datum') ]

        self.heap.sort_in_place(list)

        self.assertEqual([ (3, 'datum'), (2, 'datum'), (1, 'datum') ], list)
        self.assertEqual(3, self.heap.size)

    def test_sort_on_unsorted_four_element_list(self):
        list = [ (1, 'datum'), (2, 'datum'), (3, 'datum'), (4, 'datum') ]

        self.heap.sort_in_place(list)

        self.assertEqual([ (4, 'datum'), (3, 'datum'),
            (2, 'datum'), (1, 'datum') ], list)
        self.assertEqual(4, self.heap.size)

    def test_sort_on_sorted_five_element_list(self):
        list = [ (4, 'datum'), (3, 'datum'), (2, 'datum'), (1, 'datum') ]

        self.heap.sort_in_place(list)

        self.assertEqual([ (4, 'datum'), (3, 'datum'),
            (2, 'datum'), (1, 'datum') ], list)
        self.assertEqual(4, self.heap.size)

    def test_sort_on_unsorted_five_element_list(self):
        list = [ (2, 'datum'), (4, 'datum'), (5, 'datum'),
            (8, 'datum'), (9, 'datum') ]

        self.heap.sort_in_place(list)

        self.assertEqual([ (9, 'datum'), (8, 'datum'), (5, 'datum'),
            (4, 'datum'), (2, 'datum') ], list)
        self.assertEqual(5, self.heap.size)

    def test_sort_on_sorted_five_element_list(self):
        list = [ (9, 'datum'), (8, 'datum'), (5, 'datum'),
            (4, 'datum'), (2, 'datum') ]

        self.heap.sort_in_place(list)

        self.assertEqual([ (9, 'datum'), (8, 'datum'), (5, 'datum'),
            (4, 'datum'), (2, 'datum') ], list)
        self.assertEqual(5, self.heap.size)

    def test_sort_on_seven_element_list_with_duplicates(self):
        list = [ (9, 'datum'), (5, 'datum'), (4, 'datum'), (2, 'datum'),
            (5, 'datum'), (2, 'datum'), (8, 'datum') ]

        self.heap.sort_in_place(list)

        self.assertEqual([ (9, 'datum'), (8, 'datum'), (5, 'datum'),
            (5, 'datum'), (4, 'datum'), (2, 'datum'), (2, 'datum') ], list)
        self.assertEqual(7, self.heap.size)

class BinHeapAsMaxTestCase(unittest.TestCase):

    def setUp(self):
        self.heap = BinHeap(HeapMode.max)

    def tearDown(self):
        pass

    def test_constructor(self):
        self.assertEqual(0, self.heap.size)
        self.assertEqual([], self.heap.elements)

    def test_str_on_empty_heap(self):
        self.assertEqual('[]', str(self.heap))

    def test_repr_on_empty_heap(self):
        self.assertEqual('[mode=HeapMode.max, size=0, list=[]]',
            repr(self.heap))

    def test_str_on_three_element_heap(self):
        self.heap.build([ (1, 'datum1'), (2, 'datum2'), (3, 'datum3') ])

        self.assertEqual("[(3, 'datum3'), (2, 'datum2'), (1, 'datum1')]",
            str(self.heap))

    def test_repr_on_three_element_heap(self):
        self.heap.build([ (1, 'datum1'),
            (2, 'datum2'), (3, 'datum3') ])

        self.assertEqual("[mode=HeapMode.max, size=3, " +
            "list=[(3, 'datum3'), (2, 'datum2'), (1, 'datum1')]]",
            repr(self.heap))

    def test_build_on_empty_list(self):
        self.heap.build([])

        self.assertEqual(0, self.heap.size)
        self.assertEqual([], self.heap.elements)

    def test_build_on_one_element_list(self):
        self.heap.build([ (1, 'datum') ])

        self.assertEqual(1, self.heap.size)
        self.assertEqual([ (1, 'datum') ], self.heap.elements)

    def test_build_on_two_element_list_as_1_2(self):
        self.heap.build([ (1, 'datum'), (2, 'datum') ])

        self.assertEqual(2, self.heap.size)
        self.assertEqual([ (2, 'datum'), (1, 'datum') ], self.heap.elements)

    def test_build_on_two_element_list_as_2_1(self):
        self.heap.build([ (2, 'datum'), (1, 'datum') ])

        self.assertEqual(2, self.heap.size)
        self.assertEqual([ (2, 'datum'), (1, 'datum') ], self.heap.elements)

    def test_build_on_three_element_list_as_1_2_3(self):
        self.heap.build([ (1, 'datum'), (2, 'datum'), (3, 'datum') ])

        self.assertEqual(3, self.heap.size)
        self.assertEqual([ (3, 'datum'), (2, 'datum'), (1, 'datum') ],
            self.heap.elements)

    def test_build_on_three_element_list_as_1_3_2(self):
        self.heap.build([ (1, 'datum'), (3, 'datum'), (2, 'datum') ])

        self.assertEqual(3, self.heap.size)
        self.assertEqual([ (3, 'datum'), (1, 'datum'), (2, 'datum') ],
            self.heap.elements)

    def test_build_on_three_element_list_as_2_1_3(self):
        self.heap.build([ (2, 'datum'), (1, 'datum'), (3, 'datum') ])

        self.assertEqual(3, self.heap.size)
        self.assertEqual([ (3, 'datum'), (1, 'datum'), (2, 'datum') ],
            self.heap.elements)

    def test_build_on_three_element_list_as_2_3_1(self):
        self.heap.build([ (2, 'datum'), (3, 'datum'), (1, 'datum') ])

        self.assertEqual(3, self.heap.size)
        self.assertEqual([ (3, 'datum'), (2, 'datum'), (1, 'datum') ],
            self.heap.elements)

    def test_build_on_three_element_list_as_3_1_2(self):
        self.heap.build([ (3, 'datum'), (1, 'datum'), (2, 'datum') ])

        self.assertEqual(3, self.heap.size)
        self.assertEqual([ (3, 'datum'), (1, 'datum'), (2, 'datum') ],
            self.heap.elements)

    def test_build_on_three_element_list_as_3_2_1(self):
        self.heap.build([ (3, 'datum'), (2, 'datum'), (1, 'datum') ])

        self.assertEqual(3, self.heap.size)
        self.assertEqual([ (3, 'datum'), (2, 'datum'), (1, 'datum') ],
            self.heap.elements)

    def test_build_on_four_element_list(self):
        self.heap.build([ (2, 'datum'), (5, 'datum'), (6, 'datum'),
            (9, 'datum') ])

        self.assertEqual(4, self.heap.size)
        self.assertEqual([ (9, 'datum'), (5, 'datum'), (6, 'datum'),
            (2, 'datum') ], self.heap.elements)

    def test_build_on_five_element_list(self):
        self.heap.build([ (2, 'datum'), (5, 'datum'), (6, 'datum'),
            (9, 'datum'), (10, 'datum') ])

        self.assertEqual(5, self.heap.size)
        self.assertEqual([ (10, 'datum'), (9, 'datum'), (6, 'datum'),
            (2, 'datum'), (5, 'datum') ], self.heap.elements)

    def test_build_on_six_element_list(self):
        self.heap.build([ (2, 'datum'), (5, 'datum'), (6, 'datum'),
            (9, 'datum'), (10, 'datum'), (11, 'datum') ])

        self.assertEqual(6, self.heap.size)
        self.assertEqual([ (11, 'datum'), (10, 'datum'), (6, 'datum'),
            (9, 'datum'), (5, 'datum'), (2, 'datum') ], self.heap.elements)

    def test_build_on_seven_element_list(self):
        self.heap.build([ (2, 'datum'), (5, 'datum'), (6, 'datum'),
            (9, 'datum'), (10, 'datum'), (11, 'datum'), (12, 'datum') ])

        self.assertEqual(7, self.heap.size)
        self.assertEqual([ (12, 'datum'), (10, 'datum'), (11, 'datum'),
            (9, 'datum'), (5, 'datum'), (2, 'datum'), (6, 'datum') ],
            self.heap.elements)

    def test_build_on_seven_element_list_with_duplicates(self):
        self.heap.build([ (2, 'datum'), (6, 'datum'), (6, 'datum'),
            (9, 'datum'), (10, 'datum'), (10, 'datum'), (12, 'datum') ])

        self.assertEqual(7, self.heap.size)
        self.assertEqual([ (12, 'datum'), (10, 'datum'), (10, 'datum'),
            (9, 'datum'), (6, 'datum'), (2, 'datum'), (6, 'datum') ],
            self.heap.elements)

    def test_build_on_seven_duplicate_element_list(self):
        self.heap.build([ (3, 'datum'), (3, 'datum'), (3, 'datum'),
            (3, 'datum'), (3, 'datum'), (3, 'datum'), (3, 'datum') ])

        self.assertEqual(7, self.heap.size)
        self.assertEqual([ (3, 'datum'), (3, 'datum'), (3, 'datum'),
            (3, 'datum'), (3, 'datum'), (3, 'datum'), (3, 'datum') ],
            self.heap.elements)

    def test_extract_on_five_element_list(self):
        self.heap.build([ (2, 'datum'), (5, 'datum'), (6, 'datum'),
            (9, 'datum'), (10, 'datum') ])

        self.assertEqual(5, self.heap.size)
        self.assertEqual([ (10, 'datum'), (9, 'datum'), (6, 'datum'),
            (2, 'datum'), (5, 'datum') ], self.heap.elements)

        max = self.heap.extract()

        self.assertEqual((10, 'datum'), max)
        self.assertEqual(4, self.heap.size)
        self.assertEqual([ (9, 'datum'), (5, 'datum'), (6, 'datum'),
            (2, 'datum') ], self.heap.elements)

        max = self.heap.extract()

        self.assertEqual((9, 'datum'), max)
        self.assertEqual(3, self.heap.size)
        self.assertEqual([ (6, 'datum'), (5, 'datum'), (2, 'datum') ],
            self.heap.elements)

        max = self.heap.extract()

        self.assertEqual((6, 'datum'), max)
        self.assertEqual(2, self.heap.size)
        self.assertEqual([ (5, 'datum'), (2, 'datum') ], self.heap.elements)

        max = self.heap.extract()

        self.assertEqual((5, 'datum'), max)
        self.assertEqual(1, self.heap.size)
        self.assertEqual([ (2, 'datum') ], self.heap.elements)

        max = self.heap.extract()

        self.assertEqual((2, 'datum'), max)
        self.assertEqual(0, self.heap.size)
        self.assertEqual([], self.heap.elements)

    def test_insert_on_empty_list(self):
        self.assertEqual(0, self.heap.size)
        self.assertEqual([], self.heap.elements)

        self.heap.insert((1, 'datum'))

        self.assertEqual(1, self.heap.size)
        self.assertEqual([ (1, 'datum') ], self.heap.elements)

    def test_insert_on_one_element_list(self):
        self.heap.build([ (2, 'datum') ])

        self.assertEqual(1, self.heap.size)
        self.assertEqual([ (2, 'datum') ], self.heap.elements)

        self.heap.insert((1, 'datum'))

        self.assertEqual(2, self.heap.size)
        self.assertEqual([ (2, 'datum'), (1, 'datum') ], self.heap.elements)

    def test_insert_on_two_element_list(self):
        self.heap.build([ (3, 'datum'), (2, 'datum') ])

        self.assertEqual(2, self.heap.size)
        self.assertEqual([ (3, 'datum'), (2, 'datum') ], self.heap.elements)

        self.heap.insert((4, 'datum'))

        self.assertEqual(3, self.heap.size)
        self.assertEqual([ (4, 'datum'), (2, 'datum'), (3, 'datum') ],
            self.heap.elements)

    def test_insert_on_three_element_list(self):
        self.heap.build([ (4, 'datum'), (3, 'datum'), (2, 'datum') ])

        self.assertEqual(3, self.heap.size)
        self.assertEqual([ (4, 'datum'), (3, 'datum'), (2, 'datum') ],
            self.heap.elements)

        self.heap.insert((5, 'datum'))

        self.assertEqual(4, self.heap.size)
        self.assertEqual([ (5, 'datum'), (4, 'datum'), (2, 'datum'),
            (3, 'datum') ], self.heap.elements)

    def test_insert_on_four_element_list(self):
        self.heap.build([ (5, 'datum'), (4, 'datum'), (3, 'datum'),
            (2, 'datum') ])

        self.assertEqual(4, self.heap.size)
        self.assertEqual([ (5, 'datum'), (4, 'datum'), (3, 'datum'),
            (2, 'datum') ], self.heap.elements)

        self.heap.insert((6, 'datum'))

        self.assertEqual(5, self.heap.size)
        self.assertEqual([ (6, 'datum'), (5, 'datum'), (3, 'datum'),
            (2, 'datum'), (4, 'datum') ], self.heap.elements)

    def test_insert_on_five_element_list(self):
        self.heap.build([ (9, 'datum'), (5, 'datum'), (6, 'datum'),
            (2, 'datum'), (3, 'datum') ])

        self.assertEqual(5, self.heap.size)
        self.assertEqual([ (9, 'datum'), (5, 'datum'), (6, 'datum'),
            (2, 'datum'), (3, 'datum') ], self.heap.elements)

        self.heap.insert((10, 'datum'))

        self.assertEqual(6, self.heap.size)
        self.assertEqual([ (10, 'datum'), (5, 'datum'), (9, 'datum'),
            (2, 'datum'), (3, 'datum'), (6, 'datum') ], self.heap.elements)

    def test_change_priority_on_empty_list(self):
        with self.assertRaisesRegex(IndexError, ''):
            self.heap.change_priority(0, 1)

    def test_change_priority_on_non_empty_list_with_preceeding_index(self):
        self.heap.build([ (9, 'datum'), (5, 'datum'), (6, 'datum'),
            (2, 'datum'), (3, 'datum') ])
        with self.assertRaisesRegex(IndexError, ''):
            self.heap.change_priority(-1, 1)

    def test_change_priority_on_non_empty_list_with_exceeding_index(self):
        self.heap.build([ (9, 'datum'), (5, 'datum'), (6, 'datum'),
            (2, 'datum'), (3, 'datum') ])
        with self.assertRaisesRegex(IndexError, ''):
            self.heap.change_priority(self.heap.size, 1)

    def test_change_priority_on_one_element_list(self):
        self.heap.build([ (9, 'datum') ])

        self.assertEqual(1, self.heap.size)
        self.assertEqual([ (9, 'datum') ], self.heap.elements)

        self.heap.change_priority(0, 1)

        self.assertEqual(1, self.heap.size)
        self.assertEqual([ (1, 'datum') ], self.heap.elements)

    def test_change_priority_on_two_element_list_without_sift(self):
        self.heap.build([ (9, 'datum'), (6, 'datum') ])

        self.assertEqual(2, self.heap.size)
        self.assertEqual([ (9, 'datum'), (6, 'datum') ], self.heap.elements)

        self.heap.change_priority(0, 7)

        self.assertEqual(2, self.heap.size)
        self.assertEqual([ (7, 'datum'), (6, 'datum') ], self.heap.elements)

        self.heap.change_priority(1, 5)

        self.assertEqual(2, self.heap.size)
        self.assertEqual([ (7, 'datum'), (5, 'datum') ], self.heap.elements)

    def test_change_priority_on_two_element_list_with_sift_down_and_up(self):
        self.heap.build([ (9, 'datum'), (6, 'datum') ])

        self.assertEqual(2, self.heap.size)
        self.assertEqual([ (9, 'datum'), (6, 'datum') ], self.heap.elements)

        self.heap.change_priority(0, 5)

        self.assertEqual(2, self.heap.size)
        self.assertEqual([ (6, 'datum'), (5, 'datum') ], self.heap.elements)

        self.heap.change_priority(1, 7)

        self.assertEqual(2, self.heap.size)
        self.assertEqual([ (7, 'datum'), (6, 'datum') ], self.heap.elements)

    def test_change_priority_on_five_element_list_with_sift_down(self):
        self.heap.build([ (9, 'datum'), (6, 'datum'), (5, 'datum'),
            (4, 'datum'), (3, 'datum') ])

        self.assertEqual(5, self.heap.size)
        self.assertEqual([ (9, 'datum'), (6, 'datum'), (5, 'datum'),
            (4, 'datum'), (3, 'datum') ], self.heap.elements)

        self.heap.change_priority(1, 0)

        self.assertEqual(5, self.heap.size)
        self.assertEqual([ (9, 'datum'), (4, 'datum'), (5, 'datum'),
            (0, 'datum'), (3, 'datum') ], self.heap.elements)

    def test_change_priority_on_five_element_list_with_sift_up(self):
        self.heap.build([ (9, 'datum'), (6, 'datum'), (5, 'datum'),
            (4, 'datum'), (3, 'datum') ])

        self.assertEqual(5, self.heap.size)
        self.assertEqual([ (9, 'datum'), (6, 'datum'), (5, 'datum'),
            (4, 'datum'), (3, 'datum') ], self.heap.elements)

        self.heap.change_priority(1, 10)

        self.assertEqual(5, self.heap.size)
        self.assertEqual([ (10, 'datum'), (9, 'datum'), (5, 'datum'),
            (4, 'datum'), (3, 'datum') ], self.heap.elements)

    def test_sort_on_empty_list(self):
        list = []

        self.heap.sort_in_place(list)

        self.assertEqual([], list)
        self.assertEqual(0, self.heap.size)

    def test_sort_on_one_element_list(self):
        list = [ (1, 'datum') ]

        self.heap.sort_in_place(list)

        self.assertEqual([ (1, 'datum') ], list)
        self.assertEqual(1, self.heap.size)

    def test_sort_on_sorted_two_element_list(self):
        list = [ (1, 'datum'), (2, 'datum') ]

        self.heap.sort_in_place(list)

        self.assertEqual([ (1, 'datum'), (2, 'datum') ], list)
        self.assertEqual(2, self.heap.size)

    def test_sort_on_unsorted_two_element_list(self):
        list = [ (2, 'datum'), (1, 'datum') ]

        self.heap.sort_in_place(list)

        self.assertEqual([ (1, 'datum'), (2, 'datum') ], list)
        self.assertEqual(2, self.heap.size)

    def test_sort_on_sorted_three_element_list(self):
        list = [ (1, 'datum'), (2, 'datum'), (3, 'datum') ]

        self.heap.sort_in_place(list)

        self.assertEqual([ (1, 'datum'), (2, 'datum'), (3, 'datum') ], list)
        self.assertEqual(3, self.heap.size)

    def test_sort_on_unsorted_three_element_list(self):
        list = [ (3, 'datum'), (2, 'datum'), (1, 'datum') ]

        self.heap.sort_in_place(list)

        self.assertEqual([ (1, 'datum'), (2, 'datum'), (3, 'datum') ], list)
        self.assertEqual(3, self.heap.size)

    def test_sort_on_sorted_four_element_list(self):
        list = [ (1, 'datum'), (2, 'datum'), (3, 'datum'), (4, 'datum') ]

        self.heap.sort_in_place(list)

        self.assertEqual([ (1, 'datum'), (2, 'datum'), (3, 'datum'),
            (4, 'datum') ], list)
        self.assertEqual(4, self.heap.size)

    def test_sort_on_unsorted_five_element_list(self):
        list = [ (4, 'datum'), (3, 'datum'), (2, 'datum'), (1, 'datum') ]

        self.heap.sort_in_place(list)

        self.assertEqual([ (1, 'datum'), (2, 'datum'), (3, 'datum'),
            (4, 'datum') ], list)
        self.assertEqual(4, self.heap.size)

    def test_sort_on_sorted_five_element_list(self):
        list = [ (2, 'datum'), (4, 'datum'), (5, 'datum'), (8, 'datum'),
            (9, 'datum') ]

        self.heap.sort_in_place(list)

        self.assertEqual([ (2, 'datum'), (4, 'datum'), (5, 'datum'),
            (8, 'datum'), (9, 'datum') ], list)
        self.assertEqual(5, self.heap.size)

    def test_sort_on_unsorted_five_element_list(self):
        list = [ (9, 'datum'), (8, 'datum'), (5, 'datum'), (4, 'datum'),
            (2, 'datum') ]

        self.heap.sort_in_place(list)

        self.assertEqual([ (2, 'datum'), (4, 'datum'), (5, 'datum'),
            (8, 'datum'), (9, 'datum') ], list)
        self.assertEqual(5, self.heap.size)

    def test_sort_on_seven_element_list_with_duplicates(self):
        list = [ (9, 'datum'), (5, 'datum'), (4, 'datum'), (2, 'datum'),
            (5, 'datum'), (2, 'datum'), (8, 'datum') ]

        self.heap.sort_in_place(list)

        self.assertEqual([ (2, 'datum'), (2, 'datum'), (4, 'datum'),
            (5, 'datum'), (5, 'datum'), (8, 'datum'), (9, 'datum') ], list)
        self.assertEqual(7, self.heap.size)

class BinHeapAsMinWithTuplesTestCase(unittest.TestCase):

    def setUp(self):
        self.heap = BinHeap(HeapMode.min)

    def tearDown(self):
        pass

    def test_constructor(self):
        self.assertEqual(0, self.heap.size)
        self.assertEqual([], self.heap.elements)

    def test_build_on_empty_list(self):
        self.heap.build([])

        self.assertEqual(0, self.heap.size)
        self.assertEqual([], self.heap.elements)

    def test_build_on_one_element_list(self):
        self.heap.build([ (1, 1) ])

        self.assertEqual(1, self.heap.size)
        self.assertEqual([ (1, 1) ], self.heap.elements)

    def test_build_on_two_element_list_as_1_1_and_2_2(self):
        self.heap.build([ (1, 1), (2, 2) ])

        self.assertEqual(2, self.heap.size)
        self.assertEqual([ (1, 1), (2, 2) ],
            self.heap.elements)

    def test_build_on_two_element_list_as_2_2_and_1_1(self):
        self.heap.build([ (2, 2), (1, 1) ])

        self.assertEqual(2, self.heap.size)
        self.assertEqual([ (1, 1), (2, 2) ],
            self.heap.elements)

    def test_build_on_two_element_list_as_2_1_and_2_2(self):
        self.heap.build([ (2, 1), (2, 2) ])

        self.assertEqual(2, self.heap.size)
        self.assertEqual([ (2, 1), (2, 2) ],
            self.heap.elements)

    def test_build_on_two_element_list_as_2_2_and_2_1(self):
        self.heap.build([ (2, 2), (2, 1) ])

        self.assertEqual(2, self.heap.size)
        self.assertEqual([ (2, 1), (2, 2) ],
            self.heap.elements)

    def test_build_on_three_element_list_as_1_2_3(self):
        self.heap.build([ (1, 1), (2, 2), (3, 3) ])

        self.assertEqual(3, self.heap.size)
        self.assertEqual([ (1, 1), (2, 2), (3, 3) ],
            self.heap.elements)

    def test_build_on_three_element_list_as_1_3_2(self):
        self.heap.build([ (1, 1), (3, 3), (2, 2) ])

        self.assertEqual(3, self.heap.size)
        self.assertEqual([ (1, 1), (3, 3), (2, 2) ],
            self.heap.elements)

    def test_build_on_three_element_list_as_2_1_3(self):
        data = [ (2, 2), (1, 1), (3, 3) ]

        self.heap.build(data)

        self.assertEqual(3, self.heap.size)
        self.assertEqual([ (1, 1), (2, 2), (3, 3) ],
            self.heap.elements)

    def test_build_on_three_element_list_as_2_3_1(self):
        self.heap.build([ (2, 2), (3, 3), (1, 1) ])

        self.assertEqual(3, self.heap.size)
        self.assertEqual([ (1, 1), (3, 3), (2, 2) ],
            self.heap.elements)

    def test_build_on_three_element_list_as_3_1_2(self):
        self.heap.build([ (3, 3), (1, 1), (2, 2) ])

        self.assertEqual(3, self.heap.size)
        self.assertEqual([ (1, 1), (3, 3), (2, 2) ],
            self.heap.elements)

    def test_build_on_three_element_list_as_3_2_1(self):
        self.heap.build([ (3, 3), (2, 2), (1, 1) ])

        self.assertEqual(3, self.heap.size)
        self.assertEqual([ (1, 1), (2, 2), (3, 3) ],
            self.heap.elements)

    def test_build_on_three_element_list_with_equal_priorities(self):
        self.heap.build([ (2, 3), (2, 2), (2, 1) ])

        self.assertEqual(3, self.heap.size)
        self.assertEqual([ (2, 1), (2, 2), (2, 3) ],
            self.heap.elements)

    def test_build_on_four_element_list(self):
        self.heap.build([ (9, 9), (5, 5), (6, 6),
            (2, 2) ])

        self.assertEqual(4, self.heap.size)
        self.assertEqual([ (2, 2), (5, 5), (6, 6),
            (9, 9) ], self.heap.elements)

    def test_build_on_four_element_list_with_equal_priorities(self):
        self.heap.build([ (2, 4), (2, 3), (2, 2),
            (2, 1) ])

        self.assertEqual(4, self.heap.size)
        self.assertEqual([ (2, 1), (2, 3), (2, 2),
            (2, 4) ], self.heap.elements)

    def test_build_on_five_element_list(self):
        self.heap.build([ (9, 9), (5, 5), (6, 6),
            (2, 2), (3, 3) ])

        self.assertEqual(5, self.heap.size)
        self.assertEqual([ (2, 2), (3, 3), (6, 6),
            (5, 5), (9, 9) ], self.heap.elements)

    def test_build_on_five_element_list_with_equal_priorities(self):
        self.heap.build([ (2, 5), (2, 4), (2, 3),
            (2, 2), (2, 1) ])

        self.assertEqual(5, self.heap.size)
        self.assertEqual([ (2, 1), (2, 2), (2, 3),
            (2, 5), (2, 4) ], self.heap.elements)

if __name__ == '__main__':
    class_names = \
    [
        BinHeapAsMinTestCase,
        BinHeapAsMaxTestCase,
        BinHeapAsMinWithTuplesTestCase
    ]

    suite = unittest.TestSuite()

    for c in class_names:
        suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(c))

    unittest.TextTestRunner().run(suite)
