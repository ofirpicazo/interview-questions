#!/usr/bin/env python
# encoding: utf-8
"""
Implements a stack data structure.

Copyright (c) 2012 Ofir Picazo. All rights reserved.
"""

import unittest


class Stack:
    def __init__(self):
        self._current = None
        self._count = 0

    def __len__(self):
        return self._count

    def push(self, value):
        node = self._Node(value)
        node.next = self._current
        self._current = node
        self._count += 1

    def pop(self):
        if self._count > 0:
            popped_value = self._current.value
            self._current = self._current.next
            self._count -= 1
            return popped_value
        else:
            raise IndexError('pop from empty stack')

    class _Node:
        def __init__(self, value):
            self.value = value
            self.next = None


class StackTests(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_push(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(len(self.stack), 3)

    def test_pop(self):
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 1)

    def test_pop_empty(self):
        self.assertEqual(len(self.stack), 0)
        self.assertRaises(IndexError, self.stack.pop)


if __name__ == '__main__':
    unittest.main()
