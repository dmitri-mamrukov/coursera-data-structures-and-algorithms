#!/usr/bin/python3

import unittest

import phone_book

class QueryTestCase(unittest.TestCase):

    def test_constructor_with_add_non_number_name(self):
        with self.assertRaisesRegex(ValueError,
            "invalid literal for int\(\) with base 10: 'n'"):
            phone_book.Query([ 'add', 'n', 'x' ])

    def test_constructor_with_add_number_name(self):
        query = phone_book.Query([ 'add', '123', 'x' ])

        self.assertEqual('add', query.type)
        self.assertEqual(123, query.number)
        self.assertEqual('x', query.name)

    def test_constructor_with_del_non_number(self):
        with self.assertRaisesRegex(ValueError,
            "invalid literal for int\(\) with base 10: 'n'"):
            phone_book.Query([ 'del', 'n' ])

    def test_constructor_with_del_number(self):
        query = phone_book.Query([ 'del', '123' ])

        self.assertEqual('del', query.type)
        self.assertEqual(123, query.number)
        self.assertFalse(hasattr(query, 'name'))

    def test_constructor_with_find_non_number(self):
        with self.assertRaisesRegex(ValueError,
            "invalid literal for int\(\) with base 10: 'n'"):
            phone_book.Query([ 'find', 'n' ])

    def test_constructor_with_find_number(self):
        query = phone_book.Query([ 'find', '123' ])

        self.assertEqual('find', query.type)
        self.assertEqual(123, query.number)
        self.assertFalse(hasattr(query, 'name'))

class PhoneBookTestCase(unittest.TestCase):

    def setUp(self):
        self.phone_book = phone_book.PhoneBook()

    def teadDown(self):
        pass

    def test_constructor(self):
        self.assertEqual(0, len(self.phone_book.contacts))

    def test_add_query_on_empty_book(self):
        queries = \
        [
            phone_book.Query('add 911 police'.split()),
        ]
        expected_result = []

        result = self.phone_book.process_queries(queries)

        self.assertEqual(expected_result, result)
        self.assertEqual(1, len(self.phone_book.contacts))
        self.assertEqual('police', self.phone_book.contacts[911])

    def test_find_query_on_empty_book(self):
        queries = \
        [
            phone_book.Query('find 911'.split()),
        ]
        expected_result = [ 'not found' ]

        result = self.phone_book.process_queries(queries)

        self.assertEqual(expected_result, result)
        self.assertEqual(0, len(self.phone_book.contacts))

    def test_del_query_on_empty_book(self):
        queries = \
        [
            phone_book.Query('del 911'.split()),
        ]

        result = self.phone_book.process_queries(queries)

        self.assertEqual([], result)
        self.assertEqual(0, len(self.phone_book.contacts))

    def test_add_two_diff_queries(self):
        queries = \
        [
            phone_book.Query('add 911 police'.split()),
            phone_book.Query('add 711 relay'.split()),
        ]
        expected_result = []

        result = self.phone_book.process_queries(queries)

        self.assertEqual(expected_result, result)
        self.assertEqual(2, len(self.phone_book.contacts))
        self.assertEqual('police', self.phone_book.contacts[911])
        self.assertEqual('relay', self.phone_book.contacts[711])

    def test_add_two_same_queries(self):
        queries = \
        [
            phone_book.Query('add 911 police'.split()),
            phone_book.Query('add 911 police'.split()),
        ]
        expected_result = []

        result = self.phone_book.process_queries(queries)

        self.assertEqual(expected_result, result)
        self.assertEqual(1, len(self.phone_book.contacts))
        self.assertEqual('police', self.phone_book.contacts[911])

    def test_add_two_same_number_queries(self):
        queries = \
        [
            phone_book.Query('add 911 police'.split()),
            phone_book.Query('add 911 fire'.split()),
        ]
        expected_result = []

        result = self.phone_book.process_queries(queries)

        self.assertEqual(expected_result, result)
        self.assertEqual(1, len(self.phone_book.contacts))
        self.assertEqual('fire', self.phone_book.contacts[911])

    def test_add_and_find_queries(self):
        queries = \
        [
            phone_book.Query('add 911 police'.split()),
            phone_book.Query('find 911'.split()),
        ]
        expected_result = [ 'police' ]

        result = self.phone_book.process_queries(queries)

        self.assertEqual(expected_result, result)
        self.assertEqual(1, len(self.phone_book.contacts))
        self.assertEqual('police', self.phone_book.contacts[911])

    def test_add_and_del_queries(self):
        queries = \
        [
            phone_book.Query('add 911 police'.split()),
            phone_book.Query('del 911'.split()),
        ]
        expected_result = []

        result = self.phone_book.process_queries(queries)

        self.assertEqual(expected_result, result)
        self.assertEqual(0, len(self.phone_book.contacts))

    def test_eight_queries(self):
        queries = \
        [
            phone_book.Query('find 3839442'.split()),
            phone_book.Query('add 123456 me'.split()),
            phone_book.Query('add 0 granny'.split()),
            phone_book.Query('find 0'.split()),
            phone_book.Query('find 123456'.split()),
            phone_book.Query('del 0'.split()),
            phone_book.Query('del 0'.split()),
            phone_book.Query('find 0'.split())
        ]
        expected_result = \
        [
            'not found',
            'granny',
            'me',
            'not found'
        ]

        result = self.phone_book.process_queries(queries)

        self.assertEqual(expected_result, result)
        self.assertEqual(1, len(self.phone_book.contacts))
        self.assertEqual('me', self.phone_book.contacts[123456])

    def test_twelve_queries(self):
        queries = \
        [
            phone_book.Query('add 911 police'.split()),
            phone_book.Query('add 76213 Mom'.split()),
            phone_book.Query('add 17239 Bob'.split()),
            phone_book.Query('find 76213'.split()),
            phone_book.Query('find 910'.split()),
            phone_book.Query('find 911'.split()),
            phone_book.Query('del 910'.split()),
            phone_book.Query('del 911'.split()),
            phone_book.Query('find 911'.split()),
            phone_book.Query('find 76213'.split()),
            phone_book.Query('add 76213 daddy'.split()),
            phone_book.Query('find 76213'.split())
        ]
        expected_result = \
        [
            'Mom',
            'not found',
            'police',
            'not found',
            'Mom',
            'daddy'
        ]

        result = self.phone_book.process_queries(queries)

        self.assertEqual(expected_result, result)
        self.assertEqual(2, len(self.phone_book.contacts))
        self.assertEqual('Bob', self.phone_book.contacts[17239])
        self.assertEqual('daddy', self.phone_book.contacts[76213])

if __name__ == '__main__':
    unittest.main()
