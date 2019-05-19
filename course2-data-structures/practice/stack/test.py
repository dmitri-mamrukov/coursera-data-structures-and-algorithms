#!/usr/bin/python3

import unittest

from stack import Stack

class StackTestCase(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()

    def tearDown(self):
        pass

    def test_empty(self):
        self.assertTrue(self.stack.empty())

    def test_size_on_empty_stack(self):
        self.assertEqual(0, self.stack.size())

    def test_top_on_empty_stack(self):
        with self.assertRaisesRegex(Exception, 'The stack is empty.'):
            self.stack.top()

    def test_push_one_element(self):
        element = 1

        self.stack.push(element)
        self.assertEqual(1, self.stack.size())
        self.assertFalse(self.stack.empty())
        self.assertEqual(element, self.stack.top())

    def test_push_two_elements(self):
        element1 = 1
        element2 = 2

        self.stack.push(element1)
        self.assertEqual(1, self.stack.size())
        self.assertFalse(self.stack.empty())
        self.assertEqual(element1, self.stack.top())

        self.stack.push(element2)
        self.assertEqual(2, self.stack.size())
        self.assertFalse(self.stack.empty())
        self.assertEqual(element2, self.stack.top())

    def test_push_three_elements(self):
        element1 = 1
        element2 = 2
        element3 = 3

        self.stack.push(element1)
        self.assertEqual(1, self.stack.size())
        self.assertFalse(self.stack.empty())
        self.assertEqual(element1, self.stack.top())

        self.stack.push(element2)
        self.assertEqual(2, self.stack.size())
        self.assertFalse(self.stack.empty())
        self.assertEqual(element2, self.stack.top())

        self.stack.push(element3)
        self.assertEqual(3, self.stack.size())
        self.assertFalse(self.stack.empty())
        self.assertEqual(element3, self.stack.top())

    def test_pop_on_empty_stack(self):
        with self.assertRaisesRegex(Exception, 'The stack is empty.'):
            self.stack.pop()

    def test_pop_from_one_element_stack(self):
        element = 1

        self.stack.push(element)
        popped_element = self.stack.pop()

        self.assertEqual(0, self.stack.size())
        self.assertTrue(self.stack.empty())
        self.assertEqual(element, popped_element)

    def test_pop_from_two_element_stack(self):
        element1 = 1
        element2 = 2

        self.stack.push(element1)
        self.stack.push(element2)

        popped_elementl = self.stack.pop()

        self.assertEqual(1, self.stack.size())
        self.assertFalse(self.stack.empty())
        self.assertEqual(element2, popped_elementl)
        self.assertEqual(element1, self.stack.top())

        popped_element2 = self.stack.pop()

        self.assertEqual(0, self.stack.size())
        self.assertTrue(self.stack.empty())
        self.assertEqual(element1, popped_element2)

    def test_pop_from_three_element_stack(self):
        element1 = 1
        element2 = 2
        element3 = 3

        self.stack.push(element1)
        self.stack.push(element2)
        self.stack.push(element3)

        poppedielementl = self.stack.pop()

        self.assertEqual(2, self.stack.size())
        self.assertFalse(self.stack.empty())
        self.assertEqual(element3, poppedielementl)
        self.assertEqual(element2, self.stack.top())

        poppedielement2 = self.stack.pop()

        self.assertEqual(1, self.stack.size())
        self.assertFalse(self.stack.empty())
        self.assertEqual(element2, poppedielement2)
        self.assertEqual(element1, self.stack.top())

        poppedielement3 = self.stack.pop()

        self.assertEqual(0, self.stack.size())
        self.assertTrue(self.stack.empty())
        self.assertEqual(element1, poppedielement3)

    def test_str_on_empty_stack(self):
        self.assertEqual(str([]), str(self.stack))

    def test_str_on_one_element_stack(self):
        element = 1

        self.stack.push(element)

        self.assertEqual(str([ element ]), str(self.stack))

    def test_str_on_three_element_stack(self):
        element1 = 1
        element2 = 2
        element3 = 3

        self.stack.push(element1)
        self.stack.push(element2)
        self.stack.push(element3)

        self.assertEqual(str([ element1, element2, element3 ]),
            str(self.stack))

    def test_repr_on_empty_stack(self):
        self.assertEqual(str([]), repr(self.stack))

    def test_repr_on_one_element_stack(self):
        element = 1

        self.stack.push(element)

        self.assertEqual(str([ element ]), repr(self.stack))

    def test_repr_on_three_element_stack(self):
        element1 = 1
        element2 = 2
        element3 = 3

        self.stack.push(element1)
        self.stack.push(element2)
        self.stack.push(element3)

        self.assertEqual(str([ element1, element2, element3 ]),
            repr(self.stack))

if __name__ == '__main__':
    unittest.main()
