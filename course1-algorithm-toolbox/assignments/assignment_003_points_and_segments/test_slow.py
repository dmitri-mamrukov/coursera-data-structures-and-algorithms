#!/usr/bin/python3

import unittest

from points_and_segments_slow import naive_count_segments, \
    fast_count_segments_slow, quick_sort_on_two_lists, sort_segments

class QuickSortOnTwoListsTestCase(unittest.TestCase):

    @staticmethod
    def less_than(a, b):
        return a < b

    @staticmethod
    def greater_than(a, b):
        return a > b

    def test_with_data1_larger_than_data2(self):
        data1 = [ 1, 2, 3 ]
        data2 = [ 'a' ]
        with self.assertRaisesRegex(AssertionError, ''):
            quick_sort_on_two_lists(data1, data2,
            QuickSortOnTwoListsTestCase.less_than)

    def test_with_data1_smaller_than_data2(self):
        data1 = [ 1 ]
        data2 = [ 'a', 'b', 'c' ]
        with self.assertRaisesRegex(AssertionError, ''):
            quick_sort_on_two_lists(data1, data2,
            QuickSortOnTwoListsTestCase.less_than)

    def test_with_empty_data(self):
        data1 = []
        data2 = []
        quick_sort_on_two_lists(data1, data2,
            QuickSortOnTwoListsTestCase.less_than)
        self.assertEqual([], data1)
        self.assertEqual([], data2)

    def test_with_one_element(self):
        data1 = [ 3 ]
        data2 = [ 'a' ]
        quick_sort_on_two_lists(data1, data2,
            QuickSortOnTwoListsTestCase.less_than)
        self.assertEqual([ 3 ], data1)
        self.assertEqual([ 'a' ], data2)

    def test_with_two_elements1(self):
        data1 = [ 1, 2 ]
        data2 = [ 'a', 'b' ]
        quick_sort_on_two_lists(data1, data2,
            QuickSortOnTwoListsTestCase.less_than)
        self.assertEqual([ 1, 2 ], data1)
        self.assertEqual([ 'a', 'b' ], data2)

    def test_with_two_elements2(self):
        data1 = [ 2, 1 ]
        data2 = [ 'a', 'b' ]
        quick_sort_on_two_lists(data1, data2,
            QuickSortOnTwoListsTestCase.less_than)
        self.assertEqual([ 1, 2 ], data1)
        self.assertEqual([ 'b', 'a' ], data2)

    def test_with_two_elements3(self):
        data1 = [ 3, 3 ]
        data2 = [ 'a', 'b' ]
        quick_sort_on_two_lists(data1, data2,
            QuickSortOnTwoListsTestCase.less_than)
        self.assertEqual([ 3, 3 ], data1)
        self.assertEqual([ 'a', 'b' ], data2)

    def test_with_three_elements1(self):
        data1 = [ 1, 2, 3 ]
        data2 = [ 'a', 'b', 'c' ]
        quick_sort_on_two_lists(data1, data2,
            QuickSortOnTwoListsTestCase.less_than)
        self.assertEqual([ 1, 2, 3 ], data1)
        self.assertEqual([ 'a', 'b', 'c' ], data2)

    def test_with_three_elements2(self):
        data1 = [ 2, 1, 3 ]
        data2 = [ 'a', 'b', 'c' ]
        quick_sort_on_two_lists(data1, data2,
            QuickSortOnTwoListsTestCase.less_than)
        self.assertEqual([ 1, 2, 3 ], data1)
        self.assertEqual([ 'b', 'a', 'c' ], data2)

    def test_with_three_elements3(self):
        data1 = [ 3, 3, 3 ]
        data2 = [ 'a', 'b', 'c' ]
        quick_sort_on_two_lists(data1, data2,
            QuickSortOnTwoListsTestCase.less_than)
        self.assertEqual([ 3, 3, 3 ], data1)
        self.assertEqual([ 'a', 'b', 'c' ], data2)

    def test_with_several_elements1(self):
        data1 = [ 5, -7, 3, 0, 9, -1, 9 ]
        data2 = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g' ]
        quick_sort_on_two_lists(data1, data2,
            QuickSortOnTwoListsTestCase.less_than)
        self.assertEqual([ -7, -1, 0, 3, 5, 9, 9 ], data1)
        self.assertEqual([ 'b', 'f', 'd', 'c', 'a', 'e', 'g' ], data2)

    def test_with_several_elements2(self):
        data1 = [ 7, 2, 5, 3, 7, 13, 1, 6 ]
        data2 = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h' ]
        quick_sort_on_two_lists(data1, data2,
            QuickSortOnTwoListsTestCase.less_than)
        self.assertEqual([ 1, 2, 3, 5, 6, 7, 7, 13 ], data1)
        self.assertEqual([ 'g', 'b', 'd', 'c', 'h', 'a', 'e', 'f' ], data2)

    def test_with_several_elements3(self):
        data1 = [ 54, 26, 93, 17, 77, 31, 44, 55, 20 ]
        data2 = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i' ]
        quick_sort_on_two_lists(data1, data2,
            QuickSortOnTwoListsTestCase.less_than)
        self.assertEqual([ 17, 20, 26, 31, 44, 54, 55, 77, 93 ], data1)
        self.assertEqual([ 'd', 'i', 'b', 'f', 'g', 'a', 'h', 'e', 'c' ],
            data2)

    def test_with_several_elements_and_less_than_comparator(self):
        data1 = [ 7, 2, 5, 3, 7, 13, 1, 6 ]
        data2 = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h' ]
        quick_sort_on_two_lists(data1, data2,
            QuickSortOnTwoListsTestCase.less_than)
        self.assertEqual([ 1, 2, 3, 5, 6, 7, 7, 13 ], data1)
        self.assertEqual([ 'g', 'b', 'd', 'c', 'h', 'a', 'e', 'f' ], data2)

    def test_with_several_elements_and_greater_than_comparator(self):
        data1 = [ 7, 2, 5, 3, 7, 13, 1, 6 ]
        data2 = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h' ]
        quick_sort_on_two_lists(data1, data2,
            QuickSortOnTwoListsTestCase.greater_than)
        self.assertEqual([ 13, 7, 7, 6, 5, 3, 2, 1 ], data1)
        self.assertEqual([ 'f', 'a', 'e', 'h', 'c', 'd', 'b', 'g' ], data2)

