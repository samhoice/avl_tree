from __future__ import annotations
from typing import Optional, Any
from enum import Enum


class Order(Enum):
    IN = 0
    PRE = 1
    POST = 2


class AVLNode:
    """Initially implementing a BST

    This will be slowly updated to impment an AVL tree.
    """

    def __init__(
        self,
        value: Any = None,
    ):
        # TODO: If we can pass a value for the current node, then we have
        # to expect None children. We shouldn't be able to pass values for
        # the children here.

        self._left = None
        self._balance = 0
        self._right = None
        self._value = value

    def _init_children(self):
        """create children

        Can't do this in init because we don't want to call init
        recursively.
        """
        if not self._left:
            self._left = AVLNode()
        if not self._right:
            self._right = AVLNode()

    def insert(self, value: Any):
        """insert a node into the tree

        Could probably return +1 if the tree gets taller or 0 otherwise?
        Probably need to maintain a height
        """
        if not self._value:
            self._value = value
            self._init_children()
        elif value > self._value:
            if not self._right:
                # This shouldn't happen
                print("WARNING! NO RIGHT CHILD")
            else:
                self._right.insert(value)
        elif value < self._value:
            if not self._left:
                # This shouldn't happen
                print("WARNING! NO LEFT CHILD")
            else:
                self._left.insert(value)
        else:
            # FIXME: Drop dupes for now
            pass

    def __str__(self):
        return f"Node: {self._value} - left: {self._left}, right: {self._right}"

    @classmethod
    def traverse(cls, node, function, order=Order.IN):
        """recursively traverse the tree structure"""

        if not node:
            return

        if node._value:
            if order == Order.IN:
                cls.traverse(node._left, function, order=Order.IN)
                function(node._value)
                cls.traverse(node._right, function, order=Order.IN)
            elif order == Order.PRE:
                function(node._value)
                cls.traverse(node._left, function, order=Order.PRE)
                cls.traverse(node._right, function, order=Order.PRE)
            else:
                cls.traverse(node._left, function, order=Order.POST)
                cls.traverse(node._right, function, order=Order.POST)
                function(node._value)

    @staticmethod
    def rotate_left(node):
        child = node._right
        node._right = child._left
        child._left = node
        return child

    @staticmethod
    def rotate_right(node):
        child = node._left
        node._left = child._right
        child._right = node
        return child

    def delete(self, value=None):
        """remove a node from the tree

        match value and remove?
        """
        pass
