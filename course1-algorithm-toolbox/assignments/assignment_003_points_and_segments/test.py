#!/usr/bin/python3

import unittest

from points_and_segments import naive_count_segments, fast_count_segments

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

    def test_with_one_segment_of_duplicate_negative_points1(self):
        starts = [ -1 ]
        ends = [ -1 ]
        points = [ -3 ]
        self.assertEqual([ 0 ],
            self.method_under_test(starts, ends, points))

    def test_with_one_segment_of_duplicate_negative_points2(self):
        starts = [ -1 ]
        ends = [ -1 ]
        points = [ -2 ]
        self.assertEqual([ 0 ],
            self.method_under_test(starts, ends, points))

    def test_with_one_segment_of_duplicate_negative_points3(self):
        starts = [ -1 ]
        ends = [ -1 ]
        points = [ -1 ]
        self.assertEqual([ 1 ],
            self.method_under_test(starts, ends, points))

    def test_with_one_segment_of_duplicate_negative_points4(self):
        starts = [ -1 ]
        ends = [ -1 ]
        points = [ 0 ]
        self.assertEqual([ 0 ],
            self.method_under_test(starts, ends, points))

    def test_with_one_segment_of_duplicate_negative_points5(self):
        starts = [ -1 ]
        ends = [ -1 ]
        points = [ -3, -2, -1, 0 ]
        self.assertEqual([ 0, 0, 1, 0 ],
            self.method_under_test(starts, ends, points))

    def test_with_one_segment_of_duplicate_points1(self):
        starts = [ 1 ]
        ends = [ 1 ]
        points = [ -1 ]
        self.assertEqual([ 0 ],
            self.method_under_test(starts, ends, points))

    def test_with_one_segment_of_duplicate_points2(self):
        starts = [ 1 ]
        ends = [ 1 ]
        points = [ 0 ]
        self.assertEqual([ 0 ],
            self.method_under_test(starts, ends, points))

    def test_with_one_segment_of_duplicate_points3(self):
        starts = [ 1 ]
        ends = [ 1 ]
        points = [ 1 ]
        self.assertEqual([ 1 ],
            self.method_under_test(starts, ends, points))

    def test_with_one_segment_of_duplicate_points4(self):
        starts = [ 1 ]
        ends = [ 1 ]
        points = [ 2 ]
        self.assertEqual([ 0 ],
            self.method_under_test(starts, ends, points))

    def test_with_one_segment_of_duplicate_points5(self):
        starts = [ 1 ]
        ends = [ 1 ]
        points = [ -1, 0, 1, 2 ]
        self.assertEqual([ 0, 0, 1, 0 ],
            self.method_under_test(starts, ends, points))

    def test_with_one_negative_segment1(self):
        starts = [ -4 ]
        ends = [ -1 ]
        points = [ -5 ]
        self.assertEqual([ 0 ],
            self.method_under_test(starts, ends, points))

    def test_with_one_negative_segment2(self):
        starts = [ -4 ]
        ends = [ -1 ]
        points = [ -4 ]
        self.assertEqual([ 1 ],
            self.method_under_test(starts, ends, points))

    def test_with_one_negative_segment3(self):
        starts = [ -4 ]
        ends = [ -1 ]
        points = [ -3 ]
        self.assertEqual([ 1 ],
            self.method_under_test(starts, ends, points))

    def test_with_one_negative_segment4(self):
        starts = [ -4 ]
        ends = [ -1 ]
        points = [ -2 ]
        self.assertEqual([ 1 ],
            self.method_under_test(starts, ends, points))

    def test_with_one_negative_segment5(self):
        starts = [ -4 ]
        ends = [ -1 ]
        points = [ -1 ]
        self.assertEqual([ 1 ],
            self.method_under_test(starts, ends, points))

    def test_with_one_negative_segment6(self):
        starts = [ -4 ]
        ends = [ -1 ]
        points = [ 0 ]
        self.assertEqual([ 0 ],
            self.method_under_test(starts, ends, points))

    def test_with_one_negative_segment7(self):
        starts = [ -4 ]
        ends = [ -1 ]
        points = [ -5, -4, -3, -2, -1, 0 ]
        self.assertEqual([ 0, 1, 1, 1, 1, 0 ],
            self.method_under_test(starts, ends, points))

    def test_with_one_negative_and_positive_segment1(self):
        starts = [ -4 ]
        ends = [ 4 ]
        points = [ -5 ]
        self.assertEqual([ 0 ],
            self.method_under_test(starts, ends, points))

    def test_with_one_negative_and_positive_segment2(self):
        starts = [ -4 ]
        ends = [ 4 ]
        points = [ -4 ]
        self.assertEqual([ 1 ],
            self.method_under_test(starts, ends, points))

    def test_with_one_negative_and_positive_segment3(self):
        starts = [ -4 ]
        ends = [ 4 ]
        points = [ -3 ]
        self.assertEqual([ 1 ],
            self.method_under_test(starts, ends, points))

    def test_with_one_negative_and_positive_segment4(self):
        starts = [ -4 ]
        ends = [ 4 ]
        points = [ -2 ]
        self.assertEqual([ 1 ],
            self.method_under_test(starts, ends, points))

    def test_with_one_negative_and_positive_segment5(self):
        starts = [ -4 ]
        ends = [ 4 ]
        points = [ -1 ]
        self.assertEqual([ 1 ],
            self.method_under_test(starts, ends, points))

    def test_with_one_negative_and_positive_segment6(self):
        starts = [ -4 ]
        ends = [ 4 ]
        points = [ 0 ]
        self.assertEqual([ 1 ],
            self.method_under_test(starts, ends, points))

    def test_with_one_negative_and_positive_segment7(self):
        starts = [ -4 ]
        ends = [ 4 ]
        points = [ 1 ]
        self.assertEqual([ 1 ],
            self.method_under_test(starts, ends, points))

    def test_with_one_negative_and_positive_segment8(self):
        starts = [ -4 ]
        ends = [ 4 ]
        points = [ 2 ]
        self.assertEqual([ 1 ],
            self.method_under_test(starts, ends, points))

    def test_with_one_negative_and_positive_segment9(self):
        starts = [ -4 ]
        ends = [ 4 ]
        points = [ 3 ]
        self.assertEqual([ 1 ],
            self.method_under_test(starts, ends, points))

    def test_with_one_negative_and_positive_segment10(self):
        starts = [ -4 ]
        ends = [ 4 ]
        points = [ 4 ]
        self.assertEqual([ 1 ],
            self.method_under_test(starts, ends, points))

    def test_with_one_negative_and_positive_segment11(self):
        starts = [ -4 ]
        ends = [ 4 ]
        points = [ -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5 ]
        self.assertEqual([ 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0 ],
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

    def test_with_two_segments_and_overlap_of_zero_units1(self):
        starts = [ 1, 5 ]
        ends = [ 3, 6 ]
        points = [ -1 ]
        self.assertEqual([ 0 ],
            self.method_under_test(starts, ends, points))

    def test_with_two_segments_and_overlap_of_zero_units2(self):
        starts = [ 1, 5 ]
        ends = [ 3, 6 ]
        points = [ 0 ]
        self.assertEqual([ 0 ],
            self.method_under_test(starts, ends, points))

    def test_with_two_segments_and_overlap_of_zero_units3(self):
        starts = [ 1, 5 ]
        ends = [ 3, 6 ]
        points = [ 1 ]
        self.assertEqual([ 1 ],
            self.method_under_test(starts, ends, points))

    def test_with_two_segments_and_overlap_of_zero_units4(self):
        starts = [ 1, 5 ]
        ends = [ 3, 6 ]
        points = [ 2 ]
        self.assertEqual([ 1 ],
            self.method_under_test(starts, ends, points))

    def test_with_two_segments_and_overlap_of_zero_units5(self):
        starts = [ 1, 5 ]
        ends = [ 3, 6 ]
        points = [ 3 ]
        self.assertEqual([ 1 ],
            self.method_under_test(starts, ends, points))

    def test_with_two_segments_and_overlap_of_zero_units6(self):
        starts = [ 1, 5 ]
        ends = [ 3, 6 ]
        points = [ 4 ]
        self.assertEqual([ 0 ],
            self.method_under_test(starts, ends, points))

    def test_with_two_segments_and_overlap_of_zero_units7(self):
        starts = [ 1, 5 ]
        ends = [ 3, 6 ]
        points = [ 5 ]
        self.assertEqual([ 1 ],
            self.method_under_test(starts, ends, points))

    def test_with_two_segments_and_overlap_of_zero_units8(self):
        starts = [ 1, 5 ]
        ends = [ 3, 6 ]
        points = [ 6 ]
        self.assertEqual([ 1 ],
            self.method_under_test(starts, ends, points))

    def test_with_two_segments_and_overlap_of_zero_units9(self):
        starts = [ 1, 5 ]
        ends = [ 3, 6 ]
        points = [ 7 ]
        self.assertEqual([ 0 ],
            self.method_under_test(starts, ends, points))

    def test_with_two_segments_and_overlap_of_zero_units10(self):
        starts = [ 1, 5 ]
        ends = [ 3, 6 ]
        points = [ -1, 0, 1, 2, 3, 4, 5, 6, 7 ]
        self.assertEqual([ 0, 0, 1, 1, 1, 0, 1, 1, 0 ],
            self.method_under_test(starts, ends, points))

    def test_with_two_segments_and_overlap_as_point1(self):
        starts = [ 1, 3 ]
        ends = [ 3, 6 ]
        points = [ -1 ]
        self.assertEqual([ 0 ],
            self.method_under_test(starts, ends, points))

    def test_with_two_segments_and_overlap_as_point2(self):
        starts = [ 1, 3 ]
        ends = [ 3, 6 ]
        points = [ 0 ]
        self.assertEqual([ 0 ],
            self.method_under_test(starts, ends, points))

    def test_with_two_segments_and_overlap_as_point3(self):
        starts = [ 1, 3 ]
        ends = [ 3, 6 ]
        points = [ 1 ]
        self.assertEqual([ 1 ],
            self.method_under_test(starts, ends, points))

    def test_with_two_segments_and_overlap_as_point4(self):
        starts = [ 1, 3 ]
        ends = [ 3, 6 ]
        points = [ 2 ]
        self.assertEqual([ 1 ],
            self.method_under_test(starts, ends, points))

    def test_with_two_segments_and_overlap_as_point5(self):
        starts = [ 1, 3 ]
        ends = [ 3, 6 ]
        points = [ 3 ]
        self.assertEqual([ 2 ],
            self.method_under_test(starts, ends, points))

    def test_with_two_segments_and_overlap_as_point6(self):
        starts = [ 1, 3 ]
        ends = [ 3, 6 ]
        points = [ 4 ]
        self.assertEqual([ 1 ],
            self.method_under_test(starts, ends, points))

    def test_with_two_segments_and_overlap_as_point7(self):
        starts = [ 1, 3 ]
        ends = [ 3, 6 ]
        points = [ 5 ]
        self.assertEqual([ 1 ],
            self.method_under_test(starts, ends, points))

    def test_with_two_segments_and_overlap_as_point8(self):
        starts = [ 1, 3 ]
        ends = [ 3, 6 ]
        points = [ 6 ]
        self.assertEqual([ 1 ],
            self.method_under_test(starts, ends, points))

    def test_with_two_segments_and_overlap_as_point9(self):
        starts = [ 1, 3 ]
        ends = [ 3, 6 ]
        points = [ 7 ]
        self.assertEqual([ 0 ],
            self.method_under_test(starts, ends, points))

    def test_with_two_segments_and_overlap_as_point10(self):
        starts = [ 1, 3 ]
        ends = [ 3, 6 ]
        points = [ -1, 0, 1, 2, 3, 4, 5, 6, 7 ]
        self.assertEqual([ 0, 0, 1, 1, 2, 1, 1, 1, 0 ],
            self.method_under_test(starts, ends, points))

    def test_with_two_segments_and_overlap_of_one_units1(self):
        starts = [ 1, 3 ]
        ends = [ 4, 6 ]
        points = [ -1 ]
        self.assertEqual([ 0 ],
            self.method_under_test(starts, ends, points))

    def test_with_two_segments_and_overlap_of_one_units2(self):
        starts = [ 1, 3 ]
        ends = [ 4, 6 ]
        points = [ 0 ]
        self.assertEqual([ 0 ],
            self.method_under_test(starts, ends, points))

    def test_with_two_segments_and_overlap_of_one_units3(self):
        starts = [ 1, 3 ]
        ends = [ 4, 6 ]
        points = [ 1 ]
        self.assertEqual([ 1 ],
            self.method_under_test(starts, ends, points))

    def test_with_two_segments_and_overlap_of_one_units4(self):
        starts = [ 1, 3 ]
        ends = [ 4, 6 ]
        points = [ 2 ]
        self.assertEqual([ 1 ],
            self.method_under_test(starts, ends, points))

    def test_with_two_segments_and_overlap_of_one_units5(self):
        starts = [ 1, 3 ]
        ends = [ 4, 6 ]
        points = [ 3 ]
        self.assertEqual([ 2 ],
            self.method_under_test(starts, ends, points))

    def test_with_two_segments_and_overlap_of_one_units6(self):
        starts = [ 1, 3 ]
        ends = [ 4, 6 ]
        points = [ 4 ]
        self.assertEqual([ 2 ],
            self.method_under_test(starts, ends, points))

    def test_with_two_segments_and_overlap_of_one_units7(self):
        starts = [ 1, 3 ]
        ends = [ 4, 6 ]
        points = [ 5 ]
        self.assertEqual([ 1 ],
            self.method_under_test(starts, ends, points))

    def test_with_two_segments_and_overlap_of_one_units8(self):
        starts = [ 1, 3 ]
        ends = [ 4, 6 ]
        points = [ 6 ]
        self.assertEqual([ 1 ],
            self.method_under_test(starts, ends, points))

    def test_with_two_segments_and_overlap_of_one_units9(self):
        starts = [ 1, 3 ]
        ends = [ 4, 6 ]
        points = [ 7 ]
        self.assertEqual([ 0 ],
            self.method_under_test(starts, ends, points))

    def test_with_two_segments_and_overlap_of_one_units10(self):
        starts = [ 1, 3 ]
        ends = [ 4, 6 ]
        points = [ -1, 0, 1, 2, 3, 4, 5, 6, 7 ]
        self.assertEqual([ 0, 0, 1, 1, 2, 2, 1, 1, 0 ],
            self.method_under_test(starts, ends, points))

    def test_with_two_segments_and_overlap_of_two_units1(self):
        starts = [ 1, 2 ]
        ends = [ 4, 6 ]
        points = [ -1 ]
        self.assertEqual([ 0 ],
            self.method_under_test(starts, ends, points))

    def test_with_two_segments_and_overlap_of_two_units2(self):
        starts = [ 1, 2 ]
        ends = [ 4, 6 ]
        points = [ 0 ]
        self.assertEqual([ 0 ],
            self.method_under_test(starts, ends, points))

    def test_with_two_segments_and_overlap_of_two_units3(self):
        starts = [ 1, 2 ]
        ends = [ 4, 6 ]
        points = [ 1 ]
        self.assertEqual([ 1 ],
            self.method_under_test(starts, ends, points))

    def test_with_two_segments_and_overlap_of_two_units4(self):
        starts = [ 1, 2 ]
        ends = [ 4, 6 ]
        points = [ 2 ]
        self.assertEqual([ 2 ],
            self.method_under_test(starts, ends, points))

    def test_with_two_segments_and_overlap_of_two_units5(self):
        starts = [ 1, 2 ]
        ends = [ 4, 6 ]
        points = [ 3 ]
        self.assertEqual([ 2 ],
            self.method_under_test(starts, ends, points))

    def test_with_two_segments_and_overlap_of_two_units6(self):
        starts = [ 1, 2 ]
        ends = [ 4, 6 ]
        points = [ 4 ]
        self.assertEqual([ 2 ],
            self.method_under_test(starts, ends, points))

    def test_with_two_segments_and_overlap_of_two_units7(self):
        starts = [ 1, 2 ]
        ends = [ 4, 6 ]
        points = [ 5 ]
        self.assertEqual([ 1 ],
            self.method_under_test(starts, ends, points))

    def test_with_two_segments_and_overlap_of_two_units8(self):
        starts = [ 1, 2 ]
        ends = [ 4, 6 ]
        points = [ 6 ]
        self.assertEqual([ 1 ],
            self.method_under_test(starts, ends, points))

    def test_with_two_segments_and_overlap_of_two_units9(self):
        starts = [ 1, 2 ]
        ends = [ 4, 6 ]
        points = [ 7 ]
        self.assertEqual([ 0 ],
            self.method_under_test(starts, ends, points))

    def test_with_two_segments_and_overlap_of_two_units10(self):
        starts = [ 1, 2 ]
        ends = [ 4, 6 ]
        points = [ -1, 0, 1, 2, 3, 4, 5, 6, 7 ]
        self.assertEqual([ 0, 0, 1, 2, 2, 2, 1, 1, 0 ],
            self.method_under_test(starts, ends, points))

    def test_with_two_segments_and_overlap_of_three_units1(self):
        starts = [ 1, 2 ]
        ends = [ 5, 6 ]
        points = [ -1 ]
        self.assertEqual([ 0 ],
            self.method_under_test(starts, ends, points))

    def test_with_two_segments_and_overlap_of_three_units2(self):
        starts = [ 1, 2 ]
        ends = [ 5, 6 ]
        points = [ 0 ]
        self.assertEqual([ 0 ],
            self.method_under_test(starts, ends, points))

    def test_with_two_segments_and_overlap_of_three_units3(self):
        starts = [ 1, 2 ]
        ends = [ 5, 6 ]
        points = [ 1 ]
        self.assertEqual([ 1 ],
            self.method_under_test(starts, ends, points))

    def test_with_two_segments_and_overlap_of_three_units4(self):
        starts = [ 1, 2 ]
        ends = [ 5, 6 ]
        points = [ 2 ]
        self.assertEqual([ 2 ],
            self.method_under_test(starts, ends, points))

    def test_with_two_segments_and_overlap_of_three_units5(self):
        starts = [ 1, 2 ]
        ends = [ 5, 6 ]
        points = [ 3 ]
        self.assertEqual([ 2 ],
            self.method_under_test(starts, ends, points))

    def test_with_two_segments_and_overlap_of_three_units6(self):
        starts = [ 1, 2 ]
        ends = [ 5, 6 ]
        points = [ 4 ]
        self.assertEqual([ 2 ],
            self.method_under_test(starts, ends, points))

    def test_with_two_segments_and_overlap_of_three_units7(self):
        starts = [ 1, 2 ]
        ends = [ 5, 6 ]
        points = [ 5 ]
        self.assertEqual([ 2 ],
            self.method_under_test(starts, ends, points))

    def test_with_two_segments_and_overlap_of_three_units8(self):
        starts = [ 1, 2 ]
        ends = [ 5, 6 ]
        points = [ 6 ]
        self.assertEqual([ 1 ],
            self.method_under_test(starts, ends, points))

    def test_with_two_segments_and_overlap_of_three_units9(self):
        starts = [ 1, 2 ]
        ends = [ 5, 6 ]
        points = [ 7 ]
        self.assertEqual([ 0 ],
            self.method_under_test(starts, ends, points))

    def test_with_two_segments_and_overlap_of_three_units10(self):
        starts = [ 1, 2 ]
        ends = [ 5, 6 ]
        points = [ -1, 0, 1, 2, 3, 4, 5, 6, 7 ]
        self.assertEqual([ 0, 0, 1, 2, 2, 2, 2, 1, 0 ],
            self.method_under_test(starts, ends, points))

    def test_with_two_segments_and_overlap_of_four_units1(self):
        starts = [ 1, 1 ]
        ends = [ 5, 6 ]
        points = [ -1 ]
        self.assertEqual([ 0 ],
            self.method_under_test(starts, ends, points))

    def test_with_two_segments_and_overlap_of_four_units2(self):
        starts = [ 1, 1 ]
        ends = [ 5, 6 ]
        points = [ 0 ]
        self.assertEqual([ 0 ],
            self.method_under_test(starts, ends, points))

    def test_with_two_segments_and_overlap_of_four_units3(self):
        starts = [ 1, 1 ]
        ends = [ 5, 6 ]
        points = [ 1 ]
        self.assertEqual([ 2 ],
            self.method_under_test(starts, ends, points))

    def test_with_two_segments_and_overlap_of_four_units4(self):
        starts = [ 1, 1 ]
        ends = [ 5, 6 ]
        points = [ 2 ]
        self.assertEqual([ 2 ],
            self.method_under_test(starts, ends, points))

    def test_with_two_segments_and_overlap_of_four_units5(self):
        starts = [ 1, 1 ]
        ends = [ 5, 6 ]
        points = [ 3 ]
        self.assertEqual([ 2 ],
            self.method_under_test(starts, ends, points))

    def test_with_two_segments_and_overlap_of_four_units6(self):
        starts = [ 1, 1 ]
        ends = [ 5, 6 ]
        points = [ 4 ]
        self.assertEqual([ 2 ],
            self.method_under_test(starts, ends, points))

    def test_with_two_segments_and_overlap_of_four_units7(self):
        starts = [ 1, 1 ]
        ends = [ 5, 6 ]
        points = [ 5 ]
        self.assertEqual([ 2 ],
            self.method_under_test(starts, ends, points))

    def test_with_two_segments_and_overlap_of_four_units8(self):
        starts = [ 1, 1 ]
        ends = [ 5, 6 ]
        points = [ 6 ]
        self.assertEqual([ 1 ],
            self.method_under_test(starts, ends, points))

    def test_with_two_segments_and_overlap_of_four_units9(self):
        starts = [ 1, 1 ]
        ends = [ 5, 6 ]
        points = [ 7 ]
        self.assertEqual([ 0 ],
            self.method_under_test(starts, ends, points))

    def test_with_two_segments_and_overlap_of_four_units10(self):
        starts = [ 1, 1 ]
        ends = [ 5, 6 ]
        points = [ -1, 0, 1, 2, 3, 4, 5, 6, 7 ]
        self.assertEqual([ 0, 0, 2, 2, 2, 2, 2, 1, 0 ],
            self.method_under_test(starts, ends, points))

    def test_with_two_segments_and_overlap_of_five_units1(self):
        starts = [ 1, 1 ]
        ends = [ 6, 6 ]
        points = [ -1 ]
        self.assertEqual([ 0 ],
            self.method_under_test(starts, ends, points))

    def test_with_two_segments_and_overlap_of_five_units2(self):
        starts = [ 1, 1 ]
        ends = [ 6, 6 ]
        points = [ 0 ]
        self.assertEqual([ 0 ],
            self.method_under_test(starts, ends, points))

    def test_with_two_segments_and_overlap_of_five_units3(self):
        starts = [ 1, 1 ]
        ends = [ 6, 6 ]
        points = [ 1 ]
        self.assertEqual([ 2 ],
            self.method_under_test(starts, ends, points))

    def test_with_two_segments_and_overlap_of_five_units4(self):
        starts = [ 1, 1 ]
        ends = [ 6, 6 ]
        points = [ 2 ]
        self.assertEqual([ 2 ],
            self.method_under_test(starts, ends, points))

    def test_with_two_segments_and_overlap_of_five_units5(self):
        starts = [ 1, 1 ]
        ends = [ 6, 6 ]
        points = [ 3 ]
        self.assertEqual([ 2 ],
            self.method_under_test(starts, ends, points))

    def test_with_two_segments_and_overlap_of_five_units6(self):
        starts = [ 1, 1 ]
        ends = [ 6, 6 ]
        points = [ 4 ]
        self.assertEqual([ 2 ],
            self.method_under_test(starts, ends, points))

    def test_with_two_segments_and_overlap_of_five_units7(self):
        starts = [ 1, 1 ]
        ends = [ 6, 6 ]
        points = [ 5 ]
        self.assertEqual([ 2 ],
            self.method_under_test(starts, ends, points))

    def test_with_two_segments_and_overlap_of_five_units8(self):
        starts = [ 1, 1 ]
        ends = [ 6, 6 ]
        points = [ 6 ]
        self.assertEqual([ 2 ],
            self.method_under_test(starts, ends, points))

    def test_with_two_segments_and_overlap_of_five_units9(self):
        starts = [ 1, 1 ]
        ends = [ 6, 6 ]
        points = [ 7 ]
        self.assertEqual([ 0 ],
            self.method_under_test(starts, ends, points))

    def test_with_two_segments_and_overlap_of_five_units10(self):
        starts = [ 1, 1 ]
        ends = [ 6, 6 ]
        points = [ -1, 0, 1, 2, 3, 4, 5, 6, 7 ]
        self.assertEqual([ 0, 0, 2, 2, 2, 2, 2, 2, 0 ],
            self.method_under_test(starts, ends, points))

    def test_with_three_segments_and_no_overlaps(self):
        starts = [ 1, 5, 9 ]
        ends = [ 3, 7, 11 ]
        points = [ -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ]
        self.assertEqual([ 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0 ],
            self.method_under_test(starts, ends, points))

    def test_with_three_segments_and_overlap_of_1_and_2_as_point(self):
        starts = [ 1, 3, 9 ]
        ends = [ 3, 7, 11 ]
        points = [ -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ]
        self.assertEqual([ 0, 0, 1, 1, 2, 1, 1, 1, 1, 0, 1, 1, 1, 0 ],
            self.method_under_test(starts, ends, points))

    def test_with_three_segments_and_overlap_of_1_and_2_as_segment(self):
        starts = [ 1, 2, 9 ]
        ends = [ 3, 7, 11 ]
        points = [ -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ]
        self.assertEqual([ 0, 0, 1, 2, 2, 1, 1, 1, 1, 0, 1, 1, 1, 0 ],
            self.method_under_test(starts, ends, points))

    def test_with_three_segments_and_overlap_of_2_and_3_as_point(self):
        starts = [ 1, 5, 7 ]
        ends = [ 3, 7, 11 ]
        points = [ -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ]
        self.assertEqual([ 0, 0, 1, 1, 1, 0, 1, 1, 2, 1, 1, 1, 1, 0 ],
            self.method_under_test(starts, ends, points))

    def test_with_three_segments_and_overlap_of_2_and_3_as_segment(self):
        starts = [ 1, 5, 6 ]
        ends = [ 3, 7, 11 ]
        points = [ -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ]
        self.assertEqual([ 0, 0, 1, 1, 1, 0, 1, 2, 2, 1, 1, 1, 1, 0 ],
            self.method_under_test(starts, ends, points))

    def test_with_three_segments_and_overlap_of_all_as_segments(self):
        starts = [ 1, 2, 6 ]
        ends = [ 3, 7, 11 ]
        points = [ -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ]
        self.assertEqual([ 0, 0, 1, 2, 2, 1, 1, 2, 2, 1, 1, 1, 1, 0 ],
            self.method_under_test(starts, ends, points))

    def test_with_three_mixed_segments_and_no_overlaps(self):
        starts = [ -6, -2, 4 ]
        ends = [ -4, 2, 5 ]
        points = [ -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6 ]
        self.assertEqual([ 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0 ],
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

    def test_with_several_mixed_segments1(self):
        starts = [ -10, 3, 3, 8, 9 ]
        ends = [ 5, 9, 9, 10, 10 ]
        points = [ -4, 6, -8, -9 ]
        self.assertEqual([ 1, 2, 1, 1 ],
            self.method_under_test(starts, ends, points))

    def test_with_several_mixed_segments2(self):
        starts = [ -10, 3, 3, 8, 9 ]
        ends = [ 5, 9, 9, 10, 10 ]
        points = [ 3 ]
        self.assertEqual([ 3 ],
            self.method_under_test(starts, ends, points))

    def test_with_several_mixed_segments3(self):
        starts = [ -10, 3, 3, 8, 9 ]
        ends = [ 5, 9, 9, 10, 10 ]
        points = [ -4, 6, -8, 3, -9 ]
        self.assertEqual([ 1, 2, 1, 3, 1 ],
            self.method_under_test(starts, ends, points))

class NaiveCountSegmentsTestCase(CommonCountSegmentsTestCase):

    def setUp(self):
        self.method_under_test = naive_count_segments

    def tearDown(self):
        pass

class FastCountSegmentsTestCase(CommonCountSegmentsTestCase):

    def setUp(self):
        self.method_under_test = fast_count_segments

    def tearDown(self):
        pass

if __name__ == '__main__':
    class_names = \
    [
        NaiveCountSegmentsTestCase,
        FastCountSegmentsTestCase,
    ]

    suite = unittest.TestSuite()

    for c in class_names:
        suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(c))

    unittest.TextTestRunner().run(suite)
