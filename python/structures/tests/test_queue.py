# encoding: utf-8
"""
Tests for the queue data structure.

@author: Ofir Picazo - ofirpicazo@gmail.com
@date: March 2012
"""

import unittest

from structures import queue

class QueueTests(unittest.TestCase):
    def setUp(self):
        self.queue = queue.Queue()

    def test_enqueue(self):
        self.queue.enqueue('a')
        self.queue.enqueue('b')
        self.queue.enqueue('c')
        self.assertEqual(3, len(self.queue))

    def test_dequeue(self):
        self.queue.enqueue('a')
        self.queue.enqueue('b')
        self.queue.enqueue('c')
        self.assertEqual('a', self.queue.dequeue())
        self.assertEqual('b', self.queue.dequeue())

    def test_dequeue_empty(self):
        self.assertEqual(0, len(self.queue))
        self.assertRaises(IndexError, self.queue.dequeue)
