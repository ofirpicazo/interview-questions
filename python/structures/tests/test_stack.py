# encoding: utf-8
"""
Tests for the stack data structure.

@author: Ofir Picazo - ofirpicazo@gmail.com
@date: March 2012
"""

import unittest

from structures import stack


class StackTests(unittest.TestCase):
    def setUp(self):
        self.stack = stack.Stack()

    def test_push(self):
        self.stack.push('a')
        self.stack.push('b')
        self.stack.push('c')
        self.assertEqual(3, len(self.stack))

    def test_pop(self):
        self.stack.push('a')
        self.stack.push('b')
        self.stack.push('c')
        self.assertEqual('c', self.stack.pop())
        self.assertEqual('b', self.stack.pop())

    def test_pop_empty(self):
        self.assertEqual(0, len(self.stack))
        self.assertRaises(IndexError, self.stack.pop)
