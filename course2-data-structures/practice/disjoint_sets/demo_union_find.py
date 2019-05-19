#!/usr/bin/python3

import itertools

import union_find

class Node:

    def __init__ (self, label):
        self.label = label

    def __str__(self):
        return str(self.label)

def print_sets(nodes):
    sets = [ str(union_find.find(x)) for x in nodes ]
    print('set representatives: %s' % (sets))
    print('number of disjoint sets: %s' %
        (len([ i for i in itertools.groupby(sets) ])))
    print()

union_find = union_find.UnionFind()

nodes = [ Node(ch) for ch in 'abcdefg' ]

print('labels: %s' % ([ str(i) for i in nodes ]))
for node in nodes:
    union_find.make_set(node)

print_sets(nodes)

assert(union_find.find(nodes[0]) != union_find.find(nodes[2]))
union_find.union(nodes[0], nodes[2])
assert(union_find.find(nodes[0]) == union_find.find(nodes[2]))

print_sets(nodes)

assert(union_find.find(nodes[0]) != union_find.find(nodes[1]))
assert(union_find.find(nodes[1]) != union_find.find(nodes[2]))
union_find.union(nodes[0], nodes[1])
assert(union_find.find(nodes[0]) == union_find.find(nodes[1]))
assert(union_find.find(nodes[1]) == union_find.find(nodes[2]))

print_sets(nodes)

assert(union_find.find(nodes[-2]) != union_find.find(nodes[-1]))
union_find.union(nodes[-2], nodes[-1])
assert(union_find.find(nodes[-2]) == union_find.find(nodes[-1]))

print_sets(nodes)

assert(union_find.find(nodes[-3]) != union_find.find(nodes[-1]))
union_find.union(nodes[-3], nodes[-1])
assert(union_find.find(nodes[-3]) == union_find.find(nodes[-1]))

print_sets(nodes)
