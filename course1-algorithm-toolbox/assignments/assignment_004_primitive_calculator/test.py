#!/usr/bin/python3

import unittest

from primitive_calculator import optimal_sequence, \
    optimal_sequence_simplified, Operation

class OptimalSequenceTestCase(unittest.TestCase):

    def assert_sequences_and_operations(self, n, sequences, operations):
        self.assertEqual(len(sequences), len(operations))
        sequence_length = -1
        for i in range(0, len(sequences)):
            if sequence_length == -1:
                sequence_length = len(sequences[i])
            self.assertEqual(sequence_length, len(sequences[i]))

            self.assertEqual(len(sequences[i]), len(operations[i]) + 1)

            x = 1
            self.assertEqual(sequences[i][0], x)
            for j in range(0, len(sequences[i]) - 1):
                if operations[i][j] == Operation.multiply_by_three.name:
                    x *= 3
                elif operations[i][j] == Operation.multiply_by_two.name:
                    x *= 2
                elif operations[i][j] == Operation.add_one.name:
                    x += 1
                self.assertEqual(sequences[i][j + 1], x)
            self.assertEqual(n, x)

    def test_with_negative(self):
        with self.assertRaisesRegex(AssertionError, ''):
            optimal_sequence(0)

    def test_with_0(self):
        with self.assertRaisesRegex(AssertionError, ''):
            optimal_sequence(0)

    def test_with_1(self):
        n = 1
        sequences, operations = optimal_sequence(n)
        self.assertEqual([ [ 1 ] ], sequences)
        self.assertEqual([ [] ], operations)
        self.assert_sequences_and_operations(n, sequences, operations)

    def test_with_2(self):
        n = 2
        sequences, operations = optimal_sequence(n)
        self.assertEqual(
            [
                [ 1, 2 ],
                [ 1, 2 ]
            ],
            sequences)
        self.assertEqual(
            [
                [ 'multiply_by_two' ],
                [ 'add_one' ]
            ],
            operations)
        self.assert_sequences_and_operations(n, sequences, operations)

    def test_with_3(self):
        n = 3
        sequences, operations = optimal_sequence(n)
        self.assertEqual(
            [
                [ 1, 3 ]
            ],
            sequences)
        self.assertEqual(
            [
                [ 'multiply_by_three' ],
            ],
            operations)
        self.assert_sequences_and_operations(n, sequences, operations)

    def test_with_4(self):
        n = 4
        sequences, operations = optimal_sequence(n)
        self.assertEqual(
            [
                [ 1, 2, 4 ],
                [ 1, 2, 4 ],
                [ 1, 3, 4 ]
            ],
            sequences)
        self.assertEqual(
            [
                [ 'multiply_by_two', 'multiply_by_two' ],
                [ 'add_one', 'multiply_by_two' ],
                [ 'multiply_by_three', 'add_one' ]
            ],
            operations)
        self.assert_sequences_and_operations(n, sequences, operations)

    def test_with_5(self):
        n = 5
        sequences, operations = optimal_sequence(n)
        self.assertEqual(
            [
                [ 1, 2, 4, 5 ],
                [ 1, 2, 4, 5 ],
                [ 1, 3, 4, 5 ]
            ],
            sequences)
        self.assertEqual(
            [
                [ 'multiply_by_two', 'multiply_by_two', 'add_one' ],
                [ 'add_one', 'multiply_by_two', 'add_one' ],
                [ 'multiply_by_three', 'add_one', 'add_one' ]
            ],
            operations)
        self.assert_sequences_and_operations(n, sequences, operations)

    def test_with_6(self):
        n = 6
        sequences, operations = optimal_sequence(n)
        self.assertEqual(
            [
                [ 1, 2, 6 ],
                [ 1, 2, 6 ],
                [ 1, 3, 6 ]
            ],
            sequences)
        self.assertEqual(
            [
                [ 'multiply_by_two', 'multiply_by_three' ],
                [ 'add_one', 'multiply_by_three' ],
                [ 'multiply_by_three', 'multiply_by_two' ]
            ],
            operations)
        self.assert_sequences_and_operations(n, sequences, operations)

    def test_with_7(self):
        n = 7
        sequences, operations = optimal_sequence(n)
        self.assertEqual(
            [
                [ 1, 2, 6, 7 ],
                [ 1, 2, 6, 7 ],
                [ 1, 3, 6, 7 ]
            ],
            sequences)
        self.assertEqual(
            [
                [ 'multiply_by_two', 'multiply_by_three', 'add_one' ],
                [ 'add_one', 'multiply_by_three', 'add_one' ],
                [ 'multiply_by_three', 'multiply_by_two', 'add_one' ]
            ],
            operations)
        self.assert_sequences_and_operations(n, sequences, operations)

    def test_with_8(self):
        n = 8
        sequences, operations = optimal_sequence(n)
        self.assertEqual(
            [
                [ 1, 2, 4, 8 ],
                [ 1, 2, 4, 8 ],
                [ 1, 3, 4, 8 ]
            ],
            sequences)
        self.assertEqual(
            [
                [ 'multiply_by_two', 'multiply_by_two', 'multiply_by_two' ],
                [ 'add_one', 'multiply_by_two', 'multiply_by_two' ],
                [ 'multiply_by_three', 'add_one', 'multiply_by_two' ]
            ],
            operations)
        self.assert_sequences_and_operations(n, sequences, operations)

    def test_with_9(self):
        n = 9
        sequences, operations = optimal_sequence(n)
        self.assertEqual(
            [
                [ 1, 3, 9 ]
            ],
            sequences)
        self.assertEqual(
            [
                [ 'multiply_by_three', 'multiply_by_three' ]
            ],
            operations)
        self.assert_sequences_and_operations(n, sequences, operations)

    def test_with_10(self):
        n = 10
        sequences, operations = optimal_sequence(n)
        self.assertEqual(
            [
                [ 1, 3, 9, 10 ]
            ],
            sequences)
        self.assertEqual(
            [
                [ 'multiply_by_three', 'multiply_by_three', 'add_one' ]
            ],
            operations)
        self.assert_sequences_and_operations(n, sequences, operations)

    def test_with_96234(self):
        n = 96234
        sequences, operations = optimal_sequence(n)
        self.assertEqual(
            [
                [
                    1, 3, 9, 10, 11, 22, 66, 198, 594, 1782, 5346, 16038,
                    16039, 32078, 96234
                ],
                [
                    1, 2, 6, 7, 21, 22, 66, 198, 594, 1782, 5346, 16038,
                    16039, 32078, 96234
                ],
                [
                    1, 2, 6, 7, 21, 22, 66, 198, 594, 1782, 5346, 16038,
                    16039, 32078, 96234
                ],
                [
                    1, 3, 6, 7, 21, 22, 66, 198, 594, 1782, 5346, 16038,
                    16039, 32078, 96234
                ],
                [
                    1, 3, 9, 10, 11, 33, 66, 198, 594, 1782, 5346, 16038,
                    16039, 32078, 96234
                ],
                [
                    1, 3, 9, 10, 11, 33, 99, 198, 594, 1782, 5346, 16038,
                    16039, 32078, 96234
                ],
                [
                    1, 3, 9, 10, 11, 33, 99, 297, 594, 1782, 5346, 16038,
                    16039, 32078, 96234
                ],
                [
                    1, 3, 9, 10, 11, 33, 99, 297, 891, 1782, 5346, 16038,
                    16039, 32078, 96234
                ],
                [
                    1, 3, 9, 10, 11, 33, 99, 297, 891, 2673, 5346, 16038,
                    16039, 32078, 96234
                ],
                [
                    1, 3, 9, 10, 11, 33, 99, 297, 891, 2673, 8019, 16038,
                    16039, 32078, 96234
                ],
                [
                    1, 3, 9, 10, 11, 22, 66, 198, 594, 1782, 5346, 16038,
                    16039, 48117, 96234
                ],
                [
                    1, 2, 6, 7, 21, 22, 66, 198, 594, 1782, 5346, 16038,
                    16039, 48117, 96234
                ],
                [
                    1, 2, 6, 7, 21, 22, 66, 198, 594, 1782, 5346, 16038,
                    16039, 48117, 96234
                ],
                [
                    1, 3, 6, 7, 21, 22, 66, 198, 594, 1782, 5346, 16038,
                    16039, 48117, 96234
                ],
                [
                    1, 3, 9, 10, 11, 33, 66, 198, 594, 1782, 5346, 16038,
                    16039, 48117, 96234
                ],
                [
                    1, 3, 9, 10, 11, 33, 99, 198, 594, 1782, 5346, 16038,
                    16039, 48117, 96234
                ],
                [
                    1, 3, 9, 10, 11, 33, 99, 297, 594, 1782, 5346, 16038,
                    16039, 48117, 96234
                ],
                [
                    1, 3, 9, 10, 11, 33, 99, 297, 891, 1782, 5346, 16038,
                    16039, 48117, 96234
                ],
                [
                    1, 3, 9, 10, 11, 33, 99, 297, 891, 2673, 5346, 16038,
                    16039, 48117, 96234
                ],
                [
                    1, 3, 9, 10, 11, 33, 99, 297, 891, 2673, 8019, 16038,
                    16039, 48117, 96234
                ]
            ],
            sequences)
        self.assertEqual(
            [
                [
                    'multiply_by_three', 'multiply_by_three', 'add_one',
                    'add_one', 'multiply_by_two',
                    'multiply_by_three', 'multiply_by_three',
                    'multiply_by_three', 'multiply_by_three',
                    'multiply_by_three', 'multiply_by_three',
                    'add_one', 'multiply_by_two', 'multiply_by_three'
                ],
                [
                    'multiply_by_two', 'multiply_by_three', 'add_one',
                    'multiply_by_three', 'add_one', 'multiply_by_three',
                    'multiply_by_three', 'multiply_by_three',
                    'multiply_by_three', 'multiply_by_three',
                    'multiply_by_three', 'add_one', 'multiply_by_two',
                    'multiply_by_three'
                ],
                [
                    'add_one', 'multiply_by_three', 'add_one',
                    'multiply_by_three', 'add_one', 'multiply_by_three',
                    'multiply_by_three', 'multiply_by_three',
                    'multiply_by_three', 'multiply_by_three',
                    'multiply_by_three', 'add_one', 'multiply_by_two',
                    'multiply_by_three'
                ],
                [
                    'multiply_by_three', 'multiply_by_two', 'add_one',
                    'multiply_by_three', 'add_one', 'multiply_by_three',
                    'multiply_by_three', 'multiply_by_three',
                    'multiply_by_three', 'multiply_by_three',
                    'multiply_by_three', 'add_one', 'multiply_by_two',
                    'multiply_by_three'
                ],
                [
                    'multiply_by_three', 'multiply_by_three', 'add_one',
                    'add_one', 'multiply_by_three', 'multiply_by_two',
                    'multiply_by_three', 'multiply_by_three',
                    'multiply_by_three', 'multiply_by_three',
                    'multiply_by_three', 'add_one', 'multiply_by_two',
                    'multiply_by_three'
                ],
                [
                    'multiply_by_three', 'multiply_by_three', 'add_one',
                    'add_one', 'multiply_by_three', 'multiply_by_three',
                    'multiply_by_two', 'multiply_by_three',
                    'multiply_by_three', 'multiply_by_three',
                    'multiply_by_three', 'add_one', 'multiply_by_two',
                    'multiply_by_three'
                ],
                [
                    'multiply_by_three', 'multiply_by_three', 'add_one',
                    'add_one', 'multiply_by_three', 'multiply_by_three',
                    'multiply_by_three', 'multiply_by_two',
                    'multiply_by_three', 'multiply_by_three',
                    'multiply_by_three', 'add_one', 'multiply_by_two',
                    'multiply_by_three'
                ],
                [
                    'multiply_by_three', 'multiply_by_three', 'add_one',
                    'add_one', 'multiply_by_three', 'multiply_by_three',
                    'multiply_by_three', 'multiply_by_three',
                    'multiply_by_two', 'multiply_by_three',
                    'multiply_by_three', 'add_one', 'multiply_by_two',
                    'multiply_by_three'
                ],
                [
                    'multiply_by_three', 'multiply_by_three', 'add_one',
                    'add_one', 'multiply_by_three', 'multiply_by_three',
                    'multiply_by_three', 'multiply_by_three',
                    'multiply_by_three', 'multiply_by_two',
                    'multiply_by_three', 'add_one', 'multiply_by_two',
                    'multiply_by_three'
                ],
                [
                    'multiply_by_three', 'multiply_by_three', 'add_one',
                    'add_one', 'multiply_by_three', 'multiply_by_three',
                    'multiply_by_three', 'multiply_by_three',
                    'multiply_by_three', 'multiply_by_three',
                    'multiply_by_two', 'add_one', 'multiply_by_two',
                    'multiply_by_three'
                ],
                [
                    'multiply_by_three', 'multiply_by_three', 'add_one',
                    'add_one', 'multiply_by_two', 'multiply_by_three',
                    'multiply_by_three', 'multiply_by_three',
                    'multiply_by_three', 'multiply_by_three',
                    'multiply_by_three', 'add_one', 'multiply_by_three',
                    'multiply_by_two'
                ],
                [
                    'multiply_by_two', 'multiply_by_three', 'add_one',
                    'multiply_by_three', 'add_one', 'multiply_by_three',
                    'multiply_by_three', 'multiply_by_three',
                    'multiply_by_three', 'multiply_by_three',
                    'multiply_by_three', 'add_one', 'multiply_by_three',
                    'multiply_by_two'
                ],
                [
                    'add_one', 'multiply_by_three', 'add_one',
                    'multiply_by_three', 'add_one', 'multiply_by_three',
                    'multiply_by_three', 'multiply_by_three',
                    'multiply_by_three', 'multiply_by_three',
                    'multiply_by_three', 'add_one', 'multiply_by_three',
                    'multiply_by_two'
                ],
                [
                    'multiply_by_three', 'multiply_by_two', 'add_one',
                    'multiply_by_three', 'add_one', 'multiply_by_three',
                    'multiply_by_three', 'multiply_by_three',
                    'multiply_by_three', 'multiply_by_three',
                    'multiply_by_three', 'add_one', 'multiply_by_three',
                    'multiply_by_two'
                ],
                [
                    'multiply_by_three', 'multiply_by_three', 'add_one',
                    'add_one', 'multiply_by_three', 'multiply_by_two',
                    'multiply_by_three', 'multiply_by_three',
                    'multiply_by_three', 'multiply_by_three',
                    'multiply_by_three', 'add_one', 'multiply_by_three',
                    'multiply_by_two'
                ],
                [
                    'multiply_by_three', 'multiply_by_three', 'add_one',
                    'add_one', 'multiply_by_three', 'multiply_by_three',
                    'multiply_by_two', 'multiply_by_three',
                    'multiply_by_three', 'multiply_by_three',
                    'multiply_by_three', 'add_one', 'multiply_by_three',
                    'multiply_by_two'
                ],
                [
                    'multiply_by_three', 'multiply_by_three', 'add_one',
                    'add_one', 'multiply_by_three', 'multiply_by_three',
                    'multiply_by_three', 'multiply_by_two',
                    'multiply_by_three', 'multiply_by_three',
                    'multiply_by_three', 'add_one', 'multiply_by_three',
                    'multiply_by_two'
                ],
                [
                    'multiply_by_three', 'multiply_by_three', 'add_one',
                    'add_one', 'multiply_by_three', 'multiply_by_three',
                    'multiply_by_three', 'multiply_by_three',
                    'multiply_by_two', 'multiply_by_three',
                    'multiply_by_three', 'add_one', 'multiply_by_three',
                    'multiply_by_two'
                ],
                [
                    'multiply_by_three', 'multiply_by_three', 'add_one',
                    'add_one', 'multiply_by_three', 'multiply_by_three',
                    'multiply_by_three', 'multiply_by_three',
                    'multiply_by_three', 'multiply_by_two',
                    'multiply_by_three', 'add_one', 'multiply_by_three',
                    'multiply_by_two'
                ],
                [
                    'multiply_by_three', 'multiply_by_three', 'add_one',
                    'add_one', 'multiply_by_three', 'multiply_by_three',
                    'multiply_by_three', 'multiply_by_three',
                    'multiply_by_three', 'multiply_by_three',
                    'multiply_by_two', 'add_one', 'multiply_by_three',
                    'multiply_by_two'
                ]
            ],
            operations)
        self.assert_sequences_and_operations(n, sequences, operations)

