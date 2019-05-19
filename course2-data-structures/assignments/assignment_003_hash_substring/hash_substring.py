#!/usr/bin/python3

import random

class SearchPattern:

    @staticmethod
    def poly_hash(text, p, x):
        """
        p is a fixed prime.
        1 <= x <= p - 1.
        """
        hash = 0
        for ch in reversed(text):
            hash = (hash * x + ord(ch)) % p

        return hash

    @staticmethod
    def precompute_hashes(text, pattern_len, p, x):
        """
        p is a fixed prime.
        1 <= x <= p - 1.
        """

        if len(text) < pattern_len or pattern_len == 0:
            return []

        hashes = [ 0 ] * (len(text) - pattern_len + 1)

        slice = text[len(text) - pattern_len:]
        hashes[len(text) - pattern_len] = SearchPattern.poly_hash(
            slice, p, x)

        y = 1
        for i in range(1, pattern_len + 1):
            y = (y * x) % p
        for i in range(len(text) - pattern_len - 1, -1, -1):
            hashes[i] = (x * hashes[i + 1] + ord(text[i]) -
                y * ord(text[i + pattern_len])) % p

        return hashes

    @staticmethod
    def rabin_karp_match(text='', pattern=''):
        p = 10000019
        x = random.randint(1, p - 1)
        text_len = len(text)
        pattern_len = len(pattern)

        offsets = []

        pattern_hash = SearchPattern.poly_hash(pattern, p, x)
        for i in range(0, text_len - pattern_len + 1):
            slice = text[i:i + pattern_len]
            text_hash = SearchPattern.poly_hash(slice, p, x)
            if pattern_hash != text_hash:
                continue
            if slice == pattern:
                offsets.append(i)

        return offsets

    @staticmethod
    def precomputed_rabin_karp_match(text='', pattern=''):
        p = 10000019
        x = random.randint(1, p - 1)
        text_len = len(text)
        pattern_len = len(pattern)

        offsets = []

        pattern_hash = SearchPattern.poly_hash(pattern, p, x)
        hashes = SearchPattern.precompute_hashes(text, len(pattern), p, x)
        for i in range(0, text_len - pattern_len + 1):
            if len(hashes) > 0 and pattern_hash != hashes[i]:
                continue
            if text[i:i + pattern_len] == pattern:
                offsets.append(i)

        return offsets

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    return SearchPattern.precomputed_rabin_karp_match(text, pattern)

def get_occurrences_still_slow(pattern, text):
    return SearchPattern.rabin_karp_match(text, pattern)

def get_occurrences_slow(pattern, text):
    return \
    [
        i
        for i in range(len(text) - len(pattern) + 1)
        if text[i:i + len(pattern)] == pattern
    ]

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
