# encoding: utf-8
"""
Tests for the merge_sort module.

@author: Ofir Picazo - ofirpicazo@gmail.com
@date: March 2012
"""

import unittest

from sorting import merge_sort


class MergeSortTest(unittest.TestCase):
    def test_get_permutations(self):
        input_list = [7, 23, 5, 1, 0, 65, 3, 56, -4, 22, 10, 1, 81]
        expected_list = [-4, 0, 1, 1, 3, 5, 7, 10, 22, 23, 56, 65, 81]
        self.assertEquals(expected_list, merge_sort.merge_sort(input_list))
