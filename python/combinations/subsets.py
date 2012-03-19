#!/usr/bin/env python
# encoding: utf-8
"""
Returns all the subsets of a given set.

@author: Ofir Picazo - ofirpicazo@gmail.com
@date: March 2012
"""

import unittest

def get_subsets(input_set):
    def _convert_combination_to_set(combination):
        subset = set()
        for i, value in enumerate(combination):
            if value == '1':
                subset.add(immutable_input_set[i])
        return subset

    subsets = []
    size = len(input_set)
    immutable_input_set = tuple(input_set)
    combination = 0

    while combination < 2**size:
        binary_combination = bin(combination)[2:].rjust(size, '0')
        subset = _convert_combination_to_set(binary_combination)
        subsets.append(subset)
        combination += 1
    return subsets


class GetSubsetsTest(unittest.TestCase):
    def setUp(self):
        self.set = set([1, 2, 3, 4])

    def test_get_subsets(self):
        expected_subsets = [
            set(),
            set([4]),
            set([3]),
            set([3, 4]),
            set([2]),
            set([2, 4]),
            set([2, 3]),
            set([2, 3, 4]),
            set([1]),
            set([1, 4]),
            set([1, 3]),
            set([1, 3, 4]),
            set([1, 2]),
            set([1, 2, 4]),
            set([1, 2, 3]),
            set([1, 2, 3, 4])]
        self.assertEquals(expected_subsets, get_subsets(self.set))


if __name__ == '__main__':
    unittest.main()
