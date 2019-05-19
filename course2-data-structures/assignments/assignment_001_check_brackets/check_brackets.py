#!/usr/bin/python3

import sys

class Bracket:

    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True

        return False

OPENING_BRACKETS = [ '(', '[', '{' ]
CLOSING_BRACKETS = [ ')', ']', '}' ]

def is_balanced(text):
    """If the text uses brackets correctly, output True. Otherwise, output:
      - the 1-based index of the first unmatched closing bracket, and
      - if there are no unmatched closing brackets, output the 1-based index
        of the first unmatched opening bracket.
    """
    stack = []

    for i, next in enumerate(text):
        if next in OPENING_BRACKETS:
            stack.append(Bracket(next, i + 1))
        elif next in CLOSING_BRACKETS:
            if len(stack) == 0:
                return i + 1
            top = stack.pop(-1)
            if top.match(next):
                continue
            else:
                return i + 1

    return True if len(stack) == 0 else stack[-1].position

def process(text):
    result = is_balanced(text)

    if isinstance(result, bool) and result == True:
        return 'Success'
    else:
        return result

if __name__ == '__main__':
    text = sys.stdin.read().strip()

    print(process(text))
