#!/usr/bin/python3

def make_2d_list(rows, cols):
    a = []
    for row in range(rows):
        a += [[ 0 ] * cols]

    return a

if __name__ == '__main__':
    rows = 3
    cols = 5
    matrix = make_2d_list(rows, cols);

    val = 0
    for row in range(rows):
        for col in range(cols):
            matrix[row][col] = val
            val += 1

    print('indices/contents:')
    for row in range(rows):
        for col in range(cols):
            print('a(%s, %s) = %s' % (row, col, matrix[row][col]), end = ' ')
        print()

    print('matrix:')
    print(matrix)
