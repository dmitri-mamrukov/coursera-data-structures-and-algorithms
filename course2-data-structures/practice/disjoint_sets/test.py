#!/usr/bin/python3

import unittest

from union_find_with_rank import UnionFindWithRank
from union_find_with_rank_and_compression \
    import UnionFindWithRankAndCompression
from union_find_with_smallest import UnionFindWithSmallest

class UnionFindWithSmallestTestCase(unittest.TestCase):

    def test_constructor_with_n_as_negative(self):
        with self.assertRaisesRegex(ValueError, 'n must be > 0.'):
            UnionFindWithSmallest(-1)

    def test_constructor_with_n_as_zero(self):
        with self.assertRaisesRegex(ValueError, 'n must be > 0.'):
            UnionFindWithSmallest(0)

    def test_constructor_with_n_as_one(self):
        n = 1
        union_find = UnionFindWithSmallest(n)

        self.assertEqual(n, len(union_find.smallest))
        self.assertEqual([ 0 ], union_find.smallest)

    def test_constructor_with_n_as_two(self):
        n = 2
        union_find = UnionFindWithSmallest(n)

        self.assertEqual(n, len(union_find.smallest))
        self.assertEqual([ 0, 0 ], union_find.smallest)

    def test_constructor_with_n_as_three(self):
        n = 3
        union_find = UnionFindWithSmallest(n)

        self.assertEqual(n, len(union_find.smallest))
        self.assertEqual([ 0, 0, 0 ], union_find.smallest)

    def test_str_with_one_element(self):
        self.assertEqual('[0]', str(UnionFindWithSmallest(1)))

    def test_str_with_two_elements(self):
        self.assertEqual('[0, 0]', str(UnionFindWithSmallest(2)))

    def test_str_with_three_elements(self):
        self.assertEqual('[0, 0, 0]', str(UnionFindWithSmallest(3)))

    def test_repr_with_one_element(self):
        self.assertEqual('[0]', repr(UnionFindWithSmallest(1)))

    def test_repr_with_two_elements(self):
        self.assertEqual('[0, 0]', repr(UnionFindWithSmallest(2)))

    def test_repr_with_three_elements(self):
        self.assertEqual('[0, 0, 0]', repr(UnionFindWithSmallest(3)))

    def test_make_set_on_one_element_with_negative(self):
        union_find = UnionFindWithSmallest(1)

        with self.assertRaisesRegex(ValueError,
            "x must be within the set's range."):
            union_find.make_set(-1)

    def test_make_set_on_one_element_with_exceeding(self):
        union_find = UnionFindWithSmallest(1)

        with self.assertRaisesRegex(ValueError,
            "x must be within the set's range."):
            union_find.make_set(1)

    def test_make_set_on_two_elements_with_negative(self):
        union_find = UnionFindWithSmallest(2)

        with self.assertRaisesRegex(ValueError,
            "x must be within the set's range."):
            union_find.make_set(-1)

    def test_make_set_on_two_elements_with_exceeding(self):
        union_find = UnionFindWithSmallest(2)

        with self.assertRaisesRegex(ValueError,
            "x must be within the set's range."):
            union_find.make_set(2)

    def test_make_set_on_one_element(self):
        union_find = UnionFindWithSmallest(1)

        union_find.make_set(0)

        self.assertEqual([ 0 ], union_find.smallest)

    def test_make_set_on_two_elements(self):
        union_find = UnionFindWithSmallest(2)

        union_find.make_set(0)

        self.assertEqual([ 0, 0 ], union_find.smallest)

        union_find.make_set(1)

        self.assertEqual([ 0, 1 ], union_find.smallest)

    def test_make_set_on_three_elements(self):
        union_find = UnionFindWithSmallest(3)

        union_find.make_set(0)

        self.assertEqual([ 0, 0, 0 ], union_find.smallest)

        union_find.make_set(1)

        self.assertEqual([ 0, 1, 0 ], union_find.smallest)

        union_find.make_set(2)

        self.assertEqual([ 0, 1, 2 ], union_find.smallest)

    def test_make_set_on_three_elements_with_repetitions(self):
        union_find = UnionFindWithSmallest(3)

        union_find.make_set(0)

        self.assertEqual([ 0, 0, 0 ], union_find.smallest)

        union_find.make_set(0)

        self.assertEqual([ 0, 0, 0 ], union_find.smallest)

        union_find.make_set(1)

        self.assertEqual([ 0, 1, 0 ], union_find.smallest)

        union_find.make_set(1)

        self.assertEqual([ 0, 1, 0 ], union_find.smallest)

        union_find.make_set(2)

        self.assertEqual([ 0, 1, 2 ], union_find.smallest)

        union_find.make_set(2)

        self.assertEqual([ 0, 1, 2 ], union_find.smallest)

    def test_find_on_one_element_with_negative(self):
        union_find = UnionFindWithSmallest(1)

        with self.assertRaisesRegex(ValueError,
            "x must be within the set's range."):
            union_find.find(-1)

    def test_find_on_one_element_with_exceeding(self):
        union_find = UnionFindWithSmallest(1)

        with self.assertRaisesRegex(ValueError,
            "x must be within the set's range."):
            union_find.find(1)

    def test_find_on_two_elements_with_negative(self):
        union_find = UnionFindWithSmallest(2)

        with self.assertRaisesRegex(ValueError,
            "x must be within the set's range."):
            union_find.find(-1)

    def test_find_on_two_elements_with_exceeding(self):
        union_find = UnionFindWithSmallest(2)

        with self.assertRaisesRegex(ValueError,
            "x must be within the set's range."):
            union_find.find(2)

    def test_find_on_one_element_before_and_after_make_set(self):
        union_find = UnionFindWithSmallest(1)

        self.assertEqual(0, union_find.find(0))

        union_find.make_set(0)

        self.assertEqual(0, union_find.find(0))

    def test_find_on_two_elements_before_and_after_make_set(self):
        union_find = UnionFindWithSmallest(2)

        self.assertEqual(0, union_find.find(0))

        union_find.make_set(0)

        self.assertEqual(0, union_find.find(0))

        self.assertEqual(0, union_find.find(1))

        union_find.make_set(1)

        self.assertEqual(1, union_find.find(1))

    def test_find_on_three_elements_before_and_after_make_set(self):
        union_find = UnionFindWithSmallest(3)

        self.assertEqual(0, union_find.find(0))

        union_find.make_set(0)

        self.assertEqual(0, union_find.find(0))

        self.assertEqual(0, union_find.find(1))

        union_find.make_set(1)

        self.assertEqual(1, union_find.find(1))

        self.assertEqual(0, union_find.find(2))

        union_find.make_set(2)

        self.assertEqual(2, union_find.find(2))

    def test_union_on_one_element_with_negative_x(self):
        union_find = UnionFindWithSmallest(1)

        with self.assertRaisesRegex(ValueError,
            "x must be within the set's range."):
            union_find.union(-1, 0)

    def test_union_on_one_element_with_exceeding_x(self):
        union_find = UnionFindWithSmallest(1)

        with self.assertRaisesRegex(ValueError,
            "x must be within the set's range."):
            union_find.union(1, 0)

    def test_union_on_one_element_with_negative_y(self):
        union_find = UnionFindWithSmallest(1)

        with self.assertRaisesRegex(ValueError,
            "y must be within the set's range."):
            union_find.union(0, -1)

    def test_union_on_one_element_with_exceeding_y(self):
        union_find = UnionFindWithSmallest(1)

        with self.assertRaisesRegex(ValueError,
            "y must be within the set's range."):
            union_find.union(0, 1)

    def test_union_on_two_elements_with_negative_x(self):
        union_find = UnionFindWithSmallest(1)

        with self.assertRaisesRegex(ValueError,
            "x must be within the set's range."):
            union_find.union(-1, 0)

    def test_union_on_two_elements_with_exceeding_x(self):
        union_find = UnionFindWithSmallest(2)

        with self.assertRaisesRegex(ValueError,
            "x must be within the set's range."):
            union_find.union(2, 0)

    def test_union_on_two_elements_with_negative_y(self):
        union_find = UnionFindWithSmallest(1)

        with self.assertRaisesRegex(ValueError,
            "y must be within the set's range."):
            union_find.union(0, -1)

    def test_union_on_two_elements_with_exceeding_y(self):
        union_find = UnionFindWithSmallest(2)

        with self.assertRaisesRegex(ValueError,
            "y must be within the set's range."):
            union_find.union(0, 2)

    def test_union_on_one_element_with_x_and_y_as_same_before_make_set(self):
        union_find = UnionFindWithSmallest(1)

        union_find.union(0, 0)

        self.assertEqual([ 0 ], union_find.smallest)

    def test_union_on_one_element_with_x_and_y_as_same_after_make_set(self):
        union_find = UnionFindWithSmallest(1)

        union_find.make_set(0)

        self.assertEqual([ 0 ], union_find.smallest)

        union_find.union(0, 0)

        self.assertEqual([ 0 ], union_find.smallest)

    def test_union_on_two_element_with_x_and_y_as_same_before_make_set(self):
        union_find = UnionFindWithSmallest(2)

        union_find.union(0, 0)

        self.assertEqual([ 0, 0 ], union_find.smallest)

    def test_union_on_two_elements_with_x_and_y_as_same_after_make_set(self):
        union_find = UnionFindWithSmallest(2)

        union_find.make_set(0)
        union_find.make_set(1)

        self.assertEqual([ 0, 1 ], union_find.smallest)

        union_find.union(0, 0)

        self.assertEqual([ 0, 1 ], union_find.smallest)

        union_find.union(1, 1)

        self.assertEqual([ 0, 1 ], union_find.smallest)

    def test_union_on_two_element_with_x_and_y_as_diff_before_make_set(self):
        union_find = UnionFindWithSmallest(2)

        union_find.union(0, 1)

        self.assertEqual([ 0, 0 ], union_find.smallest)

        union_find.union(1, 0)

        self.assertEqual([ 0, 0 ], union_find.smallest)

    def test_union_on_two_elements_with_x_and_y_as_diff_after_make_set(self):
        union_find = UnionFindWithSmallest(2)

        union_find.make_set(0)
        union_find.make_set(1)

        self.assertEqual([ 0, 1 ], union_find.smallest)

        union_find.union(0, 1)

        self.assertEqual([ 0, 0 ], union_find.smallest)

        union_find.make_set(0)
        union_find.make_set(1)

        self.assertEqual([ 0, 1 ], union_find.smallest)

        union_find.union(1, 0)

        self.assertEqual([ 0, 0 ], union_find.smallest)

    def test_union_on_three_elements_before_make_set(self):
        union_find = UnionFindWithSmallest(3)

        union_find.union(0, 1)

        self.assertEqual([ 0, 0, 0 ], union_find.smallest)

        union_find.union(0, 2)

        self.assertEqual([ 0, 0, 0 ], union_find.smallest)

        union_find.union(1, 0)

        self.assertEqual([ 0, 0, 0 ], union_find.smallest)

        union_find.union(1, 2)

        self.assertEqual([ 0, 0, 0 ], union_find.smallest)

        union_find.union(2, 0)

        self.assertEqual([ 0, 0, 0 ], union_find.smallest)

        union_find.union(2, 1)

        self.assertEqual([ 0, 0, 0 ], union_find.smallest)

    def test_union_on_three_elements_after_make_set_with_0_and_1(self):
        union_find = UnionFindWithSmallest(3)

        union_find.make_set(0)
        union_find.make_set(1)
        union_find.make_set(2)

        self.assertEqual([ 0, 1, 2 ], union_find.smallest)

        union_find.union(0, 1)

        self.assertEqual([ 0, 0, 2 ], union_find.smallest)

    def test_union_on_three_elements_after_make_set_with_1_and_0(self):
        union_find = UnionFindWithSmallest(3)

        union_find.make_set(0)
        union_find.make_set(1)
        union_find.make_set(2)

        self.assertEqual([ 0, 1, 2 ], union_find.smallest)

        union_find.union(1, 0)

        self.assertEqual([ 0, 0, 2 ], union_find.smallest)

    def test_union_on_three_elements_after_make_set_with_0_and_2(self):
        union_find = UnionFindWithSmallest(3)

        union_find.make_set(0)
        union_find.make_set(1)
        union_find.make_set(2)

        self.assertEqual([ 0, 1, 2 ], union_find.smallest)

        union_find.union(0, 2)

        self.assertEqual([ 0, 1, 0 ], union_find.smallest)

    def test_union_on_three_elements_after_make_set_with_2_and_0(self):
        union_find = UnionFindWithSmallest(3)

        union_find.make_set(0)
        union_find.make_set(1)
        union_find.make_set(2)

        self.assertEqual([ 0, 1, 2 ], union_find.smallest)

        union_find.union(2, 0)

        self.assertEqual([ 0, 1, 0 ], union_find.smallest)

    def test_union_on_three_elements_after_make_set_with_1_and_2(self):
        union_find = UnionFindWithSmallest(3)

        union_find.make_set(0)
        union_find.make_set(1)
        union_find.make_set(2)

        self.assertEqual([ 0, 1, 2 ], union_find.smallest)

        union_find.union(1, 2)

        self.assertEqual([ 0, 1, 1 ], union_find.smallest)

    def test_union_on_three_elements_after_make_set_with_2_and_1(self):
        union_find = UnionFindWithSmallest(3)

        union_find.make_set(0)
        union_find.make_set(1)
        union_find.make_set(2)

        self.assertEqual([ 0, 1, 2 ], union_find.smallest)

        union_find.union(2, 1)

        self.assertEqual([ 0, 1, 1 ], union_find.smallest)

    def test_union_on_three_elements_to_make_one_set_on_left(self):
        union_find = UnionFindWithSmallest(3)

        union_find.make_set(0)
        union_find.make_set(1)
        union_find.make_set(2)

        self.assertEqual([ 0, 1, 2 ], union_find.smallest)
        self.assertEqual(0, union_find.find(0))
        self.assertEqual(1, union_find.find(1))
        self.assertEqual(2, union_find.find(2))

        union_find.union(0, 1)

        self.assertEqual([ 0, 0, 2 ], union_find.smallest)
        self.assertEqual(0, union_find.find(0))
        self.assertEqual(0, union_find.find(1))
        self.assertEqual(2, union_find.find(2))

        union_find.union(1, 2)

        self.assertEqual([ 0, 0, 0 ], union_find.smallest)
        self.assertEqual(0, union_find.find(0))
        self.assertEqual(0, union_find.find(1))
        self.assertEqual(0, union_find.find(2))

    def test_union_on_three_elements_to_make_one_set_in_middle(self):
        union_find = UnionFindWithSmallest(3)

        union_find.make_set(0)
        union_find.make_set(1)
        union_find.make_set(2)

        self.assertEqual([ 0, 1, 2 ], union_find.smallest)
        self.assertEqual(0, union_find.find(0))
        self.assertEqual(1, union_find.find(1))
        self.assertEqual(2, union_find.find(2))

        union_find.union(1, 2)

        self.assertEqual([ 0, 1, 1 ], union_find.smallest)
        self.assertEqual(0, union_find.find(0))
        self.assertEqual(1, union_find.find(1))
        self.assertEqual(1, union_find.find(2))

        union_find.union(1, 0)

        self.assertEqual([ 0, 0, 0 ], union_find.smallest)
        self.assertEqual(0, union_find.find(0))
        self.assertEqual(0, union_find.find(1))
        self.assertEqual(0, union_find.find(2))

    def test_union_on_three_elements_to_make_one_set_on_right(self):
        union_find = UnionFindWithSmallest(3)

        union_find.make_set(0)
        union_find.make_set(1)
        union_find.make_set(2)

        self.assertEqual([ 0, 1, 2 ], union_find.smallest)
        self.assertEqual(0, union_find.find(0))
        self.assertEqual(1, union_find.find(1))
        self.assertEqual(2, union_find.find(2))

        union_find.union(2, 1)

        self.assertEqual([ 0, 1, 1 ], union_find.smallest)
        self.assertEqual(0, union_find.find(0))
        self.assertEqual(1, union_find.find(1))
        self.assertEqual(1, union_find.find(2))

        union_find.union(1, 0)

        self.assertEqual([ 0, 0, 0 ], union_find.smallest)
        self.assertEqual(0, union_find.find(0))
        self.assertEqual(0, union_find.find(1))
        self.assertEqual(0, union_find.find(2))

