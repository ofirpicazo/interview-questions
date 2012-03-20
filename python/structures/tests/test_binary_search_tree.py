# encoding: utf-8
"""
Tests for the binary search tree data structure.

@author: Ofir Picazo - ofirpicazo@gmail.com
@date: March 2012
"""

import unittest

from structures import binary_search_tree


class BinarySearchTreeTests(unittest.TestCase):
    def setUp(self):
        self.tree = binary_search_tree.BinarySearchTree()
        input_keys = [10, 6, 7, 8, 9, 5, 11, 20, 16]
        for key in input_keys:
            self.tree.insert(key, key**2)

    def test_pre_order(self):
        self.assertEqual([10, 6, 5, 7, 8, 9, 11, 20, 16], self.tree.pre_order())

    def test_in_order(self):
        self.assertEqual([5, 6, 7, 8, 9, 10, 11, 16, 20], self.tree.in_order())

    def test_post_order(self):
        self.assertEqual([5, 9, 8, 7, 6, 16, 20, 11, 10], self.tree.post_order())

    def test_get_existing_item(self):
        self.assertEqual(49, self.tree[7])

    def test_get_nonexisting_item(self):
        self.assertRaises(KeyError, self.tree.__getitem__, 50)

    def test_in_operator(self):
        self.assertTrue(20 in self.tree)
        self.assertTrue(50 not in self.tree)

    def test_dot_syntax(self):
        output = 'digraph G { graph [ordering="out"]; 10 -> 6; 6 -> 5; 6 -> 7; 7 -> 8; 8 -> 9; 10 -> 11; 11 -> 20; 20 -> 16; }'
        self.assertTrue(output, self.tree.dot_syntax())

    def test_is_balanced(self):
        self.assertFalse(self.tree.is_balanced())