# encoding: utf-8
"""
Implements a singly linked list data structure.

@author: Ofir Picazo - ofirpicazo@gmail.com
@date: March 2012
"""


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
