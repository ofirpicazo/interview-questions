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

    def __getitem__(self, key):
        """Allows the x[key] syntax for retrieving elements."""
        if self.root:
            return self._find(key, self.root)
        else:
            raise KeyError(key)

    def __contains__(self, key):
        """Allows the use of the "in" operator to check for existing keys."""
        try:
            value = self.__getitem__(key)
        except KeyError:
            return False
        return True

    def _find(self, key, node):
        if key == node.key:
            return node.value
        elif key < node.key and node.left:
            return self._find(key, node.left)
        elif key > node.key and node.right:
            return self._find(key, node.right)
        else:
            raise KeyError(key)

    def pre_order(self):
        if self.root:
            return self._pre_order(self.root)
        else:
            return []

    def _pre_order(self, node):
        sequence = [node.key]
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
        sequence.append(node.key)
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
        sequence.append(node.key)
        return sequence

    def insert(self, key, value):
        """Inserts a new value keeping the tree sorted."""
        new_node = self._Node(key, value)
        if self.root:
            self._insert_child(self.root, new_node)            
        else:
            self.root = new_node

    def _insert_child(self, parent, child):
        """Insert a child node under a parent node recursively."""
        if child.key < parent.key:
            if parent.left:
                self._insert_child(parent.left, child)
            else:
                parent.left = child
        elif child.key > parent.key:
            if parent.right:
                self._insert_child(parent.right, child)
            else:
                parent.right = child

    class _Node(object):
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.left = None
            self.right = None


class BinarySearchTreeTests(unittest.TestCase):
    def setUp(self):
        self.tree = BinarySearchTree()
        input_keys = [10, 6, 7, 8, 9, 5, 11, 20, 16]
        for key in input_keys:
            self.tree.insert(key, key**2)

    def test_pre_order(self):
        self.assertEqual(self.tree.pre_order(), [10, 6, 5, 7, 8, 9, 11, 20, 16])

    def test_in_order(self):
        self.assertEqual(self.tree.in_order(), [5, 6, 7, 8, 9, 10, 11, 16, 20])

    def test_post_order(self):
        self.assertEqual(self.tree.post_order(), [5, 9, 8, 7, 6, 16, 20, 11, 10])

    def test_get_existing_item(self):
        self.assertEqual(self.tree[7], 49)

    def test_get_nonexisting_item(self):
        self.assertRaises(KeyError, self.tree.__getitem__, 50)

    def test_in_operator(self):
        self.assertTrue(20 in self.tree)
        self.assertTrue(50 not in self.tree)

if __name__ == '__main__':
    unittest.main()