class SortSegmentsTestCase(unittest.TestCase):

    def test_with_starts_larger_than_ends(self):
        starts = [ 1, 2, 3 ]
        ends = [ 5 ]
        with self.assertRaisesRegex(AssertionError, ''):
            sort_segments(starts, ends)

    def test_with_starts_smaller_than_ends(self):
        starts = [ 1 ]
        ends = [ 1, 2, 3 ]
        with self.assertRaisesRegex(AssertionError, ''):
            sort_segments(starts, ends)

    def test_with_empty_data(self):
        starts = []
        ends = []
        sort_segments(starts, ends)
        self.assertEqual([], starts)
        self.assertEqual([], ends)

    def test_with_duplicate_starts(self):
        starts = [ 5, 5, 5, 5, 5 ]
        ends = [ 3, 6, 2, 1, 7 ]
        sort_segments(starts, ends)
        self.assertEqual([ 5, 5, 5, 5, 5 ], starts)
        self.assertEqual([ 1, 2, 3, 6, 7 ], ends)

    def test_with_duplicate_ends(self):
        starts = [ 5, 4, 3, 2, 1 ]
        ends = [ 5, 5, 5, 5, 5 ]
        sort_segments(starts, ends)
        self.assertEqual([ 1, 2, 3, 4, 5 ], starts)
        self.assertEqual([ 5, 5, 5, 5, 5 ], ends)

    def test_with_duplicate_starts_and_ends(self):
        starts = [ 6, 6, 6, 6, 6 ]
        ends = [ 5, 5, 5, 5, 5 ]
        sort_segments(starts, ends)
        self.assertEqual([ 6, 6, 6, 6, 6 ], starts)
        self.assertEqual([ 5, 5, 5, 5, 5 ], ends)

    def test_with_several_elements1(self):
        starts = [ 7, 13, 0, 0, 1, 6, -3, -3, -3, 0 ]
        ends = [ 6, 4, 7, 3, 2, 4, 9, 15, 3, 8 ]
        sort_segments(starts, ends)
        self.assertEqual([ -3, -3, -3, 0, 0, 0, 1, 6, 7, 13 ], starts)
        self.assertEqual([ 3, 9, 15, 3, 7, 8, 2, 4, 6, 4 ], ends)

    def test_with_several_elements2(self):
        starts = [ 7, 13, 0, 0, 1, 6, -3, -3, -3, 0 ]
        ends = [ 6, 4, 8, 3, 2, 4, 9, 15, 9, 8 ]
        sort_segments(starts, ends)
        self.assertEqual([ -3, -3, -3, 0, 0, 0, 1, 6, 7, 13 ], starts)
        self.assertEqual([ 9, 9, 15, 3, 8, 8, 2, 4, 6, 4 ], ends)

