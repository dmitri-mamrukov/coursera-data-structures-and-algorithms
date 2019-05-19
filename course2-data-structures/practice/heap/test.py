#!/usr/bin/python3

import unittest

from heap import BinHeap, HeapItem, HeapMode
import heap_sort

class HeapItemTestCase(unittest.TestCase):

    def test_constructor_with_priority(self):
        priority = 123
        item = HeapItem(priority)

        self.assertEqual(priority, item.priority)
        self.assertEqual(None, item.datum)

    def test_constructor_with_priority_and_datum(self):
        priority = 123
        datum = 'datum'
        item = HeapItem(priority, datum)

        self.assertEqual(priority, item.priority)
        self.assertEqual(datum, item.datum)

    def test_str_with_priority(self):
        item = HeapItem(123)

        self.assertEqual('None', str(item))

    def test_str_with_priority_and_datum(self):
        item = HeapItem(123, 'datum')

        self.assertEqual('datum', str(item))

    def test_repr_with_priority(self):
        item = HeapItem(123)

        self.assertEqual('[priority=123, datum=None]', repr(item))

    def test_repr_with_priority_and_datum(self):
        item = HeapItem(123, 'test-datum')

        self.assertEqual('[priority=123, datum=test-datum]', repr(item))

    def test_lt_with_priority_as_equal(self):
        item = HeapItem(123)
        other = HeapItem(123)

        self.assertFalse(item < other)
        self.assertFalse(other < item)

    def test_lt_with_priority_as_not_equal(self):
        item = HeapItem(123)
        other = HeapItem(456)

        self.assertTrue(item < other)
        self.assertFalse(other < item)

    def test_lt_with_priority_and_datum_as_equal(self):
        item = HeapItem(123, 'datum')
        other = HeapItem(123, 'datum')

        self.assertFalse(item < other)
        self.assertFalse(other < item)

    def test_lt_with_priority_and_datum_as_not_equal_priorities(self):
        item = HeapItem(123, 'datum')
        other = HeapItem(456, 'datum')

        self.assertTrue(item < other)
        self.assertFalse(other < item)

    def test_lt_with_priority_and_datum_as_not_equal_data(self):
        item = HeapItem(123, 'datum1')
        other = HeapItem(123, 'datum2')

        self.assertTrue(item < other)
        self.assertFalse(other < item)

    def test_lt_with_priority_and_datum_as_not_equal(self):
        item = HeapItem(123, 'datum1')
        other = HeapItem(456, 'datum2')

        self.assertTrue(item < other)
        self.assertFalse(other < item)

    def test_eq_with_priority_as_equal(self):
        item = HeapItem(123)
        other = HeapItem(123)

        self.assertTrue(item == other)
        self.assertTrue(other == item)

    def test_eq_with_priority_as_not_equal(self):
        item = HeapItem(123)
        other = HeapItem(456)

        self.assertFalse(item == other)
        self.assertFalse(other == item)

    def test_eq_with_priority_and_datum_as_equal(self):
        item = HeapItem(123, 'datum')
        other = HeapItem(123, 'datum')

        self.assertTrue(item == other)
        self.assertTrue(other == item)

    def test_eq_with_priority_and_datum_as_not_equal_priorities(self):
        item = HeapItem(123, 'datum')
        other = HeapItem(456, 'datum')

        self.assertFalse(item == other)
        self.assertFalse(other == item)

    def test_eq_with_priority_and_datum_as_not_equal_data(self):
        item = HeapItem(123, 'datum1')
        other = HeapItem(123, 'datum2')

        self.assertFalse(item == other)
        self.assertFalse(other == item)

    def test_eq_with_priority_and_datum_as_not_equal(self):
        item = HeapItem(123, 'datum1')
        other = HeapItem(456, 'datum2')

        self.assertFalse(item == other)
        self.assertFalse(other == item)

    def test_gt_with_priority_as_equal(self):
        item = HeapItem(123)
        other = HeapItem(123)

        self.assertFalse(item > other)
        self.assertFalse(other > item)

    def test_gt_with_priority_as_not_equal(self):
        item = HeapItem(123)
        other = HeapItem(456)

        self.assertFalse(item > other)
        self.assertTrue(other > item)

    def test_gt_with_priority_and_datum_as_equal(self):
        item = HeapItem(123, 'datum')
        other = HeapItem(123, 'datum')

        self.assertFalse(item > other)
        self.assertFalse(other > item)

    def test_gt_with_priority_and_datum_as_not_equal_priorities(self):
        item = HeapItem(123, 'datum')
        other = HeapItem(456, 'datum')

        self.assertFalse(item > other)
        self.assertTrue(other > item)

    def test_gt_with_priority_and_datum_as_not_equal_data(self):
        item = HeapItem(123, 'datum1')
        other = HeapItem(123, 'datum2')

        self.assertFalse(item > other)
        self.assertTrue(other > item)

    def test_gt_with_priority_and_datum_as_not_equal(self):
        item = HeapItem(123, 'datum1')
        other = HeapItem(456, 'datum2')

        self.assertFalse(item > other)
        self.assertTrue(other > item)

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
        self.heap.build([ HeapItem(1, 'datum1'),
            HeapItem(2, 'datum2'), HeapItem(3, 'datum3') ])

        self.assertEqual('[[priority=1, datum=datum1], ' +
            '[priority=2, datum=datum2], [priority=3, datum=datum3]]',
            str(self.heap))

    def test_repr_on_three_element_heap(self):
        self.heap.build([ HeapItem(1, 'datum1'),
            HeapItem(2, 'datum2'), HeapItem(3, 'datum3') ])

        self.assertEqual('[mode=HeapMode.min, size=3, ' +
            'list=[[priority=1, datum=datum1], ' +
            '[priority=2, datum=datum2], [priority=3, datum=datum3]]]',
            repr(self.heap))

    def test_build_on_empty_list(self):
        self.heap.build([])

        self.assertEqual(0, self.heap.size)
        self.assertEqual([], self.heap.elements)

    def test_build_on_one_element_list(self):
        self.heap.build([ HeapItem(1) ])

        self.assertEqual(1, self.heap.size)
        self.assertEqual([ HeapItem(1) ], self.heap.elements)

    def test_build_on_two_element_list_as_1_2(self):
        self.heap.build([ HeapItem(1), HeapItem(2) ])

        self.assertEqual(2, self.heap.size)
        self.assertEqual([ HeapItem(1), HeapItem(2) ], self.heap.elements)

    def test_build_on_two_element_list_as_2_1(self):
        self.heap.build([ HeapItem(2), HeapItem(1) ])

        self.assertEqual(2, self.heap.size)
        self.assertEqual([ HeapItem(1), HeapItem(2) ], self.heap.elements)

    def test_build_on_three_element_list_as_1_2_3(self):
        self.heap.build([ HeapItem(1), HeapItem(2), HeapItem(3) ])

        self.assertEqual(3, self.heap.size)
        self.assertEqual([ HeapItem(1), HeapItem(2), HeapItem(3) ],
            self.heap.elements)

    def test_build_on_three_element_list_as_1_3_2(self):
        self.heap.build([ HeapItem(1), HeapItem(3), HeapItem(2) ])

        self.assertEqual(3, self.heap.size)
        self.assertEqual([ HeapItem(1), HeapItem(3), HeapItem(2) ],
            self.heap.elements)

    def test_build_on_three_element_list_as_2_1_3(self):
        data = [ HeapItem(2), HeapItem(1), HeapItem(3) ]

        self.heap.build(data)

        self.assertEqual(3, self.heap.size)
        self.assertEqual([ HeapItem(1), HeapItem(2), HeapItem(3) ],
            self.heap.elements)

    def test_build_on_three_element_list_as_2_3_1(self):
        self.heap.build([ HeapItem(2), HeapItem(3), HeapItem(1) ])

        self.assertEqual(3, self.heap.size)
        self.assertEqual([ HeapItem(1), HeapItem(3), HeapItem(2) ],
            self.heap.elements)

    def test_build_on_three_element_list_as_3_1_2(self):
        self.heap.build([ HeapItem(3), HeapItem(1), HeapItem(2) ])

        self.assertEqual(3, self.heap.size)
        self.assertEqual([ HeapItem(1), HeapItem(3), HeapItem(2) ],
            self.heap.elements)

    def test_build_on_three_element_list_as_3_2_1(self):
        self.heap.build([ HeapItem(3), HeapItem(2), HeapItem(1) ])

        self.assertEqual(3, self.heap.size)
        self.assertEqual([ HeapItem(1), HeapItem(2), HeapItem(3) ],
            self.heap.elements)

    def test_build_on_four_element_list(self):
        self.heap.build([ HeapItem(9), HeapItem(5), HeapItem(6),
            HeapItem(2) ])

        self.assertEqual(4, self.heap.size)
        self.assertEqual([ HeapItem(2), HeapItem(5), HeapItem(6),
            HeapItem(9) ], self.heap.elements)

    def test_build_on_five_element_list(self):
        self.heap.build([ HeapItem(9), HeapItem(5), HeapItem(6),
            HeapItem(2), HeapItem(3) ])

        self.assertEqual(5, self.heap.size)
        self.assertEqual([ HeapItem(2), HeapItem(3), HeapItem(6),
            HeapItem(5), HeapItem(9) ], self.heap.elements)

    def test_build_on_six_element_list(self):
        self.heap.build([ HeapItem(9), HeapItem(5), HeapItem(6),
            HeapItem(2), HeapItem(3), HeapItem(1) ])

        self.assertEqual(6, self.heap.size)
        self.assertEqual([ HeapItem(1), HeapItem(2), HeapItem(6),
            HeapItem(5), HeapItem(3), HeapItem(9) ], self.heap.elements)

    def test_build_on_seven_element_list(self):
        self.heap.build([ HeapItem(9), HeapItem(5), HeapItem(6),
            HeapItem(2), HeapItem(3), HeapItem(1), HeapItem(0) ])

        self.assertEqual(7, self.heap.size)
        self.assertEqual([ HeapItem(0), HeapItem(2), HeapItem(1),
            HeapItem(5), HeapItem(3), HeapItem(9), HeapItem(6) ],
            self.heap.elements)

    def test_build_on_seven_element_list_with_duplicates(self):
        self.heap.build([ HeapItem(9), HeapItem(5), HeapItem(2),
            HeapItem(2), HeapItem(1), HeapItem(1), HeapItem(0) ])

        self.assertEqual(7, self.heap.size)
        self.assertEqual([ HeapItem(0), HeapItem(1), HeapItem(1),
            HeapItem(2), HeapItem(5), HeapItem(9), HeapItem(2) ],
            self.heap.elements)

    def test_build_on_seven_duplicate_element_list(self):
        self.heap.build([ HeapItem(3), HeapItem(3), HeapItem(3),
            HeapItem(3), HeapItem(3), HeapItem(3), HeapItem(3) ])

        self.assertEqual(7, self.heap.size)
        self.assertEqual([ HeapItem(3), HeapItem(3), HeapItem(3),
            HeapItem(3), HeapItem(3), HeapItem(3), HeapItem(3) ],
            self.heap.elements)

    def test_extract_on_five_element_list(self):
        self.heap.build([ HeapItem(9), HeapItem(5), HeapItem(6),
            HeapItem(2), HeapItem(3) ])

        self.assertEqual(5, self.heap.size)
        self.assertEqual([ HeapItem(2), HeapItem(3), HeapItem(6),
            HeapItem(5), HeapItem(9) ], self.heap.elements)

        min = self.heap.extract()

        self.assertEqual(HeapItem(2), min)
        self.assertEqual(4, self.heap.size)
        self.assertEqual([ HeapItem(3), HeapItem(5),
            HeapItem(6), HeapItem(9) ], self.heap.elements)

        min = self.heap.extract()

        self.assertEqual(HeapItem(3), min)
        self.assertEqual(3, self.heap.size)
        self.assertEqual([ HeapItem(5), HeapItem(9), HeapItem(6) ],
            self.heap.elements)

        min = self.heap.extract()

        self.assertEqual(HeapItem(5), min)
        self.assertEqual(2, self.heap.size)
        self.assertEqual([ HeapItem(6), HeapItem(9) ], self.heap.elements)

        min = self.heap.extract()

        self.assertEqual(HeapItem(6), min)
        self.assertEqual(1, self.heap.size)
        self.assertEqual([ HeapItem(9) ], self.heap.elements)

        min = self.heap.extract()

        self.assertEqual(HeapItem(9), min)
        self.assertEqual(0, self.heap.size)
        self.assertEqual([], self.heap.elements)

    def test_insert_on_empty_list(self):
        self.heap.insert(HeapItem(1))

        self.assertEqual(1, self.heap.size)
        self.assertEqual([ HeapItem(1) ], self.heap.elements)

    def test_insert_on_one_element_list(self):
        self.heap.build([ HeapItem(2) ])

        self.assertEqual(1, self.heap.size)
        self.assertEqual([ HeapItem(2) ], self.heap.elements)

        self.heap.insert(HeapItem(1))

        self.assertEqual(2, self.heap.size)
        self.assertEqual([ HeapItem(1), HeapItem(2) ], self.heap.elements)

    def test_insert_on_two_element_list(self):
        self.heap.build([ HeapItem(2), HeapItem(3) ])

        self.assertEqual(2, self.heap.size)
        self.assertEqual([ HeapItem(2), HeapItem(3) ], self.heap.elements)

        self.heap.insert(HeapItem(1))

        self.assertEqual(3, self.heap.size)
        self.assertEqual([ HeapItem(1), HeapItem(3), HeapItem(2) ],
            self.heap.elements)

    def test_insert_on_three_element_list(self):
        self.heap.build([ HeapItem(2), HeapItem(3), HeapItem(4) ])

        self.assertEqual(3, self.heap.size)
        self.assertEqual([ HeapItem(2), HeapItem(3), HeapItem(4) ],
            self.heap.elements)

        self.heap.insert(HeapItem(1))

        self.assertEqual(4, self.heap.size)
        self.assertEqual([ HeapItem(1), HeapItem(2), HeapItem(4),
            HeapItem(3) ], self.heap.elements)

    def test_insert_on_four_element_list(self):
        self.heap.build([ HeapItem(2), HeapItem(3), HeapItem(4),
            HeapItem(5) ])

        self.assertEqual(4, self.heap.size)
        self.assertEqual([ HeapItem(2), HeapItem(3), HeapItem(4),
            HeapItem(5) ], self.heap.elements)

        self.heap.insert(HeapItem(1))

        self.assertEqual(5, self.heap.size)
        self.assertEqual([ HeapItem(1), HeapItem(2), HeapItem(4),
            HeapItem(5), HeapItem(3) ], self.heap.elements)

    def test_insert_on_five_element_list(self):
        self.heap.build([ HeapItem(2), HeapItem(3), HeapItem(6),
            HeapItem(5), HeapItem(9) ])

        self.assertEqual(5, self.heap.size)
        self.assertEqual([ HeapItem(2), HeapItem(3), HeapItem(6),
            HeapItem(5), HeapItem(9) ], self.heap.elements)

        self.heap.insert(HeapItem(1))

        self.assertEqual(6, self.heap.size)
        self.assertEqual([ HeapItem(1), HeapItem(3), HeapItem(2),
            HeapItem(5), HeapItem(9), HeapItem(6) ], self.heap.elements)

    def test_change_priority_on_empty_list(self):
        with self.assertRaisesRegex(IndexError, ''):
            self.heap.change_priority(0, 1)

    def test_change_priority_on_non_empty_list_with_preceeding_index(self):
        self.heap.build([ HeapItem(9), HeapItem(5), HeapItem(6),
            HeapItem(2), HeapItem(3) ])
        with self.assertRaisesRegex(IndexError, ''):
            self.heap.change_priority(-1, 1)

    def test_change_priority_on_non_empty_list_with_exceeding_index(self):
        self.heap.build([ HeapItem(9), HeapItem(5), HeapItem(6),
            HeapItem(2), HeapItem(3) ])
        with self.assertRaisesRegex(IndexError, ''):
            self.heap.change_priority(self.heap.size, 1)

    def test_change_priority_on_one_element_list(self):
        self.heap.build([ HeapItem(9) ])

        self.assertEqual(1, self.heap.size)
        self.assertEqual([ HeapItem(9)], self.heap.elements)

        self.heap.change_priority(0, 1)

        self.assertEqual(1, self.heap.size)
        self.assertEqual([ HeapItem(1) ], self.heap.elements)

    def test_change_priority_on_two_element_list_without_sift(self):
        self.heap.build([ HeapItem(9), HeapItem(6) ])

        self.assertEqual(2, self.heap.size)
        self.assertEqual([ HeapItem(6), HeapItem(9) ], self.heap.elements)

        self.heap.change_priority(0, 1)

        self.assertEqual(2, self.heap.size)
        self.assertEqual([ HeapItem(1), HeapItem(9) ], self.heap.elements)

        self.heap.change_priority(1, 2)

        self.assertEqual(2, self.heap.size)
        self.assertEqual([ HeapItem(1), HeapItem(2) ], self.heap.elements)

    def test_change_priority_on_two_element_list_with_sift_down_up(self):
        self.heap.build([ HeapItem(9), HeapItem(6) ])

        self.assertEqual(2, self.heap.size)
        self.assertEqual([ HeapItem(6), HeapItem(9) ], self.heap.elements)

        self.heap.change_priority(0, 10)

        self.assertEqual(2, self.heap.size)
        self.assertEqual([ HeapItem(9), HeapItem(10) ], self.heap.elements)

        self.heap.change_priority(1, 8)

        self.assertEqual(2, self.heap.size)
        self.assertEqual([ HeapItem(8), HeapItem(9) ], self.heap.elements)

    def test_change_priority_on_five_element_list_with_sift_down(self):
        self.heap.build([ HeapItem(3), HeapItem(4), HeapItem(5),
            HeapItem(6), HeapItem(9) ])

        self.assertEqual(5, self.heap.size)
        self.assertEqual([ HeapItem(3), HeapItem(4), HeapItem(5),
            HeapItem(6), HeapItem(9) ], self.heap.elements)

        self.heap.change_priority(1, 10)

        self.assertEqual(5, self.heap.size)
        self.assertEqual([ HeapItem(3), HeapItem(6), HeapItem(5),
            HeapItem(10), HeapItem(9) ], self.heap.elements)

    def test_change_priority_on_five_element_list_with_sift_up(self):
        self.heap.build([ HeapItem(3), HeapItem(4), HeapItem(5),
            HeapItem(6), HeapItem(9) ])

        self.assertEqual(5, self.heap.size)
        self.assertEqual([ HeapItem(3), HeapItem(4), HeapItem(5),
            HeapItem(6), HeapItem(9) ], self.heap.elements)

        self.heap.change_priority(3, 0)

        self.assertEqual(5, self.heap.size)
        self.assertEqual([ HeapItem(0), HeapItem(3), HeapItem(5),
            HeapItem(4), HeapItem(9) ], self.heap.elements)

    def test_sort_on_empty_list(self):
        list = []

        self.heap.sort_in_place(list)

        self.assertEqual([], list)
        self.assertEqual(0, self.heap.size)

    def test_sort_on_one_element_list(self):
        list = [ HeapItem(1) ]

        self.heap.sort_in_place(list)

        self.assertEqual([ HeapItem(1) ], list)
        self.assertEqual(1, self.heap.size)

    def test_sort_on_unsorted_two_element_list(self):
        list = [ HeapItem(1), HeapItem(2) ]

        self.heap.sort_in_place(list)

        self.assertEqual([ HeapItem(2), HeapItem(1) ], list)
        self.assertEqual(2, self.heap.size)

    def test_sort_on_sorted_two_element_list(self):
        list = [ HeapItem(2), HeapItem(1) ]

        self.heap.sort_in_place(list)

        self.assertEqual([ HeapItem(2), HeapItem(1) ], list)
        self.assertEqual(2, self.heap.size)

    def test_sort_on_unsorted_three_element_list(self):
        list = [ HeapItem(1), HeapItem(2), HeapItem(3) ]

        self.heap.sort_in_place(list)

        self.assertEqual([ HeapItem(3), HeapItem(2), HeapItem(1) ], list)
        self.assertEqual(3, self.heap.size)

    def test_sort_on_sorted_three_element_list(self):
        list = [ HeapItem(3), HeapItem(2), HeapItem(1) ]

        self.heap.sort_in_place(list)

        self.assertEqual([ HeapItem(3), HeapItem(2), HeapItem(1) ], list)
        self.assertEqual(3, self.heap.size)

    def test_sort_on_unsorted_four_element_list(self):
        list = [ HeapItem(1), HeapItem(2), HeapItem(3), HeapItem(4) ]

        self.heap.sort_in_place(list)

        self.assertEqual([ HeapItem(4), HeapItem(3),
            HeapItem(2), HeapItem(1) ], list)
        self.assertEqual(4, self.heap.size)

    def test_sort_on_sorted_five_element_list(self):
        list = [ HeapItem(4), HeapItem(3), HeapItem(2), HeapItem(1) ]

        self.heap.sort_in_place(list)

        self.assertEqual([ HeapItem(4), HeapItem(3),
            HeapItem(2), HeapItem(1) ], list)
        self.assertEqual(4, self.heap.size)

    def test_sort_on_unsorted_five_element_list(self):
        list = [ HeapItem(2), HeapItem(4), HeapItem(5),
            HeapItem(8), HeapItem(9) ]

        self.heap.sort_in_place(list)

        self.assertEqual([ HeapItem(9), HeapItem(8), HeapItem(5),
            HeapItem(4), HeapItem(2) ], list)
        self.assertEqual(5, self.heap.size)

    def test_sort_on_sorted_five_element_list(self):
        list = [ HeapItem(9), HeapItem(8), HeapItem(5),
            HeapItem(4), HeapItem(2) ]

        self.heap.sort_in_place(list)

        self.assertEqual([ HeapItem(9), HeapItem(8), HeapItem(5),
            HeapItem(4), HeapItem(2) ], list)
        self.assertEqual(5, self.heap.size)

    def test_sort_on_seven_element_list_with_duplicates(self):
        list = [ HeapItem(9), HeapItem(5), HeapItem(4), HeapItem(2),
            HeapItem(5), HeapItem(2), HeapItem(8) ]

        self.heap.sort_in_place(list)

        self.assertEqual([ HeapItem(9), HeapItem(8), HeapItem(5),
            HeapItem(5), HeapItem(4), HeapItem(2), HeapItem(2) ], list)
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
        self.assertEqual('[mode=HeapMode.max, size=0, list=[]]', repr(self.heap))

    def test_str_on_three_element_heap(self):
        self.heap.build([ HeapItem(1, 'datum1'),
            HeapItem(2, 'datum2'), HeapItem(3, 'datum3') ])

        self.assertEqual('[[priority=3, datum=datum3], ' +
            '[priority=2, datum=datum2], [priority=1, datum=datum1]]',
            str(self.heap))

    def test_repr_on_three_element_heap(self):
        self.heap.build([ HeapItem(1, 'datum1'),
            HeapItem(2, 'datum2'), HeapItem(3, 'datum3') ])

        self.assertEqual('[mode=HeapMode.max, size=3, ' +
            'list=[[priority=3, datum=datum3], ' +
            '[priority=2, datum=datum2], [priority=1, datum=datum1]]]',
            repr(self.heap))

    def test_build_on_empty_list(self):
        self.heap.build([])

        self.assertEqual(0, self.heap.size)
        self.assertEqual([], self.heap.elements)

    def test_build_on_one_element_list(self):
        self.heap.build([ HeapItem(1) ])

        self.assertEqual(1, self.heap.size)
        self.assertEqual([ HeapItem(1) ], self.heap.elements)

    def test_build_on_two_element_list_as_1_2(self):
        self.heap.build([ HeapItem(1), HeapItem(2) ])

        self.assertEqual(2, self.heap.size)
        self.assertEqual([ HeapItem(2), HeapItem(1) ], self.heap.elements)

    def test_build_on_two_element_list_as_2_1(self):
        self.heap.build([ HeapItem(2), HeapItem(1) ])

        self.assertEqual(2, self.heap.size)
        self.assertEqual([ HeapItem(2), HeapItem(1) ], self.heap.elements)

    def test_build_on_three_element_list_as_1_2_3(self):
        self.heap.build([ HeapItem(1), HeapItem(2), HeapItem(3) ])

        self.assertEqual(3, self.heap.size)
        self.assertEqual([ HeapItem(3), HeapItem(2), HeapItem(1) ],
            self.heap.elements)

    def test_build_on_three_element_list_as_1_3_2(self):
        self.heap.build([ HeapItem(1), HeapItem(3), HeapItem(2) ])

        self.assertEqual(3, self.heap.size)
        self.assertEqual([ HeapItem(3), HeapItem(1), HeapItem(2) ],
            self.heap.elements)

    def test_build_on_three_element_list_as_2_1_3(self):
        self.heap.build([ HeapItem(2), HeapItem(1), HeapItem(3) ])

        self.assertEqual(3, self.heap.size)
        self.assertEqual([ HeapItem(3), HeapItem(1), HeapItem(2) ],
            self.heap.elements)

    def test_build_on_three_element_list_as_2_3_1(self):
        self.heap.build([ HeapItem(2), HeapItem(3), HeapItem(1) ])

        self.assertEqual(3, self.heap.size)
        self.assertEqual([ HeapItem(3), HeapItem(2), HeapItem(1) ],
            self.heap.elements)

    def test_build_on_three_element_list_as_3_1_2(self):
        self.heap.build([ HeapItem(3), HeapItem(1), HeapItem(2) ])

        self.assertEqual(3, self.heap.size)
        self.assertEqual([ HeapItem(3), HeapItem(1), HeapItem(2) ],
            self.heap.elements)

    def test_build_on_three_element_list_as_3_2_1(self):
        self.heap.build([ HeapItem(3), HeapItem(2), HeapItem(1) ])

        self.assertEqual(3, self.heap.size)
        self.assertEqual([ HeapItem(3), HeapItem(2), HeapItem(1) ],
            self.heap.elements)

    def test_build_on_four_element_list(self):
        self.heap.build([ HeapItem(2), HeapItem(5), HeapItem(6),
            HeapItem(9) ])

        self.assertEqual(4, self.heap.size)
        self.assertEqual([ HeapItem(9), HeapItem(5), HeapItem(6),
            HeapItem(2) ], self.heap.elements)

    def test_build_on_five_element_list(self):
        self.heap.build([ HeapItem(2), HeapItem(5), HeapItem(6),
            HeapItem(9), HeapItem(10) ])

        self.assertEqual(5, self.heap.size)
        self.assertEqual([ HeapItem(10), HeapItem(9), HeapItem(6),
            HeapItem(2), HeapItem(5) ], self.heap.elements)

    def test_build_on_six_element_list(self):
        self.heap.build([ HeapItem(2), HeapItem(5), HeapItem(6), HeapItem(9),
            HeapItem(10), HeapItem(11) ])

        self.assertEqual(6, self.heap.size)
        self.assertEqual([ HeapItem(11), HeapItem(10), HeapItem(6),
            HeapItem(9), HeapItem(5), HeapItem(2) ], self.heap.elements)

    def test_build_on_seven_element_list(self):
        self.heap.build([ HeapItem(2), HeapItem(5), HeapItem(6), HeapItem(9),
            HeapItem(10), HeapItem(11), HeapItem(12) ])

        self.assertEqual(7, self.heap.size)
        self.assertEqual([ HeapItem(12), HeapItem(10), HeapItem(11),
            HeapItem(9), HeapItem(5), HeapItem(2), HeapItem(6) ],
            self.heap.elements)

    def test_build_on_seven_element_list_with_duplicates(self):
        self.heap.build([ HeapItem(2), HeapItem(6), HeapItem(6), HeapItem(9),
            HeapItem(10), HeapItem(10), HeapItem(12) ])

        self.assertEqual(7, self.heap.size)
        self.assertEqual([ HeapItem(12), HeapItem(10), HeapItem(10),
            HeapItem(9), HeapItem(6), HeapItem(2), HeapItem(6) ],
            self.heap.elements)

    def test_build_on_seven_duplicate_element_list(self):
        self.heap.build([ HeapItem(3), HeapItem(3), HeapItem(3), HeapItem(3),
            HeapItem(3), HeapItem(3), HeapItem(3) ])

        self.assertEqual(7, self.heap.size)
        self.assertEqual([ HeapItem(3), HeapItem(3), HeapItem(3), HeapItem(3),
            HeapItem(3), HeapItem(3), HeapItem(3) ], self.heap.elements)

    def test_extract_on_five_element_list(self):
        self.heap.build([ HeapItem(2), HeapItem(5), HeapItem(6), HeapItem(9),
            HeapItem(10) ])

        self.assertEqual(5, self.heap.size)
        self.assertEqual([ HeapItem(10), HeapItem(9), HeapItem(6),
            HeapItem(2), HeapItem(5) ], self.heap.elements)

        max = self.heap.extract()

        self.assertEqual(HeapItem(10), max)
        self.assertEqual(4, self.heap.size)
        self.assertEqual([ HeapItem(9), HeapItem(5), HeapItem(6),
            HeapItem(2) ], self.heap.elements)

        max = self.heap.extract()

        self.assertEqual(HeapItem(9), max)
        self.assertEqual(3, self.heap.size)
        self.assertEqual([ HeapItem(6), HeapItem(5), HeapItem(2) ],
            self.heap.elements)

        max = self.heap.extract()

        self.assertEqual(HeapItem(6), max)
        self.assertEqual(2, self.heap.size)
        self.assertEqual([ HeapItem(5), HeapItem(2) ], self.heap.elements)

        max = self.heap.extract()

        self.assertEqual(HeapItem(5), max)
        self.assertEqual(1, self.heap.size)
        self.assertEqual([ HeapItem(2) ], self.heap.elements)

        max = self.heap.extract()

        self.assertEqual(HeapItem(2), max)
        self.assertEqual(0, self.heap.size)
        self.assertEqual([], self.heap.elements)

    def test_insert_on_empty_list(self):
        self.assertEqual(0, self.heap.size)
        self.assertEqual([], self.heap.elements)

        self.heap.insert(HeapItem(1))

        self.assertEqual(1, self.heap.size)
        self.assertEqual([ HeapItem(1) ], self.heap.elements)

    def test_insert_on_one_element_list(self):
        self.heap.build([ HeapItem(2) ])

        self.assertEqual(1, self.heap.size)
        self.assertEqual([ HeapItem(2) ], self.heap.elements)

        self.heap.insert(HeapItem(1))

        self.assertEqual(2, self.heap.size)
        self.assertEqual([ HeapItem(2), HeapItem(1) ], self.heap.elements)

    def test_insert_on_two_element_list(self):
        self.heap.build([ HeapItem(3), HeapItem(2) ])

        self.assertEqual(2, self.heap.size)
        self.assertEqual([ HeapItem(3), HeapItem(2) ], self.heap.elements)

        self.heap.insert(HeapItem(4))

        self.assertEqual(3, self.heap.size)
        self.assertEqual([ HeapItem(4), HeapItem(2), HeapItem(3) ],
            self.heap.elements)

    def test_insert_on_three_element_list(self):
        self.heap.build([ HeapItem(4), HeapItem(3), HeapItem(2) ])

        self.assertEqual(3, self.heap.size)
        self.assertEqual([ HeapItem(4), HeapItem(3), HeapItem(2) ],
            self.heap.elements)

        self.heap.insert(HeapItem(5))

        self.assertEqual(4, self.heap.size)
        self.assertEqual([ HeapItem(5), HeapItem(4), HeapItem(2),
            HeapItem(3) ], self.heap.elements)

    def test_insert_on_four_element_list(self):
        self.heap.build([ HeapItem(5), HeapItem(4), HeapItem(3),
            HeapItem(2) ])

        self.assertEqual(4, self.heap.size)
        self.assertEqual([ HeapItem(5), HeapItem(4), HeapItem(3),
            HeapItem(2) ], self.heap.elements)

        self.heap.insert(HeapItem(6))

        self.assertEqual(5, self.heap.size)
        self.assertEqual([ HeapItem(6), HeapItem(5), HeapItem(3),
            HeapItem(2), HeapItem(4) ], self.heap.elements)

    def test_insert_on_five_element_list(self):
        self.heap.build([ HeapItem(9), HeapItem(5), HeapItem(6),
            HeapItem(2), HeapItem(3) ])

        self.assertEqual(5, self.heap.size)
        self.assertEqual([ HeapItem(9), HeapItem(5), HeapItem(6),
            HeapItem(2), HeapItem(3) ], self.heap.elements)

        self.heap.insert(HeapItem(10))

        self.assertEqual(6, self.heap.size)
        self.assertEqual([ HeapItem(10), HeapItem(5), HeapItem(9),
            HeapItem(2), HeapItem(3), HeapItem(6) ], self.heap.elements)

    def test_change_priority_on_empty_list(self):
        with self.assertRaisesRegex(IndexError, ''):
            self.heap.change_priority(0, 1)

    def test_change_priority_on_non_empty_list_with_preceeding_index(self):
        self.heap.build([ HeapItem(9), HeapItem(5), HeapItem(6),
            HeapItem(2), HeapItem(3) ])
        with self.assertRaisesRegex(IndexError, ''):
            self.heap.change_priority(-1, 1)

    def test_change_priority_on_non_empty_list_with_exceeding_index(self):
        self.heap.build([ HeapItem(9), HeapItem(5), HeapItem(6),
            HeapItem(2), HeapItem(3) ])
        with self.assertRaisesRegex(IndexError, ''):
            self.heap.change_priority(self.heap.size, 1)

    def test_change_priority_on_one_element_list(self):
        self.heap.build([ HeapItem(9) ])

        self.assertEqual(1, self.heap.size)
        self.assertEqual([ HeapItem(9) ], self.heap.elements)

        self.heap.change_priority(0, 1)

        self.assertEqual(1, self.heap.size)
        self.assertEqual([ HeapItem(1) ], self.heap.elements)

    def test_change_priority_on_two_element_list_without_sift(self):
        self.heap.build([ HeapItem(9), HeapItem(6) ])

        self.assertEqual(2, self.heap.size)
        self.assertEqual([ HeapItem(9), HeapItem(6) ], self.heap.elements)

        self.heap.change_priority(0, 7)

        self.assertEqual(2, self.heap.size)
        self.assertEqual([ HeapItem(7), HeapItem(6) ], self.heap.elements)

        self.heap.change_priority(1, 5)

        self.assertEqual(2, self.heap.size)
        self.assertEqual([ HeapItem(7), HeapItem(5) ], self.heap.elements)

    def test_change_priority_on_two_element_list_with_sift_down_and_up(self):
        self.heap.build([ HeapItem(9), HeapItem(6) ])

        self.assertEqual(2, self.heap.size)
        self.assertEqual([ HeapItem(9), HeapItem(6) ], self.heap.elements)

        self.heap.change_priority(0, 5)

        self.assertEqual(2, self.heap.size)
        self.assertEqual([ HeapItem(6), HeapItem(5) ], self.heap.elements)

        self.heap.change_priority(1, 7)

        self.assertEqual(2, self.heap.size)
        self.assertEqual([ HeapItem(7), HeapItem(6) ], self.heap.elements)

    def test_change_priority_on_five_element_list_with_sift_down(self):
        self.heap.build([ HeapItem(9), HeapItem(6), HeapItem(5),
            HeapItem(4), HeapItem(3) ])

        self.assertEqual(5, self.heap.size)
        self.assertEqual([ HeapItem(9), HeapItem(6), HeapItem(5),
            HeapItem(4), HeapItem(3) ], self.heap.elements)

        self.heap.change_priority(1, 0)

        self.assertEqual(5, self.heap.size)
        self.assertEqual([ HeapItem(9), HeapItem(4), HeapItem(5),
            HeapItem(0), HeapItem(3) ], self.heap.elements)

    def test_change_priority_on_five_element_list_with_sift_up(self):
        self.heap.build([ HeapItem(9), HeapItem(6), HeapItem(5),
            HeapItem(4), HeapItem(3) ])

        self.assertEqual(5, self.heap.size)
        self.assertEqual([ HeapItem(9), HeapItem(6), HeapItem(5),
            HeapItem(4), HeapItem(3) ], self.heap.elements)

        self.heap.change_priority(1, 10)

        self.assertEqual(5, self.heap.size)
        self.assertEqual([ HeapItem(10), HeapItem(9), HeapItem(5),
            HeapItem(4), HeapItem(3) ], self.heap.elements)

    def test_sort_on_empty_list(self):
        list = []

        self.heap.sort_in_place(list)

        self.assertEqual([], list)
        self.assertEqual(0, self.heap.size)

    def test_sort_on_one_element_list(self):
        list = [ HeapItem(1) ]

        self.heap.sort_in_place(list)

        self.assertEqual([ HeapItem(1) ], list)
        self.assertEqual(1, self.heap.size)

    def test_sort_on_sorted_two_element_list(self):
        list = [ HeapItem(1), HeapItem(2) ]

        self.heap.sort_in_place(list)

        self.assertEqual([ HeapItem(1), HeapItem(2) ], list)
        self.assertEqual(2, self.heap.size)

    def test_sort_on_unsorted_two_element_list(self):
        list = [ HeapItem(2), HeapItem(1) ]

        self.heap.sort_in_place(list)

        self.assertEqual([ HeapItem(1), HeapItem(2) ], list)
        self.assertEqual(2, self.heap.size)

    def test_sort_on_sorted_three_element_list(self):
        list = [ HeapItem(1), HeapItem(2), HeapItem(3) ]

        self.heap.sort_in_place(list)

        self.assertEqual([ HeapItem(1), HeapItem(2), HeapItem(3) ], list)
        self.assertEqual(3, self.heap.size)

    def test_sort_on_unsorted_three_element_list(self):
        list = [ HeapItem(3), HeapItem(2), HeapItem(1) ]

        self.heap.sort_in_place(list)

        self.assertEqual([ HeapItem(1), HeapItem(2), HeapItem(3) ], list)
        self.assertEqual(3, self.heap.size)

    def test_sort_on_sorted_four_element_list(self):
        list = [ HeapItem(1), HeapItem(2), HeapItem(3), HeapItem(4) ]

        self.heap.sort_in_place(list)

        self.assertEqual([ HeapItem(1), HeapItem(2), HeapItem(3),
            HeapItem(4) ], list)
        self.assertEqual(4, self.heap.size)

    def test_sort_on_unsorted_five_element_list(self):
        list = [ HeapItem(4), HeapItem(3), HeapItem(2), HeapItem(1) ]

        self.heap.sort_in_place(list)

        self.assertEqual([ HeapItem(1), HeapItem(2), HeapItem(3),
            HeapItem(4) ], list)
        self.assertEqual(4, self.heap.size)

    def test_sort_on_sorted_five_element_list(self):
        list = [ HeapItem(2), HeapItem(4), HeapItem(5), HeapItem(8),
            HeapItem(9) ]

        self.heap.sort_in_place(list)

        self.assertEqual([ HeapItem(2), HeapItem(4), HeapItem(5),
            HeapItem(8), HeapItem(9) ], list)
        self.assertEqual(5, self.heap.size)

    def test_sort_on_unsorted_five_element_list(self):
        list = [ HeapItem(9), HeapItem(8), HeapItem(5), HeapItem(4),
            HeapItem(2) ]

        self.heap.sort_in_place(list)

        self.assertEqual([ HeapItem(2), HeapItem(4), HeapItem(5),
            HeapItem(8), HeapItem(9) ], list)
        self.assertEqual(5, self.heap.size)

    def test_sort_on_seven_element_list_with_duplicates(self):
        list = [ HeapItem(9), HeapItem(5), HeapItem(4), HeapItem(2),
            HeapItem(5), HeapItem(2), HeapItem(8) ]

        self.heap.sort_in_place(list)

        self.assertEqual([ HeapItem(2), HeapItem(2), HeapItem(4),
            HeapItem(5), HeapItem(5), HeapItem(8), HeapItem(9) ], list)
        self.assertEqual(7, self.heap.size)

