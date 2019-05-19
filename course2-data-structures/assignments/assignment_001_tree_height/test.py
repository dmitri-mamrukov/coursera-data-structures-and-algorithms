#!/usr/bin/python3

import unittest

from tree_height import TreeHeight

class TreeHeightBinarySearchTestCase(unittest.TestCase):

    def setUp(self):
        self.tree = TreeHeight()

    def tearDown(self):
        pass

    def compare(self, a, b):
        if a < b:
            return -1
        elif a == b:
            return 0
        else:
            return 1

    def test_empty_data(self):
        self.assertEqual(-1, self.tree._binary_search(
            [], 5, self.compare))

    def test_one_element_data_and_missing_key(self):
        self.assertEqual(-1, self.tree._binary_search(
            [ 3 ], 5, self.compare))

    def test_one_element_data_and_present_key(self):
        self.assertEqual(0, self.tree._binary_search(
            [ 5 ], 5, self.compare))

    def test_two_element_data_and_missing_key(self):
        self.assertEqual(-1, self.tree._binary_search(
            [ 1, 2 ], 5, self.compare))

    def test_two_element_data_and_present_key(self):
        self.assertEqual(0, self.tree._binary_search(
            [ 1, 2 ], 1, self.compare))
        self.assertEqual(1, self.tree._binary_search(
            [ 1, 2 ], 2, self.compare))

    def test_three_element_data_and_missing_key(self):
        self.assertEqual(-1, self.tree._binary_search(
            [ 1, 2, 3 ], 5, self.compare))

    def test_three_element_data_and_present_key(self):
        self.assertEqual(0, self.tree._binary_search(
            [ 1, 2, 3 ], 1, self.compare))
        self.assertEqual(1, self.tree._binary_search(
            [ 1, 2, 3 ], 2, self.compare))
        self.assertEqual(2, self.tree._binary_search(
            [ 1, 2, 3 ], 3, self.compare))

    def test_several_element_data_and_missing_key(self):
        self.assertEqual(-1, self.tree._binary_search(
            [ -7, -1, 0, 3, 5, 8, 9 ], 4, self.compare))

    def test_several_element_data_and_present_key(self):
        self.assertEqual(5, self.tree._binary_search(
            [ -7, -1, 0, 3, 5, 8, 9 ], 8, self.compare))

    def test_several_element_data_with_duplicates_and_missing_key(self):
        self.assertEqual(-1, self.tree._binary_search(
            [ -7, -1, 0, 3, 5, 9, 9 ], 4, self.compare))

    def test_several_element_data_with_duplicates_and_present_key(self):
        self.assertEqual(2, self.tree._binary_search(
            [ -7, -1, 0, 3, 5, 9, 9 ], 0, self.compare))

    def test_two_duplicates_and_missing_key_as_less(self):
        self.assertEqual(-1, self.tree._binary_search(
            [ 1, 1 ], 0, self.compare))

    def test_two_duplicates_and_present_key(self):
        self.assertEqual(0, self.tree._binary_search(
            [ 1, 1 ], 1, self.compare))

    def test_two_duplicates_and_missing_key_as_greater(self):
        self.assertEqual(-1, self.tree._binary_search(
            [ 1, 1 ], 2, self.compare))

    def test_three_duplicates_and_missing_key_as_less(self):
        self.assertEqual(-1, self.tree._binary_search(
            [ 1, 1, 1 ], 0, self.compare))

    def test_three_duplicates_and_present_key(self):
        self.assertEqual(0, self.tree._binary_search(
            [ 1, 1, 1 ], 1, self.compare))

    def test_three_duplicates_and_missing_key_as_greater(self):
        self.assertEqual(-1, self.tree._binary_search(
            [ 1, 1, 1 ], 2, self.compare))

    def test_several_and_two_duplicates_and_missing_key_as_less(self):
        self.assertEqual(-1, self.tree._binary_search(
            [ -2, -1, 1, 1 ], 0, self.compare))

    def test_several_and_two_duplicates_and_present_key(self):
        self.assertEqual(2, self.tree._binary_search(
            [ -2, -1, 1, 1 ], 1, self.compare))

    def test_several_and_two_duplicates_and_missing_key_as_greater(self):
        self.assertEqual(-1, self.tree._binary_search(
            [ -2, -1, 1, 1, 1 ], 2, self.compare))

    def test_several_and_three_duplicates_and_missing_key_as_less(self):
        self.assertEqual(-1, self.tree._binary_search(
            [ -2, -1, 1, 1, 1 ], 0, self.compare))

    def test_several_and_three_duplicates_and_present_key(self):
        self.assertEqual(2, self.tree._binary_search(
            [ -2, -1, 1, 1, 1 ], 1, self.compare))

    def test_several_and_three_duplicates_and_missing_key_as_greater(self):
        self.assertEqual(-1, self.tree._binary_search(
            [ -2, -1, 1, 1, 1 ], 2, self.compare))

