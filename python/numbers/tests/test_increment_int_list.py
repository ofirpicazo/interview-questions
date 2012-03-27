# encoding: utf-8
"""
Tests for the increment_int_list module.

@author: Ofir Picazo - ofirpicazo@gmail.com
@date: March 2012
"""

import unittest

from numbers.increment_int_list import increment


class IncrementIntListTest(unittest.TestCase):
    def test_increment(self):
        input_list = [8, 7, 9, 9]
        expected_list = [8, 8, 0, 0]
        self.assertEquals(expected_list, increment(input_list))

    def test_increment_all9s(self):
        input_list = [9, 9, 9, 9, 9]
        expected_list = [1, 0, 0, 0, 0, 0]
        self.assertEquals(expected_list, increment(input_list))