class CommonHeapSortTestCase(unittest.TestCase):

    def test_empty_list(self):
        list = []

        self.method_under_test(list)

        self.assertEqual([], list)

    def test_one_element_list(self):
        list = [ HeapItem(1) ]

        self.method_under_test(list)

        self.assertEqual([ HeapItem(1) ], list)

    def test_sorted_two_element_list(self):
        list = [ HeapItem(1), HeapItem(2) ]

        self.method_under_test(list)

        self.assertEqual([ HeapItem(1), HeapItem(2) ], list)

    def test_unsorted_two_element_list(self):
        list = [ HeapItem(2), HeapItem(1) ]

        self.method_under_test(list)

        self.assertEqual([ HeapItem(1), HeapItem(2) ], list)

    def test_sorted_three_element_list(self):
        list = [ HeapItem(1), HeapItem(2), HeapItem(3) ]

        self.method_under_test(list)

        self.assertEqual([ HeapItem(1), HeapItem(2), HeapItem(3) ], list)

    def test_unsorted_three_element_list(self):
        list = [ HeapItem(3), HeapItem(2), HeapItem(1) ]

        self.method_under_test(list)

        self.assertEqual([ HeapItem(1), HeapItem(2), HeapItem(3) ], list)

    def test_sorted_four_element_list(self):
        list = [ HeapItem(1), HeapItem(2), HeapItem(3), HeapItem(4) ]

        self.method_under_test(list)

        self.assertEqual([ HeapItem(1), HeapItem(2), HeapItem(3),
            HeapItem(4) ], list)

    def test_sorted_five_element_list(self):
        list = [ HeapItem(4), HeapItem(3), HeapItem(2), HeapItem(1) ]

        self.method_under_test(list)

        self.assertEqual([ HeapItem(1), HeapItem(2), HeapItem(3),
            HeapItem(4) ], list)

    def test_sorted_five_element_list(self):
        list = [ HeapItem(2), HeapItem(4), HeapItem(5), HeapItem(8),
            HeapItem(9) ]

        self.method_under_test(list)

        self.assertEqual([ HeapItem(2), HeapItem(4), HeapItem(5),
            HeapItem(8), HeapItem(9) ], list)

    def test_unsorted_five_element_list(self):
        list = [ HeapItem(9), HeapItem(4), HeapItem(2), HeapItem(5),
            HeapItem(8) ]

        self.method_under_test(list)

        self.assertEqual([ HeapItem(2), HeapItem(4), HeapItem(5),
            HeapItem(8), HeapItem(9) ], list)

    def test_seven_element_list_with_duplicates(self):
        list = [ HeapItem(9), HeapItem(5), HeapItem(4), HeapItem(2),
            HeapItem(5), HeapItem(2), HeapItem(8) ]

        self.method_under_test(list)

        self.assertEqual([ HeapItem(2), HeapItem(2), HeapItem(4),
            HeapItem(5), HeapItem(5), HeapItem(8), HeapItem(9) ], list)