class CommonTreeHeightComputeHeightTestCase(unittest.TestCase):

    def create_tree(self,):
        self.tree = TreeHeight()

    def init(self, parents):
        self.tree.init(len(parents), parents)

    def test_0_parents(self):
        """
        empty tree
        """
        parents = []
        self.init(parents)
        self.assertEqual(0, self.method_under_test())

    def test_1_parent_as_minus_1(self):
        """
        0
        """
        parents = [ -1 ]
        self.init(parents)
        self.assertEqual(1, self.method_under_test())

    def test_3_parents_as_minus_1_0(self):
        """
        0
         \
          1
        """
        parents = [ -1, 0 ]
        self.init(parents)
        self.assertEqual(2, self.method_under_test())

    def test_3_parents_as_minus_1_0_1(self):
        """
        0
         \
          1
           \
            2
        """
        parents = [ -1, 0, 1 ]
        self.init(parents)
        self.assertEqual(3, self.method_under_test())

    def test_4_parents_as_minus_1_0_1_2(self):
        """
        0
         \
          1
           \
            2
             \
              3
        """
        parents = [ -1, 0, 1, 2 ]
        self.init(parents)
        self.assertEqual(4, self.method_under_test())

    def test_5_parents_as_minus_1_0_1_2_3(self):
        """
        0
         \
          1
           \
            2
             \
              3
               \
                4
        """
        parents = [ -1, 0, 1, 2, 3 ]
        self.init(parents)
        self.assertEqual(5, self.method_under_test())

    def test_6_parents_as_minus_1_0_1_2_3_4(self):
        """
        0
         \
          1
           \
            2
             \
              3
               \
                4
                 \
                  5
        """
        parents = [ -1, 0, 1, 2, 3, 4 ]
        self.init(parents)
        self.assertEqual(6, self.method_under_test())

    def test_2_parents_as_minus_1_1(self):
        """
          0
         /
        1
        """
        parents = [ -1, 0 ]
        self.init(parents)
        self.assertEqual(2, self.method_under_test())

    def test_2_parents_as_1_minus_1(self):
        """
          1
         /
        0
        """
        parents = [ 1, -1 ]
        self.init(parents)
        self.assertEqual(2, self.method_under_test())

    def test_3_parents_as_1_minus_1_1(self):
        """
          1
         / \
        0   2
        """
        parents = [ 1, -1, 1 ]
        self.init(parents)
        self.assertEqual(2, self.method_under_test())

    def test_4_parents_as_1_minus_1_1_0(self):
        """
            1
           / \
          0   2
         /
        3
        """
        parents = [ 1, -1, 1, 0 ]
        self.init(parents)
        self.assertEqual(3, self.method_under_test())

    def test_5_parents_as_1_minus_1_1_0_0(self):
        """
            1
           / \
          0   2
         / \
        3   4
        """
        parents = [ 1, -1, 1, 0, 0 ]
        self.init(parents)
        self.assertEqual(3, self.method_under_test())

    def test_5_parents_as_1_minus_1_1_0_0_2_2(self):
        """
               1
             /  \
            /    \
           0      2
          / \    / \
         /   \  /   \
        3     4 5    6
        """
        parents = [ 1, -1, 1, 0, 0, 2, 2 ]
        self.init(parents)
        self.assertEqual(3, self.method_under_test())

    def test_5_parents_as_4_minus_1_4_1_1(self):
        """
          1
         / \
        3   4
           / \
          0   2
        """
        parents = [ 4, -1, 4, 1, 1 ]
        self.init(parents)
        self.assertEqual(3, self.method_under_test())

    def test_5_parents_as_minus_1_0_4_0_3(self):
        """
          0
         / \
        1   3
            |
            4
            |
            2
        """
        parents = [ -1, 0, 4, 0, 3 ]
        self.init(parents)
        self.assertEqual(4, self.method_under_test())

    def test_5_parents_as_minus_1_0_0_1_2(self):
        """
            0
           / \
          1   2
         /     \
        3       4
        """
        parents = [ -1, 0, 0, 1, 2 ]
        self.init(parents)
        self.assertEqual(3, self.method_under_test())

    def test_7_parents_as_minus_1_0_0_1_2_3_4(self):
        """
              0
             / \
            1   2
           /     \
          3       4
         /         \
        5           6
        """
        parents = [ -1, 0, 0, 1, 2, 3, 4 ]
        self.init(parents)
        self.assertEqual(4, self.method_under_test())

    def test_8_parents_as_minus_1_0_0_1_2_3_4_5(self):
        """
                0
               / \
              1   2
             /     \
            3       4
           /         \
          5           6
         /
        7
        """
        parents = [ -1, 0, 0, 1, 2, 3, 4, 5 ]
        self.init(parents)
        self.assertEqual(5, self.method_under_test())

    def test_9_parents_as_minus_1_0_0_1_2_3_4_5_5(self):
        """
                0
               / \
              1   2
             /     \
            3       4
           /         \
          5           6
         / \
        7   8
        """
        parents = [ -1, 0, 0, 1, 2, 3, 4, 5, 5 ]
        self.init(parents)
        self.assertEqual(5, self.method_under_test())

    def test_10_parents_as_minus_1_0_0_1_2_3_3_4_6_6(self):
        """
              0
             / \
            1   2
           /     \
          3       4
         / \       \
        5   6       7
           / \
          8   9
        """
        parents = [ -1, 0, 0, 1, 2, 3, 3, 4, 6, 6 ]
        self.init(parents)
        self.assertEqual(5, self.method_under_test())

    def test_12_parents_as_minus_1_0_0_1_1_2_3_4_4_5_7_7(self):
        """
              0
             / \
            1   2
           / \   \
          3  4    5
         /  / \    \
        6  7   8    9
          / \
        10  11
        """
        parents = [ -1, 0, 0, 1, 1, 2, 3, 4, 4, 5, 7, 7 ]
        self.init(parents)
        self.assertEqual(5, self.method_under_test())

    def test_12_parents_as_minus_1_0_0_1_1_2_3_4_4_5_7_7_9_12(self):
        """
              0
             / \
            1   2
           / \   \
          3  4    5
         /  / \    \
        6  7   8    9
          / \        \
        10  11       12
                     /
                   13
        """
        parents = [ -1, 0, 0, 1, 1, 2, 3, 4, 4, 5, 7, 7, 9, 12 ]
        self.init(parents)
        self.assertEqual(6, self.method_under_test())

    def test_ternary_tree_of_height_2(self):
        """
           0
         / | \
        1  2  3
        """
        parents = [ -1, 0, 0, 0 ]
        self.init(parents)
        self.assertEqual(2, self.method_under_test())

    def test_ternary_tree_of_height_3_with_deepest_path_on_left(self):
        """
           0
         / | \
        1  2  3
        |
        4
        """
        parents = [ -1, 0, 0, 0, 1 ]
        self.init(parents)
        self.assertEqual(3, self.method_under_test())

    def test_ternary_tree_of_height_3_with_deepest_path_in_middle(self):
        """
           0
         / | \
        1  2  3
           |
           4
        """
        parents = [ -1, 0, 0, 0, 2 ]
        self.init(parents)
        self.assertEqual(3, self.method_under_test())

    def test_ternary_tree_of_height_3_with_deepest_path_on_right(self):
        """
           0
         / | \
        1  2  3
              |
              4
        """
        parents = [ -1, 0, 0, 0, 3 ]
        self.init(parents)
        self.assertEqual(3, self.method_under_test())

    def test_100_parents_as_heavily_branched_tree_of_height_3(self):
        parents = [ 61, 61, 61, 61, 61, 61, 61, 61, 61, 61,
            61, 61, 61, 61, 61, 61, 61, 61, 61, 61,
            61, 61, 61, 61, 61, 61, 61, 61, 61, 61,
            61, 61, 61, 61, 61, 61, 61, 61, 61, 61,
            61, 61, 61, 61, 61, 61, 61, 61, 61, 61,
            61, 98, 61, 61, 61, 61, 61, 61, 61, 61,
            61, -1, 61, 61, 61, 61, 61, 61, 61, 61,
            61, 61, 61, 61, 61, 61, 61, 61, 61, 61,
            61, 61, 61, 61, 61, 61, 61, 61, 61, 61,
            61, 61, 61, 61, 61, 61, 61, 61, 61, 61 ]
        self.init(parents)
        self.assertEqual(3, self.method_under_test())

class SlowTreeHeightComputeHeightTestCase(
    CommonTreeHeightComputeHeightTestCase):

    def setUp(self):
        self.create_tree()
        self.method_under_test = self.tree.compute_height_slow

    def tearDown(self):
        pass

class StillSlowTreeHeightComputeHeightTestCase(
    CommonTreeHeightComputeHeightTestCase):

    def setUp(self):
        self.create_tree()
        self.method_under_test = self.tree.compute_height_still_slow

    def tearDown(self):
        pass

class FastTreeHeightComputeHeightTestCase(
    CommonTreeHeightComputeHeightTestCase):

    def setUp(self):
        self.create_tree()
        self.method_under_test = self.tree.compute_height

    def tearDown(self):
        pass

if __name__ == '__main__':
    class_names = \
    [
        TreeHeightBinarySearchTestCase,
        SlowTreeHeightComputeHeightTestCase,
        StillSlowTreeHeightComputeHeightTestCase,
        FastTreeHeightComputeHeightTestCase,
    ]

    suite = unittest.TestSuite()

    for c in class_names:
        suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(c))

    unittest.TextTestRunner().run(suite)
