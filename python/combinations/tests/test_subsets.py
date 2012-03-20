# encoding: utf-8
"""
Test for the subsets module.

@author: Ofir Picazo - ofirpicazo@gmail.com
@date: March 2012
"""

import unittest

from combinations import subsets


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
        self.assertEquals(expected_subsets, subsets.get_subsets(self.set))
