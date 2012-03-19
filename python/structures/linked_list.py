#!/usr/bin/env python
# encoding: utf-8
"""
Implements a stack data structure using a linked list.

@author: Ofir Picazo - ofirpicazo@gmail.com
@date: March 2012
"""

import unittest


class LinkedList:
    def __init__(self, iterable=None):
        self._first_node = None
        self._count = 0
        for element in iterable:
            self.add(element)

    def __len__(self):
        return self._count

    def __str__(self):
        values = []
        current = self._first_node
        while(current):
            values.append(str(current.value))
            current = current.next
        return  '[%s]' % ' -> '.join(values)

    def add(self, value):
    	if self._count > 0:
            current_node = self._first_node
            while current_node.next:
                current_node = current_node.next
            current_node.next = self._Node(value)
        else:
            self._first_node = self._Node(value)
        self._count += 1

    def insert_at(self, index, value):
        if index > self._count:
            raise IndexError('index %s is out of range' % index)
        else:
            current_node = self._first_node
            i = 0
            while i <= index:
                current_node = current_node.next
                i += 1
            current_node.next = self._Node(value)
            self._count += 1

    def get_at(self, index):
        if index >= self._count:
            raise IndexError('index %s is out of range' % index)
        else:
            current_node = self._first_node
            i = 0
            while i < index:
                current_node = current_node.next
                i += 1
            return current_node.value

    def remove(self):
        if self._first_node:
            removed_node = self._first_node
            self._first_node = self._first_node.next
            self._count -= 1
            return removed_node.value
        else:
            raise IndexError('remove from empty list')

    class _Node:
        def __init__(self, value):
            self.value = value
            self.next = None


class LinkedListTests(unittest.TestCase):
    def setUp(self):
        self.linked_list = LinkedList([1, 2, 3, 4, 5])

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


if __name__ == '__main__':
    unittest.main()
