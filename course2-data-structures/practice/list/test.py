#!/usr/bin/python3

import unittest

from singly_linked_list import Sing1yLinkedListNode, Sing1yLinkedList

class Sing1yLinkedListNodeTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_constructor_with_key(self):
        key = 'key'
        node = Sing1yLinkedListNode(key)

        self.assertEqual(key, node.key)
        self.assertEqual(None, node.next)

    def test_constructor_with_key_and_next(self):
        key1 = 'key1'
        node1 = Sing1yLinkedListNode(key1)
        key2 = 'key2'
        node2 = Sing1yLinkedListNode(key2, node1)

        self.assertEqual(key2, node2.key)
        self.assertEqual(node1, node2.next)

        self.assertEqual(key1, node1.key)
        self.assertEqual(None, node1.next)

    def test_str_on_node_with_next_as_none(self):
        key = 'test-key'
        node = Sing1yLinkedListNode(key)

        self.assertEqual(key, str(node))

    def test_str_on_node_with_next_as_node(self):
        key1 = 'key1'
        node1 = Sing1yLinkedListNode(key1)
        key2 = 'key2'
        node2 = Sing1yLinkedListNode(key2, node1)

        self.assertEqual(key1, str(node1))
        self.assertEqual(key2, str(node2))

    def test_repr_on_node_with_next_as_none(self):
        key = 'test-key'
        node = Sing1yLinkedListNode(key)

        self.assertEqual('[key=test-key, next=None]', repr(node))

    def test_repr_on_node_with_next_as_node(self):
        key1 = 'key1'
        node1 = Sing1yLinkedListNode(key1)
        key2 = 'key2'
        node2 = Sing1yLinkedListNode(key2, node1)

        self.assertEqual('[key=key1, next=None]', repr(node1))
        self.assertEqual('[key=key2, next=key1]', repr(node2))

