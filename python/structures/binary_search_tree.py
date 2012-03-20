# encoding: utf-8
"""
Implements a binary search tree data structure.

@author: Ofir Picazo - ofirpicazo@gmail.com
@date: March 2012
"""


class BinarySearchTree(object):
    def __init__(self):
        self._root = None

    def __getitem__(self, key):
        """Allows the x[key] syntax for retrieving elements."""
        if self._root:
            return self._find(key, self._root)
        else:
            raise KeyError(key)

    def __contains__(self, key):
        """Allows the use of the "in" operator to check for existing keys."""
        try:
            value = self.__getitem__(key)
        except KeyError:
            return False
        return True

    def dot_syntax(self):
        sequence = []
        if self._root:
            sequence = ['%s;' % self._root.key]
            sequence = self._get_node_dot_syntax(self._root)
        return 'digraph G { graph [ordering="out"]; %s }' % ' '.join(sequence)

    def _get_node_dot_syntax(self, node):
        sequence = []
        if node.left:
            sequence.append('%s -> %s;' % (node.key, node.left.key))
            sequence.extend(self._get_node_dot_syntax(node.left))
        if node.right:
            sequence.append('%s -> %s;' % (node.key, node.right.key))
            sequence.extend(self._get_node_dot_syntax(node.right))
        return sequence

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
        if self._root:
            return self._pre_order(self._root)
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
        if self._root:
            return self._in_order(self._root)
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
        if self._root:
            return self._post_order(self._root)
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
        if self._root:
            self._insert_child(self._root, new_node)
        else:
            self._root = new_node

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

    def is_balanced(self):
        """Tests whether the tree is balanced or not."""
        if self._root:
            try:
                self._get_node_height(self._root)
            except IndexError:
                return False
        return True

    def _get_node_height(self, node):
        left_height = 0
        right_height = 0

        if node.left:
            left_height += 1
            left_height += self._get_node_height(node.left)
        if node.right:
            right_height += 1
            right_height += self._get_node_height(node.right)

        height = abs(left_height - right_height)
        if height > 1:
            raise IndexError('Node %s is unbalanced' % node.key)
        return height

    class _Node(object):
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.left = None
            self.right = None
