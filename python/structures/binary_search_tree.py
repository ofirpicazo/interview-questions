#!/usr/bin/env python
# encoding: utf-8
"""
Implements a binary search tree data structure.

@author: Ofir Picazo - ofirpicazo@gmail.com
@date: March 2012
"""

import unittest


class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def pre_order(self):
        if self.root:
            return self._pre_order(self.root)
        else:
            return []

    def _pre_order(self, node):
        sequence = [node.value]
        if node.left:
            sequence.extend(self._pre_order(node.left))
        if node.right:
            sequence.extend(self._pre_order(node.right))
        return sequence

    def in_order(self):
        if self.root:
            return self._in_order(self.root)
        else:
            return []

    def _in_order(self, node):
        sequence = []
        if node.left:
            sequence.extend(self._in_order(node.left))
        sequence.append(node.value)
        if node.right:
            sequence.extend(self._in_order(node.right))
        return sequence

    def post_order(self):
        if self.root:
            return self._post_order(self.root)
        else:
            return []

    def _post_order(self, node):
        sequence = []
        if node.left:
            sequence.extend(self._post_order(node.left))
        if node.right:
            sequence.extend(self._post_order(node.right))
        sequence.append(node.value)
        return sequence

    def insert(self, value):
        """Inserts a new value keeping the tree sorted."""
        new_node = self._Node(value)
        if self.root:
            self._insert_child(self.root, new_node)            
        else:
            self.root = new_node

    def _insert_child(self, parent, child):
        """Insert a child node under a parent node recursively."""
        if child.value < parent.value:
            if parent.left:
                self._insert_child(parent.left, child)
            else:
                parent.left = child
        elif child.value > parent.value:
            if parent.right:
                self._insert_child(parent.right, child)
            else:
                parent.right = child

    class _Node(object):
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None


class BinarySearchTreeTests(unittest.TestCase):
    def setUp(self):
        self.tree = BinarySearchTree()
        input_values = [10, 6, 7, 8, 9, 5, 11, 20, 16]
        for value in input_values:
            self.tree.insert(value)

    def test_pre_order(self):
        self.assertEqual(self.tree.pre_order(), [10, 6, 5, 7, 8, 9, 11, 20, 16])

    def test_in_order(self):
        self.assertEqual(self.tree.in_order(), [5, 6, 7, 8, 9, 10, 11, 16, 20])

    def test_post_order(self):
        self.assertEqual(self.tree.post_order(), [5, 9, 8, 7, 6, 16, 20, 11, 10])


if __name__ == '__main__':
    unittest.main()
