# encoding: utf-8
"""
Tests for the linked list data structure.

@author: Ofir Picazo - ofirpicazo@gmail.com
@date: March 2012
"""

import unittest

from structures import linked_list


class LinkedListTests(unittest.TestCase):
    def setUp(self):
        self.linked_list = linked_list.LinkedList([1, 2, 3, 4, 5])

    def test_get_at(self):
        self.assertEquals(2, self.linked_list.get_at(1))
        self.assertEquals(4, self.linked_list.get_at(3))

    def test_add(self):
        self.linked_list.add(6)
        self.linked_list.add(7)
        self.assertEquals(6, self.linked_list.get_at(5))
        self.assertEquals(7, self.linked_list.get_at(6))

    def insert_at(self):
        self.linked_list.insert_at(2, 'a')
        self.linked_list.insert_at(0, 'b')
        self.assertEquals('a', self.linked_list.get_at(2))
        self.assertEquals('b', self.linked_list.get_at(0))
        self.assertRaises(IndexError, self.linked_list.insert_at, 20, 'b')

    def test_remove(self):
        self.assertEquals(1, self.linked_list.remove())
        self.assertEquals(2, self.linked_list.remove())
        self.assertEquals(3, self.linked_list.remove())
        self.assertEquals(4, self.linked_list.remove())
        self.assertEquals(5, self.linked_list.remove())
        self.assertRaises(IndexError, self.linked_list.remove)

    def test__len__(self):
        self.assertEquals(5, self.linked_list.__len__())

    def test__str__(self):
        self.assertEquals('[1 -> 2 -> 3 -> 4 -> 5]', self.linked_list.__str__())

