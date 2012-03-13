#!/usr/bin/env python
# encoding: utf-8
"""
Implements a queue data structure using a linked list.

@author: Ofir Picazo - ofirpicazo@gmail.com
@date: March 2012
"""

import unittest


class Queue:
    def __init__(self):
        self._first = None
        self._last = None
        self._count = 0

    def __len__(self):
        return self._count

    def __str__(self):
        values = []
        current = self._first
        while(current):
            values.append(str(current.value))
            current = current.next
        return  '[%s]' % ', '.join(values)

    def enqueue(self, value):
        node = self._Node(value)
        if self._last:
            self._last.next = node
            self._last = self._last.next
        else:
            self._first = node
            self._last = self._first
        self._count += 1

    def dequeue(self):
        if self._first:
            value = self._first.value
            self._first = self._first.next
            self._count -= 1
            return value
        else:
            raise IndexError('dequeue from empty queue')

    class _Node:
        def __init__(self, value):
            self.value = value
            self.next = None


class QueueTests(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_enqueue(self):
        self.queue.enqueue('a')
        self.queue.enqueue('b')
        self.queue.enqueue('c')
        self.assertEqual(len(self.queue), 3)

    def test_dequeue(self):
        self.queue.enqueue('a')
        self.queue.enqueue('b')
        self.queue.enqueue('c')
        self.assertEqual(self.queue.dequeue(), 'a')
        self.assertEqual(self.queue.dequeue(), 'b')

    def test_dequeue_empty(self):
        self.assertEqual(len(self.queue), 0)
        self.assertRaises(IndexError, self.queue.dequeue)


if __name__ == '__main__':
    unittest.main()
