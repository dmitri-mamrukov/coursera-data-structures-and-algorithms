from functools import cmp_to_key

class Util():

    @staticmethod
    def _cyclic_rotation_character(word, i, n):
        """
        Returns the nth character of the cyclic rotation (to the right)
        by i characters.

        Note: Negative indices mean those from the right end. For example, -1
        references the first element from the end, -2 the second from the end,
        -3 the third from the end, and so on.
        """

        return word[n - i % len(word)]

    @staticmethod
    def _cyclic_compare(word, i, j):
        """
        Compares cyclic rotations without generating the entire rotation.
        """

        length = len(word)
        n = 0
        while n < length:
            i_char = Util._cyclic_rotation_character(word, i, n)
            j_char = Util._cyclic_rotation_character(word, j, n)
            if i_char == j_char:
                n += 1
            elif i_char < j_char:
                return -1
            else:
                return 1

        return 0

    @staticmethod
    def _cyclic_sort(word):
        """
        Sorts the cyclic rotations based on their shift.
        """

        length = len(word)
        shifts = range(length)
        return sorted(shifts,
                      key=cmp_to_key(lambda i, j:
                                     Util._cyclic_compare(word, i, j)))

    @staticmethod
    def _enumerate_word(word):
        """
        Enumerates the same characters in the order of their appearance in
        the given word.

        For example,

        'abcbba' returns ['a0', 'b0', 'c0', 'b1', 'b2', 'a1']
        """

        char_count = {}
        enumerated_cars = []

        for ch in word:
            if ch not in char_count:
                char_count[ch] = 0
            else:
                char_count[ch] += 1

            enumerated_cars.append(ch + str(char_count[ch]))

        return enumerated_cars

    @staticmethod
    def _burrows_wheeler_matching(transform_word, last_to_first, pattern):
        """
        Counts the number of occurrences of a given pattern in the original
        text, which is inferred from the Burrows-Wheeler Transform text.

        The Last-to-First array, denoted LastToFirst(i), answers the following
        question: given a symbol at position i in LastColumn, what is its
        position in FirstColumn?

        For example, if Text = panamabananas$, BWT(Text) = smnpbnnaaaaa$a,
        FirstCol(Text) = $aaaaaabmnnnps, then we can rewrite
        BWT(Text) = s1m1n1p1b1n2n3a1a2a3a4a5$1a6 and FirstCol(Text) =
        $1a1a2a3a4a5a6b1m1n1n2n3p1s1, and now we see that a3 in BWT(Text)
        corresponds to a3 in FirstCol(Text).

        Note: The last column as cited below means the Burrows-Wheeler
        Transform text.
        """

        top = 0
        bottom = len(transform_word) - 1
        while top <= bottom:
            if pattern != '':
                # The last char in the pattern.
                symbol = pattern[-1]
                # Remove the last char from the pattern.
                pattern = pattern[:-1]
                # Check if the positions from the top to the bottom in the
                # last column (the transform word) contain the symbol.
                part = transform_word[top:bottom + 1]
                if symbol in part:
                    reverse_part = part[::-1]
                    # The first position of the symbol among positions from the
                    # top to the bottom in the last column (the transform word).
                    top_index = top + part.index(symbol)
                    # The last position of the symbol among positions from the
                    # top to the bottom in the last column (the transform word).
                    bottom_index = bottom - reverse_part.index(symbol)
                    top = last_to_first[top_index]
                    bottom = last_to_first[bottom_index]
                else:
                    return 0
            else:
                return bottom - top + 1

    def _better_burrows_wheeler_matching(transform_word,
                                         first_occurrence,
                                         count,
                                         pattern):
        """
        Counts the number of occurrences of a given pattern in the original
        text, which is inferred from the Burrows-Wheeler Transform text.

        The original Burrows-Wheeler Matching algorithm is slow. The reason for
        its sluggishness is that updating the pointers top and bottom is
        time-intensive, since it requires examining every symbol in LastColumn
        between top and bottom at each step. To improve the algorithm, we
        introduce a function Count symbol (i, LastColumn), which returns the
        number of occurrences of symbol in the first i positions of LastColumn.

        For example,

        Count 'n' (10, smnpbnnaaaaa$a) = 3 and
        Count 'a' (4, smnpbnnaaaaa$a) = 0.

        Define FirstOccurrence(symbol) as the first position of symbol in
        FirstColumn.

        If Text = panamabananas$, then FirstColumn is $aaaaaabmnnnps, and the
        array holding all values of FirstOccurrence is [0, 1, 7, 8, 9, 12, 13]
        because there are 7 distinct chars $, a, b, m, n, p, and s.

        For DNA strings of any length, the array FirstOccurrence contains only
        five elements.
        """

        top = 0
        bottom = len(transform_word) - 1
        while top <= bottom:
            if pattern != '':
                # The last char in the pattern.
                symbol = pattern[-1]
                # Remove the last char from the pattern.
                pattern = pattern[:-1]
                # Check if the positions from the top to the bottom in the
                # last column (the transform word) contain the symbol.
                if symbol in transform_word[top:bottom + 1]:
                    top = first_occurrence[symbol] + count[top][symbol]
                    bottom = (first_occurrence[symbol] +
                              count[bottom + 1][symbol] - 1)
                else:
                    return 0
            else:
                return bottom - top + 1

    @staticmethod
    def burrows_wheeler_transform(word):
        """
        Collects characters corresponding to the last indices of cyclic
        rotations in the sorted order and returns them as a string.
        """

        cyclic_sort = Util._cyclic_sort(word)
        last_index_chars = [Util._cyclic_rotation_character(word, i, -1)
                            for i in cyclic_sort]
        return ''.join(last_index_chars)

    @staticmethod
    def inverse_burrows_wheeler_transform(transform_word):
        """
        Returns the inverse transform of the Burrows-Wheeler Transform text.
        """

        enumerated_word = Util._enumerate_word(transform_word)
        enumerated_sorted_word = Util._enumerate_word(sorted(transform_word))

        # Make a mapping between the enumerated characters at each index of the
        # enumerated Burrows-Wheeler Transform text and its sorted version.
        char_indices = range(len(transform_word))
        inverse_map = {}
        for i in char_indices:
            inverse_map[enumerated_word[i]] = enumerated_sorted_word[i]

        # Make the inverse Burrows-Wheeler Transform text by a traversal
        # through the inverse map.
        inverse_word = ''
        current_char = enumerated_word[0]
        for i in char_indices:
            current_char = inverse_map[current_char]
            inverse_word += current_char[0]

        # The actual inverse word must end in the marker char, so shift the
        # sequence to the left by one.
        marker_char = inverse_word[0]
        actual_inverse_word = inverse_word[1:] + marker_char

        return actual_inverse_word

    @staticmethod
    def get_pattern_count(transform_word, patterns):
        """
        Precomputes the necessary information for Burrows-Wheeler Matching on
        each pattern.
        """

        # The first column is just the sorted Burrows-Wheeler Transform.
        # Perform enumeration on characters in the first and last column.
        first_column = Util._enumerate_word(sorted(transform_word))
        last_column = Util._enumerate_word(transform_word)

        # Get the last-to-first property values.
        indices = range(len(transform_word))
        last_to_first = list(map(lambda i: first_column.index(last_column[i]),
                                 indices))

        # Perform Burrows-Wheeler Matching on each pattern, using the
        # precomputed information.
        result = []
        for pattern in patterns:
            result.append(Util._burrows_wheeler_matching(transform_word,
                                                         last_to_first,
                                                         pattern))

        return result

    def get_pattern_count_better(transform_word, patterns):
        """
        Precomputes the necessary information for Better Burrows-Wheeler
        Matching on each pattern.
        """

        symbols = set(transform_word)

        # Create the count map.
        current_count = {}
        for ch in symbols:
            current_count[ch] = 0
        count = { 0: {} }
        for ch in symbols:
            count[0][ch] = current_count[ch]

        for i in range(len(transform_word)):
            current_count[transform_word[i]] += 1
            count[i + 1] = {ch: current_count[ch] for ch in symbols}

        # Get the index of the first occurrence of each character in the
        # sorted Burrows-Wheeler Transform word.
        sorted_transform_word = sorted(transform_word)
        first_occurrence = {}
        for ch in symbols:
            first_occurrence[ch] = sorted_transform_word.index(ch)

        # Perform Burrows-Wheeler Matching on each pattern, using the
        # precomputed information.
        result = []
        for pattern in patterns:
            result.append(Util._better_burrows_wheeler_matching(
                                                               transform_word,
                                                               first_occurrence,
                                                               count,
                                                               pattern))

        return result
