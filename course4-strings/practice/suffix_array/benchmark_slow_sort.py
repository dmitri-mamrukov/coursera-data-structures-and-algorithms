#!/usr/bin/python3

import suffix_array

if __name__ == '__main__':
    text = input()

    result = suffix_array.Util.construct_suffix_array(text)

    print(result)