class Sing1yLinkedListTestCase(unittest.TestCase):

    def setUp(self):
        self.list = Sing1yLinkedList()
        pass

    def tearDown(self):
        pass

    def test_constructor(self):
        self.assertEqual(0, self.list.size)
        self.assertEqual(None, self.list.top_front)
        self.assertEqual(None, self.list.top_back)

    def test_empty_on_zero_element_list(self):
        self.assertTrue(self.list.empty())

    def test_empty_on_one_element_list(self):
        self.list.push_front('key')

        self.assertFalse(self.list.empty())

    def test_push_front_once(self):
        key = 'key'
        node = self.list.push_front(key)

        self.assertFalse(self.list.empty())
        self.assertEqual(1, self.list.size)
        self.assertEqual(key, node.key)
        self.assertEqual(None, node.next)
        self.assertEqual(node, self.list.top_front)
        self.assertEqual(node, self.list.top_back)

    def test_push_front_twice(self):
        key1 = 'key1'
        node1 = self.list.push_front(key1)

        self.assertFalse(self.list.empty())
        self.assertEqual(1, self.list.size)
        self.assertEqual(key1, node1.key)
        self.assertEqual(None, node1.next)
        self.assertEqual(node1, self.list.top_front)
        self.assertEqual(node1, self.list.top_back)

        key2 = 'key2'
        node2 = self.list.push_front(key2)

        self.assertFalse(self.list.empty())
        self.assertEqual(2, self.list.size)
        self.assertEqual(key2, node2.key)
        self.assertEqual(node1, node2.next)
        self.assertEqual(key1, node1.key)
        self.assertEqual(None, node1.next)
        self.assertEqual(node2, self.list.top_front)
        self.assertEqual(node1, self.list.top_back)

    def test_pop_front_on_empty_list(self):
        with self.assertRaisesRegex(Exception, 'The list is empty.'):
            self.list.pop_front()

    def test_pop_front_on_one_element_list(self):
        node = self.list.push_front('key')

        popped_node = self.list.pop_front()

        self.assertEqual(node, popped_node)
        self.assertTrue(self.list.empty())
        self.assertEqual(None, self.list.top_front)
        self.assertEqual(None, self.list.top_back)

    def test_pop_front_on_two_element_list(self):
        node1 = self.list.push_front('key1')
        node2 = self.list.push_front('key2')

        popped_node1 = self.list.pop_front()

        self.assertEqual(node2, popped_node1)
        self.assertEqual(1, self.list.size)
        self.assertEqual(node1, self.list.top_front)
        self.assertEqual(node1, self.list.top_back)

        popped_node2 = self.list.pop_front()

        self.assertEqual(node2, popped_node1)
        self.assertTrue(self.list.empty())
        self.assertEqual(None, self.list.top_front)
        self.assertEqual(None, self.list.top_back)

    def test_pop_front_on_three_element_list(self):
        node1 = self.list.push_front('key1')
        node2 = self.list.push_front('key2')
        node3 = self.list.push_front('key3')

        popped_node1 = self.list.pop_front()

        self.assertEqual(node3, popped_node1)
        self.assertEqual(2, self.list.size)
        self.assertEqual(node2, self.list.top_front)
        self.assertEqual(node1, self.list.top_back)

        popped_node2 = self.list.pop_front()

        self.assertEqual(node2, popped_node2)
        self.assertEqual(1, self.list.size)
        self.assertEqual(node1, self.list.top_front)
        self.assertEqual(node1, self.list.top_back)

        popped_node3 = self.list.pop_front()

        self.assertEqual(node1, popped_node3)
        self.assertTrue(self.list.empty())
        self.assertEqual(None, self.list.top_front)
        self.assertEqual(None, self.list.top_back)

    def test_push_back_once(self):
        key = 'key'
        node = self.list.push_back(key)

        self.assertFalse(self.list.empty())
        self.assertEqual(1, self.list.size)
        self.assertEqual(key, node.key)
        self.assertEqual(None, node.next)
        self.assertEqual(node, self.list.top_front)
        self.assertEqual(node, self.list.top_back)

    def test_push_back_twice(self):
        key1 = 'key1'
        node1 = self.list.push_back(key1)

        self.assertFalse(self.list.empty())
        self.assertEqual(1, self.list.size)
        self.assertEqual(key1, node1.key)
        self.assertEqual(None, node1.next)
        self.assertEqual(node1, self.list.top_front)
        self.assertEqual(node1, self.list.top_back)

        key2 = 'key2'
        node2 = self.list.push_back(key2)

        self.assertFalse(self.list.empty())
        self.assertEqual(2, self.list.size)
        self.assertEqual(key2, node2.key)
        self.assertEqual(None, node2.next)
        self.assertEqual(key1, node1.key)
        self.assertEqual(node2, node1.next)
        self.assertEqual(node1, self.list.top_front)
        self.assertEqual(node2, self.list.top_back)

    def test_pop_back_on_empty_list(self):
        with self.assertRaisesRegex(Exception, 'The list is empty.'):
            self.list.pop_back()

    def test_pop_back_on_one_element_list(self):
        node = self.list.push_front('key')

        popped_node = self.list.pop_back()

        self.assertEqual(node, popped_node)
        self.assertTrue(self.list.empty())
        self.assertEqual(None, self.list.top_front)
        self.assertEqual(None, self.list.top_back)

    def test_pop_back_on_two_element_list(self):
        node1 = self.list.push_front('key1')
        node2 = self.list.push_front('key2')

        popped_node1 = self.list.pop_back()

        self.assertEqual(node1, popped_node1)
        self.assertEqual(1, self.list.size)
        self.assertEqual(node2, self.list.top_front)
        self.assertEqual(node2, self.list.top_back)

        popped_node2 = self.list.pop_back()

        self.assertEqual(node2, popped_node2)
        self.assertTrue(self.list.empty())
        self.assertEqual(None, self.list.top_front)
        self.assertEqual(None, self.list.top_back)

    def test_pop_back_on_three_element_list(self):
        node1 = self.list.push_front('key1')
        node2 = self.list.push_front('key2')
        node3 = self.list.push_front('key3')

        popped_node1 = self.list.pop_back()

        self.assertEqual(node1, popped_node1)
        self.assertEqual(2, self.list.size)
        self.assertEqual(node3, self.list.top_front)
        self.assertEqual(node2, self.list.top_back)

        popped_node2 = self.list.pop_back()

        self.assertEqual(node2, popped_node2)
        self.assertEqual(1, self.list.size)
        self.assertEqual(node3, self.list.top_front)
        self.assertEqual(node3, self.list.top_back)

        popped_node3 = self.list.pop_back()

        self.assertEqual(node3, popped_node3)
        self.assertTrue(self.list.empty())
        self.assertEqual(None, self.list.top_front)
        self.assertEqual(None, self.list.top_back)

    def test_add_after_with_node_as_none(self):
        with self.assertRaisesRegex(ValueError,
            'The node cannot be None.'):
            self.list.add_after(None, 'data')

    def test_add_after_on_empty_list(self):
        with self.assertRaisesRegex(ValueError,
            'The node is not in the list.'):
            self.list.add_after(Sing1yLinkedListNode('key'), 'data')

    def test_add_after_on_one_element_node(self):
        key1 = 'key1'
        node1 = self.list.push_back(key1)

        key2 = 'key2'
        node2 = self.list.add_after(node1, key2)

        self.assertEqual(2, self.list.size)
        self.assertEqual(key1, node1.key)
        self.assertEqual(node2, node1.next)
        self.assertEqual(key2, node2.key)
        self.assertEqual(None, node2.next)
        self.assertEqual(node1, self.list.top_front)
        self.assertEqual(node2, self.list.top_back)

    def test_add_after_on_two_element_node(self):
        key1 = 'key1'
        node1 = self.list.push_back(key1)
        key2 = 'key2'
        node2 = self.list.push_back(key2)

        key3 = 'key3'
        node3 = self.list.add_after(node1, key3)

        self.assertEqual(3, self.list.size)
        self.assertEqual(key1, node1.key)
        self.assertEqual(node3, node1.next)
        self.assertEqual(key3, node3.key)
        self.assertEqual(node2, node3.next)
        self.assertEqual(key2, node2.key)
        self.assertEqual(None, node2.next)
        self.assertEqual(node1, self.list.top_front)
        self.assertEqual(node2, self.list.top_back)

    def test_add_after_on_three_element_node(self):
        key1 = 'key1'
        node1 = self.list.push_back(key1)
        key2 = 'key2'
        node2 = self.list.push_back(key2)
        key3 = 'key3'
        node3 = self.list.push_back(key3)

        key4 = 'key4'
        node4 = self.list.add_after(node2, key4)

        self.assertEqual(4, self.list.size)
        self.assertEqual(key1, node1.key)
        self.assertEqual(node2, node1.next)
        self.assertEqual(key2, node2.key)
        self.assertEqual(node4, node2.next)
        self.assertEqual(key4, node4.key)
        self.assertEqual(node3, node4.next)
        self.assertEqual(key3, node3.key)
        self.assertEqual(None, node3.next)
        self.assertEqual(node1, self.list.top_front)
        self.assertEqual(node3, self.list.top_back)

    def test_add_before_with_node_as_none(self):
        with self.assertRaisesRegex(ValueError,
            'The node cannot be None.'):
            self.list.add_before(None, 'data')

    def test_add_before_on_empty_list(self):
        with self.assertRaisesRegex(ValueError,
            'The node is not in the list.'):
            self.list.add_before(Sing1yLinkedListNode('key'), 'data')

    def test_add_before_on_one_element_node(self):
        key1 = 'key1'
        node1 = self.list.push_back(key1)

        key2 = 'key2'
        node2 = self.list.add_before(node1, key2)

        self.assertEqual(2, self.list.size)
        self.assertEqual(key1, node1.key)
        self.assertEqual(None, node1.next)
        self.assertEqual(key2, node2.key)
        self.assertEqual(node1, node2.next)
        self.assertEqual(node2, self.list.top_front)
        self.assertEqual(node1, self.list.top_back)

    def test_add_before_on_two_element_node(self):
        key1 = 'key1'
        node1 = self.list.push_back(key1)
        key2 = 'key2'
        node2 = self.list.push_back(key2)

        key3 = 'key3'
        node3 = self.list.add_before(node2, key3)

        self.assertEqual(3, self.list.size)
        self.assertEqual(key1, node1.key)
        self.assertEqual(node3, node1.next)
        self.assertEqual(key3, node3.key)
        self.assertEqual(node2, node3.next)
        self.assertEqual(key2, node2.key)
        self.assertEqual(None, node2.next)
        self.assertEqual(node1, self.list.top_front)
        self.assertEqual(node2, self.list.top_back)

    def test_add_before_on_three_element_node(self):
        key1 = 'key1'
        node1 = self.list.push_back(key1)
        key2 = 'key2'
        node2 = self.list.push_back(key2)
        key3 = 'key3'
        node3 = self.list.push_back(key3)

        key4 = 'key4'
        node4 = self.list.add_before(node3, key4)

        self.assertEqual(4, self.list.size)
        self.assertEqual(key1, node1.key)
        self.assertEqual(node2, node1.next)
        self.assertEqual(key2, node2.key)
        self.assertEqual(node4, node2.next)
        self.assertEqual(key4, node4.key)
        self.assertEqual(node3, node4.next)
        self.assertEqual(key3, node3.key)
        self.assertEqual(None, node3.next)
        self.assertEqual(node1, self.list.top_front)
        self.assertEqual(node3, self.list.top_back)

    def test_find_on_empty(self):
        self.assertEqual(None, self.list.find('data'))

    def test_find_on_one_element_list_with_missing_key(self):
        node = self.list.push_back('key')

        self.assertEqual(None, self.list.find('data'))

    def test_find_on_one_element_list_with_existing_key(self):
        node = self.list.push_back('key')

        self.assertEqual(node, self.list.find(node.key))

    def test_find_on_two_element_node_with_missing_key(self):
        node1 = self.list.push_back('key1')
        node2 = self.list.push_back('key2')

        self.assertEqual(None, self.list.find('data'))

    def test_find_on_two_element_node_with_existing_key_as_first(self):
        node1 = self.list.push_back('key1')
        node2 = self.list.push_back('key2')

        self.assertEqual(node1, self.list.find(node1.key))

    def test_find_on_two_element_node_with_existing_key_as_second(self):
        node1 = self.list.push_back('key1')
        node2 = self.list.push_back('key2')

        self.assertEqual(node2, self.list.find(node2.key))

    def test_find_on_three_element_node_with_missing_key(self):
        node1 = self.list.push_back('key1')
        node2 = self.list.push_back('key2')
        node3 = self.list.push_back('key3')

        self.assertEqual(None, self.list.find('data'))

    def test_find_on_three_element_node_with_existing_key_as_first(self):
        node1 = self.list.push_back('key1')
        node2 = self.list.push_back('key2')
        node3 = self.list.push_back('key3')

        self.assertEqual(node1, self.list.find(node1.key))

    def test_find_on_three_element_node_with_existing_key_as_second(self):
        node1 = self.list.push_back('key1')
        node2 = self.list.push_back('key2')
        node3 = self.list.push_back('key3')

        self.assertEqual(node2, self.list.find(node2.key))

    def test_find_on_three_element_node_with_existing_key_as_third(self):
        node1 = self.list.push_back('key1')
        node2 = self.list.push_back('key2')
        node3 = self.list.push_back('key3')

        self.assertEqual(node3, self.list.find(node3.key))

    def test_erase_on_empty_list(self):
        with self.assertRaisesRegex(ValueError,
            'The key is not in the list.'):
            self.list.erase('data')

    def test_erase_on_one_element_list_with_missing_key(self):
        node = self.list.push_back('key')

        with self.assertRaisesRegex(ValueError,
            'The key is not in the list.'):
            self.list.erase('data')

    def test_erase_on_one_element_list_with_existing_key(self):
        key = 'key'
        node = self.list.push_back(key)

        erased_node = self.list.erase(key)

        self.assertEqual(node, erased_node)
        self.assertTrue(self.list.empty())
        self.assertEqual(None, self.list.top_front)
        self.assertEqual(None, self.list.top_back)

    def test_erase_on_two_element_node_with_missing_key(self):
        node1 = self.list.push_back('key1')
        node2 = self.list.push_back('key2')

        with self.assertRaisesRegex(ValueError,
            'The key is not in the list.'):
            self.list.erase('data')

    def test_erase_on_two_element_node_with_existing_key_as_first(self):
        node1 = self.list.push_back('key1')
        node2 = self.list.push_back('key2')

        erased_node = self.list.erase(node1.key)

        self.assertEqual(node1, erased_node)
        self.assertEqual(1, self.list.size)
        self.assertEqual(node2, self.list.top_front)
        self.assertEqual(node2, self.list.top_back)

    def test_erase_on_two_element_node_with_existing_key_as_second(self):
        node1 = self.list.push_back('key1')
        node2 = self.list.push_back('key2')

        erased_node = self.list.erase(node2.key)

        self.assertEqual(node2, erased_node)
        self.assertEqual(1, self.list.size)
        self.assertEqual(node1, self.list.top_front)
        self.assertEqual(node1, self.list.top_back)

    def test_erase_on_three_element_node_with_missing_key(self):
        node1 = self.list.push_back('key1')
        node2 = self.list.push_back('key2')
        node3 = self.list.push_back('key3')

        with self.assertRaisesRegex(ValueError,
            'The key is not in the list.'):
            self.list.erase('data')

    def test_erase_on_three_element_node_with_existing_key_as_first(self):
        node1 = self.list.push_back('key1')
        node2 = self.list.push_back('key2')
        node3 = self.list.push_back('key3')

        erased_node = self.list.erase(node1.key)

        self.assertEqual(node1, erased_node)
        self.assertEqual(2, self.list.size)
        self.assertEqual(node2, self.list.top_front)
        self.assertEqual(node3, self.list.top_back)

    def test_erase_on_three_element_node_with_existing_key_as_second(self):
        node1 = self.list.push_back('key1')
        node2 = self.list.push_back('key2')
        node3 = self.list.push_back('key3')

        erased_node = self.list.erase(node3.key)

        self.assertEqual(node3, erased_node)
        self.assertEqual(2, self.list.size)
        self.assertEqual(node1, self.list.top_front)
        self.assertEqual(node2, self.list.top_back)

    def test_erase_on_two_element_list_from_beginning(self):
        node1 = self.list.push_back('key1')
        node2 = self.list.push_back('key2')

        erased_node1 = self.list.erase(node1.key)

        self.assertEqual(node1, erased_node1)
        self.assertEqual(1, self.list.size)
        self.assertEqual(node2, self.list.top_front)
        self.assertEqual(node2, self.list.top_back)

        erased_node2 = self.list.erase(node2.key)

        self.assertEqual(node2, erased_node2)
        self.assertTrue(self.list.empty())
        self.assertEqual(None, self.list.top_front)
        self.assertEqual(None, self.list.top_back)

    def test_erase_on_two_element_list_from_end(self):
        node1 = self.list.push_back('key1')
        node2 = self.list.push_back('key2')

        erased_node1 = self.list.erase(node2.key)

        self.assertEqual(node2, erased_node1)
        self.assertEqual(1, self.list.size)
        self.assertEqual(node1, self.list.top_front)
        self.assertEqual(node1, self.list.top_back)

        erased_node2 = self.list.erase(node1.key)

        self.assertEqual(node1, erased_node2)
        self.assertTrue(self.list.empty())
        self.assertEqual(None, self.list.top_front)
        self.assertEqual(None, self.list.top_back)

    def test_erase_on_three_element_list_from_beginning(self):
        node1 = self.list.push_back('key1')
        node2 = self.list.push_back('key2')
        node3 = self.list.push_back('key3')

        erased_node1 = self.list.erase(node1.key)

        self.assertEqual(node1, erased_node1)
        self.assertEqual(2, self.list.size)
        self.assertEqual(node2, self.list.top_front)
        self.assertEqual(node3, self.list.top_back)

        erased_node2 = self.list.erase(node2.key)

        self.assertEqual(node2, erased_node2)
        self.assertEqual(1, self.list.size)
        self.assertEqual(node3, self.list.top_front)
        self.assertEqual(node3, self.list.top_back)

        erased_node3 = self.list.erase(node3.key)

        self.assertEqual(node3, erased_node3)
        self.assertTrue(self.list.empty())
        self.assertEqual(None, self.list.top_front)
        self.assertEqual(None, self.list.top_back)

    def test_erase_on_three_element_list_from_end(self):
        node1 = self.list.push_back('key1')
        node2 = self.list.push_back('key2')
        node3 = self.list.push_back('key3')

        erased_node1 = self.list.erase(node3.key)

        self.assertEqual(node3, erased_node1)
        self.assertEqual(2, self.list.size)
        self.assertEqual(node1, self.list.top_front)
        self.assertEqual(node2, self.list.top_back)

        erased_node2 = self.list.erase(node2.key)

        self.assertEqual(node2, erased_node2)
        self.assertEqual(1, self.list.size)
        self.assertEqual(node1, self.list.top_front)
        self.assertEqual(node1, self.list.top_back)

        erased_node3 = self.list.erase(node1.key)

        self.assertEqual(node1, erased_node3)
        self.assertTrue(self.list.empty())
        self.assertEqual(None, self.list.top_front)
        self.assertEqual(None, self.list.top_back)

if __name__ == '__main__':
    unittest.main()
