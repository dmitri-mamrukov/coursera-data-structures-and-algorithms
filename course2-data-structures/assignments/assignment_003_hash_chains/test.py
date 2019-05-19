#!/usr/bin/python3

import math
import unittest

import hash_chains

class QueryTestCase(unittest.TestCase):

    def test_constructor_with_add_text(self):
        query = hash_chains.Query([ 'add', 'x' ])

        self.assertEqual('add', query.type)
        self.assertEqual('x', query.text)

    def test_constructor_with_del_text(self):
        query = hash_chains.Query([ 'del', 'x' ])

        self.assertEqual('del', query.type)
        self.assertEqual('x', query.text)

    def test_constructor_with_find_text(self):
        query = hash_chains.Query([ 'find', 'x' ])

        self.assertEqual('find', query.type)
        self.assertEqual('x', query.text)

    def test_constructor_with_check_non_number(self):
        with self.assertRaisesRegex(ValueError,
            "invalid literal for int\(\) with base 10: 'n'"):
            hash_chains.Query([ 'check', 'n' ])

    def test_constructor_with_check_index(self):
        query = hash_chains.Query([ 'check', '123' ])

        self.assertEqual('check', query.type)
        self.assertEqual(123, query.index)

class HashUtilTestCase(unittest.TestCase):

    def test_properties(self):
        self.assertEqual(263, hash_chains.HashUtil.MULTIPLIER)
        self.assertEqual(1000000007, hash_chains.HashUtil.PRIME)

    def test_hash_function_with_empty_string(self):
        bucket_count = 5

        text = ''

        self.assertEqual(0,
            hash_chains.HashUtil.hash_function(text, bucket_count))

    def test_hash_function_with_one_char_string_as_a(self):
        bucket_count = 5

        p = hash_chains.HashUtil.PRIME
        m = bucket_count
        text = 'a'
        expected_hash_value = (97 % p) % m

        self.assertEqual(2, expected_hash_value)
        self.assertEqual(expected_hash_value,
            hash_chains.HashUtil.hash_function(text, bucket_count))

    def test_hash_function_with_one_char_string_as_b(self):
        bucket_count = 5

        p = hash_chains.HashUtil.PRIME
        m = bucket_count
        text = 'b'
        expected_hash_value = (98 % p) % m

        self.assertEqual(3, expected_hash_value)
        self.assertEqual(expected_hash_value,
            hash_chains.HashUtil.hash_function(text, bucket_count))

    def test_hash_function_with_one_char_string_as_z(self):
        bucket_count = 5

        p = hash_chains.HashUtil.PRIME
        m = bucket_count
        text = 'z'
        expected_hash_value = (122 % p) % m

        self.assertEqual(2, expected_hash_value)
        self.assertEqual(expected_hash_value,
            hash_chains.HashUtil.hash_function(text, bucket_count))

    def test_hash_function_with_one_char_string_as_ab(self):
        bucket_count = 5

        p = hash_chains.HashUtil.PRIME
        x = hash_chains.HashUtil.MULTIPLIER
        m = bucket_count
        text = 'ab'
        expected_hash_value = (
            (97 +
            (98 * x**1))
            % p % m)

        self.assertEqual(1, expected_hash_value)
        self.assertEqual(expected_hash_value,
            hash_chains.HashUtil.hash_function(text, bucket_count))

    def test_hash_function_with_one_char_string_as_abc(self):
        bucket_count = 5

        p = hash_chains.HashUtil.PRIME
        x = hash_chains.HashUtil.MULTIPLIER
        m = bucket_count
        text = 'abc'
        expected_hash_value = (
            (97 +
            (98 * x**1) +
            (99 * x**2))
            % p % m)

        self.assertEqual(2, expected_hash_value)
        self.assertEqual(expected_hash_value,
            hash_chains.HashUtil.hash_function(text, bucket_count))

    def test_hash_function_with_one_char_string_as_abcx(self):
        bucket_count = 5

        p = hash_chains.HashUtil.PRIME
        x = hash_chains.HashUtil.MULTIPLIER
        m = bucket_count
        text = 'abcx'
        expected_hash_value = (
            (97 +
            (98 * x**1) +
            (99 * x**2) +
            (120 * x**3))
            % p % m)

        self.assertEqual(3, expected_hash_value)
        self.assertEqual(expected_hash_value,
            hash_chains.HashUtil.hash_function(text, bucket_count))

    def test_hash_function_with_one_char_string_as_abcxy(self):
        bucket_count = 5

        p = hash_chains.HashUtil.PRIME
        x = hash_chains.HashUtil.MULTIPLIER
        m = bucket_count
        text = 'abcxy'
        expected_hash_value = (
            (97 +
            (98 * x**1) +
            (99 * x**2) +
            (120 * x**3) +
            (121 * x**4))
            % p % m)

        self.assertEqual(1, expected_hash_value)
        self.assertEqual(expected_hash_value,
            hash_chains.HashUtil.hash_function(text, bucket_count))

    def test_hash_function_with_one_char_string_as_abcxyz(self):
        bucket_count = 5

        p = hash_chains.HashUtil.PRIME
        x = hash_chains.HashUtil.MULTIPLIER
        m = bucket_count
        text = 'abcxyz'
        expected_hash_value = (
            (97 +
            (98 * x**1) +
            (99 * x**2) +
            (120 * x**3) +
            (121 * x**4) +
            (122 * x**5))
            % p % m)

        self.assertEqual(2, expected_hash_value)
        self.assertEqual(expected_hash_value,
            hash_chains.HashUtil.hash_function(text, bucket_count))

