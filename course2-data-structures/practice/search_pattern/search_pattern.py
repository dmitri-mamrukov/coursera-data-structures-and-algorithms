import random

class SearchPattern:

    @staticmethod
    def are_equal(s1, s2):
        if len(s1) != len(s2):
            return False

        for i in range(0, len(s1)):
            if s1[i] != s2[i]:
                return False

        return True

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
    def search_pattern_with_naive_match(text='', pattern=''):
        """Returns positions where the pattern is found in the text.

        We slide the string to match 'pattern' over the text
        O((n - m) * m)

        Example: For text = 'ababbababa', pattern = 'aba',
                 returns [ 0, 5, 7 ]
        @param text the string to search for the pattern
        @param pattern the string to search for
        @return a list containing offsets, where the pattern is
        found inside the text
        """

        n = len(text)
        m = len(pattern)
        offsets = []
        for i in range(n - m + 1):
            if pattern == text[i:i + m]:
                offsets.append(i)

        return offsets

    @staticmethod
    def search_pattern_with_rabin_karp_match(text='', pattern=''):
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
    def search_pattern_with_precomputed_rabin_karp_match(text='', pattern=''):
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
