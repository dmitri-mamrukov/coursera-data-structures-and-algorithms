#!/usr/bin/python3

import binary_search_tree

if __name__ == '__main__':
    tree = binary_search_tree.BinarySearchTree()
    tree[3] = "red"
    tree[4] = "blue"
    tree[6] = "yellow"
    tree[2] = "at"

    print(tree[6])
    print(tree[2])
