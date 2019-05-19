#!/usr/bin/python3

import unittest

from dynamic_array import DynamicArray

class DynamicArrayTestCase(unittest.TestCase):

    def setUp(self):
        self.array = DynamicArray()

    def tearDown(self):
        pass

    def test_constructor(self):
        self.assertEqual(0, self.array.size)

    def test_str_on_empty_array(self):
        self.assertEqual(str([ None, None ]), str(self.array))

    def test_str_on_one_element_array(self):
        element = 1

        self.array.push_back(element)

        self.assertEqual(str([ element, None ]), str(self.array))

    def test_str_on_two_element_array(self):
        element1 = 1
        element2 = 2

        self.array.push_back(element1)
        self.array.push_back(element2)

        self.assertEqual(str([ element1, element2 ]),
            str(self.array))

    def test_str_on_three_element_array(self):
        element1 = 1
        element2 = 2
        element3 = 3

        self.array.push_back(element1)
        self.array.push_back(element2)
        self.array.push_back(element3)

        self.assertEqual(str([ element1, element2, element3, None ]),
            str(self.array))

    def test_repr_on_empty_array(self):
        self.assertEqual('[size=0, capacity=2, array=[None, None]]',
            repr(self.array))

    def test_repr_on_one_element_array(self):
        self.array.push_back(1)

        self.assertEqual('[size=1, capacity=2, array=[1, None]]',
            repr(self.array))

    def test_repr_on_two_element_array(self):
        self.array.push_back(1)
        self.array.push_back(2)

        self.assertEqual('[size=2, capacity=2, array=[1, 2]]',
            repr(self.array))

    def test_repr_on_three_element_array(self):
        self.array.push_back(1)
        self.array.push_back(2)
        self.array.push_back(3)

        self.assertEqual('[size=3, capacity=4, array=[1, 2, 3, None]]',
            repr(self.array))

    def test_get_on_empty_array_with_negative(self):
        with self.assertRaisesRegex(IndexError, ''):
            self.array.get(-1)

    def test_get_on_empty_array_with_zero(self):
        with self.assertRaisesRegex(IndexError, ''):
            self.array.get(0)

    def test_get_on_empty_array_with_positive(self):
        with self.assertRaisesRegex(IndexError, ''):
            self.array.get(1)

    def test_get_on_one_element_array_with_preceding(self):
        self.array.push_back(1)

        with self.assertRaisesRegex(IndexError, ''):
            self.array.get(-1)

    def test_get_on_one_element_array(self):
        element = 1

        self.array.push_back(element)

        self.assertEqual(element, self.array.get(0))

    def test_get_on_one_element_array_with_exceeding(self):
        self.array.push_back(1)

        with self.assertRaisesRegex(IndexError, ''):
            self.array.get(1)

    def test_get_on_two_element_array_with_preceding(self):
        self.array.push_back(1)
        self.array.push_back(2)

        with self.assertRaisesRegex(IndexError, ''):
            self.array.get(-1)

    def test_get_on_two_element_array(self):
        element1 = 1
        element2 = 2

        self.array.push_back(element1)
        self.array.push_back(element2)

        self.assertEqual(element1, self.array.get(0))
        self.assertEqual(element2, self.array.get(1))

    def test_get_on_two_element_array_with_exceeding(self):
        self.array.push_back(1)
        self.array.push_back(2)

        with self.assertRaisesRegex(IndexError, ''):
            self.array.get(2)

    def test_set_on_empty_array_with_negative(self):
        with self.assertRaisesRegex(IndexError, ''):
            self.array.set(-1, 'value')

    def test_set_on_empty_array_with_zero(self):
        with self.assertRaisesRegex(IndexError, ''):
            self.array.set(0, 'value')

    def test_set_on_empty_array_with_positive(self):
        with self.assertRaisesRegex(IndexError, ''):
            self.array.set(1, 'value')

    def test_set_on_one_element_array_with_preceding(self):
        self.array.push_back(1)

        with self.assertRaisesRegex(IndexError, ''):
            self.array.set(-1, 'value')

    def test_set_on_one_element_array(self):
        self.array.push_back(1)

        value = 'value'
        self.array.set(0, value)

        self.assertEqual('value', self.array.get(0))

    def test_set_on_one_element_array_with_exceeding(self):
        self.array.push_back(1)

        with self.assertRaisesRegex(IndexError, ''):
            self.array.set(1, 'value')

    def test_set_on_two_element_array_with_preceding(self):
        self.array.push_back(1)
        self.array.push_back(2)

        with self.assertRaisesRegex(IndexError, ''):
            self.array.set(-1, 'value')

    def test_set_on_two_element_array(self):
        self.array.push_back(1)
        self.array.push_back(2)

        value1 = 'value1'
        self.array.set(0, value1)

        self.assertEqual(value1, self.array.get(0))
        self.assertEqual(2, self.array.get(1))

        value2 = 'value2'
        self.array.set(1, value2)

        self.assertEqual(value1, self.array.get(0))
        self.assertEqual(value2, self.array.get(1))

    def test_set_on_two_element_array_with_exceeding(self):
        self.array.push_back(1)
        self.array.push_back(2)

        with self.assertRaisesRegex(IndexError, ''):
            self.array.set(2, 'value')

    def test_push_back(self):
        self.assertEqual('[size=0, capacity=2, array=[None, None]]',
            repr(self.array))

        element1 = 1
        element2 = 2
        element3 = 3

        self.array.push_back(element1)

        self.assertEqual('[size=1, capacity=2, array=[1, None]]',
            repr(self.array))
        self.assertEqual(element1, self.array.get(0))
        self.assertEqual(1, self.array.size)

        self.array.push_back(element2)

        self.assertEqual('[size=2, capacity=2, array=[1, 2]]',
            repr(self.array))
        self.assertEqual(element1, self.array.get(0))
        self.assertEqual(element2, self.array.get(1))
        self.assertEqual(2, self.array.size)

        self.array.push_back(element3)

        self.assertEqual('[size=3, capacity=4, array=[1, 2, 3, None]]',
            repr(self.array))
        self.assertEqual(element1, self.array.get(0))
        self.assertEqual(element2, self.array.get(1))
        self.assertEqual(element3, self.array.get(2))
        self.assertEqual(3, self.array.size)

    def test_remove_on_empty_array_with_preceding(self):
        with self.assertRaisesRegex(IndexError, ''):
            self.array.remove(-1)

    def test_remove_on_empty_array_with_zero(self):
        with self.assertRaisesRegex(IndexError, ''):
            self.array.remove(0)

    def test_remove_on_one_element_array_with_preceding(self):
        self.array.push_back(1)

        with self.assertRaisesRegex(IndexError, ''):
            self.array.remove(-1)

    def test_remove_on_one_element_array_with_exceeding(self):
        self.array.push_back(1)

        with self.assertRaisesRegex(IndexError, ''):
            self.array.remove(1)

    def test_remove_on_two_element_array_with_preceding(self):
        self.array.push_back(1)
        self.array.push_back(2)

        with self.assertRaisesRegex(IndexError, ''):
            self.array.remove(-1)

    def test_remove_on_two_element_array_with_exceeding(self):
        self.array.push_back(1)
        self.array.push_back(2)

        with self.assertRaisesRegex(IndexError, ''):
            self.array.remove(2)

    def test_remove_in_beginning(self):
        element1 = 1
        element2 = 2
        element3 = 3
        self.array.push_back(element1)
        self.array.push_back(element2)
        self.array.push_back(element3)

        self.assertEqual('[size=3, capacity=4, array=[1, 2, 3, None]]',
            repr(self.array))
        self.assertEqual(element1, self.array.get(0))
        self.assertEqual(element2, self.array.get(1))
        self.assertEqual(element3, self.array.get(2))
        self.assertEqual(3, self.array.size)

        result = self.array.remove(0)

        self.assertEqual('[size=2, capacity=4, array=[2, 3, None, None]]',
            repr(self.array))
        self.assertEqual(element2, self.array.get(0))
        self.assertEqual(element3, self.array.get(1))
        self.assertEqual(2, self.array.size)
        self.assertEqual(element1, result)

    def test_remove_in_middle(self):
        element1 = 1
        element2 = 2
        element3 = 3
        self.array.push_back(element1)
        self.array.push_back(element2)
        self.array.push_back(element3)

        self.assertEqual('[size=3, capacity=4, array=[1, 2, 3, None]]',
            repr(self.array))
        self.assertEqual(element1, self.array.get(0))
        self.assertEqual(element2, self.array.get(1))
        self.assertEqual(element3, self.array.get(2))
        self.assertEqual(3, self.array.size)

        result = self.array.remove(1)

        self.assertEqual('[size=2, capacity=4, array=[1, 3, None, None]]',
            repr(self.array))
        self.assertEqual(element1, self.array.get(0))
        self.assertEqual(element3, self.array.get(1))
        self.assertEqual(2, self.array.size)
        self.assertEqual(element2, result)

    def test_remove_in_end(self):
        element1 = 1
        element2 = 2
        element3 = 3
        self.array.push_back(element1)
        self.array.push_back(element2)
        self.array.push_back(element3)

        self.assertEqual('[size=3, capacity=4, array=[1, 2, 3, None]]',
            repr(self.array))
        self.assertEqual(element1, self.array.get(0))
        self.assertEqual(element2, self.array.get(1))
        self.assertEqual(element3, self.array.get(2))
        self.assertEqual(3, self.array.size)

        result = self.array.remove(2)

        self.assertEqual('[size=2, capacity=4, array=[1, 2, None, None]]',
            repr(self.array))
        self.assertEqual(element1, self.array.get(0))
        self.assertEqual(element2, self.array.get(1))
        self.assertEqual(2, self.array.size)
        self.assertEqual(element3, result)

    def test_remove_all(self):
        element1 = 1
        element2 = 2
        element3 = 3
        self.array.push_back(element1)
        self.array.push_back(element2)
        self.array.push_back(element3)

        self.assertEqual('[size=3, capacity=4, array=[1, 2, 3, None]]',
            repr(self.array))
        self.assertEqual(element1, self.array.get(0))
        self.assertEqual(element2, self.array.get(1))
        self.assertEqual(element3, self.array.get(2))
        self.assertEqual(3, self.array.size)

        result = self.array.remove(0)

        self.assertEqual('[size=2, capacity=4, array=[2, 3, None, None]]',
            repr(self.array))
        self.assertEqual(element2, self.array.get(0))
        self.assertEqual(element3, self.array.get(1))
        self.assertEqual(2, self.array.size)
        self.assertEqual(element1, result)

        result = self.array.remove(0)

        self.assertEqual('[size=1, capacity=4, array=[3, None, None, None]]',
            repr(self.array))
        self.assertEqual(element3, self.array.get(0))
        self.assertEqual(1, self.array.size)
        self.assertEqual(element2, result)

        result = self.array.remove(0)

        self.assertEqual('[size=0, capacity=4, array=[None, None, None, None]]',
            repr(self.array))
        self.assertEqual(0, self.array.size)
        self.assertEqual(element3, result)

if __name__ == '__main__':
    unittest.main()