class HeapSortWithMinBinHeapTestCase(CommonHeapSortTestCase):

    def setUp(self):
        self.method_under_test = heap_sort.sort_with_min_bin_heap

    def tearDown(self):
        pass

class HeapSortWithMaxBinHeapTestCase(CommonHeapSortTestCase):

    def setUp(self):
        self.method_under_test = heap_sort.sort_with_max_bin_heap

    def tearDown(self):
        pass

class PartialHeapSortTestCase(unittest.TestCase):

    def test_partially_sort_with_preceeding_k(self):
        data = [ HeapItem(9), HeapItem(5), HeapItem(6),
            HeapItem(2), HeapItem(3) ]
        with self.assertRaisesRegex(ValueError,
            'The k parameter must be within the data range.'):
            heap_sort.partially_sort(data, -1)

    def test_partially_sort_with_exceeding_k(self):
        data = [ HeapItem(9), HeapItem(5), HeapItem(6),
            HeapItem(2), HeapItem(3) ]
        with self.assertRaisesRegex(ValueError,
            'The k parameter must be within the data range.'):
            heap_sort.partially_sort(data, 6)

    def test_partially_sort_with_empty_data(self):
        k = 0
        data = []

        result = heap_sort.partially_sort(data, k)

        self.assertEqual([], result)
        self.assertEqual([], data)

    def test_partially_sort_with_one_element_data_and_k_as_0(self):
        k = 0
        data = [ HeapItem(1) ]

        result = heap_sort.partially_sort(data, k)

        self.assertEqual([], result)
        self.assertEqual([ HeapItem(1) ], data)

    def test_partially_sort_with_one_element_data_and_k_as_1(self):
        k = 1
        data = [ HeapItem(1) ]

        result = heap_sort.partially_sort(data, k)

        self.assertEqual([ HeapItem(1) ], result)
        self.assertEqual([], data)

    def test_partially_sort_with_two_element_data_and_k_as_0(self):
        k = 0
        data = [ HeapItem(2), HeapItem(1) ]

        result = heap_sort.partially_sort(data, k)

        self.assertEqual([], result)
        self.assertEqual([ HeapItem(2), HeapItem(1) ], data)

    def test_partially_sort_with_two_element_data_and_k_as_1(self):
        k = 1
        data = [ HeapItem(2), HeapItem(1) ]

        result = heap_sort.partially_sort(data, k)

        self.assertEqual([ HeapItem(2) ], result)
        self.assertEqual([ HeapItem(1) ], data)

    def test_partially_sort_with_two_element_data_and_k_as_2(self):
        k = 2
        data = [ HeapItem(2), HeapItem(1) ]

        result = heap_sort.partially_sort(data, k)

        self.assertEqual([ HeapItem(1), HeapItem(2) ], result)
        self.assertEqual([], data)

    def test_partially_sort_with_five_element_data_and_k_as_0(self):
        k = 0
        data = [ HeapItem(9), HeapItem(5), HeapItem(6),
            HeapItem(2), HeapItem(3) ]

        result = heap_sort.partially_sort(data, k)

        self.assertEqual([], result)
        self.assertEqual([ HeapItem(9), HeapItem(5), HeapItem(6),
            HeapItem(2), HeapItem(3) ], data)

    def test_partially_sort_with_five_element_data_and_k_as_1(self):
        k = 1
        data = [ HeapItem(9), HeapItem(5), HeapItem(6),
            HeapItem(2), HeapItem(3) ]

        result = heap_sort.partially_sort(data, k)

        self.assertEqual([ HeapItem(9) ], result)
        self.assertEqual([ HeapItem(6), HeapItem(5), HeapItem(3),
            HeapItem(2) ], data)

    def test_partially_sort_with_five_element_data_and_k_as_2(self):
        k = 2
        data = [ HeapItem(9), HeapItem(5), HeapItem(6),
            HeapItem(2), HeapItem(3) ]

        result = heap_sort.partially_sort(data, k)

        self.assertEqual([ HeapItem(6), HeapItem(9) ], result)
        self.assertEqual([ HeapItem(5), HeapItem(2), HeapItem(3) ], data)

    def test_partially_sort_with_five_element_data_and_k_as_3(self):
        k = 3
        data = [ HeapItem(9), HeapItem(5), HeapItem(6), HeapItem(2),
            HeapItem(3) ]

        result = heap_sort.partially_sort(data, k)

        self.assertEqual([ HeapItem(5), HeapItem(6), HeapItem(9) ], result)
        self.assertEqual([ HeapItem(3), HeapItem(2) ], data)

    def test_partially_sort_with_five_element_data_and_k_as_4(self):
        k = 4
        data = [ HeapItem(9), HeapItem(5), HeapItem(6), HeapItem(2),
            HeapItem(3) ]

        result = heap_sort.partially_sort(data, k)

        self.assertEqual([ HeapItem(3), HeapItem(5), HeapItem(6),
            HeapItem(9) ], result)
        self.assertEqual([ HeapItem(2) ], data)

    def test_partially_sort_with_five_element_data_and_k_as_5(self):
        k = 5
        data = [ HeapItem(9), HeapItem(5), HeapItem(6), HeapItem(2),
            HeapItem(3) ]

        result = heap_sort.partially_sort(data, k)

        self.assertEqual([ HeapItem(2), HeapItem(3), HeapItem(5),
            HeapItem(6), HeapItem(9) ], result)
        self.assertEqual([], data)

