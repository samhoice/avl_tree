from __future__ import annotations
from typing import Optional, Any
from enum import Enum

class Order(Enum):
    IN = 0
    PRE = 1
    POST = 2


class AVLNode:
    """ Initially implementing a BST

    This will be slowly updated to impment an AVL tree.
    """
    def __init__(self, value: Any, left=None, right=None):
        self._left = left
        self._right = right
        self._value = value

    def insert(self, value: Any):
        """ insert a node into the tree

        Could probably return +1 if the tree gets taller or 0 otherwise?
        Probably need to maintain a height
        """
        if value > self._value:
            if self._right:
                self._right.insert(value)
            else:
                self._right = AVLNode(value, None, None)
        elif value < self._value:
            if self._left:
                self._left.insert(value)
            else:
                self._left = AVLNode(value, None, None)
        else:
            # FIXME: Drop dupes for now
            pass

    def __str__(self):
        return f"Node: {self._value} - left: {self._left}, right: {self._right}"

    def traverse(self, function, parent = None, order = Order.IN):
        """ recursively traverse the tree structure
        """
        if order == Order.PRE:
            function(self._value, parent)
        if self._left:
            self._left.traverse(function, self, order)
        if order == Order.IN:
            function(self._value, parent)
        if self._right:
            self._right.traverse(function, self, order)
        if order == Order.POST:
            function(self._value, parent)


    def rotate_left(self):
        pass

    
    def rotate_right(self):
        pass


    def delete(self, value=None):
        """ remove a node from the tree

        match value and remove?
        """
        pass