class UnionFindWithRankTestCase(unittest.TestCase):

    def test_constructor_with_n_as_negative(self):
        with self.assertRaisesRegex(ValueError, 'n must be > 0.'):
            UnionFindWithRank(-1)

    def test_constructor_with_n_as_zero(self):
        with self.assertRaisesRegex(ValueError, 'n must be > 0.'):
            UnionFindWithRank(0)

    def test_constructor_with_n_as_one(self):
        n = 1
        union_find = UnionFindWithRank(n)

        self.assertEqual(n, len(union_find.parent))
        self.assertEqual([ 0 ], union_find.parent)
        self.assertEqual(n, len(union_find.rank))
        self.assertEqual([ 0 ], union_find.rank)

    def test_constructor_with_n_as_two(self):
        n = 2
        union_find = UnionFindWithRank(n)

        self.assertEqual(n, len(union_find.parent))
        self.assertEqual([ 0, 0 ], union_find.parent)
        self.assertEqual(n, len(union_find.rank))
        self.assertEqual([ 0, 0 ], union_find.rank)

    def test_constructor_with_n_as_three(self):
        n = 3
        union_find = UnionFindWithRank(n)

        self.assertEqual(n, len(union_find.parent))
        self.assertEqual([ 0, 0, 0 ], union_find.parent)
        self.assertEqual(n, len(union_find.rank))
        self.assertEqual([ 0, 0, 0 ], union_find.rank)

    def test_str_with_one_element(self):
        self.assertEqual('[parent=[0], rank=[0]]',
            str(UnionFindWithRank(1)))

    def test_str_with_two_elements(self):
        self.assertEqual('[parent=[0, 0], rank=[0, 0]]',
            str(UnionFindWithRank(2)))

    def test_str_with_three_elements(self):
        self.assertEqual('[parent=[0, 0, 0], rank=[0, 0, 0]]',
            str(UnionFindWithRank(3)))

    def test_repr_with_one_element(self):
        self.assertEqual('[parent=[0], rank=[0]]',
            repr(UnionFindWithRank(1)))

    def test_repr_with_two_elements(self):
        self.assertEqual('[parent=[0, 0], rank=[0, 0]]',
            repr(UnionFindWithRank(2)))

    def test_repr_with_three_elements(self):
        self.assertEqual('[parent=[0, 0, 0], rank=[0, 0, 0]]',
            repr(UnionFindWithRank(3)))

    def test_make_set_on_one_element_with_negative(self):
        union_find = UnionFindWithRank(1)

        with self.assertRaisesRegex(ValueError,
            "x must be within the set's range."):
            union_find.make_set(-1)

    def test_make_set_on_one_element_with_exceeding(self):
        union_find = UnionFindWithRank(1)

        with self.assertRaisesRegex(ValueError,
            "x must be within the set's range."):
            union_find.make_set(1)

    def test_make_set_on_two_elements_with_negative(self):
        union_find = UnionFindWithRank(2)

        with self.assertRaisesRegex(ValueError,
            "x must be within the set's range."):
            union_find.make_set(-1)

    def test_make_set_on_two_elements_with_exceeding(self):
        union_find = UnionFindWithRank(2)

        with self.assertRaisesRegex(ValueError,
            "x must be within the set's range."):
            union_find.make_set(2)

    def test_make_set_on_one_element(self):
        union_find = UnionFindWithRank(1)

        union_find.make_set(0)

        self.assertEqual([ 0 ], union_find.parent)
        self.assertEqual([ 0 ], union_find.rank)

    def test_make_set_on_two_elements(self):
        union_find = UnionFindWithRank(2)

        union_find.make_set(0)

        self.assertEqual([ 0, 0 ], union_find.parent)

        union_find.make_set(1)

        self.assertEqual([ 0, 1 ], union_find.parent)
        self.assertEqual([ 0, 0 ], union_find.rank)

    def test_make_set_on_three_elements(self):
        union_find = UnionFindWithRank(3)

        union_find.make_set(0)

        self.assertEqual([ 0, 0, 0 ], union_find.parent)
        self.assertEqual([ 0, 0, 0 ], union_find.rank)

        union_find.make_set(1)

        self.assertEqual([ 0, 1, 0 ], union_find.parent)
        self.assertEqual([ 0, 0, 0 ], union_find.rank)

        union_find.make_set(2)

        self.assertEqual([ 0, 1, 2 ], union_find.parent)
        self.assertEqual([ 0, 0, 0 ], union_find.rank)

    def test_make_set_on_three_elements_with_repetitions(self):
        union_find = UnionFindWithRank(3)

        union_find.make_set(0)

        self.assertEqual([ 0, 0, 0 ], union_find.parent)
        self.assertEqual([ 0, 0, 0 ], union_find.rank)

        union_find.make_set(0)

        self.assertEqual([ 0, 0, 0 ], union_find.parent)
        self.assertEqual([ 0, 0, 0 ], union_find.rank)

        union_find.make_set(1)

        self.assertEqual([ 0, 1, 0 ], union_find.parent)
        self.assertEqual([ 0, 0, 0 ], union_find.rank)

        union_find.make_set(1)

        self.assertEqual([ 0, 1, 0 ], union_find.parent)
        self.assertEqual([ 0, 0, 0 ], union_find.rank)

        union_find.make_set(2)

        self.assertEqual([ 0, 1, 2 ], union_find.parent)
        self.assertEqual([ 0, 0, 0 ], union_find.rank)

        union_find.make_set(2)

        self.assertEqual([ 0, 1, 2 ], union_find.parent)
        self.assertEqual([ 0, 0, 0 ], union_find.rank)

    def test_find_on_one_element_with_negative(self):
        union_find = UnionFindWithRank(1)

        with self.assertRaisesRegex(ValueError,
            "x must be within the set's range."):
            union_find.find(-1)

    def test_find_on_one_element_with_exceeding(self):
        union_find = UnionFindWithRank(1)

        with self.assertRaisesRegex(ValueError,
            "x must be within the set's range."):
            union_find.find(1)

    def test_find_on_two_elements_with_negative(self):
        union_find = UnionFindWithRank(2)

        with self.assertRaisesRegex(ValueError,
            "x must be within the set's range."):
            union_find.find(-1)

    def test_find_on_two_elements_with_exceeding(self):
        union_find = UnionFindWithRank(2)

        with self.assertRaisesRegex(ValueError,
            "x must be within the set's range."):
            union_find.find(2)

    def test_find_on_one_element_before_and_after_make_set(self):
        union_find = UnionFindWithRank(1)

        self.assertEqual(0, union_find.find(0))

        union_find.make_set(0)

        self.assertEqual(0, union_find.find(0))

    def test_find_on_two_elements_before_and_after_make_set(self):
        union_find = UnionFindWithRank(2)

        self.assertEqual(0, union_find.find(0))

        union_find.make_set(0)

        self.assertEqual(0, union_find.find(0))

        self.assertEqual(0, union_find.find(1))

        union_find.make_set(1)

        self.assertEqual(1, union_find.find(1))

    def test_find_on_three_elements_before_and_after_make_set(self):
        union_find = UnionFindWithRank(3)

        self.assertEqual(0, union_find.find(0))

        union_find.make_set(0)

        self.assertEqual(0, union_find.find(0))

        self.assertEqual(0, union_find.find(1))

        union_find.make_set(1)

        self.assertEqual(1, union_find.find(1))

        self.assertEqual(0, union_find.find(2))

        union_find.make_set(2)

        self.assertEqual(2, union_find.find(2))

    def test_union_on_one_element_with_negative_x(self):
        union_find = UnionFindWithRank(1)

        with self.assertRaisesRegex(ValueError,
            "x must be within the set's range."):
            union_find.union(-1, 0)

    def test_union_on_one_element_with_exceeding_x(self):
        union_find = UnionFindWithRank(1)

        with self.assertRaisesRegex(ValueError,
            "x must be within the set's range."):
            union_find.union(1, 0)

    def test_union_on_one_element_with_negative_y(self):
        union_find = UnionFindWithRank(1)

        with self.assertRaisesRegex(ValueError,
            "y must be within the set's range."):
            union_find.union(0, -1)

    def test_union_on_one_element_with_exceeding_y(self):
        union_find = UnionFindWithRank(1)

        with self.assertRaisesRegex(ValueError,
            "y must be within the set's range."):
            union_find.union(0, 1)

    def test_union_on_two_elements_with_negative_x(self):
        union_find = UnionFindWithRank(1)

        with self.assertRaisesRegex(ValueError,
            "x must be within the set's range."):
            union_find.union(-1, 0)

    def test_union_on_two_elements_with_exceeding_x(self):
        union_find = UnionFindWithRank(2)

        with self.assertRaisesRegex(ValueError,
            "x must be within the set's range."):
            union_find.union(2, 0)

    def test_union_on_two_elements_with_negative_y(self):
        union_find = UnionFindWithRank(1)

        with self.assertRaisesRegex(ValueError,
            "y must be within the set's range."):
            union_find.union(0, -1)

    def test_union_on_two_elements_with_exceeding_y(self):
        union_find = UnionFindWithRank(2)

        with self.assertRaisesRegex(ValueError,
            "y must be within the set's range."):
            union_find.union(0, 2)

    def test_union_on_one_element_with_x_and_y_as_same_before_make_set(self):
        union_find = UnionFindWithRank(1)

        union_find.union(0, 0)

        self.assertEqual([ 0 ], union_find.parent)
        self.assertEqual([ 0 ], union_find.rank)

    def test_union_on_one_element_with_x_and_y_as_same_after_make_set(self):
        union_find = UnionFindWithRank(1)

        union_find.make_set(0)

        self.assertEqual([ 0 ], union_find.parent)
        self.assertEqual([ 0 ], union_find.rank)

        union_find.union(0, 0)

        self.assertEqual([ 0 ], union_find.parent)
        self.assertEqual([ 0 ], union_find.rank)

    def test_union_on_two_element_with_x_and_y_as_same_before_make_set(self):
        union_find = UnionFindWithRank(2)

        union_find.union(0, 0)

        self.assertEqual([ 0, 0 ], union_find.parent)
        self.assertEqual([ 0, 0 ], union_find.rank)

    def test_union_on_two_elements_with_x_and_y_as_same_after_make_set(self):
        union_find = UnionFindWithRank(2)

        union_find.make_set(0)
        union_find.make_set(1)

        self.assertEqual([ 0, 1 ], union_find.parent)
        self.assertEqual([ 0, 0 ], union_find.rank)

        union_find.union(0, 0)

        self.assertEqual([ 0, 1 ], union_find.parent)
        self.assertEqual([ 0, 0 ], union_find.rank)

        union_find.union(1, 1)

        self.assertEqual([ 0, 1 ], union_find.parent)
        self.assertEqual([ 0, 0 ], union_find.rank)

    def test_union_on_two_element_with_x_and_y_as_diff_before_make_set(self):
        union_find = UnionFindWithRank(2)

        union_find.union(0, 1)

        self.assertEqual([ 0, 0 ], union_find.parent)
        self.assertEqual([ 0, 0 ], union_find.rank)

        union_find.union(1, 0)

        self.assertEqual([ 0, 0 ], union_find.parent)
        self.assertEqual([ 0, 0 ], union_find.rank)

    def test_union_on_two_elements_with_x_and_y_as_diff_after_make_set(self):
        union_find = UnionFindWithRank(2)

        union_find.make_set(0)
        union_find.make_set(1)

        self.assertEqual([ 0, 1 ], union_find.parent)
        self.assertEqual([ 0, 0 ], union_find.rank)

        union_find.union(0, 1)

        self.assertEqual([ 1, 1 ], union_find.parent)
        self.assertEqual([ 0, 1 ], union_find.rank)

        union_find.make_set(0)
        union_find.make_set(1)

        self.assertEqual([ 0, 1 ], union_find.parent)
        self.assertEqual([ 0, 0 ], union_find.rank)

        union_find.union(1, 0)

        self.assertEqual([ 0, 0 ], union_find.parent)
        self.assertEqual([ 1, 0 ], union_find.rank)

    def test_union_on_three_elements_before_make_set(self):
        union_find = UnionFindWithRank(3)

        union_find.union(0, 1)

        self.assertEqual([ 0, 0, 0 ], union_find.parent)
        self.assertEqual([ 0, 0, 0 ], union_find.rank)

        union_find.union(0, 2)

        self.assertEqual([ 0, 0, 0 ], union_find.parent)
        self.assertEqual([ 0, 0, 0 ], union_find.rank)

        union_find.union(1, 0)

        self.assertEqual([ 0, 0, 0 ], union_find.parent)
        self.assertEqual([ 0, 0, 0 ], union_find.rank)

        union_find.union(1, 2)

        self.assertEqual([ 0, 0, 0 ], union_find.parent)
        self.assertEqual([ 0, 0, 0 ], union_find.rank)

        union_find.union(2, 0)

        self.assertEqual([ 0, 0, 0 ], union_find.parent)
        self.assertEqual([ 0, 0, 0 ], union_find.rank)

        union_find.union(2, 1)

        self.assertEqual([ 0, 0, 0 ], union_find.parent)
        self.assertEqual([ 0, 0, 0 ], union_find.rank)

    def test_union_on_three_elements_after_make_set_with_0_and_1(self):
        union_find = UnionFindWithRank(3)

        union_find.make_set(0)
        union_find.make_set(1)
        union_find.make_set(2)

        self.assertEqual([ 0, 1, 2 ], union_find.parent)
        self.assertEqual([ 0, 0, 0 ], union_find.rank)

        union_find.union(0, 1)

        self.assertEqual([ 1, 1, 2 ], union_find.parent)
        self.assertEqual([ 0, 1, 0 ], union_find.rank)

    def test_union_on_three_elements_after_make_set_with_1_and_0(self):
        union_find = UnionFindWithRank(3)

        union_find.make_set(0)
        union_find.make_set(1)
        union_find.make_set(2)

        self.assertEqual([ 0, 1, 2 ], union_find.parent)
        self.assertEqual([ 0, 0, 0 ], union_find.rank)

        union_find.union(1, 0)

        self.assertEqual([ 0, 0, 2 ], union_find.parent)
        self.assertEqual([ 1, 0, 0 ], union_find.rank)

    def test_union_on_three_elements_after_make_set_with_0_and_2(self):
        union_find = UnionFindWithRank(3)

        union_find.make_set(0)
        union_find.make_set(1)
        union_find.make_set(2)

        self.assertEqual([ 0, 1, 2 ], union_find.parent)
        self.assertEqual([ 0, 0, 0 ], union_find.rank)

        union_find.union(0, 2)

        self.assertEqual([ 2, 1, 2 ], union_find.parent)
        self.assertEqual([ 0, 0, 1 ], union_find.rank)

    def test_union_on_three_elements_after_make_set_with_2_and_0(self):
        union_find = UnionFindWithRank(3)

        union_find.make_set(0)
        union_find.make_set(1)
        union_find.make_set(2)

        self.assertEqual([ 0, 1, 2 ], union_find.parent)
        self.assertEqual([ 0, 0, 0 ], union_find.rank)

        union_find.union(2, 0)

        self.assertEqual([ 0, 1, 0 ], union_find.parent)
        self.assertEqual([ 1, 0, 0 ], union_find.rank)

    def test_union_on_three_elements_after_make_set_with_1_and_2(self):
        union_find = UnionFindWithRank(3)

        union_find.make_set(0)
        union_find.make_set(1)
        union_find.make_set(2)

        self.assertEqual([ 0, 1, 2 ], union_find.parent)
        self.assertEqual([ 0, 0, 0 ], union_find.rank)

        union_find.union(1, 2)

        self.assertEqual([ 0, 2, 2 ], union_find.parent)
        self.assertEqual([ 0, 0, 1 ], union_find.rank)

    def test_union_on_three_elements_after_make_set_with_2_and_1(self):
        union_find = UnionFindWithRank(3)

        union_find.make_set(0)
        union_find.make_set(1)
        union_find.make_set(2)

        self.assertEqual([ 0, 1, 2 ], union_find.parent)
        self.assertEqual([ 0, 0, 0 ], union_find.rank)

        union_find.union(2, 1)

        self.assertEqual([ 0, 1, 1 ], union_find.parent)
        self.assertEqual([ 0, 1, 0 ], union_find.rank)

    def test_union_on_three_elements_to_make_one_set_on_left(self):
        union_find = UnionFindWithRank(3)

        union_find.make_set(0)
        union_find.make_set(1)
        union_find.make_set(2)

        self.assertEqual([ 0, 1, 2 ], union_find.parent)
        self.assertEqual([ 0, 0, 0 ], union_find.rank)
        self.assertEqual(0, union_find.find(0))
        self.assertEqual(1, union_find.find(1))
        self.assertEqual(2, union_find.find(2))
        self.assertEqual([ 0, 1, 2 ], union_find.parent)
        self.assertEqual([ 0, 0, 0 ], union_find.rank)

        union_find.union(1, 0)

        self.assertEqual([ 0, 0, 2 ], union_find.parent)
        self.assertEqual([ 1, 0, 0 ], union_find.rank)
        self.assertEqual(0, union_find.find(0))
        self.assertEqual(0, union_find.find(1))
        self.assertEqual(2, union_find.find(2))
        self.assertEqual([ 0, 0, 2 ], union_find.parent)
        self.assertEqual([ 1, 0, 0 ], union_find.rank)

        union_find.union(2, 1)

        self.assertEqual([ 0, 0, 0 ], union_find.parent)
        self.assertEqual([ 1, 0, 0 ], union_find.rank)
        self.assertEqual(0, union_find.find(0))
        self.assertEqual(0, union_find.find(1))
        self.assertEqual(0, union_find.find(2))
        self.assertEqual([ 0, 0, 0 ], union_find.parent)
        self.assertEqual([ 1, 0, 0 ], union_find.rank)

    def test_union_on_three_elements_to_make_one_set_in_middle(self):
        union_find = UnionFindWithRank(3)

        union_find.make_set(0)
        union_find.make_set(1)
        union_find.make_set(2)

        self.assertEqual([ 0, 1, 2 ], union_find.parent)
        self.assertEqual([ 0, 0, 0 ], union_find.rank)
        self.assertEqual(0, union_find.find(0))
        self.assertEqual(1, union_find.find(1))
        self.assertEqual(2, union_find.find(2))
        self.assertEqual([ 0, 1, 2 ], union_find.parent)
        self.assertEqual([ 0, 0, 0 ], union_find.rank)

        union_find.union(0, 1)

        self.assertEqual([ 1, 1, 2 ], union_find.parent)
        self.assertEqual([ 0, 1, 0 ], union_find.rank)
        self.assertEqual(1, union_find.find(0))
        self.assertEqual(1, union_find.find(1))
        self.assertEqual(2, union_find.find(2))
        self.assertEqual([ 1, 1, 2 ], union_find.parent)
        self.assertEqual([ 0, 1, 0 ], union_find.rank)

        union_find.union(1, 2)

        self.assertEqual([ 1, 1, 1 ], union_find.parent)
        self.assertEqual([ 0, 1, 0 ], union_find.rank)
        self.assertEqual(1, union_find.find(0))
        self.assertEqual(1, union_find.find(1))
        self.assertEqual(1, union_find.find(2))
        self.assertEqual([ 1, 1, 1 ], union_find.parent)
        self.assertEqual([ 0, 1, 0 ], union_find.rank)

    def test_union_on_three_elements_to_make_one_set_on_right(self):
        union_find = UnionFindWithRank(3)

        union_find.make_set(0)
        union_find.make_set(1)
        union_find.make_set(2)

        self.assertEqual([ 0, 1, 2 ], union_find.parent)
        self.assertEqual([ 0, 0, 0 ], union_find.rank)
        self.assertEqual(0, union_find.find(0))
        self.assertEqual(1, union_find.find(1))
        self.assertEqual(2, union_find.find(2))
        self.assertEqual([ 0, 1, 2 ], union_find.parent)
        self.assertEqual([ 0, 0, 0 ], union_find.rank)

        union_find.union(1, 2)

        self.assertEqual([ 0, 2, 2 ], union_find.parent)
        self.assertEqual([ 0, 0, 1 ], union_find.rank)
        self.assertEqual(0, union_find.find(0))
        self.assertEqual(2, union_find.find(1))
        self.assertEqual(2, union_find.find(2))
        self.assertEqual([ 0, 2, 2 ], union_find.parent)
        self.assertEqual([ 0, 0, 1 ], union_find.rank)

        union_find.union(0, 2)

        self.assertEqual([ 2, 2, 2 ], union_find.parent)
        self.assertEqual([ 0, 0, 1 ], union_find.rank)
        self.assertEqual(2, union_find.find(0))
        self.assertEqual(2, union_find.find(1))
        self.assertEqual(2, union_find.find(2))
        self.assertEqual([ 2, 2, 2 ], union_find.parent)
        self.assertEqual([ 0, 0, 1 ], union_find.rank)

    def test_union_on_seven_elements_to_make_one_set(self):
        union_find = UnionFindWithRank(7)

        union_find.make_set(0)
        union_find.make_set(1)
        union_find.make_set(2)
        union_find.make_set(3)
        union_find.make_set(4)
        union_find.make_set(5)
        union_find.make_set(6)

        self.assertEqual([ 0, 1, 2, 3, 4, 5, 6 ], union_find.parent)
        self.assertEqual([ 0, 0, 0, 0, 0, 0, 0 ], union_find.rank)
        self.assertEqual(0, union_find.find(0))
        self.assertEqual(1, union_find.find(1))
        self.assertEqual(2, union_find.find(2))
        self.assertEqual(3, union_find.find(3))
        self.assertEqual(4, union_find.find(4))
        self.assertEqual(5, union_find.find(5))
        self.assertEqual(6, union_find.find(6))
        self.assertEqual([ 0, 1, 2, 3, 4, 5, 6 ], union_find.parent)
        self.assertEqual([ 0, 0, 0, 0, 0, 0, 0 ], union_find.rank)

        union_find.union(0, 1)

        self.assertEqual([ 1, 1, 2, 3, 4, 5, 6 ], union_find.parent)
        self.assertEqual([ 0, 1, 0, 0, 0, 0, 0 ], union_find.rank)
        self.assertEqual(1, union_find.find(0))
        self.assertEqual(1, union_find.find(1))
        self.assertEqual(2, union_find.find(2))
        self.assertEqual(3, union_find.find(3))
        self.assertEqual(4, union_find.find(4))
        self.assertEqual(5, union_find.find(5))
        self.assertEqual(6, union_find.find(6))
        self.assertEqual([ 1, 1, 2, 3, 4, 5, 6 ], union_find.parent)
        self.assertEqual([ 0, 1, 0, 0, 0, 0, 0 ], union_find.rank)

        union_find.union(2, 3)

        self.assertEqual([ 1, 1, 3, 3, 4, 5, 6 ], union_find.parent)
        self.assertEqual([ 0, 1, 0, 1, 0, 0, 0 ], union_find.rank)
        self.assertEqual(1, union_find.find(0))
        self.assertEqual(1, union_find.find(1))
        self.assertEqual(3, union_find.find(2))
        self.assertEqual(3, union_find.find(3))
        self.assertEqual(4, union_find.find(4))
        self.assertEqual(5, union_find.find(5))
        self.assertEqual(6, union_find.find(6))
        self.assertEqual([ 1, 1, 3, 3, 4, 5, 6 ], union_find.parent)
        self.assertEqual([ 0, 1, 0, 1, 0, 0, 0 ], union_find.rank)

        union_find.union(4, 5)

        self.assertEqual([ 1, 1, 3, 3, 5, 5, 6 ], union_find.parent)
        self.assertEqual([ 0, 1, 0, 1, 0, 1, 0 ], union_find.rank)
        self.assertEqual(1, union_find.find(0))
        self.assertEqual(1, union_find.find(1))
        self.assertEqual(3, union_find.find(2))
        self.assertEqual(3, union_find.find(3))
        self.assertEqual(5, union_find.find(4))
        self.assertEqual(5, union_find.find(5))
        self.assertEqual(6, union_find.find(6))
        self.assertEqual([ 1, 1, 3, 3, 5, 5, 6 ], union_find.parent)
        self.assertEqual([ 0, 1, 0, 1, 0, 1, 0 ], union_find.rank)

        union_find.union(0, 2)

        self.assertEqual([ 1, 3, 3, 3, 5, 5, 6 ], union_find.parent)
        self.assertEqual([ 0, 1, 0, 2, 0, 1, 0 ], union_find.rank)
        self.assertEqual(3, union_find.find(0))
        self.assertEqual(3, union_find.find(1))
        self.assertEqual(3, union_find.find(2))
        self.assertEqual(3, union_find.find(3))
        self.assertEqual(5, union_find.find(4))
        self.assertEqual(5, union_find.find(5))
        self.assertEqual(6, union_find.find(6))
        self.assertEqual([ 1, 3, 3, 3, 5, 5, 6 ], union_find.parent)
        self.assertEqual([ 0, 1, 0, 2, 0, 1, 0 ], union_find.rank)

        union_find.union(5, 6)

        self.assertEqual([ 1, 3, 3, 3, 5, 5, 5 ], union_find.parent)
        self.assertEqual([ 0, 1, 0, 2, 0, 1, 0 ], union_find.rank)
        self.assertEqual(3, union_find.find(0))
        self.assertEqual(3, union_find.find(1))
        self.assertEqual(3, union_find.find(2))
        self.assertEqual(3, union_find.find(3))
        self.assertEqual(5, union_find.find(4))
        self.assertEqual(5, union_find.find(5))
        self.assertEqual(5, union_find.find(6))
        self.assertEqual([ 1, 3, 3, 3, 5, 5, 5 ], union_find.parent)
        self.assertEqual([ 0, 1, 0, 2, 0, 1, 0 ], union_find.rank)

        union_find.union(0, 4)

        self.assertEqual([ 1, 3, 3, 3, 5, 3, 5 ], union_find.parent)
        self.assertEqual([ 0, 1, 0, 2, 0, 1, 0 ], union_find.rank)
        self.assertEqual(3, union_find.find(0))
        self.assertEqual(3, union_find.find(1))
        self.assertEqual(3, union_find.find(2))
        self.assertEqual(3, union_find.find(3))
        self.assertEqual(3, union_find.find(4))
        self.assertEqual(3, union_find.find(5))
        self.assertEqual(3, union_find.find(6))
        self.assertEqual([ 1, 3, 3, 3, 5, 3, 5 ], union_find.parent)
        self.assertEqual([ 0, 1, 0, 2, 0, 1, 0 ], union_find.rank)