class CommonCountSegmentsTestCase(unittest.TestCase):

    def test_with_empty_segments_and_points(self):
        starts = []
        ends = []
        points = []
        self.assertEqual([], self.method_under_test(starts, ends, points))

    def test_with_empty_segments(self):
        starts = []
        ends = []
        points = [ 1, 2, 3 ]
        self.assertEqual([ 0, 0, 0 ],
            self.method_under_test(starts, ends, points))

    def test_with_empty_points(self):
        starts = [ 1, 2, 3 ]
        ends = [ 4, 5, 6 ]
        points = []
        self.assertEqual([],
            self.method_under_test(starts, ends, points))

    def test_with_one_segment1(self):
        starts = [ 1 ]
        ends = [ 4 ]
        points = [ -1 ]
        self.assertEqual([ 0 ],
            self.method_under_test(starts, ends, points))

    def test_with_one_segment2(self):
        starts = [ 1 ]
        ends = [ 4 ]
        points = [ 1 ]
        self.assertEqual([ 1 ],
            self.method_under_test(starts, ends, points))

    def test_with_one_segment3(self):
        starts = [ 1 ]
        ends = [ 4 ]
        points = [ 2 ]
        self.assertEqual([ 1 ],
            self.method_under_test(starts, ends, points))

    def test_with_one_segment4(self):
        starts = [ 1 ]
        ends = [ 4 ]
        points = [ 3 ]
        self.assertEqual([ 1 ],
            self.method_under_test(starts, ends, points))

    def test_with_one_segment5(self):
        starts = [ 1 ]
        ends = [ 4 ]
        points = [ 4 ]
        self.assertEqual([ 1 ],
            self.method_under_test(starts, ends, points))

    def test_with_one_segment6(self):
        starts = [ 1 ]
        ends = [ 4 ]
        points = [ 5 ]
        self.assertEqual([ 0 ],
            self.method_under_test(starts, ends, points))

    def test_with_one_segment7(self):
        starts = [ 1 ]
        ends = [ 4 ]
        points = [ -1, 0, 1, 2, 3, 4, 5 ]
        self.assertEqual([ 0, 0, 1, 1, 1, 1, 0 ],
            self.method_under_test(starts, ends, points))

    def test_with_two_segments1(self):
        starts = [ 1, 2 ]
        ends = [ 4, 5 ]
        points = [ -1 ]
        self.assertEqual([ 0 ],
            self.method_under_test(starts, ends, points))

    def test_with_two_segments2(self):
        starts = [ 1, 2 ]
        ends = [ 4, 5 ]
        points = [ 1 ]
        self.assertEqual([ 1 ],
            self.method_under_test(starts, ends, points))

    def test_with_two_segments3(self):
        starts = [ 1, 2 ]
        ends = [ 4, 5 ]
        points = [ 2 ]
        self.assertEqual([ 2 ],
            self.method_under_test(starts, ends, points))

    def test_with_two_segments4(self):
        starts = [ 1, 2 ]
        ends = [ 4, 5 ]
        points = [ 3 ]
        self.assertEqual([ 2 ],
            self.method_under_test(starts, ends, points))

    def test_with_two_segments5(self):
        starts = [ 1, 2 ]
        ends = [ 4, 5 ]
        points = [ 4 ]
        self.assertEqual([ 2 ],
            self.method_under_test(starts, ends, points))

    def test_with_two_segments6(self):
        starts = [ 1, 2 ]
        ends = [ 4, 5 ]
        points = [ 5 ]
        self.assertEqual([ 1 ],
            self.method_under_test(starts, ends, points))

    def test_with_two_segments7(self):
        starts = [ 1, 2 ]
        ends = [ 4, 5 ]
        points = [ 6 ]
        self.assertEqual([ 0 ],
            self.method_under_test(starts, ends, points))

    def test_with_two_segments8(self):
        starts = [ 1, 2 ]
        ends = [ 4, 5 ]
        points = [ -1, 0, 1, 2, 3, 4, 5, 6 ]
        self.assertEqual([ 0, 0, 1, 2, 2, 2, 1, 0 ],
            self.method_under_test(starts, ends, points))

    def test_with_several_segments1(self):
        starts = [ 0, 7 ]
        ends = [ 5, 10 ]
        points = [ 1, 6, 11 ]
        self.assertEqual([ 1, 0, 0 ],
            self.method_under_test(starts, ends, points))

    def test_with_several_segments2(self):
        starts = [ -10 ]
        ends = [ 10 ]
        points = [ -100, 100, 0 ]
        self.assertEqual([ 0, 0, 1 ],
            self.method_under_test(starts, ends, points))

    def test_with_several_segments3(self):
        starts = [ 0, -3, 7 ]
        ends = [ 5, 2, 10 ]
        points = [ 1, 6 ]
        self.assertEqual([ 2, 0 ],
            self.method_under_test(starts, ends, points))

    def test_with_several_equal_segments1(self):
        starts = [ 0, 0, 0 ]
        ends = [ 0, 0, 0 ]
        points = [ -1, 0, 1 ]
        self.assertEqual([ 0, 3, 0 ],
            self.method_under_test(starts, ends, points))

    def test_with_several_equal_segments2(self):
        starts = [ 0, 0, 0 ]
        ends = [ 1, 1, 1 ]
        points = [ -1, 0, 1, 2 ]
        self.assertEqual([ 0, 3, 3, 0 ],
            self.method_under_test(starts, ends, points))

    def test_with_huge_segments1(self):
        """
        points: -69733398, -43390377, 46584909, -65149461, 79215411
        counts:         0,         0,        2,         0,        1

        starts: -28471239, -16651407, 26250551,  57356881, 90751725
        ends:   -26580504,  95357651, 60037659,  70031990, 99598374
        """
        starts = [ 57356881, -28471239, 26250551, 90751725, -16651407 ]
        ends = [ 70031990, -26580504, 60037659, 99598374, 95357651 ]
        points = [ -69733398, -43390377, 46584909, -65149461, 79215411 ]
        self.assertEqual([ 0, 0, 2, 0, 1 ],
            self.method_under_test(starts, ends, points))

    def test_with_huge_segments2(self):
        starts = [ -82958095, -58513291, 16561991, -62195800, 69595351,
            -80465621, 67095560, 23525271, -15092577, -19366470 ]
        ends = [ -17876970, -56418445, 68393418, 1051277, 87501648,
            22270475, 72191430, 65728968, 2805348, 42444358 ]
        points = [ -68606013, 89174492, -74434082, -39578571, 57935890,
            -38499652, -11644735, 38455997, 20516305, 86791973 ]
        self.assertEqual([ 2, 0, 2, 3, 2, 3, 4, 3, 3, 1 ],
            self.method_under_test(starts, ends, points))

class NaiveCountSegmentsTestCase(CommonCountSegmentsTestCase):

    def setUp(self):
        self.method_under_test = naive_count_segments

    def tearDown(self):
        pass

class FastCountSegmentsTestCase(CommonCountSegmentsTestCase):

    def setUp(self):
        self.method_under_test = fast_count_segments_slow

    def tearDown(self):
        pass

if __name__ == '__main__':
    class_names = \
    [
        QuickSortOnTwoListsTestCase,
        SortSegmentsTestCase,
        NaiveCountSegmentsTestCase,
        FastCountSegmentsTestCase
    ]

    suite = unittest.TestSuite()

    for c in class_names:
        suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(c))

    unittest.TextTestRunner().run(suite)
