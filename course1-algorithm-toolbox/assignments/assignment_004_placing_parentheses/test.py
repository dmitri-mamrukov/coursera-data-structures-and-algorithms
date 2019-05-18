#!/usr/bin/python3

import unittest

from placing_parentheses import get_min_max

class GetMinMaxTestCase(unittest.TestCase):

    def assert_min_max_solutions(self, min, max, min_solution, max_solution,
        expected_min_solution, expected_max_solution):
        self.assertEqual(expected_min_solution, min_solution)
        self.assertEqual(expected_max_solution, max_solution)
        self.assertEqual(min, eval(min_solution))
        self.assertEqual(max, eval(max_solution))

    def test_with_empty(self):
        with self.assertRaisesRegex(AssertionError, ''):
            get_min_max('')

    def test_with_operator(self):
        with self.assertRaisesRegex(AssertionError, ''):
            get_min_max('+')

    def test_with_operand_and_operator(self):
        with self.assertRaisesRegex(AssertionError, ''):
            get_min_max('1+')

    def test_with_operator_and_operand(self):
        with self.assertRaisesRegex(AssertionError, ''):
            get_min_max('+1')

    def test_with_unsupported_operator_between_two_operands(self):
        with self.assertRaisesRegex(AssertionError, ''):
            get_min_max('1#2')

    def test_with_unsupported_operator_among_operands(self):
        with self.assertRaisesRegex(AssertionError, ''):
            get_min_max('1+2-3*4#5*6-7+8')

    def test_with_two_digit_operand(self):
        with self.assertRaisesRegex(AssertionError, ''):
            get_min_max('12')

    def test_with_two_digit_operand_in_beginning(self):
        with self.assertRaisesRegex(AssertionError, ''):
            get_min_max('12+3')

    def test_with_two_digit_operand_in_end(self):
        with self.assertRaisesRegex(AssertionError, ''):
            get_min_max('1+34')

    def test_with_two_digit_operand_in_middle(self):
        with self.assertRaisesRegex(AssertionError, ''):
            get_min_max('1+34-5')

    def test_with_three_digit_operand_in_beginning(self):
        with self.assertRaisesRegex(AssertionError, ''):
            get_min_max('123+4')

    def test_with_three_digit_operand_in_end(self):
        with self.assertRaisesRegex(AssertionError, ''):
            get_min_max('1+345')

    def test_with_three_digit_operand_in_middle(self):
        with self.assertRaisesRegex(AssertionError, ''):
            get_min_max('1+345-6')

    def test_with_1(self):
        min, max, min_solution, max_solution = get_min_max('1')
        self.assertEqual(1, min)
        self.assertEqual(1, max)
        self.assert_min_max_solutions(min, max, min_solution, max_solution,
            '(1)', '(1)')

    def test_with_5(self):
        min, max, min_solution, max_solution = get_min_max('5')
        self.assertEqual(5, min)
        self.assertEqual(5, max)
        self.assert_min_max_solutions(min, max, min_solution, max_solution,
            '(5)', '(5)')

    def test_with_9(self):
        min, max, min_solution, max_solution = get_min_max('9')
        self.assertEqual(9, min)
        self.assertEqual(9, max)
        self.assert_min_max_solutions(min, max, min_solution, max_solution,
            '(9)', '(9)')

    def test_with_1_plus_2(self):
        min, max, min_solution, max_solution = get_min_max('1+2')
        self.assertEqual(3, min)
        self.assertEqual(3, max)
        self.assert_min_max_solutions(min, max, min_solution, max_solution,
            '(1+2)', '(1+2)')

    def test_with_2_plus_1(self):
        min, max, min_solution, max_solution = get_min_max('2+1')
        self.assertEqual(3, min)
        self.assertEqual(3, max)
        self.assert_min_max_solutions(min, max, min_solution, max_solution,
            '(2+1)', '(2+1)')

    def test_with_5_plus_6(self):
        min, max, min_solution, max_solution = get_min_max('5+6')
        self.assertEqual(11, min)
        self.assertEqual(11, max)
        self.assert_min_max_solutions(min, max, min_solution, max_solution,
            '(5+6)', '(5+6)')

    def test_with_6_plus_5(self):
        min, max, min_solution, max_solution = get_min_max('6+5')
        self.assertEqual(11, min)
        self.assertEqual(11, max)
        self.assert_min_max_solutions(min, max, min_solution, max_solution,
            '(6+5)', '(6+5)')

    def test_with_8_plus_9(self):
        min, max, min_solution, max_solution = get_min_max('8+9')
        self.assertEqual(17, min)
        self.assertEqual(17, max)
        self.assert_min_max_solutions(min, max, min_solution, max_solution,
            '(8+9)', '(8+9)')

    def test_with_9_plus_8(self):
        min, max, min_solution, max_solution = get_min_max('9+8')
        self.assertEqual(17, min)
        self.assertEqual(17, max)
        self.assert_min_max_solutions(min, max, min_solution, max_solution,
            '(9+8)', '(9+8)')

    def test_with_1_plus_2_plus_3(self):
        min, max, min_solution, max_solution = get_min_max('1+2+3')
        self.assertEqual(6, min)
        self.assertEqual(6, max)
        self.assert_min_max_solutions(min, max, min_solution, max_solution,
            '((1)+(2+3))', '((1)+(2+3))')

    def test_with_1_plus_3_plus_2(self):
        min, max, min_solution, max_solution = get_min_max('1+3+2')
        self.assertEqual(6, min)
        self.assertEqual(6, max)
        self.assert_min_max_solutions(min, max, min_solution, max_solution,
            '((1)+(3+2))', '((1)+(3+2))')

    def test_with_2_plus_1_plus_3(self):
        min, max, min_solution, max_solution = get_min_max('2+1+3')
        self.assertEqual(6, min)
        self.assertEqual(6, max)
        self.assert_min_max_solutions(min, max, min_solution, max_solution,
            '((2)+(1+3))', '((2)+(1+3))')

    def test_with_2_plus_3_plus_1(self):
        min, max, min_solution, max_solution = get_min_max('2+3+1')
        self.assertEqual(6, min)
        self.assertEqual(6, max)
        self.assert_min_max_solutions(min, max, min_solution, max_solution,
            '((2)+(3+1))', '((2)+(3+1))')

    def test_with_3_plus_1_plus_2(self):
        min, max, min_solution, max_solution = get_min_max('3+1+2')
        self.assertEqual(6, min)
        self.assertEqual(6, max)
        self.assert_min_max_solutions(min, max, min_solution, max_solution,
            '((3)+(1+2))', '((3)+(1+2))')

    def test_with_3_plus_2_plus_1(self):
        min, max, min_solution, max_solution = get_min_max('3+2+1')
        self.assertEqual(6, min)
        self.assertEqual(6, max)
        self.assert_min_max_solutions(min, max, min_solution, max_solution,
            '((3)+(2+1))', '((3)+(2+1))')

    def test_with_1_plus_2_minus_3(self):
        min, max, min_solution, max_solution = get_min_max('1+2-3')
        self.assertEqual(0, min)
        self.assertEqual(0, max)
        self.assert_min_max_solutions(min, max, min_solution, max_solution,
            '((1)+(2-3))', '((1)+(2-3))')

    def test_with_1_plus_3_minus_2(self):
        min, max, min_solution, max_solution = get_min_max('1+3-2')
        self.assertEqual(2, min)
        self.assertEqual(2, max)
        self.assert_min_max_solutions(min, max, min_solution, max_solution,
            '((1)+(3-2))', '((1)+(3-2))')

    def test_with_2_plus_1_minus_3(self):
        min, max, min_solution, max_solution = get_min_max('2+1-3')
        self.assertEqual(0, min)
        self.assertEqual(0, max)
        self.assert_min_max_solutions(min, max, min_solution, max_solution,
            '((2)+(1-3))', '((2)+(1-3))')

    def test_with_2_plus_3_minus_1(self):
        min, max, min_solution, max_solution = get_min_max('2+3-1')
        self.assertEqual(4, min)
        self.assertEqual(4, max)
        self.assert_min_max_solutions(min, max, min_solution, max_solution,
            '((2)+(3-1))', '((2)+(3-1))')

    def test_with_3_plus_1_minus_2(self):
        min, max, min_solution, max_solution = get_min_max('3+1-2')
        self.assertEqual(2, min)
        self.assertEqual(2, max)
        self.assert_min_max_solutions(min, max, min_solution, max_solution,
            '((3)+(1-2))', '((3)+(1-2))')

    def test_with_3_plus_2_minus_1(self):
        min, max, min_solution, max_solution = get_min_max('3+2-1')
        self.assertEqual(4, min)
        self.assertEqual(4, max)
        self.assert_min_max_solutions(min, max, min_solution, max_solution,
            '((3)+(2-1))', '((3)+(2-1))')

    def test_with_1_plus_2_times_3_minus_4(self):
        min, max, min_solution, max_solution = get_min_max('1+2*3-4')
        self.assertEqual(-3, min)
        self.assertEqual(5, max)
        self.assert_min_max_solutions(min, max, min_solution, max_solution,
            '((1+2)*(3-4))', '(((1+2)*(3))-(4))')

    def test_with_1_plus_2_times_4_minus_3(self):
        min, max, min_solution, max_solution = get_min_max('1+2*4-3')
        self.assertEqual(3, min)
        self.assertEqual(9, max)
        self.assert_min_max_solutions(min, max, min_solution, max_solution,
            '((1)+((2)*(4-3)))', '(((1+2)*(4))-(3))')

    def test_with_1_plus_3_times_2_minus_4(self):
        min, max, min_solution, max_solution = get_min_max('1+3*2-4')
        self.assertEqual(-8, min)
        self.assertEqual(4, max)
        self.assert_min_max_solutions(min, max, min_solution, max_solution,
            '((1+3)*(2-4))', '(((1+3)*(2))-(4))')

    def test_with_1_plus_3_times_4_minus_2(self):
        min, max, min_solution, max_solution = get_min_max('1+3*4-2')
        self.assertEqual(7, min)
        self.assertEqual(14, max)
        self.assert_min_max_solutions(min, max, min_solution, max_solution,
            '((1)+((3)*(4-2)))', '(((1+3)*(4))-(2))')

    def test_with_1_plus_4_times_2_minus_3(self):
        min, max, min_solution, max_solution = get_min_max('1+4*2-3')
        self.assertEqual(-5, min)
        self.assertEqual(7, max)
        self.assert_min_max_solutions(min, max, min_solution, max_solution,
            '((1+4)*(2-3))', '(((1+4)*(2))-(3))')

    def test_with_1_plus_4_times_3_minus_2(self):
        min, max, min_solution, max_solution = get_min_max('1+4*3-2')
        self.assertEqual(5, min)
        self.assertEqual(13, max)
        self.assert_min_max_solutions(min, max, min_solution, max_solution,
            '((1)+((4)*(3-2)))', '(((1+4)*(3))-(2))')

    def test_with_2_plus_1_times_3_minus_4(self):
        min, max, min_solution, max_solution = get_min_max('2+1*3-4')
        self.assertEqual(-3, min)
        self.assertEqual(5, max)
        self.assert_min_max_solutions(min, max, min_solution, max_solution,
            '((2+1)*(3-4))', '(((2+1)*(3))-(4))')

    def test_with_2_plus_1_times_4_minus_3(self):
        min, max, min_solution, max_solution = get_min_max('2+1*4-3')
        self.assertEqual(3, min)
        self.assertEqual(9, max)
        self.assert_min_max_solutions(min, max, min_solution, max_solution,
            '((2)+((1)*(4-3)))', '(((2+1)*(4))-(3))')

    def test_with_2_plus_3_times_1_minus_4(self):
        min, max, min_solution, max_solution = get_min_max('2+3*1-4')
        self.assertEqual(-15, min)
        self.assertEqual(1, max)
        self.assert_min_max_solutions(min, max, min_solution, max_solution,
            '((2+3)*(1-4))', '((2)+((3*1)-(4)))')

    def test_with_2_plus_3_times_4_minus_1(self):
        min, max, min_solution, max_solution = get_min_max('2+3*4-1')
        self.assertEqual(11, min)
        self.assertEqual(19, max)
        self.assert_min_max_solutions(min, max, min_solution, max_solution,
            '((2)+((3)*(4-1)))', '(((2+3)*(4))-(1))')

    def test_with_2_plus_4_times_1_minus_3(self):
        min, max, min_solution, max_solution = get_min_max('2+4*1-3')
        self.assertEqual(-12, min)
        self.assertEqual(3, max)
        self.assert_min_max_solutions(min, max, min_solution, max_solution,
            '((2+4)*(1-3))', '((2)+((4*1)-(3)))')

    def test_with_2_plus_4_times_3_minus_1(self):
        min, max, min_solution, max_solution = get_min_max('2+4*3-1')
        self.assertEqual(10, min)
        self.assertEqual(17, max)
        self.assert_min_max_solutions(min, max, min_solution, max_solution,
            '((2)+((4)*(3-1)))', '(((2+4)*(3))-(1))')

    def test_with_3_plus_1_times_2_minus_4(self):
        min, max, min_solution, max_solution = get_min_max('3+1*2-4')
        self.assertEqual(-8, min)
        self.assertEqual(4, max)
        self.assert_min_max_solutions(min, max, min_solution, max_solution,
            '((3+1)*(2-4))', '(((3+1)*(2))-(4))')

    def test_with_3_plus_1_times_4_minus_2(self):
        min, max, min_solution, max_solution = get_min_max('3+1*4-2')
        self.assertEqual(5, min)
        self.assertEqual(14, max)
        self.assert_min_max_solutions(min, max, min_solution, max_solution,
            '((3)+((1)*(4-2)))', '(((3+1)*(4))-(2))')

    def test_with_3_plus_2_times_1_minus_4(self):
        min, max, min_solution, max_solution = get_min_max('3+2*1-4')
        self.assertEqual(-15, min)
        self.assertEqual(1, max)
        self.assert_min_max_solutions(min, max, min_solution, max_solution,
            '((3+2)*(1-4))', '((3)+((2*1)-(4)))')

    def test_with_3_plus_2_times_4_minus_1(self):
        min, max, min_solution, max_solution = get_min_max('3+2*4-1')
        self.assertEqual(9, min)
        self.assertEqual(19, max)
        self.assert_min_max_solutions(min, max, min_solution, max_solution,
            '((3)+((2)*(4-1)))', '(((3+2)*(4))-(1))')

    def test_with_3_plus_4_times_1_minus_2(self):
        min, max, min_solution, max_solution = get_min_max('3+4*1-2')
        self.assertEqual(-7, min)
        self.assertEqual(5, max)
        self.assert_min_max_solutions(min, max, min_solution, max_solution,
            '((3+4)*(1-2))', '((3)+((4*1)-(2)))')

    def test_with_3_plus_4_times_2_minus_1(self):
        min, max, min_solution, max_solution = get_min_max('3+4*2-1')
        self.assertEqual(7, min)
        self.assertEqual(13, max)
        self.assert_min_max_solutions(min, max, min_solution, max_solution,
            '((3)+((4)*(2-1)))', '(((3+4)*(2))-(1))')

    def test_with_4_plus_1_times_2_minus_3(self):
        min, max, min_solution, max_solution = get_min_max('4+1*2-3')
        self.assertEqual(-5, min)
        self.assertEqual(7, max)
        self.assert_min_max_solutions(min, max, min_solution, max_solution,
            '((4+1)*(2-3))', '(((4+1)*(2))-(3))')

    def test_with_4_plus_1_times_3_minus_2(self):
        min, max, min_solution, max_solution = get_min_max('4+1*3-2')
        self.assertEqual(5, min)
        self.assertEqual(13, max)
        self.assert_min_max_solutions(min, max, min_solution, max_solution,
            '((4)+((1)*(3-2)))', '(((4+1)*(3))-(2))')

    def test_with_4_plus_2_times_1_minus_3(self):
        min, max, min_solution, max_solution = get_min_max('4+2*1-3')
        self.assertEqual(-12, min)
        self.assertEqual(3, max)
        self.assert_min_max_solutions(min, max, min_solution, max_solution,
            '((4+2)*(1-3))', '((4)+((2*1)-(3)))')

    def test_with_4_plus_2_times_3_minus_1(self):
        min, max, min_solution, max_solution = get_min_max('4+2*3-1')
        self.assertEqual(8, min)
        self.assertEqual(17, max)
        self.assert_min_max_solutions(min, max, min_solution, max_solution,
            '((4)+((2)*(3-1)))', '(((4+2)*(3))-(1))')

    def test_with_4_plus_3_times_1_minus_2(self):
        min, max, min_solution, max_solution = get_min_max('4+3*1-2')
        self.assertEqual(-7, min)
        self.assertEqual(5, max)
        self.assert_min_max_solutions(min, max, min_solution, max_solution,
            '((4+3)*(1-2))', '((4)+((3*1)-(2)))')

    def test_with_4_plus_3_times_2_minus_1(self):
        min, max, min_solution, max_solution = get_min_max('4+3*2-1')
        self.assertEqual(7, min)
        self.assertEqual(13, max)
        self.assert_min_max_solutions(min, max, min_solution, max_solution,
            '((4)+((3)*(2-1)))', '(((4+3)*(2))-(1))')

    def test_with_1_plus_2_minus_3_times_4_minus_5(self):
        min, max, min_solution, max_solution = get_min_max('1+2-3*4-5')
        self.assertEqual(-14, min)
        self.assertEqual(6, max)
        self.assert_min_max_solutions(min, max, min_solution, max_solution,
            '((1)+(((2)-(3*4))-(5)))', '((1)+((2)-((3)*(4-5))))')

    def test_with_5_minus_8_plus_7_times_4_minus_8_plus_9(self):
        min, max, min_solution, max_solution = get_min_max('5-8+7*4-8+9')
        self.assertEqual(-94, min)
        self.assertEqual(200, max)
        self.assert_min_max_solutions(min, max, min_solution, max_solution,
            '((5-8)+((7)*((4)-(8+9))))', '((5)-((8+7)*((4)-(8+9))))')

    def test_with_1_minus_2_times_3_minus_4(self):
        min, max, min_solution, max_solution = get_min_max('1-2*3-4')
        self.assertEqual(-9, min)
        self.assertEqual(3, max)
        self.assert_min_max_solutions(min, max, min_solution, max_solution,
            '(((1)-(2*3))-(4))', '((1)-((2)*(3-4)))')

    def test_with_1_minus_2_times_2_minus_3_minus_4(self):
        min, max, min_solution, max_solution = get_min_max('1-2*2-3-4')
        self.assertEqual(-10, min)
        self.assertEqual(11, max)
        self.assert_min_max_solutions(min, max, min_solution, max_solution,
            '((((1)-(2*2))-(3))-(4))', '((1)-((2)*((2-3)-(4))))')

    def test_with_1_minus_2_times_2_plus_3_minus_4(self):
        min, max, min_solution, max_solution = get_min_max('1-2*2+3-4')
        self.assertEqual(-13, min)
        self.assertEqual(-1, max)
        self.assert_min_max_solutions(min, max, min_solution, max_solution,
            '(((1)-((2)*(2+3)))-(4))', '((1)-((2)*((2)+(3-4))))')

    def test_with_1_minus_4_times_2_times_2_minus_1(self):
        min, max, min_solution, max_solution = get_min_max('1-4*2*2-1')
        self.assertEqual(-16, min)
        self.assertEqual(-6, max)
        self.assert_min_max_solutions(min, max, min_solution, max_solution,
            '(((1)-((4)*(2*2)))-(1))', '((1-4)*((2)*(2-1)))')

if __name__ == '__main__':
    unittest.main()