class UnionFindWithRankAndCompressionTestCase(unittest.TestCase):

    def test_constructor_with_n_as_negative(self):
        with self.assertRaisesRegex(ValueError, 'n must be > 0.'):
            UnionFindWithRankAndCompression(-1)

    def test_constructor_with_n_as_zero(self):
        with self.assertRaisesRegex(ValueError, 'n must be > 0.'):
            UnionFindWithRankAndCompression(0)

    def test_constructor_with_n_as_one(self):
        n = 1
        union_find = UnionFindWithRankAndCompression(n)

        self.assertEqual(n, len(union_find.parent))
        self.assertEqual([ 0 ], union_find.parent)
        self.assertEqual(n, len(union_find.rank))
        self.assertEqual([ 0 ], union_find.rank)

    def test_constructor_with_n_as_two(self):
        n = 2
        union_find = UnionFindWithRankAndCompression(n)

        self.assertEqual(n, len(union_find.parent))
        self.assertEqual([ 0, 0 ], union_find.parent)
        self.assertEqual(n, len(union_find.rank))
        self.assertEqual([ 0, 0 ], union_find.rank)

    def test_constructor_with_n_as_three(self):
        n = 3
        union_find = UnionFindWithRankAndCompression(n)

        self.assertEqual(n, len(union_find.parent))
        self.assertEqual([ 0, 0, 0 ], union_find.parent)
        self.assertEqual(n, len(union_find.rank))
        self.assertEqual([ 0, 0, 0 ], union_find.rank)

    def test_str_with_one_element(self):
        self.assertEqual('[parent=[0], rank=[0]]',
            str(UnionFindWithRankAndCompression(1)))

    def test_str_with_two_elements(self):
        self.assertEqual('[parent=[0, 0], rank=[0, 0]]',
            str(UnionFindWithRankAndCompression(2)))

    def test_str_with_three_elements(self):
        self.assertEqual('[parent=[0, 0, 0], rank=[0, 0, 0]]',
            str(UnionFindWithRankAndCompression(3)))

    def test_repr_with_one_element(self):
        self.assertEqual('[parent=[0], rank=[0]]',
            repr(UnionFindWithRankAndCompression(1)))

    def test_repr_with_two_elements(self):
        self.assertEqual('[parent=[0, 0], rank=[0, 0]]',
            repr(UnionFindWithRankAndCompression(2)))

    def test_repr_with_three_elements(self):
        self.assertEqual('[parent=[0, 0, 0], rank=[0, 0, 0]]',
            repr(UnionFindWithRankAndCompression(3)))

    def test_make_set_on_one_element_with_negative(self):
        union_find = UnionFindWithRankAndCompression(1)

        with self.assertRaisesRegex(ValueError,
            "x must be within the set's range."):
            union_find.make_set(-1)

    def test_make_set_on_one_element_with_exceeding(self):
        union_find = UnionFindWithRankAndCompression(1)

        with self.assertRaisesRegex(ValueError,
            "x must be within the set's range."):
            union_find.make_set(1)

    def test_make_set_on_two_elements_with_negative(self):
        union_find = UnionFindWithRankAndCompression(2)

        with self.assertRaisesRegex(ValueError,
            "x must be within the set's range."):
            union_find.make_set(-1)

    def test_make_set_on_two_elements_with_exceeding(self):
        union_find = UnionFindWithRankAndCompression(2)

        with self.assertRaisesRegex(ValueError,
            "x must be within the set's range."):
            union_find.make_set(2)

    def test_make_set_on_one_element(self):
        union_find = UnionFindWithRankAndCompression(1)

        union_find.make_set(0)

        self.assertEqual([ 0 ], union_find.parent)
        self.assertEqual([ 0 ], union_find.rank)

    def test_make_set_on_two_elements(self):
        union_find = UnionFindWithRankAndCompression(2)

        union_find.make_set(0)

        self.assertEqual([ 0, 0 ], union_find.parent)

        union_find.make_set(1)

        self.assertEqual([ 0, 1 ], union_find.parent)
        self.assertEqual([ 0, 0 ], union_find.rank)

    def test_make_set_on_three_elements(self):
        union_find = UnionFindWithRankAndCompression(3)

        union_find.make_set(0)

        self.assertEqual([ 0, 0, 0 ], union_find.parent)
        self.assertEqual([ 0, 0, 0 ], union_find.rank)

        union_find.make_set(1)

        self.assertEqual([ 0, 1, 0 ], union_find.parent)
        self.assertEqual([ 0, 0, 0 ], union_find.rank)

        union_find.make_set(2)

        self.assertEqual([ 0, 1, 2 ], union_find.parent)
        self.assertEqual([ 0, 0, 0 ], union_find.rank)

    def test_make_set_on_three_elements_with_repetitions(self):
        union_find = UnionFindWithRankAndCompression(3)

        union_find.make_set(0)

        self.assertEqual([ 0, 0, 0 ], union_find.parent)
        self.assertEqual([ 0, 0, 0 ], union_find.rank)

        union_find.make_set(0)

        self.assertEqual([ 0, 0, 0 ], union_find.parent)
        self.assertEqual([ 0, 0, 0 ], union_find.rank)

        union_find.make_set(1)

        self.assertEqual([ 0, 1, 0 ], union_find.parent)
        self.assertEqual([ 0, 0, 0 ], union_find.rank)

        union_find.make_set(1)

        self.assertEqual([ 0, 1, 0 ], union_find.parent)
        self.assertEqual([ 0, 0, 0 ], union_find.rank)

        union_find.make_set(2)

        self.assertEqual([ 0, 1, 2 ], union_find.parent)
        self.assertEqual([ 0, 0, 0 ], union_find.rank)

        union_find.make_set(2)

        self.assertEqual([ 0, 1, 2 ], union_find.parent)
        self.assertEqual([ 0, 0, 0 ], union_find.rank)

    def test_find_on_one_element_with_negative(self):
        union_find = UnionFindWithRankAndCompression(1)

        with self.assertRaisesRegex(ValueError,
            "x must be within the set's range."):
            union_find.find(-1)

    def test_find_on_one_element_with_exceeding(self):
        union_find = UnionFindWithRankAndCompression(1)

        with self.assertRaisesRegex(ValueError,
            "x must be within the set's range."):
            union_find.find(1)

    def test_find_on_two_elements_with_negative(self):
        union_find = UnionFindWithRankAndCompression(2)

        with self.assertRaisesRegex(ValueError,
            "x must be within the set's range."):
            union_find.find(-1)

    def test_find_on_two_elements_with_exceeding(self):
        union_find = UnionFindWithRankAndCompression(2)

        with self.assertRaisesRegex(ValueError,
            "x must be within the set's range."):
            union_find.find(2)

    def test_find_on_one_element_before_and_after_make_set(self):
        union_find = UnionFindWithRankAndCompression(1)

        self.assertEqual(0, union_find.find(0))

        union_find.make_set(0)

        self.assertEqual(0, union_find.find(0))

    def test_find_on_two_elements_before_and_after_make_set(self):
        union_find = UnionFindWithRankAndCompression(2)

        self.assertEqual(0, union_find.find(0))

        union_find.make_set(0)

        self.assertEqual(0, union_find.find(0))

        self.assertEqual(0, union_find.find(1))

        union_find.make_set(1)

        self.assertEqual(1, union_find.find(1))

    def test_find_on_three_elements_before_and_after_make_set(self):
        union_find = UnionFindWithRankAndCompression(3)

        self.assertEqual(0, union_find.find(0))

        union_find.make_set(0)

        self.assertEqual(0, union_find.find(0))

        self.assertEqual(0, union_find.find(1))

        union_find.make_set(1)

        self.assertEqual(1, union_find.find(1))

        self.assertEqual(0, union_find.find(2))

        union_find.make_set(2)

        self.assertEqual(2, union_find.find(2))

    def test_union_on_one_element_with_negative_x(self):
        union_find = UnionFindWithRankAndCompression(1)

        with self.assertRaisesRegex(ValueError,
            "x must be within the set's range."):
            union_find.union(-1, 0)

    def test_union_on_one_element_with_exceeding_x(self):
        union_find = UnionFindWithRankAndCompression(1)

        with self.assertRaisesRegex(ValueError,
            "x must be within the set's range."):
            union_find.union(1, 0)

    def test_union_on_one_element_with_negative_y(self):
        union_find = UnionFindWithRankAndCompression(1)

        with self.assertRaisesRegex(ValueError,
            "y must be within the set's range."):
            union_find.union(0, -1)

    def test_union_on_one_element_with_exceeding_y(self):
        union_find = UnionFindWithRankAndCompression(1)

        with self.assertRaisesRegex(ValueError,
            "y must be within the set's range."):
            union_find.union(0, 1)

    def test_union_on_two_elements_with_negative_x(self):
        union_find = UnionFindWithRankAndCompression(1)

        with self.assertRaisesRegex(ValueError,
            "x must be within the set's range."):
            union_find.union(-1, 0)

    def test_union_on_two_elements_with_exceeding_x(self):
        union_find = UnionFindWithRankAndCompression(2)

        with self.assertRaisesRegex(ValueError,
            "x must be within the set's range."):
            union_find.union(2, 0)

    def test_union_on_two_elements_with_negative_y(self):
        union_find = UnionFindWithRankAndCompression(1)

        with self.assertRaisesRegex(ValueError,
            "y must be within the set's range."):
            union_find.union(0, -1)

    def test_union_on_two_elements_with_exceeding_y(self):
        union_find = UnionFindWithRankAndCompression(2)

        with self.assertRaisesRegex(ValueError,
            "y must be within the set's range."):
            union_find.union(0, 2)

    def test_union_on_one_element_with_x_and_y_as_same_before_make_set(self):
        union_find = UnionFindWithRankAndCompression(1)

        union_find.union(0, 0)

        self.assertEqual([ 0 ], union_find.parent)
        self.assertEqual([ 0 ], union_find.rank)

    def test_union_on_one_element_with_x_and_y_as_same_after_make_set(self):
        union_find = UnionFindWithRankAndCompression(1)

        union_find.make_set(0)

        self.assertEqual([ 0 ], union_find.parent)
        self.assertEqual([ 0 ], union_find.rank)

        union_find.union(0, 0)

        self.assertEqual([ 0 ], union_find.parent)
        self.assertEqual([ 0 ], union_find.rank)

    def test_union_on_two_element_with_x_and_y_as_same_before_make_set(self):
        union_find = UnionFindWithRankAndCompression(2)

        union_find.union(0, 0)

        self.assertEqual([ 0, 0 ], union_find.parent)
        self.assertEqual([ 0, 0 ], union_find.rank)

    def test_union_on_two_elements_with_x_and_y_as_same_after_make_set(self):
        union_find = UnionFindWithRankAndCompression(2)

        union_find.make_set(0)
        union_find.make_set(1)

        self.assertEqual([ 0, 1 ], union_find.parent)
        self.assertEqual([ 0, 0 ], union_find.rank)

        union_find.union(0, 0)

        self.assertEqual([ 0, 1 ], union_find.parent)
        self.assertEqual([ 0, 0 ], union_find.rank)

        union_find.union(1, 1)

        self.assertEqual([ 0, 1 ], union_find.parent)
        self.assertEqual([ 0, 0 ], union_find.rank)

    def test_union_on_two_element_with_x_and_y_as_diff_before_make_set(self):
        union_find = UnionFindWithRankAndCompression(2)

        union_find.union(0, 1)

        self.assertEqual([ 0, 0 ], union_find.parent)
        self.assertEqual([ 0, 0 ], union_find.rank)

        union_find.union(1, 0)

        self.assertEqual([ 0, 0 ], union_find.parent)
        self.assertEqual([ 0, 0 ], union_find.rank)

    def test_union_on_two_elements_with_x_and_y_as_diff_after_make_set(self):
        union_find = UnionFindWithRankAndCompression(2)

        union_find.make_set(0)
        union_find.make_set(1)

        self.assertEqual([ 0, 1 ], union_find.parent)
        self.assertEqual([ 0, 0 ], union_find.rank)

        union_find.union(0, 1)

        self.assertEqual([ 1, 1 ], union_find.parent)
        self.assertEqual([ 0, 1 ], union_find.rank)

        union_find.make_set(0)
        union_find.make_set(1)

        self.assertEqual([ 0, 1 ], union_find.parent)
        self.assertEqual([ 0, 0 ], union_find.rank)

        union_find.union(1, 0)

        self.assertEqual([ 0, 0 ], union_find.parent)
        self.assertEqual([ 1, 0 ], union_find.rank)

    def test_union_on_three_elements_before_make_set(self):
        union_find = UnionFindWithRankAndCompression(3)

        union_find.union(0, 1)

        self.assertEqual([ 0, 0, 0 ], union_find.parent)
        self.assertEqual([ 0, 0, 0 ], union_find.rank)

        union_find.union(0, 2)

        self.assertEqual([ 0, 0, 0 ], union_find.parent)
        self.assertEqual([ 0, 0, 0 ], union_find.rank)

        union_find.union(1, 0)

        self.assertEqual([ 0, 0, 0 ], union_find.parent)
        self.assertEqual([ 0, 0, 0 ], union_find.rank)

        union_find.union(1, 2)

        self.assertEqual([ 0, 0, 0 ], union_find.parent)
        self.assertEqual([ 0, 0, 0 ], union_find.rank)

        union_find.union(2, 0)

        self.assertEqual([ 0, 0, 0 ], union_find.parent)
        self.assertEqual([ 0, 0, 0 ], union_find.rank)

        union_find.union(2, 1)

        self.assertEqual([ 0, 0, 0 ], union_find.parent)
        self.assertEqual([ 0, 0, 0 ], union_find.rank)

    def test_union_on_three_elements_after_make_set_with_0_and_1(self):
        union_find = UnionFindWithRankAndCompression(3)

        union_find.make_set(0)
        union_find.make_set(1)
        union_find.make_set(2)

        self.assertEqual([ 0, 1, 2 ], union_find.parent)
        self.assertEqual([ 0, 0, 0 ], union_find.rank)

        union_find.union(0, 1)

        self.assertEqual([ 1, 1, 2 ], union_find.parent)
        self.assertEqual([ 0, 1, 0 ], union_find.rank)

    def test_union_on_three_elements_after_make_set_with_1_and_0(self):
        union_find = UnionFindWithRankAndCompression(3)

        union_find.make_set(0)
        union_find.make_set(1)
        union_find.make_set(2)

        self.assertEqual([ 0, 1, 2 ], union_find.parent)
        self.assertEqual([ 0, 0, 0 ], union_find.rank)

        union_find.union(1, 0)

        self.assertEqual([ 0, 0, 2 ], union_find.parent)
        self.assertEqual([ 1, 0, 0 ], union_find.rank)

    def test_union_on_three_elements_after_make_set_with_0_and_2(self):
        union_find = UnionFindWithRankAndCompression(3)

        union_find.make_set(0)
        union_find.make_set(1)
        union_find.make_set(2)

        self.assertEqual([ 0, 1, 2 ], union_find.parent)
        self.assertEqual([ 0, 0, 0 ], union_find.rank)

        union_find.union(0, 2)

        self.assertEqual([ 2, 1, 2 ], union_find.parent)
        self.assertEqual([ 0, 0, 1 ], union_find.rank)

    def test_union_on_three_elements_after_make_set_with_2_and_0(self):
        union_find = UnionFindWithRankAndCompression(3)

        union_find.make_set(0)
        union_find.make_set(1)
        union_find.make_set(2)

        self.assertEqual([ 0, 1, 2 ], union_find.parent)
        self.assertEqual([ 0, 0, 0 ], union_find.rank)

        union_find.union(2, 0)

        self.assertEqual([ 0, 1, 0 ], union_find.parent)
        self.assertEqual([ 1, 0, 0 ], union_find.rank)

    def test_union_on_three_elements_after_make_set_with_1_and_2(self):
        union_find = UnionFindWithRankAndCompression(3)

        union_find.make_set(0)
        union_find.make_set(1)
        union_find.make_set(2)

        self.assertEqual([ 0, 1, 2 ], union_find.parent)
        self.assertEqual([ 0, 0, 0 ], union_find.rank)

        union_find.union(1, 2)

        self.assertEqual([ 0, 2, 2 ], union_find.parent)
        self.assertEqual([ 0, 0, 1 ], union_find.rank)

    def test_union_on_three_elements_after_make_set_with_2_and_1(self):
        union_find = UnionFindWithRankAndCompression(3)

        union_find.make_set(0)
        union_find.make_set(1)
        union_find.make_set(2)

        self.assertEqual([ 0, 1, 2 ], union_find.parent)
        self.assertEqual([ 0, 0, 0 ], union_find.rank)

        union_find.union(2, 1)

        self.assertEqual([ 0, 1, 1 ], union_find.parent)
        self.assertEqual([ 0, 1, 0 ], union_find.rank)

    def test_union_on_three_elements_to_make_one_set_on_left(self):
        union_find = UnionFindWithRankAndCompression(3)

        union_find.make_set(0)
        union_find.make_set(1)
        union_find.make_set(2)

        self.assertEqual([ 0, 1, 2 ], union_find.parent)
        self.assertEqual([ 0, 0, 0 ], union_find.rank)
        self.assertEqual(0, union_find.find(0))
        self.assertEqual(1, union_find.find(1))
        self.assertEqual(2, union_find.find(2))
        self.assertEqual([ 0, 1, 2 ], union_find.parent)
        self.assertEqual([ 0, 0, 0 ], union_find.rank)

        union_find.union(1, 0)

        self.assertEqual([ 0, 0, 2 ], union_find.parent)
        self.assertEqual([ 1, 0, 0 ], union_find.rank)
        self.assertEqual(0, union_find.find(0))
        self.assertEqual(0, union_find.find(1))
        self.assertEqual(2, union_find.find(2))
        self.assertEqual([ 0, 0, 2 ], union_find.parent)
        self.assertEqual([ 1, 0, 0 ], union_find.rank)

        union_find.union(2, 1)

        self.assertEqual([ 0, 0, 0 ], union_find.parent)
        self.assertEqual([ 1, 0, 0 ], union_find.rank)
        self.assertEqual(0, union_find.find(0))
        self.assertEqual(0, union_find.find(1))
        self.assertEqual(0, union_find.find(2))
        self.assertEqual([ 0, 0, 0 ], union_find.parent)
        self.assertEqual([ 1, 0, 0 ], union_find.rank)

    def test_union_on_three_elements_to_make_one_set_in_middle(self):
        union_find = UnionFindWithRankAndCompression(3)

        union_find.make_set(0)
        union_find.make_set(1)
        union_find.make_set(2)

        self.assertEqual([ 0, 1, 2 ], union_find.parent)
        self.assertEqual([ 0, 0, 0 ], union_find.rank)
        self.assertEqual(0, union_find.find(0))
        self.assertEqual(1, union_find.find(1))
        self.assertEqual(2, union_find.find(2))
        self.assertEqual([ 0, 1, 2 ], union_find.parent)
        self.assertEqual([ 0, 0, 0 ], union_find.rank)

        union_find.union(0, 1)

        self.assertEqual([ 1, 1, 2 ], union_find.parent)
        self.assertEqual([ 0, 1, 0 ], union_find.rank)
        self.assertEqual(1, union_find.find(0))
        self.assertEqual(1, union_find.find(1))
        self.assertEqual(2, union_find.find(2))
        self.assertEqual([ 1, 1, 2 ], union_find.parent)
        self.assertEqual([ 0, 1, 0 ], union_find.rank)

        union_find.union(1, 2)

        self.assertEqual([ 1, 1, 1 ], union_find.parent)
        self.assertEqual([ 0, 1, 0 ], union_find.rank)
        self.assertEqual(1, union_find.find(0))
        self.assertEqual(1, union_find.find(1))
        self.assertEqual(1, union_find.find(2))
        self.assertEqual([ 1, 1, 1 ], union_find.parent)
        self.assertEqual([ 0, 1, 0 ], union_find.rank)

    def test_union_on_three_elements_to_make_one_set_on_right(self):
        union_find = UnionFindWithRankAndCompression(3)

        union_find.make_set(0)
        union_find.make_set(1)
        union_find.make_set(2)

        self.assertEqual([ 0, 1, 2 ], union_find.parent)
        self.assertEqual([ 0, 0, 0 ], union_find.rank)
        self.assertEqual(0, union_find.find(0))
        self.assertEqual(1, union_find.find(1))
        self.assertEqual(2, union_find.find(2))
        self.assertEqual([ 0, 1, 2 ], union_find.parent)
        self.assertEqual([ 0, 0, 0 ], union_find.rank)

        union_find.union(1, 2)

        self.assertEqual([ 0, 2, 2 ], union_find.parent)
        self.assertEqual([ 0, 0, 1 ], union_find.rank)
        self.assertEqual(0, union_find.find(0))
        self.assertEqual(2, union_find.find(1))
        self.assertEqual(2, union_find.find(2))
        self.assertEqual([ 0, 2, 2 ], union_find.parent)
        self.assertEqual([ 0, 0, 1 ], union_find.rank)

        union_find.union(0, 2)

        self.assertEqual([ 2, 2, 2 ], union_find.parent)
        self.assertEqual([ 0, 0, 1 ], union_find.rank)
        self.assertEqual(2, union_find.find(0))
        self.assertEqual(2, union_find.find(1))
        self.assertEqual(2, union_find.find(2))
        self.assertEqual([ 2, 2, 2 ], union_find.parent)
        self.assertEqual([ 0, 0, 1 ], union_find.rank)

    def test_path_compression_on_seven_elements_to_make_one_set(self):
        union_find = UnionFindWithRankAndCompression(7)

        union_find.make_set(0)
        union_find.make_set(1)
        union_find.make_set(2)
        union_find.make_set(3)
        union_find.make_set(4)
        union_find.make_set(5)
        union_find.make_set(6)

        self.assertEqual([ 0, 1, 2, 3, 4, 5, 6 ], union_find.parent)
        self.assertEqual([ 0, 0, 0, 0, 0, 0, 0 ], union_find.rank)
        self.assertEqual(0, union_find.find(0))
        self.assertEqual(1, union_find.find(1))
        self.assertEqual(2, union_find.find(2))
        self.assertEqual(3, union_find.find(3))
        self.assertEqual(4, union_find.find(4))
        self.assertEqual(5, union_find.find(5))
        self.assertEqual(6, union_find.find(6))
        self.assertEqual([ 0, 1, 2, 3, 4, 5, 6 ], union_find.parent)
        self.assertEqual([ 0, 0, 0, 0, 0, 0, 0 ], union_find.rank)

        union_find.union(0, 1)

        self.assertEqual([ 1, 1, 2, 3, 4, 5, 6 ], union_find.parent)
        self.assertEqual([ 0, 1, 0, 0, 0, 0, 0 ], union_find.rank)
        self.assertEqual(1, union_find.find(0))
        self.assertEqual(1, union_find.find(1))
        self.assertEqual(2, union_find.find(2))
        self.assertEqual(3, union_find.find(3))
        self.assertEqual(4, union_find.find(4))
        self.assertEqual(5, union_find.find(5))
        self.assertEqual(6, union_find.find(6))
        self.assertEqual([ 1, 1, 2, 3, 4, 5, 6 ], union_find.parent)
        self.assertEqual([ 0, 1, 0, 0, 0, 0, 0 ], union_find.rank)

        union_find.union(2, 3)

        self.assertEqual([ 1, 1, 3, 3, 4, 5, 6 ], union_find.parent)
        self.assertEqual([ 0, 1, 0, 1, 0, 0, 0 ], union_find.rank)
        self.assertEqual(1, union_find.find(0))
        self.assertEqual(1, union_find.find(1))
        self.assertEqual(3, union_find.find(2))
        self.assertEqual(3, union_find.find(3))
        self.assertEqual(4, union_find.find(4))
        self.assertEqual(5, union_find.find(5))
        self.assertEqual(6, union_find.find(6))
        self.assertEqual([ 1, 1, 3, 3, 4, 5, 6 ], union_find.parent)
        self.assertEqual([ 0, 1, 0, 1, 0, 0, 0 ], union_find.rank)

        union_find.union(4, 5)

        self.assertEqual([ 1, 1, 3, 3, 5, 5, 6 ], union_find.parent)
        self.assertEqual([ 0, 1, 0, 1, 0, 1, 0 ], union_find.rank)
        self.assertEqual(1, union_find.find(0))
        self.assertEqual(1, union_find.find(1))
        self.assertEqual(3, union_find.find(2))
        self.assertEqual(3, union_find.find(3))
        self.assertEqual(5, union_find.find(4))
        self.assertEqual(5, union_find.find(5))
        self.assertEqual(6, union_find.find(6))
        self.assertEqual([ 1, 1, 3, 3, 5, 5, 6 ], union_find.parent)
        self.assertEqual([ 0, 1, 0, 1, 0, 1, 0 ], union_find.rank)

        union_find.union(0, 2)

        self.assertEqual([ 1, 3, 3, 3, 5, 5, 6 ], union_find.parent)
        self.assertEqual([ 0, 1, 0, 2, 0, 1, 0 ], union_find.rank)
        self.assertEqual(3, union_find.find(0))
        self.assertEqual(3, union_find.find(1))
        self.assertEqual(3, union_find.find(2))
        self.assertEqual(3, union_find.find(3))
        self.assertEqual(5, union_find.find(4))
        self.assertEqual(5, union_find.find(5))
        self.assertEqual(6, union_find.find(6))
        self.assertEqual([ 3, 3, 3, 3, 5, 5, 6 ], union_find.parent)
        self.assertEqual([ 0, 1, 0, 2, 0, 1, 0 ], union_find.rank)

        union_find.union(5, 6)

        self.assertEqual([ 3, 3, 3, 3, 5, 5, 5 ], union_find.parent)
        self.assertEqual([ 0, 1, 0, 2, 0, 1, 0 ], union_find.rank)
        self.assertEqual(3, union_find.find(0))
        self.assertEqual(3, union_find.find(1))
        self.assertEqual(3, union_find.find(2))
        self.assertEqual(3, union_find.find(3))
        self.assertEqual(5, union_find.find(4))
        self.assertEqual(5, union_find.find(5))
        self.assertEqual(5, union_find.find(6))
        self.assertEqual([ 3, 3, 3, 3, 5, 5, 5 ], union_find.parent)
        self.assertEqual([ 0, 1, 0, 2, 0, 1, 0 ], union_find.rank)

        union_find.union(0, 4)

        self.assertEqual([ 3, 3, 3, 3, 5, 3, 5 ], union_find.parent)
        self.assertEqual([ 0, 1, 0, 2, 0, 1, 0 ], union_find.rank)
        self.assertEqual(3, union_find.find(0))
        self.assertEqual(3, union_find.find(1))
        self.assertEqual(3, union_find.find(2))
        self.assertEqual(3, union_find.find(3))
        self.assertEqual(3, union_find.find(4))
        self.assertEqual(3, union_find.find(5))
        self.assertEqual(3, union_find.find(6))
        self.assertEqual([ 3, 3, 3, 3, 3, 3, 3 ], union_find.parent)
        self.assertEqual([ 0, 1, 0, 2, 0, 1, 0 ], union_find.rank)

if __name__ == '__main__':
    class_names = \
    [
        UnionFindWithSmallestTestCase,
        UnionFindWithRankTestCase,
        UnionFindWithRankAndCompressionTestCase,
    ]

    suite = unittest.TestSuite()

    for c in class_names:
        suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(c))

    unittest.TextTestRunner().run(suite)
