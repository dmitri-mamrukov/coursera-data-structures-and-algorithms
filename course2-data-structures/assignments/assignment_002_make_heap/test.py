#!/usr/bin/python3

import unittest

from build_heap import MinBinHeap

class MinBinHeapTestCase(unittest.TestCase):

    def setUp(self):
        self.heap = MinBinHeap()

    def tearDown(self):
        pass

    def test_constructor(self):
        self.assertEqual(0, self.heap.size)
        self.assertEqual([], self.heap.elements)

    def test_str_on_empty_heap(self):
        self.assertEqual('[]', str(self.heap))

    def test_repr_on_empty_heap(self):
        self.assertEqual('[size=0, list=[]]', repr(self.heap))

    def test_str_on_three_element_heap(self):
        self.heap.build([ 1, 2, 3 ])

        self.assertEqual('[1, 2, 3]', str(self.heap))

    def test_repr_on_three_element_heap(self):
        self.heap.build([ 1, 2, 3 ])

        self.assertEqual('[size=3, list=[1, 2, 3]]', repr(self.heap))

    def test_build_on_empty_list(self):
        self.heap.build([])

        self.assertEqual(0, self.heap.size)
        self.assertEqual([], self.heap.elements)

    def test_build_on_one_element_list(self):
        self.heap.build([ 1 ])

        self.assertEqual(1, self.heap.size)
        self.assertEqual([ 1 ], self.heap.elements)

    def test_build_on_two_element_list_as_1_2(self):
        self.heap.build([ 1, 2 ])

        self.assertEqual(2, self.heap.size)
        self.assertEqual([ 1, 2 ], self.heap.elements)

    def test_build_on_two_element_list_as_2_1(self):
        self.heap.build([ 2, 1 ])

        self.assertEqual(2, self.heap.size)
        self.assertEqual([ 1, 2 ], self.heap.elements)

    def test_build_on_three_element_list_as_1_2_3(self):
        self.heap.build([ 1, 2, 3 ])

        self.assertEqual(3, self.heap.size)
        self.assertEqual([ 1, 2, 3 ], self.heap.elements)

    def test_build_on_three_element_list_as_1_3_2(self):
        self.heap.build([ 1, 3, 2 ])

        self.assertEqual(3, self.heap.size)
        self.assertEqual([ 1, 3, 2 ], self.heap.elements)

    def test_build_on_three_element_list_as_2_1_3(self):
        data = [ 2, 1, 3 ]

        self.heap.build(data)

        self.assertEqual(3, self.heap.size)
        self.assertEqual([ 1, 2, 3 ], self.heap.elements)

    def test_build_on_three_element_list_as_2_3_1(self):
        self.heap.build([ 2, 3, 1 ])

        self.assertEqual(3, self.heap.size)
        self.assertEqual([ 1, 3, 2 ], self.heap.elements)

    def test_build_on_three_element_list_as_3_1_2(self):
        self.heap.build([ 3, 1, 2 ])

        self.assertEqual(3, self.heap.size)
        self.assertEqual([ 1, 3, 2 ], self.heap.elements)

    def test_build_on_three_element_list_as_3_2_1(self):
        self.heap.build([ 3, 2, 1 ])

        self.assertEqual(3, self.heap.size)
        self.assertEqual([ 1, 2, 3 ], self.heap.elements)

    def test_build_on_four_element_list(self):
        self.heap.build([ 9, 5, 6, 2 ])

        self.assertEqual(4, self.heap.size)
        self.assertEqual([ 2, 5, 6, 9 ], self.heap.elements)

    def test_build_on_five_element_list(self):
        self.heap.build([ 9, 5, 6, 2, 3 ])

        self.assertEqual(5, self.heap.size)
        self.assertEqual([ 2, 3, 6, 5, 9 ], self.heap.elements)

    def test_build_on_six_element_list(self):
        self.heap.build([ 9, 5, 6, 2, 3, 1 ])

        self.assertEqual(6, self.heap.size)
        self.assertEqual([ 1, 2, 6, 5, 3, 9 ], self.heap.elements)

    def test_build_on_seven_element_list(self):
        self.heap.build([ 9, 5, 6, 2, 3, 1, 0 ])

        self.assertEqual(7, self.heap.size)
        self.assertEqual([ 0, 2, 1, 5, 3, 9, 6 ], self.heap.elements)

    def test_build_on_seven_element_list_with_duplicates(self):
        self.heap.build([ 9, 5, 2, 2, 1, 1, 0 ])

        self.assertEqual(7, self.heap.size)
        self.assertEqual([ 0, 1, 1, 2, 5, 9, 2 ], self.heap.elements)

    def test_build_on_seven_duplicate_element_list(self):
        self.heap.build([ 3, 3, 3, 3, 3, 3, 3 ])

        self.assertEqual(7, self.heap.size)
        self.assertEqual([ 3, 3, 3, 3, 3, 3, 3 ], self.heap.elements)

    def test_extract_on_five_element_list(self):
        self.heap.build([ 9, 5, 6, 2, 3 ])

        self.assertEqual(5, self.heap.size)
        self.assertEqual([ 2, 3, 6, 5, 9 ], self.heap.elements)

        min = self.heap.extract()

        self.assertEqual(2, min)
        self.assertEqual(4, self.heap.size)
        self.assertEqual([ 3, 5, 6, 9 ], self.heap.elements)

        min = self.heap.extract()

        self.assertEqual(3, min)
        self.assertEqual(3, self.heap.size)
        self.assertEqual([ 5, 9, 6 ], self.heap.elements)

        min = self.heap.extract()

        self.assertEqual(5, min)
        self.assertEqual(2, self.heap.size)
        self.assertEqual([ 6, 9 ], self.heap.elements)

        min = self.heap.extract()

        self.assertEqual(6, min)
        self.assertEqual(1, self.heap.size)
        self.assertEqual([ 9 ], self.heap.elements)

        min = self.heap.extract()

        self.assertEqual(9, min)
        self.assertEqual(0, self.heap.size)
        self.assertEqual([], self.heap.elements)

    def test_insert_on_empty_list(self):
        self.heap.insert(1)

        self.assertEqual(1, self.heap.size)
        self.assertEqual([ 1 ], self.heap.elements)

    def test_insert_on_one_element_list(self):
        self.heap.build([ 2 ])

        self.assertEqual(1, self.heap.size)
        self.assertEqual([ 2 ], self.heap.elements)

        self.heap.insert(1)

        self.assertEqual(2, self.heap.size)
        self.assertEqual([ 1, 2 ], self.heap.elements)

    def test_insert_on_two_element_list(self):
        self.heap.build([ 2, 3 ])

        self.assertEqual(2, self.heap.size)
        self.assertEqual([ 2, 3 ], self.heap.elements)

        self.heap.insert(1)

        self.assertEqual(3, self.heap.size)
        self.assertEqual([ 1, 3, 2 ], self.heap.elements)

    def test_insert_on_three_element_list(self):
        self.heap.build([ 2, 3, 4 ])

        self.assertEqual(3, self.heap.size)
        self.assertEqual([ 2, 3, 4 ], self.heap.elements)

        self.heap.insert(1)

        self.assertEqual(4, self.heap.size)
        self.assertEqual([ 1, 2, 4, 3 ], self.heap.elements)

    def test_insert_on_four_element_list(self):
        self.heap.build([ 2, 3, 4, 5 ])

        self.assertEqual(4, self.heap.size)
        self.assertEqual([ 2, 3, 4, 5 ], self.heap.elements)

        self.heap.insert(1)

        self.assertEqual(5, self.heap.size)
        self.assertEqual([ 1, 2, 4, 5, 3 ], self.heap.elements)

    def test_insert_on_five_element_list(self):
        self.heap.build([ 2, 3, 6, 5, 9 ])

        self.assertEqual(5, self.heap.size)
        self.assertEqual([ 2, 3, 6, 5, 9 ], self.heap.elements)

        self.heap.insert(1)

        self.assertEqual(6, self.heap.size)
        self.assertEqual([ 1, 3, 2, 5, 9, 6 ], self.heap.elements)

    def test_change_priority_on_empty_list(self):
        with self.assertRaisesRegex(IndexError, ''):
            self.heap.change_priority(0, 1)

    def test_change_priority_on_non_empty_list_with_preceeding_index(self):
        self.heap.build([ 9, 5, 6, 2, 3 ])
        with self.assertRaisesRegex(IndexError, ''):
            self.heap.change_priority(-1, 1)

    def test_change_priority_on_non_empty_list_with_exceeding_index(self):
        self.heap.build([ 9, 5, 6, 2, 3 ])
        with self.assertRaisesRegex(IndexError, ''):
            self.heap.change_priority(self.heap.size, 1)

    def test_change_priority_on_one_element_list(self):
        self.heap.build([ 9 ])

        self.assertEqual(1, self.heap.size)
        self.assertEqual([ 9], self.heap.elements)

        self.heap.change_priority(0, 1)

        self.assertEqual(1, self.heap.size)
        self.assertEqual([ 1 ], self.heap.elements)

    def test_change_priority_on_two_element_list_without_sift(self):
        self.heap.build([ 9, 6 ])

        self.assertEqual(2, self.heap.size)
        self.assertEqual([ 6, 9 ], self.heap.elements)

        self.heap.change_priority(0, 1)

        self.assertEqual(2, self.heap.size)
        self.assertEqual([ 1, 9 ], self.heap.elements)

        self.heap.change_priority(1, 2)

        self.assertEqual(2, self.heap.size)
        self.assertEqual([ 1, 2 ], self.heap.elements)

    def test_change_priority_on_two_element_list_with_sift_down_up(self):
        self.heap.build([ 9, 6 ])

        self.assertEqual(2, self.heap.size)
        self.assertEqual([ 6, 9 ], self.heap.elements)

        self.heap.change_priority(0, 10)

        self.assertEqual(2, self.heap.size)
        self.assertEqual([ 9, 10 ], self.heap.elements)

        self.heap.change_priority(1, 8)

        self.assertEqual(2, self.heap.size)
        self.assertEqual([ 8, 9 ], self.heap.elements)

    def test_change_priority_on_five_element_list_with_sift_down(self):
        self.heap.build([ 3, 4, 5, 6, 9 ])

        self.assertEqual(5, self.heap.size)
        self.assertEqual([ 3, 4, 5, 6, 9 ], self.heap.elements)

        self.heap.change_priority(1, 10)

        self.assertEqual(5, self.heap.size)
        self.assertEqual([ 3, 6, 5, 10, 9 ], self.heap.elements)

    def test_change_priority_on_five_element_list_with_sift_up(self):
        self.heap.build([ 3, 4, 5, 6, 9 ])

        self.assertEqual(5, self.heap.size)
        self.assertEqual([ 3, 4, 5, 6, 9 ], self.heap.elements)

        self.heap.change_priority(3, 0)

        self.assertEqual(5, self.heap.size)
        self.assertEqual([ 0, 3, 5, 4, 9 ], self.heap.elements)

