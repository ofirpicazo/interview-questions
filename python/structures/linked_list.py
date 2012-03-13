#!/usr/bin/env python
# encoding: utf-8
"""
Implements a linked list.

Copyright (c) 2012 Ofir Picazo. All rights reserved.
"""

import sys
import os
import unittest


class LinkedList:
	def __init__(self):
		self.first_node = _Node()

	def add(self, value):
		current_node = self.first_node
		while(current_node.next)
			current_node = current_node.next
		current_node.next = _Node(value)

	def insert_at(self, index, value):
		running_index = 0
		currentNode = self.first_node
		

class _Node:
	def __init__(self, value=None):
		self.value = value
		self.next = None

class untitledTests(unittest.TestCase):
	def setUp(self):
		pass


if __name__ == '__main__':
	unittest.main()