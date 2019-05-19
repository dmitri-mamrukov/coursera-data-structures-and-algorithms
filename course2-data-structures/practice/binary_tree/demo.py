#!/usr/bin/python3

from tree import TreeNode

if __name__ == '__main__':
    root = TreeNode('Harry')
    node1 = root.set_left('Jane')
    node11 = node1.set_left('Jog')
    node12 = node1.set_right('Diane')
    node121 = node12.set_left('George')
    node1211 = node121.set_left('Jill')
    node12111 = node1211.set_left('Carol')
    node122 = node12.set_right('Mary')
    node2 = root.set_right('Bill')
    node21 = node2.set_left('Grace')

    root.display()

    print('***** DEPTH-FIRST GENERATOR ITERATION *****')
    for node in root.depth_first_traverse_gen():
        print(node)

    print('***** DEPTH-FIRST ITERATION *****')
    root.depth_first_traverse(print)

    print('***** BREADTH-FIRST GENERATOR ITERATION *****')
    for node in root.breadth_first_traverse_gen():
        print(node)

    print('***** BREADTH-FIRST ITERATION *****')
    root.breadth_first_traverse(print)

    print('***** HEIGHT *****')
    print(node12111.height)
    print(node1211.height)
    print(node121.height)
    print(node122.height)
    print(node11.height)
    print(node12.height)
    print(node1.height)
    print(node2.height)
    print(node21.height)
    print(root.height)

    print('***** SIZE *****')
    print(node12111.size)
    print(node1211.size)
    print(node121.size)
    print(node122.size)
    print(node11.size)
    print(node12.size)
    print(node1.size)
    print(node2.size)
    print(node21.size)
    print(root.size)
