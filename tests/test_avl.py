# pytest
from avl import AVLNode, Order

def test_tests():
    assert True

def check_result(result, test_data):

    assert(len(result) == len(test_data))
    assert(sorted(result) == sorted(test_data))


def test_empty_insert():
    tree = AVLNode()

    tree.insert(5)
    
    result = []
    AVLNode.traverse(tree, lambda x: result.append(x))

    check_result(result, [5])

def test_lesser_insert():
    tree = AVLNode()

    tree.insert(5)
    tree.insert(4)

    result = []
    AVLNode.traverse(tree, lambda x: result.append(x))

    check_result(result, [4,5])

def test_greater_insert():
    tree = AVLNode()

    tree.insert(5)
    tree.insert(7)
    tree.insert(6)

    result = []
    AVLNode.traverse(tree, lambda x: result.append(x))

    check_result(result, [5, 6, 7])


def test_traversal_order():
    """traversal in various order

    TODO: Will need to be updated for more inserts
    """
    tree = AVLNode()

    tree.insert(5)
    tree.insert(6)
    tree.insert(4)

    result = []
    AVLNode.traverse(tree, lambda x: result.append(x))

    check_result(result, [4, 5, 6])

    result = []
    AVLNode.traverse(tree, lambda x: result.append(x), Order.PRE)

    check_result(result, [5, 4, 6])

    result = []
    AVLNode.traverse(tree, lambda x: result.append(x), Order.POST)

    check_result(result, [4, 6, 5])