class OptimalSequenceSimplifiedTestCase(unittest.TestCase):

    def test_with_negative(self):
        with self.assertRaisesRegex(AssertionError, ''):
            optimal_sequence_simplified(0)

    def test_with_0(self):
        with self.assertRaisesRegex(AssertionError, ''):
            optimal_sequence_simplified(0)

    def test_with_1(self):
        n = 1
        sequence = optimal_sequence_simplified(n)
        self.assertEqual([ 1 ], sequence)

    def test_with_2(self):
        n = 2
        sequence = optimal_sequence_simplified(n)
        self.assertEqual(
            [ 1, 2 ],
            sequence)

    def test_with_3(self):
        n = 3
        sequence = optimal_sequence_simplified(n)
        self.assertEqual(
            [ 1, 3 ],
            sequence)

    def test_with_4(self):
        n = 4
        sequence = optimal_sequence_simplified(n)
        self.assertEqual(
            [ 1, 2, 4 ],
            sequence)

    def test_with_5(self):
        n = 5
        sequence = optimal_sequence_simplified(n)
        self.assertEqual(
            [ 1, 2, 4, 5 ],
            sequence)

    def test_with_6(self):
        n = 6
        sequence = optimal_sequence_simplified(n)
        self.assertEqual(
            [ 1, 2, 6 ],
            sequence)

    def test_with_7(self):
        n = 7
        sequence = optimal_sequence_simplified(n)
        self.assertEqual(
            [ 1, 2, 6, 7 ],
            sequence)

    def test_with_8(self):
        n = 8
        sequence = optimal_sequence_simplified(n)
        self.assertEqual(
            [ 1, 2, 4, 8 ],
            sequence)

    def test_with_9(self):
        n = 9
        sequence = optimal_sequence_simplified(n)
        self.assertEqual(
            [ 1, 3, 9 ],
            sequence)

    def test_with_10(self):
        n = 10
        sequence = optimal_sequence_simplified(n)
        self.assertEqual(
            [ 1, 3, 9, 10 ],
            sequence)

    def test_with_96234(self):
        n = 96234
        sequence = optimal_sequence_simplified(n)
        self.assertEqual(
            [
                1, 3, 9, 10, 11, 22, 66, 198, 594, 1782, 5346, 16038,
                16039, 32078, 96234
            ],
            sequence)

if __name__ == '__main__':
    unittest.main()
