#!/usr/bin/python3

import unittest

import heap

class HeapItemTestCase(unittest.TestCase):

    def test_constructor_with_priority(self):
        priority = 123
        item = heap.HeapItem(priority)

        self.assertEqual(priority, item.priority)
        self.assertEqual(None, item.datum)

    def test_constructor_with_priority_and_datum(self):
        priority = 123
        datum = 'datum'
        item = heap.HeapItem(priority, datum)

        self.assertEqual(priority, item.priority)
        self.assertEqual(datum, item.datum)

    def test_str_with_priority(self):
        item = heap.HeapItem(123)

        self.assertEqual('None', str(item))

    def test_str_with_priority_and_datum(self):
        item = heap.HeapItem(123, 'datum')

        self.assertEqual('datum', str(item))

    def test_repr_with_priority(self):
        item = heap.HeapItem(123)

        self.assertEqual('[priority=123, datum=None]', repr(item))

    def test_repr_with_priority_and_datum(self):
        item = heap.HeapItem(123, 'test-datum')

        self.assertEqual('[priority=123, datum=test-datum]', repr(item))

    def test_lt_with_priority_as_equal(self):
        item = heap.HeapItem(123)
        other = heap.HeapItem(123)

        self.assertFalse(item < other)
        self.assertFalse(other < item)

    def test_lt_with_priority_as_not_equal(self):
        item = heap.HeapItem(123)
        other = heap.HeapItem(456)

        self.assertTrue(item < other)
        self.assertFalse(other < item)

    def test_lt_with_priority_and_datum_as_equal(self):
        item = heap.HeapItem(123, 'datum')
        other = heap.HeapItem(123, 'datum')

        self.assertFalse(item < other)
        self.assertFalse(other < item)

    def test_lt_with_priority_and_datum_as_not_equal_priorities(self):
        item = heap.HeapItem(123, 'datum')
        other = heap.HeapItem(456, 'datum')

        self.assertTrue(item < other)
        self.assertFalse(other < item)

    def test_lt_with_priority_and_datum_as_not_equal_data(self):
        item = heap.HeapItem(123, 'datum1')
        other = heap.HeapItem(123, 'datum2')

        self.assertTrue(item < other)
        self.assertFalse(other < item)

    def test_lt_with_priority_and_datum_as_not_equal(self):
        item = heap.HeapItem(123, 'datum1')
        other = heap.HeapItem(456, 'datum2')

        self.assertTrue(item < other)
        self.assertFalse(other < item)

    def test_eq_with_priority_as_equal(self):
        item = heap.HeapItem(123)
        other = heap.HeapItem(123)

        self.assertTrue(item == other)
        self.assertTrue(other == item)

    def test_eq_with_priority_as_not_equal(self):
        item = heap.HeapItem(123)
        other = heap.HeapItem(456)

        self.assertFalse(item == other)
        self.assertFalse(other == item)

    def test_eq_with_priority_and_datum_as_equal(self):
        item = heap.HeapItem(123, 'datum')
        other = heap.HeapItem(123, 'datum')

        self.assertTrue(item == other)
        self.assertTrue(other == item)

    def test_eq_with_priority_and_datum_as_not_equal_priorities(self):
        item = heap.HeapItem(123, 'datum')
        other = heap.HeapItem(456, 'datum')

        self.assertFalse(item == other)
        self.assertFalse(other == item)

    def test_eq_with_priority_and_datum_as_not_equal_data(self):
        item = heap.HeapItem(123, 'datum1')
        other = heap.HeapItem(123, 'datum2')

        self.assertFalse(item == other)
        self.assertFalse(other == item)

    def test_eq_with_priority_and_datum_as_not_equal(self):
        item = heap.HeapItem(123, 'datum1')
        other = heap.HeapItem(456, 'datum2')

        self.assertFalse(item == other)
        self.assertFalse(other == item)

    def test_gt_with_priority_as_equal(self):
        item = heap.HeapItem(123)
        other = heap.HeapItem(123)

        self.assertFalse(item > other)
        self.assertFalse(other > item)

    def test_gt_with_priority_as_not_equal(self):
        item = heap.HeapItem(123)
        other = heap.HeapItem(456)

        self.assertFalse(item > other)
        self.assertTrue(other > item)

    def test_gt_with_priority_and_datum_as_equal(self):
        item = heap.HeapItem(123, 'datum')
        other = heap.HeapItem(123, 'datum')

        self.assertFalse(item > other)
        self.assertFalse(other > item)

    def test_gt_with_priority_and_datum_as_not_equal_priorities(self):
        item = heap.HeapItem(123, 'datum')
        other = heap.HeapItem(456, 'datum')

        self.assertFalse(item > other)
        self.assertTrue(other > item)

    def test_gt_with_priority_and_datum_as_not_equal_data(self):
        item = heap.HeapItem(123, 'datum1')
        other = heap.HeapItem(123, 'datum2')

        self.assertFalse(item > other)
        self.assertTrue(other > item)

    def test_gt_with_priority_and_datum_as_not_equal(self):
        item = heap.HeapItem(123, 'datum1')
        other = heap.HeapItem(456, 'datum2')

        self.assertFalse(item > other)
        self.assertTrue(other > item)

