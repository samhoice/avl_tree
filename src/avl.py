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
    def traverse(cls, node, function, parent=None, order=Order.IN):
        """recursively traverse the tree structure"""

        if not node:
            return

        if node._value:
            if order == Order.IN:
                cls.traverse(node._left, function)
                function(node._value)
                cls.traverse(node._right, function)
            elif order == Order.PRE:
                function(node._value)
                cls.traverse(node._left, function)
                cls.traverse(node._right, function)
            else:
                cls.traverse(node._left, function)
                cls.traverse(node._right, function)
                function(node._value)

    def rotate_left(self):
        pass

    def rotate_right(self):
        pass

    def delete(self, value=None):
        """remove a node from the tree

        match value and remove?
        """
        pass