class MinBinHeapWithSwapsTestCase(unittest.TestCase):

    def setUp(self):
        self.heap = MinBinHeap()

    def tearDown(self):
        pass

    def test_build_on_empty_list(self):
        swaps = self.heap.build_and_gen_swaps([])

        self.assertEqual(0, self.heap.size)
        self.assertEqual([], self.heap.elements)

    def test_build_on_one_element_list(self):
        swaps = self.heap.build_and_gen_swaps([ 1 ])

        self.assertEqual(1, self.heap.size)
        self.assertEqual([ 1 ], self.heap.elements)
        self.assertEqual([], swaps)

    def test_build_on_two_element_list_as_1_2(self):
        swaps = self.heap.build_and_gen_swaps([ 1, 2 ])

        self.assertEqual(2, self.heap.size)
        self.assertEqual([ 1, 2 ], self.heap.elements)
        self.assertEqual([], swaps)

    def test_build_on_two_element_list_as_2_1(self):
        swaps = self.heap.build_and_gen_swaps([ 2, 1 ])

        self.assertEqual(2, self.heap.size)
        self.assertEqual([ 1, 2 ], self.heap.elements)
        self.assertEqual([ (0, 1) ], swaps)

    def test_build_on_three_element_list_as_1_2_3(self):
        swaps = self.heap.build_and_gen_swaps([ 1, 2, 3 ])

        self.assertEqual(3, self.heap.size)
        self.assertEqual([ 1, 2, 3 ], self.heap.elements)
        self.assertEqual([], swaps)

    def test_build_on_three_element_list_as_1_3_2(self):
        swaps = self.heap.build_and_gen_swaps([ 1, 3, 2 ])

        self.assertEqual(3, self.heap.size)
        self.assertEqual([ 1, 3, 2 ], self.heap.elements)
        self.assertEqual([], swaps)

    def test_build_on_three_element_list_as_2_1_3(self):
        data = [ 2, 1, 3 ]
        expected_elements = [ data[1], data[0], data[2] ]

        swaps = self.heap.build_and_gen_swaps(data)

        self.assertEqual(3, self.heap.size)
        self.assertEqual(expected_elements, self.heap.elements)
        self.assertEqual([ (0, 1) ], swaps)

    def test_build_on_three_element_list_as_2_3_1(self):
        swaps = self.heap.build_and_gen_swaps([ 2, 3, 1 ])

        self.assertEqual(3, self.heap.size)
        self.assertEqual([ 1, 3, 2 ], self.heap.elements)
        self.assertEqual([ (0, 2) ], swaps)

    def test_build_on_three_element_list_as_3_1_2(self):
        swaps = self.heap.build_and_gen_swaps([ 3, 1, 2 ])

        self.assertEqual(3, self.heap.size)
        self.assertEqual([ 1, 3, 2 ], self.heap.elements)
        self.assertEqual([ (0, 1) ], swaps)

    def test_build_on_three_element_list_as_3_2_1(self):
        swaps = self.heap.build_and_gen_swaps([ 3, 2, 1 ])

        self.assertEqual(3, self.heap.size)
        self.assertEqual([ 1, 2, 3 ], self.heap.elements)
        self.assertEqual([ (0, 2) ], swaps)

    def test_build_on_four_element_list(self):
        swaps = self.heap.build_and_gen_swaps([ 9, 5, 6, 2 ])

        self.assertEqual(4, self.heap.size)
        self.assertEqual([ 2, 5, 6, 9 ], self.heap.elements)
        self.assertEqual([ (1, 3), (0, 1), (1, 3) ], swaps)

    def test_build_on_five_element_list(self):
        swaps = self.heap.build_and_gen_swaps([ 9, 5, 6, 2, 3 ])

        self.assertEqual(5, self.heap.size)
        self.assertEqual([ 2, 3, 6, 5, 9 ], self.heap.elements)
        self.assertEqual([ (1, 3), (0, 1), (1, 4) ], swaps)

    def test_build_on_six_element_list(self):
        swaps = self.heap.build_and_gen_swaps([ 9, 5, 6, 2, 3, 1 ])

        self.assertEqual(6, self.heap.size)
        self.assertEqual([ 1, 2, 6, 5, 3, 9 ], self.heap.elements)
        self.assertEqual([ (2, 5), (1, 3), (0, 2), (2, 5) ], swaps)

    def test_build_on_seven_element_list(self):
        swaps = self.heap.build_and_gen_swaps([ 9, 5, 6, 2, 3, 1, 0 ])

        self.assertEqual(7, self.heap.size)
        self.assertEqual([ 0, 2, 1, 5, 3, 9, 6 ], self.heap.elements)
        self.assertEqual([ (2, 6), (1, 3), (0, 2), (2, 5) ], swaps)

    def test_build_on_seven_element_list_with_duplicates(self):
        swaps = self.heap.build_and_gen_swaps([ 9, 5, 2, 2, 1, 1, 0 ])

        self.assertEqual(7, self.heap.size)
        self.assertEqual([ 0, 1, 1, 2, 5, 9, 2 ], self.heap.elements)
        self.assertEqual([ (2, 6), (1, 4), (0, 2), (2, 5) ], swaps)

    def test_build_on_seven_duplicate_element_list(self):
        swaps = self.heap.build_and_gen_swaps([ 3, 3, 3, 3, 3, 3, 3 ])

        self.assertEqual(7, self.heap.size)
        self.assertEqual([ 3, 3, 3, 3, 3, 3, 3 ], self.heap.elements)
        self.assertEqual([], swaps)

if __name__ == '__main__':
    unittest.main()
