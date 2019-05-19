#!/usr/bin/python3

import unittest

from check_brackets import is_balanced

class CheckBracketsTestCase(unittest.TestCase):

    def test_with_empty(self):
        text = ''
        self.assertTrue(is_balanced(text))

    def test_with_opening_parenthesis(self):
        text = '('
        self.assertEqual(1, is_balanced(text))

    def test_with_opening_bracket(self):
        text = '['
        self.assertEqual(1, is_balanced(text))

    def test_with_opening_curly_bracket(self):
        text = '{'
        self.assertEqual(1, is_balanced(text))

    def test_with_one_char_and_opening_parenthesis(self):
        text = 'a('
        self.assertEqual(2, is_balanced(text))

    def test_with_one_char_and_opening_bracket(self):
        text = 'a['
        self.assertEqual(2, is_balanced(text))

    def test_with_one_char_and_opening_curly_bracket(self):
        text = 'a{'
        self.assertEqual(2, is_balanced(text))

    def test_with_two_chars_and_opening_parenthesis(self):
        text = 'ab('
        self.assertEqual(3, is_balanced(text))

    def test_with_two_chars_and_opening_bracket(self):
        text = 'ab['
        self.assertEqual(3, is_balanced(text))

    def test_with_two_chars_and_opening_curly_bracket(self):
        text = 'ab{'
        self.assertEqual(3, is_balanced(text))

    def test_with_three_chars_and_opening_parenthesis(self):
        text = 'abc('
        self.assertEqual(4, is_balanced(text))

    def test_with_three_chars_and_opening_bracket(self):
        text = 'abc['
        self.assertEqual(4, is_balanced(text))

    def test_with_three_chars_and_opening_curly_bracket(self):
        text = 'abc{'
        self.assertEqual(4, is_balanced(text))

    def test_with_opening_parenthesis_and_one_char(self):
        text = '(a'
        self.assertEqual(1, is_balanced(text))

    def test_with_opening_bracket_and_one_char(self):
        text = '[a'
        self.assertEqual(1, is_balanced(text))

    def test_with_opening_curly_bracket_and_one_char(self):
        text = '{a'
        self.assertEqual(1, is_balanced(text))

    def test_with_opening_parenthesis_and_two_chars(self):
        text = '(ab'
        self.assertEqual(1, is_balanced(text))

    def test_with_opening_bracket_and_two_chars(self):
        text = '[ab'
        self.assertEqual(1, is_balanced(text))

    def test_with_opening_curly_bracket_and_two_chars(self):
        text = '{ab'
        self.assertEqual(1, is_balanced(text))

    def test_with_opening_parenthesis_and_three_chars(self):
        text = '(abc'
        self.assertEqual(1, is_balanced(text))

    def test_with_opening_bracket_and_three_chars(self):
        text = '[abc'
        self.assertEqual(1, is_balanced(text))

    def test_with_opening_curly_bracket_and_three_chars(self):
        text = '{abc'
        self.assertEqual(1, is_balanced(text))

    def test_with_one_char_and_opening_parenthesis_and_one_char(self):
        text = 'a(b'
        self.assertEqual(2, is_balanced(text))

    def test_with_one_char_and_opening_bracket_and_one_char(self):
        text = 'a[b'
        self.assertEqual(2, is_balanced(text))

    def test_with_one_char_and_opening_curly_bracket_and_one_char(self):
        text = 'a{b'
        self.assertEqual(2, is_balanced(text))

    def test_with_two_chars_and_opening_parenthesis_and_two_chars(self):
        text = 'ab(cd'
        self.assertEqual(3, is_balanced(text))

    def test_with_two_chars_and_opening_bracket_and_two_chars(self):
        text = 'ab[cd'
        self.assertEqual(3, is_balanced(text))

    def test_with_two_chars_and_opening_curly_bracket_and_two_chars(self):
        text = 'ab{cd'
        self.assertEqual(3, is_balanced(text))

    def test_with_three_chars_and_opening_parenthesis_and_three_chars(self):
        text = 'abc(def'
        self.assertEqual(4, is_balanced(text))

    def test_with_three_chars_and_opening_bracket_and_three_chars(self):
        text = 'abc[def'
        self.assertEqual(4, is_balanced(text))

    def test_with_three_chars_and_opening_curly_bracket_and_three_chars(self):
        text = 'abc{def'
        self.assertEqual(4, is_balanced(text))

    def test_with_closing_parenthesis(self):
        text = ')'
        self.assertEqual(1, is_balanced(text))

    def test_with_closing_bracket(self):
        text = ']'
        self.assertEqual(1, is_balanced(text))

    def test_with_closing_curly_bracket(self):
        text = '}'
        self.assertEqual(1, is_balanced(text))

    def test_with_one_char_and_closing_parenthesis(self):
        text = 'a)'
        self.assertEqual(2, is_balanced(text))

    def test_with_one_char_and_closing_bracket(self):
        text = 'a]'
        self.assertEqual(2, is_balanced(text))

    def test_with_one_char_and_closing_curly_bracket(self):
        text = 'a}'
        self.assertEqual(2, is_balanced(text))

    def test_with_two_chars_and_closing_parenthesis(self):
        text = 'ab)'
        self.assertEqual(3, is_balanced(text))

    def test_with_two_chars_and_closing_bracket(self):
        text = 'ab]'
        self.assertEqual(3, is_balanced(text))

    def test_with_two_chars_and_closing_curly_bracket(self):
        text = 'ab}'
        self.assertEqual(3, is_balanced(text))

    def test_with_three_chars_and_closing_parenthesis(self):
        text = 'abc)'
        self.assertEqual(4, is_balanced(text))

    def test_with_three_chars_and_closing_bracket(self):
        text = 'abc]'
        self.assertEqual(4, is_balanced(text))

    def test_with_three_chars_and_closing_curly_bracket(self):
        text = 'abc}'
        self.assertEqual(4, is_balanced(text))

    def test_with_closing_parenthesis_and_one_char(self):
        text = ')a'
        self.assertEqual(1, is_balanced(text))

    def test_with_closing_bracket_and_one_char(self):
        text = ']a'
        self.assertEqual(1, is_balanced(text))

    def test_with_closing_curly_bracket_and_one_char(self):
        text = '}a'
        self.assertEqual(1, is_balanced(text))

    def test_with_closing_parenthesis_and_two_chars(self):
        text = ')ab'
        self.assertEqual(1, is_balanced(text))

    def test_with_closing_bracket_and_two_chars(self):
        text = ']ab'
        self.assertEqual(1, is_balanced(text))

    def test_with_closing_curly_bracket_and_two_chars(self):
        text = '}ab'
        self.assertEqual(1, is_balanced(text))

    def test_with_opening_parenthesis_and_three_chars(self):
        text = ')abc'
        self.assertEqual(1, is_balanced(text))

    def test_with_closing_bracket_and_three_chars(self):
        text = ']abc'
        self.assertEqual(1, is_balanced(text))

    def test_with_closing_curly_bracket_and_three_chars(self):
        text = '}abc'
        self.assertEqual(1, is_balanced(text))

    def test_with_one_char_and_closing_parenthesis_and_one_char(self):
        text = 'a)b'
        self.assertEqual(2, is_balanced(text))

    def test_with_one_char_and_closing_bracket_and_one_char(self):
        text = 'a]b'
        self.assertEqual(2, is_balanced(text))

    def test_with_one_char_and_closing_curly_bracket_and_one_char(self):
        text = 'a}b'
        self.assertEqual(2, is_balanced(text))

    def test_with_two_chars_and_closing_parenthesis_and_two_chars(self):
        text = 'ab)cd'
        self.assertEqual(3, is_balanced(text))

    def test_with_two_chars_and_closing_bracket_and_two_chars(self):
        text = 'ab]cd'
        self.assertEqual(3, is_balanced(text))

    def test_with_two_chars_and_closing_curly_bracket_and_two_chars(self):
        text = 'ab}cd'
        self.assertEqual(3, is_balanced(text))

    def test_with_three_chars_and_closing_parenthesis_and_three_chars(self):
        text = 'abc)def'
        self.assertEqual(4, is_balanced(text))

    def test_with_three_chars_and_closing_bracket_and_three_chars(self):
        text = 'abc]def'
        self.assertEqual(4, is_balanced(text))

    def test_with_three_chars_and_closing_curly_bracket_and_three_chars(self):
        text = 'abc}def'
        self.assertEqual(4, is_balanced(text))

    def test_with_matched_parentheses(self):
        text = '()'
        self.assertTrue(is_balanced(text))

    def test_with_matched_brackets(self):
        text = '[]'
        self.assertTrue(is_balanced(text))

    def test_with_matched_curly_brackets(self):
        text = '{}'
        self.assertTrue(is_balanced(text))

    def test_with_one_char_and_matched_parentheses(self):
        text = 'a()'
        self.assertTrue(is_balanced(text))

    def test_with_one_char_and_matched_brackets(self):
        text = 'a[]'
        self.assertTrue(is_balanced(text))

    def test_with_one_char_and_matched_curly_brackets(self):
        text = 'a{}'
        self.assertTrue(is_balanced(text))

    def test_with_two_chars_and_matched_parentheses(self):
        text = 'ab()'
        self.assertTrue(is_balanced(text))

    def test_with_two_chars_and_matched_brackets(self):
        text = 'ab[]'
        self.assertTrue(is_balanced(text))

    def test_with_two_chars_and_matched_curly_brackets(self):
        text = 'ab{}'
        self.assertTrue(is_balanced(text))

    def test_with_three_chars_and_matched_parentheses(self):
        text = 'abc()'
        self.assertTrue(is_balanced(text))

    def test_with_three_chars_and_matched_brackets(self):
        text = 'abc[]'
        self.assertTrue(is_balanced(text))

    def test_with_three_chars_and_matched_curly_brackets(self):
        text = 'abc{}'
        self.assertTrue(is_balanced(text))

    def test_with_matched_parentheses_and_one_char(self):
        text = '()a'
        self.assertTrue(is_balanced(text))

    def test_with_matched_brackets_and_one_char(self):
        text = '[]a'
        self.assertTrue(is_balanced(text))

    def test_with_matched_curly_brackets_and_one_char(self):
        text = '{}a'
        self.assertTrue(is_balanced(text))

    def test_with_matched_parentheses_and_two_chars(self):
        text = '()ab'
        self.assertTrue(is_balanced(text))

    def test_with_matched_brackets_and_two_chars(self):
        text = '[]ab'
        self.assertTrue(is_balanced(text))

    def test_with_matched_curly_brackets_and_two_chars(self):
        text = '{}ab'
        self.assertTrue(is_balanced(text))

    def test_with_matched_parentheses_and_three_chars(self):
        text = '()abc'
        self.assertTrue(is_balanced(text))

    def test_with_matched_brackets_and_three_chars(self):
        text = '[]abc'
        self.assertTrue(is_balanced(text))

    def test_with_matched_curly_brackets_and_three_chars(self):
        text = '{}abc'
        self.assertTrue(is_balanced(text))

    def test_with_one_char_and_matched_parentheses_and_one_char(self):
        text = 'a()b'
        self.assertTrue(is_balanced(text))

    def test_with_one_char_and_matched_brackets_and_one_char(self):
        text = 'a[]b'
        self.assertTrue(is_balanced(text))

    def test_with_one_char_and_matched_curly_brackets_and_one_char(self):
        text = 'a{}b'
        self.assertTrue(is_balanced(text))

    def test_with_two_chars_and_matched_parentheses_and_two_chars(self):
        text = 'ab()cd'
        self.assertTrue(is_balanced(text))

    def test_with_two_chars_and_matched_brackets_and_two_chars(self):
        text = 'ab[]cd'
        self.assertTrue(is_balanced(text))

    def test_with_two_chars_and_matched_curly_brackets_and_two_chars(self):
        text = 'ab{}cd'
        self.assertTrue(is_balanced(text))

    def test_with_three_chars_and_matched_parentheses_and_three_chars(self):
        text = 'abc()def'
        self.assertTrue(is_balanced(text))

    def test_with_three_chars_and_matched_brackets_and_three_chars(self):
        text = 'abc[]def'
        self.assertTrue(is_balanced(text))

    def test_with_three_chars_and_matched_curly_brackets_and_three_chars(self):
        text = 'abc{}def'
        self.assertTrue(is_balanced(text))

    def test_with_matched_parentheses_and_brackets(self):
        text = '()[]'
        self.assertTrue(is_balanced(text))

    def test_with_matched_parentheses_and_curly_brackets(self):
        text = '(){}'
        self.assertTrue(is_balanced(text))

    def test_with_matched_curly_brackets_and_parentheses(self):
        text = '{}()'
        self.assertTrue(is_balanced(text))

    def test_with_matched_curly_brackets_and_brackets(self):
        text = '{}[]'
        self.assertTrue(is_balanced(text))

    def test_with_matched_brackets_and_parentheses(self):
        text = '[]()'
        self.assertTrue(is_balanced(text))

    def test_with_matched_brackets_and_curly_brackets(self):
        text = '[]{}'
        self.assertTrue(is_balanced(text))

    def test_with_matched_parentheses_and_brackets_and_curly_brackets(self):
        text = '()[]{}'
        self.assertTrue(is_balanced(text))

    def test_with_matched_parentheses_and_curly_brackets_and_brackets(self):
        text = '(){}[]'
        self.assertTrue(is_balanced(text))

    def test_with_matched_brackets_and_parentheses_and_curly_brackets(self):
        text = '[](){}'
        self.assertTrue(is_balanced(text))

    def test_with_matched_brackets_and_curly_brackets_and_parentheses(self):
        text = '[]{}()'
        self.assertTrue(is_balanced(text))

    def test_with_matched_curly_brackets_and_parentheses_and_brackets(self):
        text = '{}()[]'
        self.assertTrue(is_balanced(text))

    def test_with_matched_curly_brackets_and_brackets_and_parentheses(self):
        text = '{}[]()'
        self.assertTrue(is_balanced(text))

    def test_with_matched_nested_parentheses_and_brackets(self):
        text = '([])'
        self.assertTrue(is_balanced(text))

    def test_with_matched_nested_parentheses_and_curly_brackets(self):
        text = '({})'
        self.assertTrue(is_balanced(text))

    def test_with_matched_nested_brackets_and_parentheses(self):
        text = '[()]'
        self.assertTrue(is_balanced(text))

    def test_with_matched_nested_brackets_and_curly_brackets(self):
        text = '[{}]'
        self.assertTrue(is_balanced(text))

    def test_with_matched_curly_brackets_and_parentheses(self):
        text = '{()}'
        self.assertTrue(is_balanced(text))

    def test_with_matched_curly_brackets_and_brackets(self):
        text = '{[]}'
        self.assertTrue(is_balanced(text))

    def test_with_matched_parentheses_and_curly_brackets_and_brackets(self):
        text = '({[]})'
        self.assertTrue(is_balanced(text))

    def test_with_matched_parentheses_and_brackets_and_curly_brackets(self):
        text = '([{}])'
        self.assertTrue(is_balanced(text))

    def test_with_matched_curly_brackets_and_parentheses_and_brackets(self):
        text = '{([])}'
        self.assertTrue(is_balanced(text))

    def test_with_matched_curly_brackets_and_brackets_and_parentheses(self):
        text = '{[()]}'
        self.assertTrue(is_balanced(text))

    def test_with_matched_brackets_and_parentheses_and_curly_brackets(self):
        text = '[({})]'
        self.assertTrue(is_balanced(text))

    def test_with_matched_brackets_and_curly_brackets_and_parentheses(self):
        text = '[{()}]'
        self.assertTrue(is_balanced(text))

    def test_with_matched_parentheses_and_parentheses(self):
        text = '(())'
        self.assertTrue(is_balanced(text))

    def test_with_matched_brackets_and_brackets(self):
        text = '[[]]'
        self.assertTrue(is_balanced(text))

    def test_with_matched_curly_brackets_and_curly_brackets(self):
        text = '{{}}'
        self.assertTrue(is_balanced(text))

    def test_with_nested_brackets_and_separate_brackets(self):
        text = '{[]}()'
        self.assertTrue(is_balanced(text))

    def test_with_unmatched_nested_parenthesis(self):
        text = '{(}'
        self.assertEqual(3, is_balanced(text))

    def test_with_unmatched_nested_bracket(self):
        text = '{[}'
        self.assertEqual(3, is_balanced(text))

    def test_with_unmatched_nested_curly_bracket(self):
        text = '({)'
        self.assertEqual(3, is_balanced(text))

    def test_with_unmatched_closing_bracket_in_beginning(self):
        text = '}()'
        self.assertEqual(1, is_balanced(text))

    def test_with_unmatched_closing_bracket_in_middle(self):
        text = '()}()'
        self.assertEqual(3, is_balanced(text))

    def test_with_unmatched_closing_bracket_in_end(self):
        text = '()}'
        self.assertEqual(3, is_balanced(text))

    def test_with_unmatched_opening_bracket_in_beginning(self):
        text = '(()[]'
        self.assertEqual(1, is_balanced(text))

    def test_with_unmatched_opening_bracket_in_middle(self):
        text = '(){[()'
        self.assertEqual(4, is_balanced(text))

    def test_with_unmatched_opening_bracket_in_end(self):
        text = '(){['
        self.assertEqual(4, is_balanced(text))

    def test_with_unmatched_nested_curly_bracket(self):
        text = 'foo(bar);'
        self.assertTrue(is_balanced(text))

    def test_with_function_and_parameter(self):
        text = 'foo(bar);'
        self.assertTrue(is_balanced(text))

    def test_with_function_and_parameter_as_array_element(self):
        text = 'foo(bar[i]);'
        self.assertTrue(is_balanced(text))

    def test_with_function_and_parameter_as_unmatched_array_element(self):
        text = 'foo(bar[i);'
        self.assertEqual(10, is_balanced(text))

    def test_with_function_calls(self):
        text = 'f(a,b)-g[c]'
        self.assertTrue(is_balanced(text))

    def test_with_array_reference(self):
        text = 'foo[bar]'
        self.assertTrue(is_balanced(text))

if __name__ == '__main__':
    unittest.main()
