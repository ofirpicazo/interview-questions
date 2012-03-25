# encoding: utf-8
"""
Tests for the find_longest_subsequence module.

@author: Ofir Picazo - ofirpicazo@gmail.com
@date: March 2012
"""

import unittest

from searching.find_longest_subsequence import find_longest_subsequence
from searching.find_longest_subsequence import find_longest_subsequence_with_sorting


class FindLongestSubsequenceTest(unittest.TestCase):
    def setUp(self):
        self.input_sequence = [10, 21, 45, 22, 7, 2, 67, 19, 13, 45, 12, 11, 18,
                               16, 17, 100, 201, 20, 101]
        self.expected_subsequence = [16, 17, 18, 19, 20, 21, 22]

    def test_find_longest_subsequence_with_sorting(self):
        resulting_sequence = find_longest_subsequence_with_sorting(
            self.input_sequence)
        self.assertEquals(self.expected_subsequence, resulting_sequence)

    def test_find_longest_subsequence(self):
        resulting_sequence = find_longest_subsequence(self.input_sequence)
        self.assertEquals(self.expected_subsequence, resulting_sequence)