class BinHeapAsMinWithItemCompareTestCase(unittest.TestCase):

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
        self.heap.build([ HeapItem(1, 1) ])

        self.assertEqual(1, self.heap.size)
        self.assertEqual([ HeapItem(1, 1) ], self.heap.elements)

    def test_build_on_two_element_list_as_1_1_and_2_2(self):
        self.heap.build([ HeapItem(1, 1), HeapItem(2, 2) ])

        self.assertEqual(2, self.heap.size)
        self.assertEqual([ HeapItem(1, 1), HeapItem(2, 2) ],
            self.heap.elements)

    def test_build_on_two_element_list_as_2_2_and_1_1(self):
        self.heap.build([ HeapItem(2, 2), HeapItem(1, 1) ])

        self.assertEqual(2, self.heap.size)
        self.assertEqual([ HeapItem(1, 1), HeapItem(2, 2) ],
            self.heap.elements)

    def test_build_on_two_element_list_as_2_1_and_2_2(self):
        self.heap.build([ HeapItem(2, 1), HeapItem(2, 2) ])

        self.assertEqual(2, self.heap.size)
        self.assertEqual([ HeapItem(2, 1), HeapItem(2, 2) ],
            self.heap.elements)

    def test_build_on_two_element_list_as_2_2_and_2_1(self):
        self.heap.build([ HeapItem(2, 2), HeapItem(2, 1) ])

        self.assertEqual(2, self.heap.size)
        self.assertEqual([ HeapItem(2, 1), HeapItem(2, 2) ],
            self.heap.elements)

    def test_build_on_three_element_list_as_1_2_3(self):
        self.heap.build([ HeapItem(1, 1), HeapItem(2, 2), HeapItem(3, 3) ])

        self.assertEqual(3, self.heap.size)
        self.assertEqual([ HeapItem(1, 1), HeapItem(2, 2), HeapItem(3, 3) ],
            self.heap.elements)

    def test_build_on_three_element_list_as_1_3_2(self):
        self.heap.build([ HeapItem(1, 1), HeapItem(3, 3), HeapItem(2, 2) ])

        self.assertEqual(3, self.heap.size)
        self.assertEqual([ HeapItem(1, 1), HeapItem(3, 3), HeapItem(2, 2) ],
            self.heap.elements)

    def test_build_on_three_element_list_as_2_1_3(self):
        data = [ HeapItem(2, 2), HeapItem(1, 1), HeapItem(3, 3) ]

        self.heap.build(data)

        self.assertEqual(3, self.heap.size)
        self.assertEqual([ HeapItem(1, 1), HeapItem(2, 2), HeapItem(3, 3) ],
            self.heap.elements)

    def test_build_on_three_element_list_as_2_3_1(self):
        self.heap.build([ HeapItem(2, 2), HeapItem(3, 3), HeapItem(1, 1) ])

        self.assertEqual(3, self.heap.size)
        self.assertEqual([ HeapItem(1, 1), HeapItem(3, 3), HeapItem(2, 2) ],
            self.heap.elements)

    def test_build_on_three_element_list_as_3_1_2(self):
        self.heap.build([ HeapItem(3, 3), HeapItem(1, 1), HeapItem(2, 2) ])

        self.assertEqual(3, self.heap.size)
        self.assertEqual([ HeapItem(1, 1), HeapItem(3, 3), HeapItem(2, 2) ],
            self.heap.elements)

    def test_build_on_three_element_list_as_3_2_1(self):
        self.heap.build([ HeapItem(3, 3), HeapItem(2, 2), HeapItem(1, 1) ])

        self.assertEqual(3, self.heap.size)
        self.assertEqual([ HeapItem(1, 1), HeapItem(2, 2), HeapItem(3, 3) ],
            self.heap.elements)

    def test_build_on_three_element_list_with_equal_priorities(self):
        self.heap.build([ HeapItem(2, 3), HeapItem(2, 2), HeapItem(2, 1) ])

        self.assertEqual(3, self.heap.size)
        self.assertEqual([ HeapItem(2, 1), HeapItem(2, 2), HeapItem(2, 3) ],
            self.heap.elements)

    def test_build_on_four_element_list(self):
        self.heap.build([ HeapItem(9, 9), HeapItem(5, 5), HeapItem(6, 6),
            HeapItem(2, 2) ])

        self.assertEqual(4, self.heap.size)
        self.assertEqual([ HeapItem(2, 2), HeapItem(5, 5), HeapItem(6, 6),
            HeapItem(9, 9) ], self.heap.elements)

    def test_build_on_four_element_list_with_equal_priorities(self):
        self.heap.build([ HeapItem(2, 4), HeapItem(2, 3), HeapItem(2, 2),
            HeapItem(2, 1) ])

        self.assertEqual(4, self.heap.size)
        self.assertEqual([ HeapItem(2, 1), HeapItem(2, 3), HeapItem(2, 2),
            HeapItem(2, 4) ], self.heap.elements)

    def test_build_on_five_element_list(self):
        self.heap.build([ HeapItem(9, 9), HeapItem(5, 5), HeapItem(6, 6),
            HeapItem(2, 2), HeapItem(3, 3) ])

        self.assertEqual(5, self.heap.size)
        self.assertEqual([ HeapItem(2, 2), HeapItem(3, 3), HeapItem(6, 6),
            HeapItem(5, 5), HeapItem(9, 9) ], self.heap.elements)

    def test_build_on_five_element_list_with_equal_priorities(self):
        self.heap.build([ HeapItem(2, 5), HeapItem(2, 4), HeapItem(2, 3),
            HeapItem(2, 2), HeapItem(2, 1) ])

        self.assertEqual(5, self.heap.size)
        self.assertEqual([ HeapItem(2, 1), HeapItem(2, 2), HeapItem(2, 3),
            HeapItem(2, 5), HeapItem(2, 4) ], self.heap.elements)

if __name__ == '__main__':
    class_names = \
    [
        HeapItemTestCase,
        BinHeapAsMinTestCase,
        BinHeapAsMaxTestCase,
        HeapSortWithMinBinHeapTestCase,
        HeapSortWithMaxBinHeapTestCase,
        PartialHeapSortTestCase,
        BinHeapAsMinWithItemCompareTestCase
    ]

    suite = unittest.TestSuite()

    for c in class_names:
        suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(c))

    unittest.TextTestRunner().run(suite)
