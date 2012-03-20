# encoding: utf-8
"""
Tests for the string_permutations module.

@author: Ofir Picazo - ofirpicazo@gmail.com
@date: March 2012
"""

import unittest

from combinations import string_permutations


class GetPermutationsTest(unittest.TestCase):
    def test_get_permutations(self):
        target_string = 'abc'
        expected_permutations = ['cba', 'bca', 'bac', 'cab', 'acb', 'abc']
        self.assertEquals(
            expected_permutations,
            string_permutations.get_permutations(target_string))