class BinHeapAsMinTestCase(unittest.TestCase):

    def setUp(self):
        self.heap = heap.BinHeap(heap.HeapMode.min)

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
        self.heap.build([ heap.HeapItem(1, 'datum1'),
                         heap.HeapItem(2, 'datum2'),
                         heap.HeapItem(3, 'datum3') ])

        self.assertEqual('[[priority=1, datum=datum1], ' +
                         '[priority=2, datum=datum2], ' +
                         '[priority=3, datum=datum3]]',
            str(self.heap))

    def test_repr_on_three_element_heap(self):
        self.heap.build([ heap.HeapItem(1, 'datum1'),
                         heap.HeapItem(2, 'datum2'),
                         heap.HeapItem(3, 'datum3') ])

        self.assertEqual('[mode=HeapMode.min, size=3, ' +
                         'list=[[priority=1, datum=datum1], ' +
                         '[priority=2, datum=datum2], ' +
                         '[priority=3, datum=datum3]]]',
            repr(self.heap))

    def test_build_on_empty_list(self):
        self.heap.build([])

        self.assertEqual(0, self.heap.size)
        self.assertEqual([], self.heap.elements)

    def test_build_on_one_element_list(self):
        self.heap.build([ heap.HeapItem(1) ])

        self.assertEqual(1, self.heap.size)
        self.assertEqual([ heap.HeapItem(1) ], self.heap.elements)

    def test_build_on_two_element_list_as_1_2(self):
        self.heap.build([ heap.HeapItem(1), heap.HeapItem(2) ])

        self.assertEqual(2, self.heap.size)
        self.assertEqual([ heap.HeapItem(1), heap.HeapItem(2) ],
                         self.heap.elements)

    def test_build_on_two_element_list_as_2_1(self):
        self.heap.build([ heap.HeapItem(2), heap.HeapItem(1) ])

        self.assertEqual(2, self.heap.size)
        self.assertEqual([ heap.HeapItem(1), heap.HeapItem(2) ],
                         self.heap.elements)

    def test_build_on_three_element_list_as_1_2_3(self):
        self.heap.build([ heap.HeapItem(1), heap.HeapItem(2),
                         heap.HeapItem(3) ])

        self.assertEqual(3, self.heap.size)
        self.assertEqual([ heap.HeapItem(1), heap.HeapItem(2),
                          heap.HeapItem(3) ],
                         self.heap.elements)

    def test_build_on_three_element_list_as_1_3_2(self):
        self.heap.build([ heap.HeapItem(1), heap.HeapItem(3),
                         heap.HeapItem(2) ])

        self.assertEqual(3, self.heap.size)
        self.assertEqual([ heap.HeapItem(1), heap.HeapItem(3),
                          heap.HeapItem(2) ],
                         self.heap.elements)

    def test_build_on_three_element_list_as_2_1_3(self):
        data = [ heap.HeapItem(2), heap.HeapItem(1), heap.HeapItem(3) ]

        self.heap.build(data)

        self.assertEqual(3, self.heap.size)
        self.assertEqual([ heap.HeapItem(1), heap.HeapItem(2),
                          heap.HeapItem(3) ],
                         self.heap.elements)

    def test_build_on_three_element_list_as_2_3_1(self):
        self.heap.build([ heap.HeapItem(2), heap.HeapItem(3),
                         heap.HeapItem(1) ])

        self.assertEqual(3, self.heap.size)
        self.assertEqual([ heap.HeapItem(1), heap.HeapItem(3),
                          heap.HeapItem(2) ],
                         self.heap.elements)

    def test_build_on_three_element_list_as_3_1_2(self):
        self.heap.build([ heap.HeapItem(3), heap.HeapItem(1),
                         heap.HeapItem(2) ])

        self.assertEqual(3, self.heap.size)
        self.assertEqual([ heap.HeapItem(1), heap.HeapItem(3),
                          heap.HeapItem(2) ],
                         self.heap.elements)

    def test_build_on_three_element_list_as_3_2_1(self):
        self.heap.build([ heap.HeapItem(3), heap.HeapItem(2),
                         heap.HeapItem(1) ])

        self.assertEqual(3, self.heap.size)
        self.assertEqual([ heap.HeapItem(1), heap.HeapItem(2),
                          heap.HeapItem(3) ],
                         self.heap.elements)

    def test_build_on_four_element_list(self):
        self.heap.build([ heap.HeapItem(9), heap.HeapItem(5),
                         heap.HeapItem(6),
                         heap.HeapItem(2) ])

        self.assertEqual(4, self.heap.size)
        self.assertEqual([ heap.HeapItem(2), heap.HeapItem(5),
                          heap.HeapItem(6), heap.HeapItem(9) ],
                         self.heap.elements)

    def test_build_on_five_element_list(self):
        self.heap.build([ heap.HeapItem(9), heap.HeapItem(5),
                         heap.HeapItem(6), heap.HeapItem(2),
                         heap.HeapItem(3) ])

        self.assertEqual(5, self.heap.size)
        self.assertEqual([ heap.HeapItem(2), heap.HeapItem(3),
                          heap.HeapItem(6), heap.HeapItem(5),
                          heap.HeapItem(9) ],
                         self.heap.elements)

    def test_build_on_six_element_list(self):
        self.heap.build([ heap.HeapItem(9), heap.HeapItem(5),
                         heap.HeapItem(6), heap.HeapItem(2),
                         heap.HeapItem(3), heap.HeapItem(1) ])

        self.assertEqual(6, self.heap.size)
        self.assertEqual([ heap.HeapItem(1), heap.HeapItem(2),
                          heap.HeapItem(6), heap.HeapItem(5),
                          heap.HeapItem(3), heap.HeapItem(9) ],
                         self.heap.elements)

    def test_build_on_seven_element_list(self):
        self.heap.build([ heap.HeapItem(9), heap.HeapItem(5),
                         heap.HeapItem(6), heap.HeapItem(2),
                         heap.HeapItem(3), heap.HeapItem(1),
                         heap.HeapItem(0) ])

        self.assertEqual(7, self.heap.size)
        self.assertEqual([ heap.HeapItem(0), heap.HeapItem(2),
                          heap.HeapItem(1), heap.HeapItem(5),
                          heap.HeapItem(3), heap.HeapItem(9),
                          heap.HeapItem(6) ],
                         self.heap.elements)

    def test_build_on_seven_element_list_with_duplicates(self):
        self.heap.build([ heap.HeapItem(9), heap.HeapItem(5),
                         heap.HeapItem(2), heap.HeapItem(2),
                         heap.HeapItem(1), heap.HeapItem(1),
                         heap.HeapItem(0) ])

        self.assertEqual(7, self.heap.size)
        self.assertEqual([ heap.HeapItem(0), heap.HeapItem(1),
                          heap.HeapItem(1), heap.HeapItem(2),
                          heap.HeapItem(5), heap.HeapItem(9),
                          heap.HeapItem(2) ],
                         self.heap.elements)

    def test_build_on_seven_duplicate_element_list(self):
        self.heap.build([ heap.HeapItem(3), heap.HeapItem(3),
                         heap.HeapItem(3), heap.HeapItem(3), heap.HeapItem(3),
                         heap.HeapItem(3), heap.HeapItem(3) ])

        self.assertEqual(7, self.heap.size)
        self.assertEqual([ heap.HeapItem(3), heap.HeapItem(3),
                          heap.HeapItem(3), heap.HeapItem(3),
                          heap.HeapItem(3), heap.HeapItem(3),
                          heap.HeapItem(3) ],
                         self.heap.elements)

    def test_extract_on_five_element_list(self):
        self.heap.build([ heap.HeapItem(9), heap.HeapItem(5),
                         heap.HeapItem(6), heap.HeapItem(2),
                         heap.HeapItem(3) ])

        self.assertEqual(5, self.heap.size)
        self.assertEqual([ heap.HeapItem(2), heap.HeapItem(3),
                          heap.HeapItem(6), heap.HeapItem(5),
                          heap.HeapItem(9) ],
                         self.heap.elements)

        min = self.heap.extract()

        self.assertEqual(heap.HeapItem(2), min)
        self.assertEqual(4, self.heap.size)
        self.assertEqual([ heap.HeapItem(3), heap.HeapItem(5),
                          heap.HeapItem(6), heap.HeapItem(9) ],
                         self.heap.elements)

        min = self.heap.extract()

        self.assertEqual(heap.HeapItem(3), min)
        self.assertEqual(3, self.heap.size)
        self.assertEqual([ heap.HeapItem(5), heap.HeapItem(9),
                          heap.HeapItem(6) ],
                         self.heap.elements)

        min = self.heap.extract()

        self.assertEqual(heap.HeapItem(5), min)
        self.assertEqual(2, self.heap.size)
        self.assertEqual([ heap.HeapItem(6), heap.HeapItem(9) ],
                         self.heap.elements)

        min = self.heap.extract()

        self.assertEqual(heap.HeapItem(6), min)
        self.assertEqual(1, self.heap.size)
        self.assertEqual([ heap.HeapItem(9) ], self.heap.elements)

        min = self.heap.extract()

        self.assertEqual(heap.HeapItem(9), min)
        self.assertEqual(0, self.heap.size)
        self.assertEqual([], self.heap.elements)

    def test_insert_on_empty_list(self):
        self.heap.insert(heap.HeapItem(1))

        self.assertEqual(1, self.heap.size)
        self.assertEqual([ heap.HeapItem(1) ], self.heap.elements)

    def test_insert_on_one_element_list(self):
        self.heap.build([ heap.HeapItem(2) ])

        self.assertEqual(1, self.heap.size)
        self.assertEqual([ heap.HeapItem(2) ], self.heap.elements)

        self.heap.insert(heap.HeapItem(1))

        self.assertEqual(2, self.heap.size)
        self.assertEqual([ heap.HeapItem(1), heap.HeapItem(2) ],
                         self.heap.elements)

    def test_insert_on_two_element_list(self):
        self.heap.build([ heap.HeapItem(2), heap.HeapItem(3) ])

        self.assertEqual(2, self.heap.size)
        self.assertEqual([ heap.HeapItem(2), heap.HeapItem(3) ],
                         self.heap.elements)

        self.heap.insert(heap.HeapItem(1))

        self.assertEqual(3, self.heap.size)
        self.assertEqual([ heap.HeapItem(1), heap.HeapItem(3),
                          heap.HeapItem(2) ],
                         self.heap.elements)

    def test_insert_on_three_element_list(self):
        self.heap.build([ heap.HeapItem(2), heap.HeapItem(3),
                         heap.HeapItem(4) ])

        self.assertEqual(3, self.heap.size)
        self.assertEqual([ heap.HeapItem(2), heap.HeapItem(3),
                          heap.HeapItem(4) ],
                         self.heap.elements)

        self.heap.insert(heap.HeapItem(1))

        self.assertEqual(4, self.heap.size)
        self.assertEqual([ heap.HeapItem(1), heap.HeapItem(2),
                          heap.HeapItem(4), heap.HeapItem(3) ],
                         self.heap.elements)

    def test_insert_on_four_element_list(self):
        self.heap.build([ heap.HeapItem(2), heap.HeapItem(3),
                         heap.HeapItem(4), heap.HeapItem(5) ])

        self.assertEqual(4, self.heap.size)
        self.assertEqual([ heap.HeapItem(2), heap.HeapItem(3),
                          heap.HeapItem(4), heap.HeapItem(5) ],
                         self.heap.elements)

        self.heap.insert(heap.HeapItem(1))

        self.assertEqual(5, self.heap.size)
        self.assertEqual([ heap.HeapItem(1), heap.HeapItem(2),
                          heap.HeapItem(4), heap.HeapItem(5),
                          heap.HeapItem(3) ],
                         self.heap.elements)

    def test_insert_on_five_element_list(self):
        self.heap.build([ heap.HeapItem(2), heap.HeapItem(3),
                         heap.HeapItem(6), heap.HeapItem(5),
                         heap.HeapItem(9) ])

        self.assertEqual(5, self.heap.size)
        self.assertEqual([ heap.HeapItem(2), heap.HeapItem(3),
                          heap.HeapItem(6), heap.HeapItem(5),
                          heap.HeapItem(9) ],
                         self.heap.elements)

        self.heap.insert(heap.HeapItem(1))

        self.assertEqual(6, self.heap.size)
        self.assertEqual([ heap.HeapItem(1), heap.HeapItem(3),
                          heap.HeapItem(2), heap.HeapItem(5),
                          heap.HeapItem(9), heap.HeapItem(6) ],
                         self.heap.elements)

    def test_change_priority_on_empty_list(self):
        with self.assertRaisesRegex(IndexError, ''):
            self.heap.change_priority(0, 1)

    def test_change_priority_on_non_empty_list_with_preceeding_index(self):
        self.heap.build([ heap.HeapItem(9), heap.HeapItem(5), heap.HeapItem(6),
                         heap.HeapItem(2), heap.HeapItem(3) ])
        with self.assertRaisesRegex(IndexError, ''):
            self.heap.change_priority(-1, 1)

    def test_change_priority_on_non_empty_list_with_exceeding_index(self):
        self.heap.build([ heap.HeapItem(9), heap.HeapItem(5), heap.HeapItem(6),
                         heap.HeapItem(2), heap.HeapItem(3) ])
        with self.assertRaisesRegex(IndexError, ''):
            self.heap.change_priority(self.heap.size, 1)

    def test_change_priority_on_one_element_list(self):
        self.heap.build([ heap.HeapItem(9) ])

        self.assertEqual(1, self.heap.size)
        self.assertEqual([ heap.HeapItem(9)], self.heap.elements)

        self.heap.change_priority(0, 1)

        self.assertEqual(1, self.heap.size)
        self.assertEqual([ heap.HeapItem(1) ], self.heap.elements)

    def test_change_priority_on_two_element_list_without_sift(self):
        self.heap.build([ heap.HeapItem(9), heap.HeapItem(6) ])

        self.assertEqual(2, self.heap.size)
        self.assertEqual([ heap.HeapItem(6), heap.HeapItem(9) ],
                         self.heap.elements)

        self.heap.change_priority(0, 1)

        self.assertEqual(2, self.heap.size)
        self.assertEqual([ heap.HeapItem(1), heap.HeapItem(9) ],
                         self.heap.elements)

        self.heap.change_priority(1, 2)

        self.assertEqual(2, self.heap.size)
        self.assertEqual([ heap.HeapItem(1), heap.HeapItem(2) ],
                         self.heap.elements)

    def test_change_priority_on_two_element_list_with_sift_down_up(self):
        self.heap.build([ heap.HeapItem(9), heap.HeapItem(6) ])

        self.assertEqual(2, self.heap.size)
        self.assertEqual([ heap.HeapItem(6), heap.HeapItem(9) ],
                         self.heap.elements)

        self.heap.change_priority(0, 10)

        self.assertEqual(2, self.heap.size)
        self.assertEqual([ heap.HeapItem(9), heap.HeapItem(10) ],
                         self.heap.elements)

        self.heap.change_priority(1, 8)

        self.assertEqual(2, self.heap.size)
        self.assertEqual([ heap.HeapItem(8), heap.HeapItem(9) ],
                         self.heap.elements)

    def test_change_priority_on_five_element_list_with_sift_down(self):
        self.heap.build([ heap.HeapItem(3), heap.HeapItem(4),
                         heap.HeapItem(5), heap.HeapItem(6),
                         heap.HeapItem(9) ])

        self.assertEqual(5, self.heap.size)
        self.assertEqual([ heap.HeapItem(3), heap.HeapItem(4),
                          heap.HeapItem(5), heap.HeapItem(6),
                          heap.HeapItem(9) ],
                         self.heap.elements)

        self.heap.change_priority(1, 10)

        self.assertEqual(5, self.heap.size)
        self.assertEqual([ heap.HeapItem(3), heap.HeapItem(6),
                          heap.HeapItem(5), heap.HeapItem(10),
                          heap.HeapItem(9) ],
                         self.heap.elements)

    def test_change_priority_on_five_element_list_with_sift_up(self):
        self.heap.build([ heap.HeapItem(3), heap.HeapItem(4),
                         heap.HeapItem(5), heap.HeapItem(6),
                         heap.HeapItem(9) ])

        self.assertEqual(5, self.heap.size)
        self.assertEqual([ heap.HeapItem(3), heap.HeapItem(4),
                          heap.HeapItem(5), heap.HeapItem(6),
                          heap.HeapItem(9) ],
                         self.heap.elements)

        self.heap.change_priority(3, 0)

        self.assertEqual(5, self.heap.size)
        self.assertEqual([ heap.HeapItem(0), heap.HeapItem(3),
                          heap.HeapItem(5), heap.HeapItem(4),
                          heap.HeapItem(9) ],
                         self.heap.elements)

    def test_sort_on_empty_list(self):
        list = []

        self.heap.sort_in_place(list)

        self.assertEqual([], list)
        self.assertEqual(0, self.heap.size)

    def test_sort_on_one_element_list(self):
        list = [ heap.HeapItem(1) ]

        self.heap.sort_in_place(list)

        self.assertEqual([ heap.HeapItem(1) ], list)
        self.assertEqual(1, self.heap.size)

    def test_sort_on_unsorted_two_element_list(self):
        list = [ heap.HeapItem(1), heap.HeapItem(2) ]

        self.heap.sort_in_place(list)

        self.assertEqual([ heap.HeapItem(2), heap.HeapItem(1) ], list)
        self.assertEqual(2, self.heap.size)

    def test_sort_on_sorted_two_element_list(self):
        list = [ heap.HeapItem(2), heap.HeapItem(1) ]

        self.heap.sort_in_place(list)

        self.assertEqual([ heap.HeapItem(2), heap.HeapItem(1) ], list)
        self.assertEqual(2, self.heap.size)

    def test_sort_on_unsorted_three_element_list(self):
        list = [ heap.HeapItem(1), heap.HeapItem(2), heap.HeapItem(3) ]

        self.heap.sort_in_place(list)

        self.assertEqual([ heap.HeapItem(3), heap.HeapItem(2),
                          heap.HeapItem(1) ],
                         list)
        self.assertEqual(3, self.heap.size)

    def test_sort_on_sorted_three_element_list(self):
        list = [ heap.HeapItem(3), heap.HeapItem(2), heap.HeapItem(1) ]

        self.heap.sort_in_place(list)

        self.assertEqual([ heap.HeapItem(3), heap.HeapItem(2),
                          heap.HeapItem(1) ],
                         list)
        self.assertEqual(3, self.heap.size)

    def test_sort_on_unsorted_four_element_list(self):
        list = [ heap.HeapItem(1), heap.HeapItem(2), heap.HeapItem(3),
                heap.HeapItem(4) ]

        self.heap.sort_in_place(list)

        self.assertEqual([ heap.HeapItem(4), heap.HeapItem(3),
                          heap.HeapItem(2), heap.HeapItem(1) ],
                         list)
        self.assertEqual(4, self.heap.size)

    def test_sort_on_sorted_five_element_list(self):
        list = [ heap.HeapItem(4), heap.HeapItem(3), heap.HeapItem(2),
                heap.HeapItem(1) ]

        self.heap.sort_in_place(list)

        self.assertEqual([ heap.HeapItem(4), heap.HeapItem(3),
                          heap.HeapItem(2), heap.HeapItem(1) ], list)
        self.assertEqual(4, self.heap.size)

    def test_sort_on_unsorted_five_element_list(self):
        list = [ heap.HeapItem(2), heap.HeapItem(4), heap.HeapItem(5),
                heap.HeapItem(8), heap.HeapItem(9) ]

        self.heap.sort_in_place(list)

        self.assertEqual([ heap.HeapItem(9), heap.HeapItem(8),
                          heap.HeapItem(5), heap.HeapItem(4),
                          heap.HeapItem(2) ],
                         list)
        self.assertEqual(5, self.heap.size)

    def test_sort_on_sorted_five_element_list(self):
        list = [ heap.HeapItem(9), heap.HeapItem(8), heap.HeapItem(5),
                heap.HeapItem(4), heap.HeapItem(2) ]

        self.heap.sort_in_place(list)

        self.assertEqual([ heap.HeapItem(9), heap.HeapItem(8),
                          heap.HeapItem(5), heap.HeapItem(4),
                          heap.HeapItem(2) ],
                         list)
        self.assertEqual(5, self.heap.size)

    def test_sort_on_seven_element_list_with_duplicates(self):
        list = [ heap.HeapItem(9), heap.HeapItem(5), heap.HeapItem(4),
                heap.HeapItem(2), heap.HeapItem(5), heap.HeapItem(2),
                heap.HeapItem(8) ]

        self.heap.sort_in_place(list)

        self.assertEqual([ heap.HeapItem(9), heap.HeapItem(8),
                          heap.HeapItem(5), heap.HeapItem(5),
                          heap.HeapItem(4), heap.HeapItem(2),
                          heap.HeapItem(2) ],
                         list)
        self.assertEqual(7, self.heap.size)

