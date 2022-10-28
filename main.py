#!/bin/python
from avl import AVLNode, Order
from random import shuffle

def tree_print(self, parent):

    print(f"{self} - child of {parent}")

tree = AVLNode(5)
# tree.insert(12)
# tree.insert(19)
# tree.insert(3)
values = list(range(11))
shuffle(values)

print(values)
for i in values:
    tree.insert(i)

print("pre order")
tree.traverse(tree_print, order=Order.PRE)
print("in order")
tree.traverse(tree_print)
print("post order")
tree.traverse(tree_print, order=Order.POST)