class QueryProcessorTestCase(unittest.TestCase):

    def assert_hash_value_of_key(self, key, expected_hash_value, char_values,
            bucket_count):
        value = 0
        for i, v in enumerate(char_values):
            value += v * hash_chains.HashUtil.MULTIPLIER**i
        value = value % hash_chains.HashUtil.PRIME % bucket_count

        self.assertEqual(value, key)
        self.assertEqual(expected_hash_value, key)

    def test_constructor(self):
        bucket_count = 123

        processor = hash_chains.QueryProcessor(bucket_count)

        self.assertEqual(bucket_count, processor.bucket_count)
        self.assertEqual(0, len(processor.table))

    def test_add_query_on_empty_book(self):
        processor = hash_chains.QueryProcessor(5)

        query = hash_chains.Query('add 1'.split())
        key = hash_chains.HashUtil.hash_function(query.text,
            processor.bucket_count)
        self.assert_hash_value_of_key(key, 4, [ 49 ], processor.bucket_count)

        result = processor.process_query(query)

        self.assertEqual(None, result)
        self.assertEqual(1, len(processor.table))
        self.assertEqual([ '1' ], processor.table[key])

    def test_two_same_add_queries(self):
        processor = hash_chains.QueryProcessor(5)

        query = hash_chains.Query('add 1'.split())
        key = hash_chains.HashUtil.hash_function(query.text,
            processor.bucket_count)
        self.assert_hash_value_of_key(key, 4, [ 49 ], processor.bucket_count)

        result1 = processor.process_query(query)

        self.assertEqual(None, result1)
        self.assertEqual(1, len(processor.table))
        self.assertEqual([ '1' ], processor.table[key])

        result2 = processor.process_query(query)

        self.assertEqual(None, result2)
        self.assertEqual(1, len(processor.table))
        self.assertEqual([ '1' ], processor.table[key])

    def test_two_different_add_queries(self):
        processor = hash_chains.QueryProcessor(5)

        query1 = hash_chains.Query('add 1'.split())
        key1 = hash_chains.HashUtil.hash_function(query1.text,
            processor.bucket_count)
        query2 = hash_chains.Query('add 2'.split())
        key2 = hash_chains.HashUtil.hash_function(query2.text,
            processor.bucket_count)
        self.assertNotEqual(key1, key2)
        self.assert_hash_value_of_key(key1, 4, [ 49 ], processor.bucket_count)
        self.assert_hash_value_of_key(key2, 0, [ 50 ], processor.bucket_count)

        result1 = processor.process_query(query1)

        self.assertEqual(None, result1)
        self.assertEqual(1, len(processor.table))
        self.assertEqual([ '1' ], processor.table[key1])

        result2 = processor.process_query(query2)

        self.assertEqual(None, result2)
        self.assertEqual(2, len(processor.table))
        self.assertEqual([ '1' ], processor.table[key1])
        self.assertEqual([ '2' ], processor.table[key2])

    def test_three_different_add_queries(self):
        processor = hash_chains.QueryProcessor(5)

        query1 = hash_chains.Query('add 1'.split())
        key1 = hash_chains.HashUtil.hash_function(query1.text,
            processor.bucket_count)
        query2 = hash_chains.Query('add 2'.split())
        key2 = hash_chains.HashUtil.hash_function(query2.text,
            processor.bucket_count)
        query3 = hash_chains.Query('add 3'.split())
        key3 = hash_chains.HashUtil.hash_function(query3.text,
            processor.bucket_count)
        self.assertNotEqual(key1, key2)
        self.assertNotEqual(key2, key3)
        self.assert_hash_value_of_key(key1, 4, [ 49 ], processor.bucket_count)
        self.assert_hash_value_of_key(key2, 0, [ 50 ], processor.bucket_count)
        self.assert_hash_value_of_key(key3, 1, [ 51 ], processor.bucket_count)

        result1 = processor.process_query(query1)

        self.assertEqual(None, result1)
        self.assertEqual(1, len(processor.table))
        self.assertEqual([ '1' ], processor.table[key1])

        result2 = processor.process_query(query2)

        self.assertEqual(None, result2)
        self.assertEqual(2, len(processor.table))
        self.assertEqual([ '1' ], processor.table[key1])
        self.assertEqual([ '2' ], processor.table[key2])

        result3 = processor.process_query(query3)

        self.assertEqual(None, result3)
        self.assertEqual(3, len(processor.table))
        self.assertEqual([ '1' ], processor.table[key1])
        self.assertEqual([ '2' ], processor.table[key2])
        self.assertEqual([ '3' ], processor.table[key3])

    def test_four_different_add_queries(self):
        processor = hash_chains.QueryProcessor(5)

        query1 = hash_chains.Query('add 1'.split())
        key1 = hash_chains.HashUtil.hash_function(query1.text,
            processor.bucket_count)
        query2 = hash_chains.Query('add 2'.split())
        key2 = hash_chains.HashUtil.hash_function(query2.text,
            processor.bucket_count)
        query3 = hash_chains.Query('add 3'.split())
        key3 = hash_chains.HashUtil.hash_function(query3.text,
            processor.bucket_count)
        query4 = hash_chains.Query('add 4'.split())
        key4 = hash_chains.HashUtil.hash_function(query4.text,
            processor.bucket_count)
        self.assertNotEqual(key1, key2)
        self.assertNotEqual(key2, key3)
        self.assertNotEqual(key3, key4)
        self.assert_hash_value_of_key(key1, 4, [ 49 ], processor.bucket_count)
        self.assert_hash_value_of_key(key2, 0, [ 50 ], processor.bucket_count)
        self.assert_hash_value_of_key(key3, 1, [ 51 ], processor.bucket_count)
        self.assert_hash_value_of_key(key4, 2, [ 52 ], processor.bucket_count)

        result1 = processor.process_query(query1)

        self.assertEqual(None, result1)
        self.assertEqual(1, len(processor.table))
        self.assertEqual([ '1' ], processor.table[key1])

        result2 = processor.process_query(query2)

        self.assertEqual(None, result2)
        self.assertEqual(2, len(processor.table))
        self.assertEqual([ '1' ], processor.table[key1])
        self.assertEqual([ '2' ], processor.table[key2])

        result3 = processor.process_query(query3)

        self.assertEqual(None, result3)
        self.assertEqual(3, len(processor.table))
        self.assertEqual([ '1' ], processor.table[key1])
        self.assertEqual([ '2' ], processor.table[key2])
        self.assertEqual([ '3' ], processor.table[key3])

        result4 = processor.process_query(query4)

        self.assertEqual(None, result4)
        self.assertEqual(4, len(processor.table))
        self.assertEqual([ '1' ], processor.table[key1])
        self.assertEqual([ '2' ], processor.table[key2])
        self.assertEqual([ '3' ], processor.table[key3])
        self.assertEqual([ '4' ], processor.table[key4])

    def test_five_different_add_queries(self):
        processor = hash_chains.QueryProcessor(5)

        query1 = hash_chains.Query('add 1'.split())
        key1 = hash_chains.HashUtil.hash_function(query1.text,
            processor.bucket_count)
        query2 = hash_chains.Query('add 2'.split())
        key2 = hash_chains.HashUtil.hash_function(query2.text,
            processor.bucket_count)
        query3 = hash_chains.Query('add 3'.split())
        key3 = hash_chains.HashUtil.hash_function(query3.text,
            processor.bucket_count)
        query4 = hash_chains.Query('add 4'.split())
        key4 = hash_chains.HashUtil.hash_function(query4.text,
            processor.bucket_count)
        query5 = hash_chains.Query('add 5'.split())
        key5 = hash_chains.HashUtil.hash_function(query5.text,
            processor.bucket_count)
        self.assertNotEqual(key1, key2)
        self.assertNotEqual(key2, key3)
        self.assertNotEqual(key3, key4)
        self.assertNotEqual(key4, key5)
        self.assert_hash_value_of_key(key1, 4, [ 49 ], processor.bucket_count)
        self.assert_hash_value_of_key(key2, 0, [ 50 ], processor.bucket_count)
        self.assert_hash_value_of_key(key3, 1, [ 51 ], processor.bucket_count)
        self.assert_hash_value_of_key(key4, 2, [ 52 ], processor.bucket_count)
        self.assert_hash_value_of_key(key5, 3, [ 53 ], processor.bucket_count)

        result1 = processor.process_query(query1)

        self.assertEqual(None, result1)
        self.assertEqual(1, len(processor.table))
        self.assertEqual([ '1' ], processor.table[key1])

        result2 = processor.process_query(query2)

        self.assertEqual(None, result2)
        self.assertEqual(2, len(processor.table))
        self.assertEqual([ '1' ], processor.table[key1])
        self.assertEqual([ '2' ], processor.table[key2])

        result3 = processor.process_query(query3)

        self.assertEqual(None, result3)
        self.assertEqual(3, len(processor.table))
        self.assertEqual([ '1' ], processor.table[key1])
        self.assertEqual([ '2' ], processor.table[key2])
        self.assertEqual([ '3' ], processor.table[key3])

        result4 = processor.process_query(query4)

        self.assertEqual(None, result4)
        self.assertEqual(4, len(processor.table))
        self.assertEqual([ '1' ], processor.table[key1])
        self.assertEqual([ '2' ], processor.table[key2])
        self.assertEqual([ '3' ], processor.table[key3])
        self.assertEqual([ '4' ], processor.table[key4])

        result5 = processor.process_query(query5)

        self.assertEqual(None, result5)
        self.assertEqual(5, len(processor.table))
        self.assertEqual([ '1' ], processor.table[key1])
        self.assertEqual([ '2' ], processor.table[key2])
        self.assertEqual([ '3' ], processor.table[key3])
        self.assertEqual([ '4' ], processor.table[key4])
        self.assertEqual([ '5' ], processor.table[key5])

    def test_six_different_add_queries(self):
        processor = hash_chains.QueryProcessor(5)

        query1 = hash_chains.Query('add 1'.split())
        key1 = hash_chains.HashUtil.hash_function(query1.text,
            processor.bucket_count)
        query2 = hash_chains.Query('add 2'.split())
        key2 = hash_chains.HashUtil.hash_function(query2.text,
            processor.bucket_count)
        query3 = hash_chains.Query('add 3'.split())
        key3 = hash_chains.HashUtil.hash_function(query3.text,
            processor.bucket_count)
        query4 = hash_chains.Query('add 4'.split())
        key4 = hash_chains.HashUtil.hash_function(query4.text,
            processor.bucket_count)
        query5 = hash_chains.Query('add 5'.split())
        key5 = hash_chains.HashUtil.hash_function(query5.text,
            processor.bucket_count)
        query6 = hash_chains.Query('add 6'.split())
        key6 = hash_chains.HashUtil.hash_function(query6.text,
            processor.bucket_count)
        self.assertNotEqual(key1, key2)
        self.assertNotEqual(key2, key3)
        self.assertNotEqual(key3, key4)
        self.assertNotEqual(key4, key5)
        self.assertEqual(key1, key6)
        self.assert_hash_value_of_key(key1, 4, [ 49 ], processor.bucket_count)
        self.assert_hash_value_of_key(key2, 0, [ 50 ], processor.bucket_count)
        self.assert_hash_value_of_key(key3, 1, [ 51 ], processor.bucket_count)
        self.assert_hash_value_of_key(key4, 2, [ 52 ], processor.bucket_count)
        self.assert_hash_value_of_key(key5, 3, [ 53 ], processor.bucket_count)
        self.assert_hash_value_of_key(key6, 4, [ 54 ], processor.bucket_count)

        result1 = processor.process_query(query1)

        self.assertEqual(None, result1)
        self.assertEqual(1, len(processor.table))
        self.assertEqual([ '1' ], processor.table[key1])

        result2 = processor.process_query(query2)

        self.assertEqual(None, result2)
        self.assertEqual(2, len(processor.table))
        self.assertEqual([ '1' ], processor.table[key1])
        self.assertEqual([ '2' ], processor.table[key2])

        result3 = processor.process_query(query3)

        self.assertEqual(None, result3)
        self.assertEqual(3, len(processor.table))
        self.assertEqual([ '1' ], processor.table[key1])
        self.assertEqual([ '2' ], processor.table[key2])
        self.assertEqual([ '3' ], processor.table[key3])

        result4 = processor.process_query(query4)

        self.assertEqual(None, result4)
        self.assertEqual(4, len(processor.table))
        self.assertEqual([ '1' ], processor.table[key1])
        self.assertEqual([ '2' ], processor.table[key2])
        self.assertEqual([ '3' ], processor.table[key3])
        self.assertEqual([ '4' ], processor.table[key4])

        result5 = processor.process_query(query5)

        self.assertEqual(None, result5)
        self.assertEqual(5, len(processor.table))
        self.assertEqual([ '1' ], processor.table[key1])
        self.assertEqual([ '2' ], processor.table[key2])
        self.assertEqual([ '3' ], processor.table[key3])
        self.assertEqual([ '4' ], processor.table[key4])
        self.assertEqual([ '5' ], processor.table[key5])

        result6 = processor.process_query(query6)

        self.assertEqual(None, result6)
        self.assertEqual(5, len(processor.table))
        self.assertEqual([ '6', '1' ], processor.table[key1])
        self.assertEqual([ '6', '1' ], processor.table[key6])
        self.assertEqual([ '2' ], processor.table[key2])
        self.assertEqual([ '3' ], processor.table[key3])
        self.assertEqual([ '4' ], processor.table[key4])
        self.assertEqual([ '5' ], processor.table[key5])

    def test_seven_different_add_queries(self):
        processor = hash_chains.QueryProcessor(5)

        query1 = hash_chains.Query('add 1'.split())
        key1 = hash_chains.HashUtil.hash_function(query1.text,
            processor.bucket_count)
        query2 = hash_chains.Query('add 2'.split())
        key2 = hash_chains.HashUtil.hash_function(query2.text,
            processor.bucket_count)
        query3 = hash_chains.Query('add 3'.split())
        key3 = hash_chains.HashUtil.hash_function(query3.text,
            processor.bucket_count)
        query4 = hash_chains.Query('add 4'.split())
        key4 = hash_chains.HashUtil.hash_function(query4.text,
            processor.bucket_count)
        query5 = hash_chains.Query('add 5'.split())
        key5 = hash_chains.HashUtil.hash_function(query5.text,
            processor.bucket_count)
        query6 = hash_chains.Query('add 6'.split())
        key6 = hash_chains.HashUtil.hash_function(query6.text,
            processor.bucket_count)
        query7 = hash_chains.Query('add 7'.split())
        key7 = hash_chains.HashUtil.hash_function(query7.text,
            processor.bucket_count)
        self.assertNotEqual(key1, key2)
        self.assertNotEqual(key2, key3)
        self.assertNotEqual(key3, key4)
        self.assertNotEqual(key4, key5)
        self.assertEqual(key1, key6)
        self.assertEqual(key2, key7)
        self.assert_hash_value_of_key(key1, 4, [ 49 ], processor.bucket_count)
        self.assert_hash_value_of_key(key2, 0, [ 50 ], processor.bucket_count)
        self.assert_hash_value_of_key(key3, 1, [ 51 ], processor.bucket_count)
        self.assert_hash_value_of_key(key4, 2, [ 52 ], processor.bucket_count)
        self.assert_hash_value_of_key(key5, 3, [ 53 ], processor.bucket_count)
        self.assert_hash_value_of_key(key6, 4, [ 54 ], processor.bucket_count)
        self.assert_hash_value_of_key(key7, 0, [ 55 ], processor.bucket_count)

        result1 = processor.process_query(query1)

        self.assertEqual(None, result1)
        self.assertEqual(1, len(processor.table))
        self.assertEqual([ '1' ], processor.table[key1])

        result2 = processor.process_query(query2)

        self.assertEqual(None, result2)
        self.assertEqual(2, len(processor.table))
        self.assertEqual([ '1' ], processor.table[key1])
        self.assertEqual([ '2' ], processor.table[key2])

        result3 = processor.process_query(query3)

        self.assertEqual(None, result3)
        self.assertEqual(3, len(processor.table))
        self.assertEqual([ '1' ], processor.table[key1])
        self.assertEqual([ '2' ], processor.table[key2])
        self.assertEqual([ '3' ], processor.table[key3])

        result4 = processor.process_query(query4)

        self.assertEqual(None, result4)
        self.assertEqual(4, len(processor.table))
        self.assertEqual([ '1' ], processor.table[key1])
        self.assertEqual([ '2' ], processor.table[key2])
        self.assertEqual([ '3' ], processor.table[key3])
        self.assertEqual([ '4' ], processor.table[key4])

        result5 = processor.process_query(query5)

        self.assertEqual(None, result5)
        self.assertEqual(5, len(processor.table))
        self.assertEqual([ '1' ], processor.table[key1])
        self.assertEqual([ '2' ], processor.table[key2])
        self.assertEqual([ '3' ], processor.table[key3])
        self.assertEqual([ '4' ], processor.table[key4])
        self.assertEqual([ '5' ], processor.table[key5])

        result6 = processor.process_query(query6)

        self.assertEqual(None, result6)
        self.assertEqual(5, len(processor.table))
        self.assertEqual([ '6', '1' ], processor.table[key1])
        self.assertEqual([ '6', '1' ], processor.table[key6])
        self.assertEqual([ '2' ], processor.table[key2])
        self.assertEqual([ '3' ], processor.table[key3])
        self.assertEqual([ '4' ], processor.table[key4])
        self.assertEqual([ '5' ], processor.table[key5])

        result7 = processor.process_query(query7)

        self.assertEqual(None, result7)
        self.assertEqual(5, len(processor.table))
        self.assertEqual([ '6', '1' ], processor.table[key1])
        self.assertEqual([ '6', '1' ], processor.table[key6])
        self.assertEqual([ '7', '2' ], processor.table[key2])
        self.assertEqual([ '7', '2' ], processor.table[key7])
        self.assertEqual([ '3' ], processor.table[key3])
        self.assertEqual([ '4' ], processor.table[key4])
        self.assertEqual([ '5' ], processor.table[key5])

    def test_eight_different_add_queries(self):
        processor = hash_chains.QueryProcessor(5)

        query1 = hash_chains.Query('add 1'.split())
        key1 = hash_chains.HashUtil.hash_function(query1.text,
            processor.bucket_count)
        query2 = hash_chains.Query('add 2'.split())
        key2 = hash_chains.HashUtil.hash_function(query2.text,
            processor.bucket_count)
        query3 = hash_chains.Query('add 3'.split())
        key3 = hash_chains.HashUtil.hash_function(query3.text,
            processor.bucket_count)
        query4 = hash_chains.Query('add 4'.split())
        key4 = hash_chains.HashUtil.hash_function(query4.text,
            processor.bucket_count)
        query5 = hash_chains.Query('add 5'.split())
        key5 = hash_chains.HashUtil.hash_function(query5.text,
            processor.bucket_count)
        query6 = hash_chains.Query('add 6'.split())
        key6 = hash_chains.HashUtil.hash_function(query6.text,
            processor.bucket_count)
        query7 = hash_chains.Query('add 7'.split())
        key7 = hash_chains.HashUtil.hash_function(query7.text,
            processor.bucket_count)
        query8 = hash_chains.Query('add 8'.split())
        key8 = hash_chains.HashUtil.hash_function(query8.text,
            processor.bucket_count)
        self.assertNotEqual(key1, key2)
        self.assertNotEqual(key2, key3)
        self.assertNotEqual(key3, key4)
        self.assertNotEqual(key4, key5)
        self.assertEqual(key1, key6)
        self.assertEqual(key2, key7)
        self.assertEqual(key3, key8)
        self.assert_hash_value_of_key(key1, 4, [ 49 ], processor.bucket_count)
        self.assert_hash_value_of_key(key2, 0, [ 50 ], processor.bucket_count)
        self.assert_hash_value_of_key(key3, 1, [ 51 ], processor.bucket_count)
        self.assert_hash_value_of_key(key4, 2, [ 52 ], processor.bucket_count)
        self.assert_hash_value_of_key(key5, 3, [ 53 ], processor.bucket_count)
        self.assert_hash_value_of_key(key6, 4, [ 54 ], processor.bucket_count)
        self.assert_hash_value_of_key(key7, 0, [ 55 ], processor.bucket_count)
        self.assert_hash_value_of_key(key8, 1, [ 56 ], processor.bucket_count)

        result1 = processor.process_query(query1)

        self.assertEqual(None, result1)
        self.assertEqual(1, len(processor.table))
        self.assertEqual([ '1' ], processor.table[key1])

        result2 = processor.process_query(query2)

        self.assertEqual(None, result2)
        self.assertEqual(2, len(processor.table))
        self.assertEqual([ '1' ], processor.table[key1])
        self.assertEqual([ '2' ], processor.table[key2])

        result3 = processor.process_query(query3)

        self.assertEqual(None, result3)
        self.assertEqual(3, len(processor.table))
        self.assertEqual([ '1' ], processor.table[key1])
        self.assertEqual([ '2' ], processor.table[key2])
        self.assertEqual([ '3' ], processor.table[key3])

        result4 = processor.process_query(query4)

        self.assertEqual(None, result4)
        self.assertEqual(4, len(processor.table))
        self.assertEqual([ '1' ], processor.table[key1])
        self.assertEqual([ '2' ], processor.table[key2])
        self.assertEqual([ '3' ], processor.table[key3])
        self.assertEqual([ '4' ], processor.table[key4])

        result5 = processor.process_query(query5)

        self.assertEqual(None, result5)
        self.assertEqual(5, len(processor.table))
        self.assertEqual([ '1' ], processor.table[key1])
        self.assertEqual([ '2' ], processor.table[key2])
        self.assertEqual([ '3' ], processor.table[key3])
        self.assertEqual([ '4' ], processor.table[key4])
        self.assertEqual([ '5' ], processor.table[key5])

        result6 = processor.process_query(query6)

        self.assertEqual(None, result6)
        self.assertEqual(5, len(processor.table))
        self.assertEqual([ '6', '1' ], processor.table[key1])
        self.assertEqual([ '6', '1' ], processor.table[key6])
        self.assertEqual([ '2' ], processor.table[key2])
        self.assertEqual([ '3' ], processor.table[key3])
        self.assertEqual([ '4' ], processor.table[key4])
        self.assertEqual([ '5' ], processor.table[key5])

        result7 = processor.process_query(query7)

        self.assertEqual(None, result7)
        self.assertEqual(5, len(processor.table))
        self.assertEqual([ '6', '1' ], processor.table[key1])
        self.assertEqual([ '6', '1' ], processor.table[key6])
        self.assertEqual([ '7', '2' ], processor.table[key2])
        self.assertEqual([ '7', '2' ], processor.table[key7])
        self.assertEqual([ '3' ], processor.table[key3])
        self.assertEqual([ '4' ], processor.table[key4])
        self.assertEqual([ '5' ], processor.table[key5])

        result8 = processor.process_query(query8)

        self.assertEqual(None, result8)
        self.assertEqual(5, len(processor.table))
        self.assertEqual([ '6', '1' ], processor.table[key1])
        self.assertEqual([ '6', '1' ], processor.table[key6])
        self.assertEqual([ '7', '2' ], processor.table[key2])
        self.assertEqual([ '7', '2' ], processor.table[key7])
        self.assertEqual([ '8', '3' ], processor.table[key3])
        self.assertEqual([ '8', '3' ], processor.table[key8])
        self.assertEqual([ '4' ], processor.table[key4])
        self.assertEqual([ '5' ], processor.table[key5])

    def test_nine_different_add_queries(self):
        processor = hash_chains.QueryProcessor(5)

        query1 = hash_chains.Query('add 1'.split())
        key1 = hash_chains.HashUtil.hash_function(query1.text,
            processor.bucket_count)
        query2 = hash_chains.Query('add 2'.split())
        key2 = hash_chains.HashUtil.hash_function(query2.text,
            processor.bucket_count)
        query3 = hash_chains.Query('add 3'.split())
        key3 = hash_chains.HashUtil.hash_function(query3.text,
            processor.bucket_count)
        query4 = hash_chains.Query('add 4'.split())
        key4 = hash_chains.HashUtil.hash_function(query4.text,
            processor.bucket_count)
        query5 = hash_chains.Query('add 5'.split())
        key5 = hash_chains.HashUtil.hash_function(query5.text,
            processor.bucket_count)
        query6 = hash_chains.Query('add 6'.split())
        key6 = hash_chains.HashUtil.hash_function(query6.text,
            processor.bucket_count)
        query7 = hash_chains.Query('add 7'.split())
        key7 = hash_chains.HashUtil.hash_function(query7.text,
            processor.bucket_count)
        query8 = hash_chains.Query('add 8'.split())
        key8 = hash_chains.HashUtil.hash_function(query8.text,
            processor.bucket_count)
        query9 = hash_chains.Query('add 9'.split())
        key9 = hash_chains.HashUtil.hash_function(query9.text,
            processor.bucket_count)
        self.assertNotEqual(key1, key2)
        self.assertNotEqual(key2, key3)
        self.assertNotEqual(key3, key4)
        self.assertNotEqual(key4, key5)
        self.assertEqual(key1, key6)
        self.assertEqual(key2, key7)
        self.assertEqual(key3, key8)
        self.assertEqual(key4, key9)
        self.assert_hash_value_of_key(key1, 4, [ 49 ], processor.bucket_count)
        self.assert_hash_value_of_key(key2, 0, [ 50 ], processor.bucket_count)
        self.assert_hash_value_of_key(key3, 1, [ 51 ], processor.bucket_count)
        self.assert_hash_value_of_key(key4, 2, [ 52 ], processor.bucket_count)
        self.assert_hash_value_of_key(key5, 3, [ 53 ], processor.bucket_count)
        self.assert_hash_value_of_key(key6, 4, [ 54 ], processor.bucket_count)
        self.assert_hash_value_of_key(key7, 0, [ 55 ], processor.bucket_count)
        self.assert_hash_value_of_key(key8, 1, [ 56 ], processor.bucket_count)
        self.assert_hash_value_of_key(key9, 2, [ 57 ], processor.bucket_count)

        result1 = processor.process_query(query1)

        self.assertEqual(None, result1)
        self.assertEqual(1, len(processor.table))
        self.assertEqual([ '1' ], processor.table[key1])

        result2 = processor.process_query(query2)

        self.assertEqual(None, result2)
        self.assertEqual(2, len(processor.table))
        self.assertEqual([ '1' ], processor.table[key1])
        self.assertEqual([ '2' ], processor.table[key2])

        result3 = processor.process_query(query3)

        self.assertEqual(None, result3)
        self.assertEqual(3, len(processor.table))
        self.assertEqual([ '1' ], processor.table[key1])
        self.assertEqual([ '2' ], processor.table[key2])
        self.assertEqual([ '3' ], processor.table[key3])

        result4 = processor.process_query(query4)

        self.assertEqual(None, result4)
        self.assertEqual(4, len(processor.table))
        self.assertEqual([ '1' ], processor.table[key1])
        self.assertEqual([ '2' ], processor.table[key2])
        self.assertEqual([ '3' ], processor.table[key3])
        self.assertEqual([ '4' ], processor.table[key4])

        result5 = processor.process_query(query5)

        self.assertEqual(None, result5)
        self.assertEqual(5, len(processor.table))
        self.assertEqual([ '1' ], processor.table[key1])
        self.assertEqual([ '2' ], processor.table[key2])
        self.assertEqual([ '3' ], processor.table[key3])
        self.assertEqual([ '4' ], processor.table[key4])
        self.assertEqual([ '5' ], processor.table[key5])

        result6 = processor.process_query(query6)

        self.assertEqual(None, result6)
        self.assertEqual(5, len(processor.table))
        self.assertEqual([ '6', '1' ], processor.table[key1])
        self.assertEqual([ '6', '1' ], processor.table[key6])
        self.assertEqual([ '2' ], processor.table[key2])
        self.assertEqual([ '3' ], processor.table[key3])
        self.assertEqual([ '4' ], processor.table[key4])
        self.assertEqual([ '5' ], processor.table[key5])

        result7 = processor.process_query(query7)

        self.assertEqual(None, result7)
        self.assertEqual(5, len(processor.table))
        self.assertEqual([ '6', '1' ], processor.table[key1])
        self.assertEqual([ '6', '1' ], processor.table[key6])
        self.assertEqual([ '7', '2' ], processor.table[key2])
        self.assertEqual([ '7', '2' ], processor.table[key7])
        self.assertEqual([ '3' ], processor.table[key3])
        self.assertEqual([ '4' ], processor.table[key4])
        self.assertEqual([ '5' ], processor.table[key5])

        result8 = processor.process_query(query8)

        self.assertEqual(None, result8)
        self.assertEqual(5, len(processor.table))
        self.assertEqual([ '6', '1' ], processor.table[key1])
        self.assertEqual([ '6', '1' ], processor.table[key6])
        self.assertEqual([ '7', '2' ], processor.table[key2])
        self.assertEqual([ '7', '2' ], processor.table[key7])
        self.assertEqual([ '8', '3' ], processor.table[key3])
        self.assertEqual([ '8', '3' ], processor.table[key8])
        self.assertEqual([ '4' ], processor.table[key4])
        self.assertEqual([ '5' ], processor.table[key5])

        result9 = processor.process_query(query9)

        self.assertEqual(None, result9)
        self.assertEqual(5, len(processor.table))
        self.assertEqual([ '6', '1' ], processor.table[key1])
        self.assertEqual([ '6', '1' ], processor.table[key6])
        self.assertEqual([ '7', '2' ], processor.table[key2])
        self.assertEqual([ '7', '2' ], processor.table[key7])
        self.assertEqual([ '8', '3' ], processor.table[key3])
        self.assertEqual([ '8', '3' ], processor.table[key8])
        self.assertEqual([ '9', '4' ], processor.table[key4])
        self.assertEqual([ '9', '4' ], processor.table[key9])
        self.assertEqual([ '5' ], processor.table[key5])

    def test_ten_different_add_queries(self):
        processor = hash_chains.QueryProcessor(5)

        query1 = hash_chains.Query('add 1'.split())
        key1 = hash_chains.HashUtil.hash_function(query1.text,
            processor.bucket_count)
        query2 = hash_chains.Query('add 2'.split())
        key2 = hash_chains.HashUtil.hash_function(query2.text,
            processor.bucket_count)
        query3 = hash_chains.Query('add 3'.split())
        key3 = hash_chains.HashUtil.hash_function(query3.text,
            processor.bucket_count)
        query4 = hash_chains.Query('add 4'.split())
        key4 = hash_chains.HashUtil.hash_function(query4.text,
            processor.bucket_count)
        query5 = hash_chains.Query('add 5'.split())
        key5 = hash_chains.HashUtil.hash_function(query5.text,
            processor.bucket_count)
        query6 = hash_chains.Query('add 6'.split())
        key6 = hash_chains.HashUtil.hash_function(query6.text,
            processor.bucket_count)
        query7 = hash_chains.Query('add 7'.split())
        key7 = hash_chains.HashUtil.hash_function(query7.text,
            processor.bucket_count)
        query8 = hash_chains.Query('add 8'.split())
        key8 = hash_chains.HashUtil.hash_function(query8.text,
            processor.bucket_count)
        query9 = hash_chains.Query('add 9'.split())
        key9 = hash_chains.HashUtil.hash_function(query9.text,
            processor.bucket_count)
        query10 = hash_chains.Query('add 10'.split())
        key10 = hash_chains.HashUtil.hash_function(query10.text,
            processor.bucket_count)
        self.assertNotEqual(key1, key2)
        self.assertNotEqual(key2, key3)
        self.assertNotEqual(key3, key4)
        self.assertNotEqual(key4, key5)
        self.assertEqual(key1, key6)
        self.assertEqual(key2, key7)
        self.assertEqual(key3, key8)
        self.assertEqual(key4, key9)
        self.assertEqual(key5, key10)
        self.assert_hash_value_of_key(key1, 4, [ 49 ], processor.bucket_count)
        self.assert_hash_value_of_key(key2, 0, [ 50 ], processor.bucket_count)
        self.assert_hash_value_of_key(key3, 1, [ 51 ], processor.bucket_count)
        self.assert_hash_value_of_key(key4, 2, [ 52 ], processor.bucket_count)
        self.assert_hash_value_of_key(key5, 3, [ 53 ], processor.bucket_count)
        self.assert_hash_value_of_key(key6, 4, [ 54 ], processor.bucket_count)
        self.assert_hash_value_of_key(key7, 0, [ 55 ], processor.bucket_count)
        self.assert_hash_value_of_key(key8, 1, [ 56 ], processor.bucket_count)
        self.assert_hash_value_of_key(key9, 2, [ 57 ], processor.bucket_count)
        self.assert_hash_value_of_key(key10, 3, [ 58 ], processor.bucket_count)

        result1 = processor.process_query(query1)

        self.assertEqual(None, result1)
        self.assertEqual(1, len(processor.table))
        self.assertEqual([ '1' ], processor.table[key1])

        result2 = processor.process_query(query2)

        self.assertEqual(None, result2)
        self.assertEqual(2, len(processor.table))
        self.assertEqual([ '1' ], processor.table[key1])
        self.assertEqual([ '2' ], processor.table[key2])

        result3 = processor.process_query(query3)

        self.assertEqual(None, result3)
        self.assertEqual(3, len(processor.table))
        self.assertEqual([ '1' ], processor.table[key1])
        self.assertEqual([ '2' ], processor.table[key2])
        self.assertEqual([ '3' ], processor.table[key3])

        result4 = processor.process_query(query4)

        self.assertEqual(None, result4)
        self.assertEqual(4, len(processor.table))
        self.assertEqual([ '1' ], processor.table[key1])
        self.assertEqual([ '2' ], processor.table[key2])
        self.assertEqual([ '3' ], processor.table[key3])
        self.assertEqual([ '4' ], processor.table[key4])

        result5 = processor.process_query(query5)

        self.assertEqual(None, result5)
        self.assertEqual(5, len(processor.table))
        self.assertEqual([ '1' ], processor.table[key1])
        self.assertEqual([ '2' ], processor.table[key2])
        self.assertEqual([ '3' ], processor.table[key3])
        self.assertEqual([ '4' ], processor.table[key4])
        self.assertEqual([ '5' ], processor.table[key5])

        result6 = processor.process_query(query6)

        self.assertEqual(None, result6)
        self.assertEqual(5, len(processor.table))
        self.assertEqual([ '6', '1' ], processor.table[key1])
        self.assertEqual([ '6', '1' ], processor.table[key6])
        self.assertEqual([ '2' ], processor.table[key2])
        self.assertEqual([ '3' ], processor.table[key3])
        self.assertEqual([ '4' ], processor.table[key4])
        self.assertEqual([ '5' ], processor.table[key5])

        result7 = processor.process_query(query7)

        self.assertEqual(None, result7)
        self.assertEqual(5, len(processor.table))
        self.assertEqual([ '6', '1' ], processor.table[key1])
        self.assertEqual([ '6', '1' ], processor.table[key6])
        self.assertEqual([ '7', '2' ], processor.table[key2])
        self.assertEqual([ '7', '2' ], processor.table[key7])
        self.assertEqual([ '3' ], processor.table[key3])
        self.assertEqual([ '4' ], processor.table[key4])
        self.assertEqual([ '5' ], processor.table[key5])

        result8 = processor.process_query(query8)

        self.assertEqual(None, result8)
        self.assertEqual(5, len(processor.table))
        self.assertEqual([ '6', '1' ], processor.table[key1])
        self.assertEqual([ '6', '1' ], processor.table[key6])
        self.assertEqual([ '7', '2' ], processor.table[key2])
        self.assertEqual([ '7', '2' ], processor.table[key7])
        self.assertEqual([ '8', '3' ], processor.table[key3])
        self.assertEqual([ '8', '3' ], processor.table[key8])
        self.assertEqual([ '4' ], processor.table[key4])
        self.assertEqual([ '5' ], processor.table[key5])

        result9 = processor.process_query(query9)

        self.assertEqual(None, result9)
        self.assertEqual(5, len(processor.table))
        self.assertEqual([ '6', '1' ], processor.table[key1])
        self.assertEqual([ '6', '1' ], processor.table[key6])
        self.assertEqual([ '7', '2' ], processor.table[key2])
        self.assertEqual([ '7', '2' ], processor.table[key7])
        self.assertEqual([ '8', '3' ], processor.table[key3])
        self.assertEqual([ '8', '3' ], processor.table[key8])
        self.assertEqual([ '9', '4' ], processor.table[key4])
        self.assertEqual([ '9', '4' ], processor.table[key9])
        self.assertEqual([ '5' ], processor.table[key5])

        result10 = processor.process_query(query10)

        self.assertEqual(None, result10)
        self.assertEqual(5, len(processor.table))
        self.assertEqual([ '6', '1' ], processor.table[key1])
        self.assertEqual([ '6', '1' ], processor.table[key6])
        self.assertEqual([ '7', '2' ], processor.table[key2])
        self.assertEqual([ '7', '2' ], processor.table[key7])
        self.assertEqual([ '8', '3' ], processor.table[key3])
        self.assertEqual([ '8', '3' ], processor.table[key8])
        self.assertEqual([ '9', '4' ], processor.table[key4])
        self.assertEqual([ '9', '4' ], processor.table[key9])
        self.assertEqual([ '10', '5' ], processor.table[key5])
        self.assertEqual([ '10', '5' ], processor.table[key10])

    def test_eleen_different_add_queries(self):
        processor = hash_chains.QueryProcessor(5)

        query1 = hash_chains.Query('add 1'.split())
        key1 = hash_chains.HashUtil.hash_function(query1.text,
            processor.bucket_count)
        query2 = hash_chains.Query('add 2'.split())
        key2 = hash_chains.HashUtil.hash_function(query2.text,
            processor.bucket_count)
        query3 = hash_chains.Query('add 3'.split())
        key3 = hash_chains.HashUtil.hash_function(query3.text,
            processor.bucket_count)
        query4 = hash_chains.Query('add 4'.split())
        key4 = hash_chains.HashUtil.hash_function(query4.text,
            processor.bucket_count)
        query5 = hash_chains.Query('add 5'.split())
        key5 = hash_chains.HashUtil.hash_function(query5.text,
            processor.bucket_count)
        query6 = hash_chains.Query('add 6'.split())
        key6 = hash_chains.HashUtil.hash_function(query6.text,
            processor.bucket_count)
        query7 = hash_chains.Query('add 7'.split())
        key7 = hash_chains.HashUtil.hash_function(query7.text,
            processor.bucket_count)
        query8 = hash_chains.Query('add 8'.split())
        key8 = hash_chains.HashUtil.hash_function(query8.text,
            processor.bucket_count)
        query9 = hash_chains.Query('add 9'.split())
        key9 = hash_chains.HashUtil.hash_function(query9.text,
            processor.bucket_count)
        query10 = hash_chains.Query('add 10'.split())
        key10 = hash_chains.HashUtil.hash_function(query10.text,
            processor.bucket_count)
        query11 = hash_chains.Query('add 11'.split())
        key11 = hash_chains.HashUtil.hash_function(query11.text,
            processor.bucket_count)
        self.assertNotEqual(key1, key2)
        self.assertNotEqual(key2, key3)
        self.assertNotEqual(key3, key4)
        self.assertNotEqual(key4, key5)
        self.assertEqual(key1, key6)
        self.assertEqual(key2, key7)
        self.assertEqual(key3, key8)
        self.assertEqual(key4, key9)
        self.assertEqual(key5, key10)
        self.assertEqual(key3, key11)
        self.assert_hash_value_of_key(key1, 4, [ 49 ], processor.bucket_count)
        self.assert_hash_value_of_key(key2, 0, [ 50 ], processor.bucket_count)
        self.assert_hash_value_of_key(key3, 1, [ 51 ], processor.bucket_count)
        self.assert_hash_value_of_key(key4, 2, [ 52 ], processor.bucket_count)
        self.assert_hash_value_of_key(key5, 3, [ 53 ], processor.bucket_count)
        self.assert_hash_value_of_key(key6, 4, [ 54 ], processor.bucket_count)
        self.assert_hash_value_of_key(key7, 0, [ 55 ], processor.bucket_count)
        self.assert_hash_value_of_key(key8, 1, [ 56 ], processor.bucket_count)
        self.assert_hash_value_of_key(key9, 2, [ 57 ], processor.bucket_count)
        self.assert_hash_value_of_key(key10, 3,
            [ 49, 48 ], processor.bucket_count)
        self.assert_hash_value_of_key(key11, 1,
            [ 49, 49 ], processor.bucket_count)

        result1 = processor.process_query(query1)

        self.assertEqual(None, result1)
        self.assertEqual(1, len(processor.table))
        self.assertEqual([ '1' ], processor.table[key1])

        result2 = processor.process_query(query2)

        self.assertEqual(None, result2)
        self.assertEqual(2, len(processor.table))
        self.assertEqual([ '1' ], processor.table[key1])
        self.assertEqual([ '2' ], processor.table[key2])

        result3 = processor.process_query(query3)

        self.assertEqual(None, result3)
        self.assertEqual(3, len(processor.table))
        self.assertEqual([ '1' ], processor.table[key1])
        self.assertEqual([ '2' ], processor.table[key2])
        self.assertEqual([ '3' ], processor.table[key3])

        result4 = processor.process_query(query4)

        self.assertEqual(None, result4)
        self.assertEqual(4, len(processor.table))
        self.assertEqual([ '1' ], processor.table[key1])
        self.assertEqual([ '2' ], processor.table[key2])
        self.assertEqual([ '3' ], processor.table[key3])
        self.assertEqual([ '4' ], processor.table[key4])

        result5 = processor.process_query(query5)

        self.assertEqual(None, result5)
        self.assertEqual(5, len(processor.table))
        self.assertEqual([ '1' ], processor.table[key1])
        self.assertEqual([ '2' ], processor.table[key2])
        self.assertEqual([ '3' ], processor.table[key3])
        self.assertEqual([ '4' ], processor.table[key4])
        self.assertEqual([ '5' ], processor.table[key5])

        result6 = processor.process_query(query6)

        self.assertEqual(None, result6)
        self.assertEqual(5, len(processor.table))
        self.assertEqual([ '6', '1' ], processor.table[key1])
        self.assertEqual([ '6', '1' ], processor.table[key6])
        self.assertEqual([ '2' ], processor.table[key2])
        self.assertEqual([ '3' ], processor.table[key3])
        self.assertEqual([ '4' ], processor.table[key4])
        self.assertEqual([ '5' ], processor.table[key5])

        result7 = processor.process_query(query7)

        self.assertEqual(None, result7)
        self.assertEqual(5, len(processor.table))
        self.assertEqual([ '6', '1' ], processor.table[key1])
        self.assertEqual([ '6', '1' ], processor.table[key6])
        self.assertEqual([ '7', '2' ], processor.table[key2])
        self.assertEqual([ '7', '2' ], processor.table[key7])
        self.assertEqual([ '3' ], processor.table[key3])
        self.assertEqual([ '4' ], processor.table[key4])
        self.assertEqual([ '5' ], processor.table[key5])

        result8 = processor.process_query(query8)

        self.assertEqual(None, result8)
        self.assertEqual(5, len(processor.table))
        self.assertEqual([ '6', '1' ], processor.table[key1])
        self.assertEqual([ '6', '1' ], processor.table[key6])
        self.assertEqual([ '7', '2' ], processor.table[key2])
        self.assertEqual([ '7', '2' ], processor.table[key7])
        self.assertEqual([ '8', '3' ], processor.table[key3])
        self.assertEqual([ '8', '3' ], processor.table[key8])
        self.assertEqual([ '4' ], processor.table[key4])
        self.assertEqual([ '5' ], processor.table[key5])

        result9 = processor.process_query(query9)

        self.assertEqual(None, result9)
        self.assertEqual(5, len(processor.table))
        self.assertEqual([ '6', '1' ], processor.table[key1])
        self.assertEqual([ '6', '1' ], processor.table[key6])
        self.assertEqual([ '7', '2' ], processor.table[key2])
        self.assertEqual([ '7', '2' ], processor.table[key7])
        self.assertEqual([ '8', '3' ], processor.table[key3])
        self.assertEqual([ '8', '3' ], processor.table[key8])
        self.assertEqual([ '9', '4' ], processor.table[key4])
        self.assertEqual([ '9', '4' ], processor.table[key9])
        self.assertEqual([ '5' ], processor.table[key5])

        result10 = processor.process_query(query10)

        self.assertEqual(None, result10)
        self.assertEqual(5, len(processor.table))
        self.assertEqual([ '6', '1' ], processor.table[key1])
        self.assertEqual([ '6', '1' ], processor.table[key6])
        self.assertEqual([ '7', '2' ], processor.table[key2])
        self.assertEqual([ '7', '2' ], processor.table[key7])
        self.assertEqual([ '8', '3' ], processor.table[key3])
        self.assertEqual([ '8', '3' ], processor.table[key8])
        self.assertEqual([ '9', '4' ], processor.table[key4])
        self.assertEqual([ '9', '4' ], processor.table[key9])
        self.assertEqual([ '10', '5' ], processor.table[key5])
        self.assertEqual([ '10', '5' ], processor.table[key10])

        result11 = processor.process_query(query11)

        self.assertEqual(None, result11)
        self.assertEqual(5, len(processor.table))
        self.assertEqual([ '6', '1' ], processor.table[key1])
        self.assertEqual([ '6', '1' ], processor.table[key6])
        self.assertEqual([ '7', '2' ], processor.table[key2])
        self.assertEqual([ '7', '2' ], processor.table[key7])
        self.assertEqual([ '11', '8', '3' ], processor.table[key3])
        self.assertEqual([ '11', '8', '3' ], processor.table[key8])
        self.assertEqual([ '11', '8', '3' ], processor.table[key11])
        self.assertEqual([ '9', '4' ], processor.table[key4])
        self.assertEqual([ '9', '4' ], processor.table[key9])
        self.assertEqual([ '10', '5' ], processor.table[key5])
        self.assertEqual([ '10', '5' ], processor.table[key10])

    def test_delete_query_on_empty_book(self):
        processor = hash_chains.QueryProcessor(5)

        query = hash_chains.Query('del 1'.split())
        key = hash_chains.HashUtil.hash_function(query.text,
            processor.bucket_count)
        self.assert_hash_value_of_key(key, 4, [ 49 ], processor.bucket_count)

        result = processor.process_query(query)

        self.assertEqual(None, result)
        self.assertEqual(0, len(processor.table))

    def test_delete_query_on_missing_key(self):
        processor = hash_chains.QueryProcessor(5)

        query1 = hash_chains.Query('add 1'.split())
        key1 = hash_chains.HashUtil.hash_function(query1.text,
            processor.bucket_count)
        query2 = hash_chains.Query('del 2'.split())
        key2 = hash_chains.HashUtil.hash_function(query2.text,
            processor.bucket_count)
        self.assert_hash_value_of_key(key1, 4, [ 49 ], processor.bucket_count)
        self.assert_hash_value_of_key(key2, 0, [ 50 ], processor.bucket_count)
        self.assertNotEqual(key1, key2)

        result = processor.process_query(query1)

        self.assertEqual(None, result)
        self.assertEqual(1, len(processor.table))
        self.assertEqual([ '1' ], processor.table[key1])

        result = processor.process_query(query2)

        self.assertEqual(None, result)
        self.assertEqual(1, len(processor.table))
        self.assertEqual([ '1' ], processor.table[key1])

    def test_delete_query_on_existing_key(self):
        processor = hash_chains.QueryProcessor(5)

        query1 = hash_chains.Query('add 1'.split())
        key1 = hash_chains.HashUtil.hash_function(query1.text,
            processor.bucket_count)
        query2 = hash_chains.Query('del 1'.split())
        key2 = hash_chains.HashUtil.hash_function(query2.text,
            processor.bucket_count)
        self.assert_hash_value_of_key(key1, 4, [ 49 ], processor.bucket_count)
        self.assertEqual(key1, key2)

        result = processor.process_query(query1)

        self.assertEqual(None, result)
        self.assertEqual(1, len(processor.table))
        self.assertEqual([ '1' ], processor.table[key1])

        result = processor.process_query(query2)

        self.assertEqual(None, result)
        self.assertEqual(1, len(processor.table))
        self.assertEqual([], processor.table[key1])

    def test_several_delete_queries(self):
        processor = hash_chains.QueryProcessor(5)

        query1 = hash_chains.Query('add 1'.split())
        key1 = hash_chains.HashUtil.hash_function(query1.text,
            processor.bucket_count)
        query2 = hash_chains.Query('add 2'.split())
        key2 = hash_chains.HashUtil.hash_function(query2.text,
            processor.bucket_count)
        query3 = hash_chains.Query('add 3'.split())
        key3 = hash_chains.HashUtil.hash_function(query3.text,
            processor.bucket_count)
        query4 = hash_chains.Query('del 2'.split())
        key4 = hash_chains.HashUtil.hash_function(query2.text,
            processor.bucket_count)
        query5 = hash_chains.Query('del 11'.split())
        key5 = hash_chains.HashUtil.hash_function(query5.text,
            processor.bucket_count)
        query6 = hash_chains.Query('del 3'.split())
        key6 = hash_chains.HashUtil.hash_function(query6.text,
            processor.bucket_count)
        query7 = hash_chains.Query('del 22'.split())
        key7 = hash_chains.HashUtil.hash_function(query7.text,
            processor.bucket_count)
        query8 = hash_chains.Query('del 1'.split())
        key8 = hash_chains.HashUtil.hash_function(query8.text,
            processor.bucket_count)
        self.assertEqual(key1, key8)
        self.assertEqual(key2, key4)
        self.assertEqual(key3, key6)

        result = processor.process_query(query1)

        self.assertEqual(None, result)
        self.assertEqual(1, len(processor.table))
        self.assertEqual([ '1' ], processor.table[key1])

        result = processor.process_query(query2)

        self.assertEqual(None, result)
        self.assertEqual(2, len(processor.table))
        self.assertEqual([ '1' ], processor.table[key1])
        self.assertEqual([ '2' ], processor.table[key2])

        result = processor.process_query(query3)

        self.assertEqual(None, result)
        self.assertEqual(3, len(processor.table))
        self.assertEqual([ '1' ], processor.table[key1])
        self.assertEqual([ '2' ], processor.table[key2])
        self.assertEqual([ '3' ], processor.table[key3])

        result = processor.process_query(query4)

        self.assertEqual(None, result)
        self.assertEqual(3, len(processor.table))
        self.assertEqual([ '1' ], processor.table[key1])
        self.assertEqual([], processor.table[key2])
        self.assertEqual([ '3' ], processor.table[key3])
        self.assertEqual([], processor.table[key4])

        result = processor.process_query(query5)

        self.assertEqual(None, result)
        self.assertEqual(3, len(processor.table))
        self.assertEqual([ '1' ], processor.table[key1])
        self.assertEqual([], processor.table[key2])
        self.assertEqual([ '3' ], processor.table[key3])
        self.assertEqual([], processor.table[key4])
        self.assertEqual([ '3' ], processor.table[key5])

        result = processor.process_query(query6)

        self.assertEqual(None, result)
        self.assertEqual(3, len(processor.table))
        self.assertEqual([ '1' ], processor.table[key1])
        self.assertEqual([], processor.table[key2])
        self.assertEqual([], processor.table[key3])
        self.assertEqual([], processor.table[key4])
        self.assertEqual([], processor.table[key5])
        self.assertEqual([], processor.table[key6])

        result = processor.process_query(query7)

        self.assertEqual(None, result)
        self.assertEqual(3, len(processor.table))
        self.assertEqual([ '1' ], processor.table[key1])
        self.assertEqual([], processor.table[key2])
        self.assertEqual([], processor.table[key3])
        self.assertEqual([], processor.table[key4])
        self.assertEqual([], processor.table[key5])
        self.assertEqual([], processor.table[key6])
        self.assertEqual([], processor.table[key7])

        result = processor.process_query(query8)

        self.assertEqual(None, result)
        self.assertEqual(3, len(processor.table))
        self.assertEqual([], processor.table[key1])
        self.assertEqual([], processor.table[key2])
        self.assertEqual([], processor.table[key3])
        self.assertEqual([], processor.table[key4])
        self.assertEqual([], processor.table[key5])
        self.assertEqual([], processor.table[key6])
        self.assertEqual([], processor.table[key7])
        self.assertEqual([], processor.table[key8])

    def test_find_query_on_empty_book(self):
        processor = hash_chains.QueryProcessor(5)

        query = hash_chains.Query('find 1'.split())
        key = hash_chains.HashUtil.hash_function(query.text,
            processor.bucket_count)
        self.assert_hash_value_of_key(key, 4, [ 49 ], processor.bucket_count)

        result = processor.process_query(query)

        self.assertEqual('no', result)
        self.assertEqual(0, len(processor.table))

    def test_find_query_on_missing_key(self):
        processor = hash_chains.QueryProcessor(5)

        query1 = hash_chains.Query('add 1'.split())
        key1 = hash_chains.HashUtil.hash_function(query1.text,
            processor.bucket_count)
        query2 = hash_chains.Query('find 2'.split())
        key2 = hash_chains.HashUtil.hash_function(query2.text,
            processor.bucket_count)
        self.assert_hash_value_of_key(key1, 4, [ 49 ], processor.bucket_count)
        self.assert_hash_value_of_key(key2, 0, [ 50 ], processor.bucket_count)
        self.assertNotEqual(key1, key2)

        result = processor.process_query(query1)

        self.assertEqual(None, result)
        self.assertEqual(1, len(processor.table))
        self.assertEqual([ '1' ], processor.table[key1])

        result = processor.process_query(query2)

        self.assertEqual('no', result)
        self.assertEqual(1, len(processor.table))
        self.assertEqual([ '1' ], processor.table[key1])

    def test_find_query_on_existing_key(self):
        processor = hash_chains.QueryProcessor(5)

        query1 = hash_chains.Query('add 1'.split())
        key1 = hash_chains.HashUtil.hash_function(query1.text,
            processor.bucket_count)
        query2 = hash_chains.Query('find 1'.split())
        key2 = hash_chains.HashUtil.hash_function(query2.text,
            processor.bucket_count)
        self.assert_hash_value_of_key(key1, 4, [ 49 ], processor.bucket_count)
        self.assert_hash_value_of_key(key2, 4, [ 49 ], processor.bucket_count)
        self.assertEqual(key1, key2)

        result = processor.process_query(query1)

        self.assertEqual(None, result)
        self.assertEqual(1, len(processor.table))
        self.assertEqual([ '1' ], processor.table[key1])

        result = processor.process_query(query2)

        self.assertEqual('yes', result)
        self.assertEqual(1, len(processor.table))
        self.assertEqual([ '1' ], processor.table[key2])

    def test_find_query_on_existing_key_twice(self):
        processor = hash_chains.QueryProcessor(5)

        query1 = hash_chains.Query('add 1'.split())
        key1 = hash_chains.HashUtil.hash_function(query1.text,
            processor.bucket_count)
        query2 = hash_chains.Query('find 1'.split())
        key2 = hash_chains.HashUtil.hash_function(query2.text,
            processor.bucket_count)
        self.assert_hash_value_of_key(key1, 4, [ 49 ], processor.bucket_count)
        self.assert_hash_value_of_key(key2, 4, [ 49 ], processor.bucket_count)
        self.assertEqual(key1, key2)

        result = processor.process_query(query1)

        self.assertEqual(None, result)
        self.assertEqual(1, len(processor.table))
        self.assertEqual([ '1' ], processor.table[key1])

        result = processor.process_query(query2)

        self.assertEqual('yes', result)
        self.assertEqual(1, len(processor.table))
        self.assertEqual([ '1' ], processor.table[key2])

        result = processor.process_query(query2)

        self.assertEqual('yes', result)
        self.assertEqual(1, len(processor.table))
        self.assertEqual([ '1' ], processor.table[key2])

    def test_check_query_on_empty_book(self):
        processor = hash_chains.QueryProcessor(5)

        query = hash_chains.Query('check 4'.split())

        result = processor.process_query(query)

        self.assertEqual('', result)
        self.assertEqual(0, len(processor.table))

    def test_check_query_on_missing_key(self):
        processor = hash_chains.QueryProcessor(5)

        query1 = hash_chains.Query('add 1'.split())
        key1 = hash_chains.HashUtil.hash_function(query1.text,
            processor.bucket_count)
        query2 = hash_chains.Query('check 44'.split())
        key2 = query2.index
        self.assert_hash_value_of_key(key1, 4, [ 49 ], processor.bucket_count)
        self.assertNotEqual(key1, key2)

        result = processor.process_query(query1)

        self.assertEqual(None, result)
        self.assertEqual(1, len(processor.table))
        self.assertEqual([ '1' ], processor.table[key1])

        result = processor.process_query(query2)

        self.assertEqual('', result)
        self.assertEqual(1, len(processor.table))
        self.assertEqual([ '1' ], processor.table[key1])

    def test_check_query_on_existing_key(self):
        processor = hash_chains.QueryProcessor(5)

        query1 = hash_chains.Query('add 1'.split())
        key1 = hash_chains.HashUtil.hash_function(query1.text,
            processor.bucket_count)
        query2 = hash_chains.Query('check 4'.split())
        key2 = query2.index
        self.assert_hash_value_of_key(key1, 4, [ 49 ], processor.bucket_count)
        self.assert_hash_value_of_key(key2, 4, [ 49 ], processor.bucket_count)
        self.assertEqual(key1, key2)

        result = processor.process_query(query1)

        self.assertEqual(None, result)
        self.assertEqual(1, len(processor.table))
        self.assertEqual([ '1' ], processor.table[key1])

        result = processor.process_query(query2)

        self.assertEqual('1', result)
        self.assertEqual(1, len(processor.table))
        self.assertEqual([ '1' ], processor.table[key1])

    def test_check_query_on_existing_key_twice(self):
        processor = hash_chains.QueryProcessor(5)

        query1 = hash_chains.Query('add 1'.split())
        key1 = hash_chains.HashUtil.hash_function(query1.text,
            processor.bucket_count)
        query2 = hash_chains.Query('check 4'.split())
        key2 = query2.index
        self.assert_hash_value_of_key(key1, 4, [ 49 ], processor.bucket_count)
        self.assert_hash_value_of_key(key2, 4, [ 49 ], processor.bucket_count)
        self.assertEqual(key1, key2)

        result = processor.process_query(query1)

        self.assertEqual(None, result)
        self.assertEqual(1, len(processor.table))
        self.assertEqual([ '1' ], processor.table[key1])

        result = processor.process_query(query2)

        self.assertEqual('1', result)
        self.assertEqual(1, len(processor.table))
        self.assertEqual([ '1' ], processor.table[key1])

        result = processor.process_query(query2)

        self.assertEqual('1', result)
        self.assertEqual(1, len(processor.table))
        self.assertEqual([ '1' ], processor.table[key1])

    def test_check_query_on_existing_key_and_long_chain(self):
        processor = hash_chains.QueryProcessor(5)

        query1 = hash_chains.Query('add 3'.split())
        key1 = hash_chains.HashUtil.hash_function(query1.text,
            processor.bucket_count)
        query2 = hash_chains.Query('add 8'.split())
        key2 = hash_chains.HashUtil.hash_function(query2.text,
            processor.bucket_count)
        query3 = hash_chains.Query('add 11'.split())
        key3 = hash_chains.HashUtil.hash_function(query3.text,
            processor.bucket_count)
        query4 = hash_chains.Query('check 1'.split())
        key4 = query4.index
        self.assertEqual(key1, key2)
        self.assertEqual(key2, key3)
        self.assertEqual(key3, key4)
        self.assert_hash_value_of_key(key1, 1, [ 51 ], processor.bucket_count)
        self.assert_hash_value_of_key(key2, 1, [ 56 ], processor.bucket_count)
        self.assert_hash_value_of_key(key3, 1,
            [ 49, 49 ], processor.bucket_count)

        result = processor.process_query(query1)

        self.assertEqual(None, result)
        self.assertEqual(1, len(processor.table))
        self.assertEqual([ '3' ], processor.table[key1])

        result = processor.process_query(query2)

        self.assertEqual(None, result)
        self.assertEqual(1, len(processor.table))
        self.assertEqual([ '8', '3' ], processor.table[key2])

        result = processor.process_query(query3)

        self.assertEqual(None, result)
        self.assertEqual(1, len(processor.table))
        self.assertEqual([ '11', '8', '3' ], processor.table[key3])

        result = processor.process_query(query4)

        self.assertEqual('11 8 3', result)
        self.assertEqual(1, len(processor.table))
        self.assertEqual([ '11', '8', '3' ], processor.table[key4])

    def test_twelve_queries_on_five_buckets(self):
        processor = hash_chains.QueryProcessor(5)

        key1 = hash_chains.HashUtil.hash_function('world',
            processor.bucket_count)
        key2 = hash_chains.HashUtil.hash_function('HellO',
            processor.bucket_count)
        key3 = hash_chains.HashUtil.hash_function('World',
            processor.bucket_count)
        key4 = 4
        key5 = hash_chains.HashUtil.hash_function('luck',
            processor.bucket_count)
        key6 = hash_chains.HashUtil.hash_function('GooD',
            processor.bucket_count)
        key7 = 2
        key8 = hash_chains.HashUtil.hash_function('good',
            processor.bucket_count)
        self.assertEqual(key1, key2)
        self.assertEqual(key2, key4)
        self.assertNotEqual(key1, key3)
        self.assertNotEqual(key1, key5)
        self.assertEqual(key5, key6)
        self.assertEqual(key6, key7)
        self.assertNotEqual(key5, key8)

        result = processor.process_query(
            hash_chains.Query('add world'.split()))

        self.assertEqual(None, result)
        self.assertEqual(1, len(processor.table))
        self.assertEqual([ 'world' ], processor.table[key1])

        result = processor.process_query(
            hash_chains.Query('add HellO'.split()))

        self.assertEqual(None, result)
        self.assertEqual(1, len(processor.table))
        self.assertEqual([ 'HellO', 'world' ], processor.table[key1])

        result = processor.process_query(
            hash_chains.Query('check 4'.split()))

        self.assertEqual('HellO world', result)
        self.assertEqual(1, len(processor.table))
        self.assertEqual([ 'HellO', 'world' ], processor.table[key1])

        result = processor.process_query(
            hash_chains.Query('find World'.split()))

        self.assertEqual('no', result)
        self.assertEqual(1, len(processor.table))
        self.assertEqual([ 'HellO', 'world' ], processor.table[key1])

        result = processor.process_query(
            hash_chains.Query('find world'.split()))

        self.assertEqual('yes', result)
        self.assertEqual(1, len(processor.table))
        self.assertEqual([ 'HellO', 'world' ], processor.table[key1])

        result = processor.process_query(
            hash_chains.Query('del world'.split()))

        self.assertEqual(None, result)
        self.assertEqual(1, len(processor.table))
        self.assertEqual([ 'HellO' ], processor.table[key1])

        result = processor.process_query(
            hash_chains.Query('check 4'.split()))

        self.assertEqual('HellO', result)
        self.assertEqual(1, len(processor.table))
        self.assertEqual([ 'HellO' ], processor.table[key1])

        result = processor.process_query(
            hash_chains.Query('del HellO'.split()))

        self.assertEqual(None, result)
        self.assertEqual(1, len(processor.table))
        self.assertEqual([], processor.table[key1])

        result = processor.process_query(
            hash_chains.Query('add luck'.split()))

        self.assertEqual(None, result)
        self.assertEqual(2, len(processor.table))
        self.assertEqual([], processor.table[key1])
        self.assertEqual([ 'luck' ], processor.table[key5])

        result = processor.process_query(
            hash_chains.Query('add GooD'.split()))

        self.assertEqual(None, result)
        self.assertEqual(2, len(processor.table))
        self.assertEqual([], processor.table[key1])
        self.assertEqual([ 'GooD', 'luck' ], processor.table[key5])

        result = processor.process_query(
            hash_chains.Query('check 2'.split()))

        self.assertEqual('GooD luck', result)
        self.assertEqual(2, len(processor.table))
        self.assertEqual([], processor.table[key1])
        self.assertEqual([ 'GooD', 'luck' ], processor.table[key5])

        result = processor.process_query(
            hash_chains.Query('del good'.split()))

        self.assertEqual(None, result)
        self.assertEqual(2, len(processor.table))
        self.assertEqual([], processor.table[key1])
        self.assertEqual([ 'GooD', 'luck' ], processor.table[key5])

    def test_eight_queries_on_four_buckets(self):
        processor = hash_chains.QueryProcessor(4)

        key1 = hash_chains.HashUtil.hash_function('test',
            processor.bucket_count)
        key2 = hash_chains.HashUtil.hash_function('Test',
            processor.bucket_count)