class BinHeapAsMaxTestCase(unittest.TestCase):

    def setUp(self):
        self.heap = heap.BinHeap(heap.HeapMode.max)

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
        self.heap.build([ heap.HeapItem(1, 'datum1'),
                         heap.HeapItem(2, 'datum2'),
                         heap.HeapItem(3, 'datum3') ])

        self.assertEqual('[[priority=3, datum=datum3], ' +
                         '[priority=2, datum=datum2], ' +
                         '[priority=1, datum=datum1]]',
            str(self.heap))

    def test_repr_on_three_element_heap(self):
        self.heap.build([ heap.HeapItem(1, 'datum1'),
                         heap.HeapItem(2, 'datum2'),
                         heap.HeapItem(3, 'datum3') ])

        self.assertEqual('[mode=HeapMode.max, size=3, ' +
                         'list=[[priority=3, datum=datum3], ' +
                         '[priority=2, datum=datum2], ' +
                         '[priority=1, datum=datum1]]]',
            repr(self.heap))

    def test_build_on_empty_list(self):
        self.heap.build([])

        self.assertEqual(0, self.heap.size)
        self.assertEqual([], self.heap.elements)

    def test_build_on_one_element_list(self):
        self.heap.build([ heap.HeapItem(1) ])

        self.assertEqual(1, self.heap.size)
        self.assertEqual([ heap.HeapItem(1) ], self.heap.elements)

    def test_build_on_two_element_list_as_1_2(self):
        self.heap.build([ heap.HeapItem(1), heap.HeapItem(2) ])

        self.assertEqual(2, self.heap.size)
        self.assertEqual([ heap.HeapItem(2), heap.HeapItem(1) ],
                         self.heap.elements)

    def test_build_on_two_element_list_as_2_1(self):
        self.heap.build([ heap.HeapItem(2), heap.HeapItem(1) ])

        self.assertEqual(2, self.heap.size)
        self.assertEqual([ heap.HeapItem(2), heap.HeapItem(1) ],
                         self.heap.elements)

    def test_build_on_three_element_list_as_1_2_3(self):
        self.heap.build([ heap.HeapItem(1), heap.HeapItem(2),
                         heap.HeapItem(3) ])

        self.assertEqual(3, self.heap.size)
        self.assertEqual([ heap.HeapItem(3), heap.HeapItem(2),
                          heap.HeapItem(1) ],
                         self.heap.elements)

    def test_build_on_three_element_list_as_1_3_2(self):
        self.heap.build([ heap.HeapItem(1), heap.HeapItem(3),
                         heap.HeapItem(2) ])

        self.assertEqual(3, self.heap.size)
        self.assertEqual([ heap.HeapItem(3), heap.HeapItem(1),
                          heap.HeapItem(2) ],
                         self.heap.elements)

    def test_build_on_three_element_list_as_2_1_3(self):
        self.heap.build([ heap.HeapItem(2), heap.HeapItem(1),
                         heap.HeapItem(3) ])

        self.assertEqual(3, self.heap.size)
        self.assertEqual([ heap.HeapItem(3), heap.HeapItem(1),
                          heap.HeapItem(2) ],
                         self.heap.elements)

    def test_build_on_three_element_list_as_2_3_1(self):
        self.heap.build([ heap.HeapItem(2), heap.HeapItem(3),
                         heap.HeapItem(1) ])

        self.assertEqual(3, self.heap.size)
        self.assertEqual([ heap.HeapItem(3), heap.HeapItem(2),
                          heap.HeapItem(1) ],
                         self.heap.elements)

    def test_build_on_three_element_list_as_3_1_2(self):
        self.heap.build([ heap.HeapItem(3), heap.HeapItem(1),
                         heap.HeapItem(2) ])

        self.assertEqual(3, self.heap.size)
        self.assertEqual([ heap.HeapItem(3), heap.HeapItem(1),
                          heap.HeapItem(2) ],
                         self.heap.elements)

    def test_build_on_three_element_list_as_3_2_1(self):
        self.heap.build([ heap.HeapItem(3), heap.HeapItem(2),
                         heap.HeapItem(1) ])

        self.assertEqual(3, self.heap.size)
        self.assertEqual([ heap.HeapItem(3), heap.HeapItem(2),
                          heap.HeapItem(1) ],
                         self.heap.elements)

    def test_build_on_four_element_list(self):
        self.heap.build([ heap.HeapItem(2), heap.HeapItem(5),
                         heap.HeapItem(6),
                         heap.HeapItem(9) ])

        self.assertEqual(4, self.heap.size)
        self.assertEqual([ heap.HeapItem(9), heap.HeapItem(5),
                          heap.HeapItem(6), heap.HeapItem(2) ],
                         self.heap.elements)

    def test_build_on_five_element_list(self):
        self.heap.build([ heap.HeapItem(2), heap.HeapItem(5),
                         heap.HeapItem(6), heap.HeapItem(9),
                         heap.HeapItem(10) ])

        self.assertEqual(5, self.heap.size)
        self.assertEqual([ heap.HeapItem(10), heap.HeapItem(9),
                          heap.HeapItem(6), heap.HeapItem(2),
                          heap.HeapItem(5) ],
                         self.heap.elements)

    def test_build_on_six_element_list(self):
        self.heap.build([ heap.HeapItem(2), heap.HeapItem(5),
                         heap.HeapItem(6), heap.HeapItem(9),
                         heap.HeapItem(10), heap.HeapItem(11) ])

        self.assertEqual(6, self.heap.size)
        self.assertEqual([ heap.HeapItem(11), heap.HeapItem(10),
                          heap.HeapItem(6), heap.HeapItem(9),
                          heap.HeapItem(5), heap.HeapItem(2) ],
                         self.heap.elements)

    def test_build_on_seven_element_list(self):
        self.heap.build([ heap.HeapItem(2), heap.HeapItem(5),
                         heap.HeapItem(6), heap.HeapItem(9),
                         heap.HeapItem(10), heap.HeapItem(11),
                         heap.HeapItem(12) ])

        self.assertEqual(7, self.heap.size)
        self.assertEqual([ heap.HeapItem(12), heap.HeapItem(10),
                          heap.HeapItem(11), heap.HeapItem(9),
                          heap.HeapItem(5), heap.HeapItem(2),
                          heap.HeapItem(6) ],
                         self.heap.elements)

    def test_build_on_seven_element_list_with_duplicates(self):
        self.heap.build([ heap.HeapItem(2), heap.HeapItem(6),
                         heap.HeapItem(6), heap.HeapItem(9),
                         heap.HeapItem(10), heap.HeapItem(10),
                         heap.HeapItem(12) ])

        self.assertEqual(7, self.heap.size)
        self.assertEqual([ heap.HeapItem(12), heap.HeapItem(10),
                          heap.HeapItem(10), heap.HeapItem(9),
                          heap.HeapItem(6), heap.HeapItem(2),
                          heap.HeapItem(6) ],
                         self.heap.elements)

    def test_build_on_seven_duplicate_element_list(self):
        self.heap.build([ heap.HeapItem(3), heap.HeapItem(3),
                         heap.HeapItem(3), heap.HeapItem(3),
                         heap.HeapItem(3), heap.HeapItem(3),
                         heap.HeapItem(3) ])

        self.assertEqual(7, self.heap.size)
        self.assertEqual([ heap.HeapItem(3), heap.HeapItem(3),
                          heap.HeapItem(3), heap.HeapItem(3),
                          heap.HeapItem(3), heap.HeapItem(3),
                          heap.HeapItem(3) ],
                         self.heap.elements)

    def test_extract_on_five_element_list(self):
        self.heap.build([ heap.HeapItem(2), heap.HeapItem(5),
                         heap.HeapItem(6), heap.HeapItem(9),
                         heap.HeapItem(10) ])

        self.assertEqual(5, self.heap.size)
        self.assertEqual([ heap.HeapItem(10), heap.HeapItem(9),
                          heap.HeapItem(6), heap.HeapItem(2),
                          heap.HeapItem(5) ],
                         self.heap.elements)

        max = self.heap.extract()

        self.assertEqual(heap.HeapItem(10), max)
        self.assertEqual(4, self.heap.size)
        self.assertEqual([ heap.HeapItem(9), heap.HeapItem(5),
                          heap.HeapItem(6), heap.HeapItem(2) ],
                         self.heap.elements)

        max = self.heap.extract()

        self.assertEqual(heap.HeapItem(9), max)
        self.assertEqual(3, self.heap.size)
        self.assertEqual([ heap.HeapItem(6), heap.HeapItem(5),
                          heap.HeapItem(2) ],
                         self.heap.elements)

        max = self.heap.extract()

        self.assertEqual(heap.HeapItem(6), max)
        self.assertEqual(2, self.heap.size)
        self.assertEqual([ heap.HeapItem(5), heap.HeapItem(2) ],
                         self.heap.elements)

        max = self.heap.extract()

        self.assertEqual(heap.HeapItem(5), max)
        self.assertEqual(1, self.heap.size)
        self.assertEqual([ heap.HeapItem(2) ], self.heap.elements)

        max = self.heap.extract()

        self.assertEqual(heap.HeapItem(2), max)
        self.assertEqual(0, self.heap.size)
        self.assertEqual([], self.heap.elements)

    def test_insert_on_empty_list(self):
        self.assertEqual(0, self.heap.size)
        self.assertEqual([], self.heap.elements)

        self.heap.insert(heap.HeapItem(1))

        self.assertEqual(1, self.heap.size)
        self.assertEqual([ heap.HeapItem(1) ], self.heap.elements)

    def test_insert_on_one_element_list(self):
        self.heap.build([ heap.HeapItem(2) ])

        self.assertEqual(1, self.heap.size)
        self.assertEqual([ heap.HeapItem(2) ], self.heap.elements)

        self.heap.insert(heap.HeapItem(1))

        self.assertEqual(2, self.heap.size)
        self.assertEqual([ heap.HeapItem(2), heap.HeapItem(1) ],
                         self.heap.elements)

    def test_insert_on_two_element_list(self):
        self.heap.build([ heap.HeapItem(3), heap.HeapItem(2) ])

        self.assertEqual(2, self.heap.size)
        self.assertEqual([ heap.HeapItem(3), heap.HeapItem(2) ],
                         self.heap.elements)

        self.heap.insert(heap.HeapItem(4))

        self.assertEqual(3, self.heap.size)
        self.assertEqual([ heap.HeapItem(4), heap.HeapItem(2),
                          heap.HeapItem(3) ],
                         self.heap.elements)

    def test_insert_on_three_element_list(self):
        self.heap.build([ heap.HeapItem(4), heap.HeapItem(3),
                         heap.HeapItem(2) ])

        self.assertEqual(3, self.heap.size)
        self.assertEqual([ heap.HeapItem(4), heap.HeapItem(3),
                          heap.HeapItem(2) ],
                         self.heap.elements)

        self.heap.insert(heap.HeapItem(5))

        self.assertEqual(4, self.heap.size)
        self.assertEqual([ heap.HeapItem(5), heap.HeapItem(4),
                          heap.HeapItem(2), heap.HeapItem(3) ],
                         self.heap.elements)

    def test_insert_on_four_element_list(self):
        self.heap.build([ heap.HeapItem(5), heap.HeapItem(4),
                         heap.HeapItem(3), heap.HeapItem(2) ])

        self.assertEqual(4, self.heap.size)
        self.assertEqual([ heap.HeapItem(5), heap.HeapItem(4),
                          heap.HeapItem(3), heap.HeapItem(2) ],
                         self.heap.elements)

        self.heap.insert(heap.HeapItem(6))

        self.assertEqual(5, self.heap.size)
        self.assertEqual([ heap.HeapItem(6), heap.HeapItem(5),
                          heap.HeapItem(3), heap.HeapItem(2),
                          heap.HeapItem(4) ],
                         self.heap.elements)

    def test_insert_on_five_element_list(self):
        self.heap.build([ heap.HeapItem(9), heap.HeapItem(5),
                         heap.HeapItem(6), heap.HeapItem(2),
                         heap.HeapItem(3) ])

        self.assertEqual(5, self.heap.size)
        self.assertEqual([ heap.HeapItem(9), heap.HeapItem(5),
                          heap.HeapItem(6), heap.HeapItem(2),
                          heap.HeapItem(3) ],
                         self.heap.elements)

        self.heap.insert(heap.HeapItem(10))

        self.assertEqual(6, self.heap.size)
        self.assertEqual([ heap.HeapItem(10), heap.HeapItem(5),
                          heap.HeapItem(9), heap.HeapItem(2),
                          heap.HeapItem(3), heap.HeapItem(6) ],
                         self.heap.elements)

    def test_change_priority_on_empty_list(self):
        with self.assertRaisesRegex(IndexError, ''):
            self.heap.change_priority(0, 1)

    def test_change_priority_on_non_empty_list_with_preceeding_index(self):
        self.heap.build([ heap.HeapItem(9), heap.HeapItem(5), heap.HeapItem(6),
                         heap.HeapItem(2), heap.HeapItem(3) ])
        with self.assertRaisesRegex(IndexError, ''):
            self.heap.change_priority(-1, 1)

    def test_change_priority_on_non_empty_list_with_exceeding_index(self):
        self.heap.build([ heap.HeapItem(9), heap.HeapItem(5), heap.HeapItem(6),
                         heap.HeapItem(2), heap.HeapItem(3) ])
        with self.assertRaisesRegex(IndexError, ''):
            self.heap.change_priority(self.heap.size, 1)

    def test_change_priority_on_one_element_list(self):
        self.heap.build([ heap.HeapItem(9) ])

        self.assertEqual(1, self.heap.size)
        self.assertEqual([ heap.HeapItem(9) ], self.heap.elements)

        self.heap.change_priority(0, 1)

        self.assertEqual(1, self.heap.size)
        self.assertEqual([ heap.HeapItem(1) ], self.heap.elements)

    def test_change_priority_on_two_element_list_without_sift(self):
        self.heap.build([ heap.HeapItem(9), heap.HeapItem(6) ])

        self.assertEqual(2, self.heap.size)
        self.assertEqual([ heap.HeapItem(9), heap.HeapItem(6) ],
                         self.heap.elements)

        self.heap.change_priority(0, 7)

        self.assertEqual(2, self.heap.size)
        self.assertEqual([ heap.HeapItem(7), heap.HeapItem(6) ],
                         self.heap.elements)

        self.heap.change_priority(1, 5)

        self.assertEqual(2, self.heap.size)
        self.assertEqual([ heap.HeapItem(7), heap.HeapItem(5) ],
                         self.heap.elements)

    def test_change_priority_on_two_element_list_with_sift_down_and_up(self):
        self.heap.build([ heap.HeapItem(9), heap.HeapItem(6) ])

        self.assertEqual(2, self.heap.size)
        self.assertEqual([ heap.HeapItem(9), heap.HeapItem(6) ],
                         self.heap.elements)

        self.heap.change_priority(0, 5)

        self.assertEqual(2, self.heap.size)
        self.assertEqual([ heap.HeapItem(6), heap.HeapItem(5) ],
                         self.heap.elements)

        self.heap.change_priority(1, 7)

        self.assertEqual(2, self.heap.size)
        self.assertEqual([ heap.HeapItem(7), heap.HeapItem(6) ],
                         self.heap.elements)

    def test_change_priority_on_five_element_list_with_sift_down(self):
        self.heap.build([ heap.HeapItem(9), heap.HeapItem(6),
                         heap.HeapItem(5), heap.HeapItem(4),
                         heap.HeapItem(3) ])

        self.assertEqual(5, self.heap.size)
        self.assertEqual([ heap.HeapItem(9), heap.HeapItem(6),
                          heap.HeapItem(5), heap.HeapItem(4),
                          heap.HeapItem(3) ],
                         self.heap.elements)

        self.heap.change_priority(1, 0)

        self.assertEqual(5, self.heap.size)
        self.assertEqual([ heap.HeapItem(9), heap.HeapItem(4),
                          heap.HeapItem(5), heap.HeapItem(0),
                          heap.HeapItem(3) ],
                         self.heap.elements)

    def test_change_priority_on_five_element_list_with_sift_up(self):
        self.heap.build([ heap.HeapItem(9), heap.HeapItem(6),
                         heap.HeapItem(5), heap.HeapItem(4),
                         heap.HeapItem(3) ])

        self.assertEqual(5, self.heap.size)
        self.assertEqual([ heap.HeapItem(9), heap.HeapItem(6),
                          heap.HeapItem(5), heap.HeapItem(4),
                          heap.HeapItem(3) ],
                         self.heap.elements)

        self.heap.change_priority(1, 10)

        self.assertEqual(5, self.heap.size)
        self.assertEqual([ heap.HeapItem(10), heap.HeapItem(9),
                          heap.HeapItem(5), heap.HeapItem(4),
                          heap.HeapItem(3) ],
                         self.heap.elements)

    def test_sort_on_empty_list(self):
        list = []

        self.heap.sort_in_place(list)

        self.assertEqual([], list)
        self.assertEqual(0, self.heap.size)

    def test_sort_on_one_element_list(self):
        list = [ heap.HeapItem(1) ]

        self.heap.sort_in_place(list)

        self.assertEqual([ heap.HeapItem(1) ], list)
        self.assertEqual(1, self.heap.size)

    def test_sort_on_sorted_two_element_list(self):
        list = [ heap.HeapItem(1), heap.HeapItem(2) ]

        self.heap.sort_in_place(list)

        self.assertEqual([ heap.HeapItem(1), heap.HeapItem(2) ], list)
        self.assertEqual(2, self.heap.size)

    def test_sort_on_unsorted_two_element_list(self):
        list = [ heap.HeapItem(2), heap.HeapItem(1) ]

        self.heap.sort_in_place(list)

        self.assertEqual([ heap.HeapItem(1), heap.HeapItem(2) ], list)
        self.assertEqual(2, self.heap.size)

    def test_sort_on_sorted_three_element_list(self):
        list = [ heap.HeapItem(1), heap.HeapItem(2), heap.HeapItem(3) ]

        self.heap.sort_in_place(list)

        self.assertEqual([ heap.HeapItem(1), heap.HeapItem(2),
                          heap.HeapItem(3) ],
                         list)
        self.assertEqual(3, self.heap.size)

    def test_sort_on_unsorted_three_element_list(self):
        list = [ heap.HeapItem(3), heap.HeapItem(2), heap.HeapItem(1) ]

        self.heap.sort_in_place(list)

        self.assertEqual([ heap.HeapItem(1), heap.HeapItem(2),
                          heap.HeapItem(3) ],
                         list)
        self.assertEqual(3, self.heap.size)

    def test_sort_on_sorted_four_element_list(self):
        list = [ heap.HeapItem(1), heap.HeapItem(2), heap.HeapItem(3),
                heap.HeapItem(4) ]

        self.heap.sort_in_place(list)

        self.assertEqual([ heap.HeapItem(1), heap.HeapItem(2),
                          heap.HeapItem(3), heap.HeapItem(4) ],
                         list)
        self.assertEqual(4, self.heap.size)

    def test_sort_on_unsorted_five_element_list(self):
        list = [ heap.HeapItem(4), heap.HeapItem(3), heap.HeapItem(2),
                heap.HeapItem(1) ]

        self.heap.sort_in_place(list)

        self.assertEqual([ heap.HeapItem(1), heap.HeapItem(2),
                          heap.HeapItem(3), heap.HeapItem(4) ], list)
        self.assertEqual(4, self.heap.size)

    def test_sort_on_sorted_five_element_list(self):
        list = [ heap.HeapItem(2), heap.HeapItem(4), heap.HeapItem(5),
                heap.HeapItem(8), heap.HeapItem(9) ]

        self.heap.sort_in_place(list)

        self.assertEqual([ heap.HeapItem(2), heap.HeapItem(4),
                          heap.HeapItem(5), heap.HeapItem(8),
                          heap.HeapItem(9) ], list)
        self.assertEqual(5, self.heap.size)

    def test_sort_on_unsorted_five_element_list(self):
        list = [ heap.HeapItem(9), heap.HeapItem(8), heap.HeapItem(5),
                heap.HeapItem(4), heap.HeapItem(2) ]

        self.heap.sort_in_place(list)

        self.assertEqual([ heap.HeapItem(2), heap.HeapItem(4),
                          heap.HeapItem(5), heap.HeapItem(8),
                          heap.HeapItem(9) ],
                         list)
        self.assertEqual(5, self.heap.size)

    def test_sort_on_seven_element_list_with_duplicates(self):
        list = [ heap.HeapItem(9), heap.HeapItem(5), heap.HeapItem(4),
                heap.HeapItem(2), heap.HeapItem(5), heap.HeapItem(2),
                heap.HeapItem(8) ]

        self.heap.sort_in_place(list)

        self.assertEqual([ heap.HeapItem(2), heap.HeapItem(2),
                          heap.HeapItem(4), heap.HeapItem(5),
                          heap.HeapItem(5), heap.HeapItem(8),
                          heap.HeapItem(9) ],
                         list)
        self.assertEqual(7, self.heap.size)

if __name__ == '__main__':
    class_names = \
    [
        HeapItemTestCase,
        BinHeapAsMinTestCase,
        BinHeapAsMaxTestCase,
    ]

    suite = unittest.TestSuite()

    for c in class_names:
        suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(c))

    unittest.TextTestRunner().run(suite)
