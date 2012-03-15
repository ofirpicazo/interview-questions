#!/usr/bin/env python
# encoding: utf-8
"""
Implements a stack data structure using a linked list.

@author: Ofir Picazo - ofirpicazo@gmail.com
@date: March 2012
"""

import unittest


class Stack(object):
    def __init__(self):
        self._last = None
        self._count = 0

    def __len__(self):
        return self._count

    def __str__(self):
        values = []
        current = self._last
        while(current):
            values.append(str(current.value))
            current = current.next
        return  '[%s]' % ', '.join(values)

    def push(self, value):
        node = self._Node(value)
        node.next = self._last
        self._last = node
        self._count += 1

    def pop(self):
        if self._count > 0:
            popped_value = self._last.value
            self._last = self._last.next
            self._count -= 1
            return popped_value
        else:
            raise IndexError('pop from empty stack')

    class _Node(object):
        def __init__(self, value):
            self.value = value
            self.next = None


class StackTests(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_push(self):
        self.stack.push('a')
        self.stack.push('b')
        self.stack.push('c')
        self.assertEqual(len(self.stack), 3)

    def test_pop(self):
        self.stack.push('a')
        self.stack.push('b')
        self.stack.push('c')
        self.assertEqual(self.stack.pop(), 'c')
        self.assertEqual(self.stack.pop(), 'b')

    def test_pop_empty(self):
        self.assertEqual(len(self.stack), 0)
        self.assertRaises(IndexError, self.stack.pop)


if __name__ == '__main__':
    unittest.main()
