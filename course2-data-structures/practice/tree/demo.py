#!/usr/bin/python3

from tree import TreeNode

if __name__ == '__main__':
    root = TreeNode('Harry')
    node1 = root.add_child('Jane')
    node11 = node1.add_child('Jog')
    node12 = node1.add_child('Diane')
    node121 = node12.add_child('George')
    node1211 = node121.add_child('Jill')
    node12111 = node1211.add_child('Carol')
    node122 = node12.add_child('Mary')
    node13 = node1.add_child('Mark')
    node2 = root.add_child('Bill')
    node21 = node2.add_child('Grace')

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
    print(node13.height)
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
    print(node13.size)
    print(node1.size)
    print(node2.size)
    print(node21.size)
    print(root.size)