#         key3 = hash_chains.HashUtil.hash_function('World',
#             processor.bucket_count)
#         key4 = 4
#         key5 = hash_chains.HashUtil.hash_function('luck',
#             processor.bucket_count)
#         key6 = hash_chains.HashUtil.hash_function('GooD',
#             processor.bucket_count)
#         key7 = 2
#         key8 = hash_chains.HashUtil.hash_function('good',
#             processor.bucket_count)
        self.assertEqual(key1, key2)
#         self.assertEqual(key2, key4)
#         self.assertNotEqual(key1, key3)
#         self.assertNotEqual(key1, key5)
#         self.assertEqual(key5, key6)
#         self.assertEqual(key6, key7)
#         self.assertNotEqual(key5, key8)

        result = processor.process_query(
            hash_chains.Query('add test'.split()))

        self.assertEqual(None, result)
        self.assertEqual(1, len(processor.table))
        self.assertEqual([ 'test' ], processor.table[key1])

        result = processor.process_query(
            hash_chains.Query('add test'.split()))

        self.assertEqual(None, result)
        self.assertEqual(1, len(processor.table))
        self.assertEqual([ 'test' ], processor.table[key1])

        result = processor.process_query(
            hash_chains.Query('find test'.split()))

        self.assertEqual('yes', result)
        self.assertEqual(1, len(processor.table))
        self.assertEqual([ 'test' ], processor.table[key1])

        result = processor.process_query(
            hash_chains.Query('del test'.split()))

        self.assertEqual(None, result)
        self.assertEqual(1, len(processor.table))
        self.assertEqual([], processor.table[key1])

        result = processor.process_query(
            hash_chains.Query('find test'.split()))

        self.assertEqual('no', result)
        self.assertEqual(1, len(processor.table))
        self.assertEqual([], processor.table[key1])

        result = processor.process_query(
            hash_chains.Query('find Test'.split()))

        self.assertEqual('no', result)
        self.assertEqual(1, len(processor.table))
        self.assertEqual([], processor.table[key1])

        result = processor.process_query(
            hash_chains.Query('add Test'.split()))

        self.assertEqual(None, result)
        self.assertEqual(1, len(processor.table))
        self.assertEqual([ 'Test' ], processor.table[key1])

        result = processor.process_query(
            hash_chains.Query('find Test'.split()))

        self.assertEqual('yes', result)
        self.assertEqual(1, len(processor.table))
        self.assertEqual([ 'Test' ], processor.table[key1])

if __name__ == '__main__':
    unittest.main()
