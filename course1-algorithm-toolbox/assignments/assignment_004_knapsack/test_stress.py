#!/usr/bin/python3

import math
from random import randint

import unittest

from knapsack_gold import optimal_weight, optimal_weight_simplified

class OptimalWeightSimplfiedStressTestCase(unittest.TestCase):

    CAPACITY = int(math.pow(10, 4))
    WEIGHT = int(math.pow(10, 5))
    N = 300

    def test(self):
        while True:
            capacity = randint(0,
                OptimalWeightSimplfiedStressTestCase.CAPACITY)

            weights = []
            for i in range(0, OptimalWeightSimplfiedStressTestCase.N):
                weights.append(randint(0,
                    OptimalWeightSimplfiedStressTestCase.WEIGHT))

            value = optimal_weight_simplified(capacity, weights)

            print('capacity: %s' % capacity)
            print('weights: %s' % weights)
            print('value: %s' % value)
            print()
            self.assertTrue(capacity >= value)

class OptimalWeightStressTestCase(unittest.TestCase):

    CAPACITY = int(math.pow(10, 4))
    WEIGHT = int(math.pow(10, 5))
    N = 300

    def assert_items_within_capacity(self, capacity, weights, value, items):
        total_weight = 0
        total_value = 0
        for i in items:
            total_weight += weights[i]
            total_value += weights[i]

    def test(self):
        while True:
            capacity = randint(0,
                OptimalWeightStressTestCase.CAPACITY)

            weights = []
            for i in range(0, OptimalWeightStressTestCase.N):
                weights.append(randint(0,
                    OptimalWeightStressTestCase.WEIGHT))

            value, items = optimal_weight(capacity, weights)

            print('capacity: %s' % capacity)
            print('weights: %s' % weights)
            print('value: %s' % value)
            print('items: %s' % items)
            print()
            self.assert_items_within_capacity(capacity, weights, value, items)

if __name__ == '__main__':
    class_names = \
    [
        OptimalWeightSimplfiedStressTestCase
    ]

    suite = unittest.TestSuite()

    for c in class_names:
        suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(c))

    unittest.TextTestRunner().run(suite)
