#!/usr/bin/python3

def edit_distance(word1, word2):
    """Our goal is to find the edit distance between two strings
    x[1...m] and y[1...n].

    The cost of an alignment is the number of columns in which the letters
    differ. And the edit distance between two strings is the cost of their
    best possible alignment.
    """
    # construct a matrix whose last element is the edit distance
    x = [[ 0 ] * (len(word2) + 1) for i in range(0, len(word1) + 1)]

    # initialization of base case values
    for i in range(0, len(word1) + 1):
        x[i][0] = i
    for j in range(0, len(word2) + 1):
        x[0][j] = j

    for i in range (1, len(word1) + 1):
        for j in range(1, len(word2) + 1):
            if word1[i - 1] == word2[j - 1]:
                x[i][j] = x[i - 1][j - 1]
            else:
                x[i][j] = min(x[i][j - 1], x[i - 1][j], x[i - 1][j - 1]) + 1

    return x[i][j]

if __name__ == "__main__":
    word1 = input()
    word2 = input()
    print(edit_distance(word1, word2))
