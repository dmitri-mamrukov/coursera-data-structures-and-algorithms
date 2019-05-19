#!/usr/bin/python3

import unittest

from queue import Queue

class QueueTestCase(unittest.TestCase):

    def setUp(self):
        self.queue = Queue()

    def tearDown(self):
        pass

    def test_empty(self):
        self.assertTrue(self.queue.empty())

    def test_size_on_empty_queue(self):
        self.assertEqual(0, self.queue.size())

    def test_enqueue_one_element(self):
        element = 1

        self.queue.enqueue(element)

        self.assertEqual(1, self.queue.size())
        self.assertFalse(self.queue.empty())

    def test_enqueue_two_elements(self):
        element1 = 1
        element2 = 2

        self.queue.enqueue(element1)

        self.assertEqual(1, self.queue.size())
        self.assertFalse(self.queue.empty())

        self.queue.enqueue(element2)

        self.assertEqual(2, self.queue.size())
        self.assertFalse(self.queue.empty())

    def test_enqueue_three_elements(self):
        element1 = 1
        element2 = 2
        element3 = 3

        self.queue.enqueue(element1)

        self.assertEqual(1, self.queue.size())
        self.assertFalse(self.queue.empty())

        self.queue.enqueue(element2)

        self.assertEqual(2, self.queue.size())
        self.assertFalse(self.queue.empty())

        self.queue.enqueue(element3)

        self.assertEqual(3, self.queue.size())
        self.assertFalse(self.queue.empty())

    def test_dequeue_on_empty_queue(self):
        with self.assertRaisesRegex(Exception, 'The queue is empty.'):
            self.queue.dequeue()

    def test_dequeue_from_one_element_queue(self):
        element = 1

        self.queue.enqueue(element)
        dequeued_element = self.queue.dequeue()

        self.assertEqual(0, self.queue.size())
        self.assertTrue(self.queue.empty())
        self.assertEqual(element, dequeued_element)

    def test_dequeue_from_two_element_queue(self):
        element1 = 1
        element2 = 2

        self.queue.enqueue(element1)
        self.queue.enqueue(element2)

        dequeued_element1 = self.queue.dequeue()

        self.assertEqual(1, self.queue.size())
        self.assertFalse(self.queue.empty())
        self.assertEqual(element1, dequeued_element1)

        dequeued_element2 = self.queue.dequeue()

        self.assertEqual(0, self.queue.size())
        self.assertTrue(self.queue.empty())
        self.assertEqual(element2, dequeued_element2)

    def test_dequeue_from_three_element_queue(self):
        element1 = 1
        element2 = 2
        element3 = 3

        self.queue.enqueue(element1)
        self.queue.enqueue(element2)
        self.queue.enqueue(element3)

        dequeued_element1 = self.queue.dequeue()

        self.assertEqual(2, self.queue.size())
        self.assertFalse(self.queue.empty())
        self.assertEqual(element1, dequeued_element1)

        dequeued_element2 = self.queue.dequeue()

        self.assertEqual(1, self.queue.size())
        self.assertFalse(self.queue.empty())
        self.assertEqual(element2, dequeued_element2)

        dequeued_element3 = self.queue.dequeue()

        self.assertEqual(0, self.queue.size())
        self.assertTrue(self.queue.empty())
        self.assertEqual(element3, dequeued_element3)

    def test_str_on_empty_queue(self):
        self.assertEqual(str([]), str(self.queue))

    def test_str_on_one_element_queue(self):
        element = 1

        self.queue.enqueue(element)

        self.assertEqual(str([ element ]), str(self.queue))

    def test_str_on_three_element_queue(self):
        element1 = 1
        element2 = 2
        element3 = 3

        self.queue.enqueue(element1)
        self.queue.enqueue(element2)
        self.queue.enqueue(element3)

        self.assertEqual(str([ element3, element2, element1 ]),
            str(self.queue))

    def test_repr_on_empty_queue(self):
        self.assertEqual(str([]), repr(self.queue))

    def test_repr_on_one_element_queue(self):
        element = 1

        self.queue.enqueue(element)

        self.assertEqual(str([ element ]), repr(self.queue))

    def test_repr_on_three_element_queue(self):
        element1 = 1
        element2 = 2
        element3 = 3

        self.queue.enqueue(element1)
        self.queue.enqueue(element2)
        self.queue.enqueue(element3)

        self.assertEqual(str([ element3, element2, element1 ]),
            repr(self.queue))

if __name__ == '__main__':
    unittest.main()
