# pytest
from avl import AVLNode

def test_tests():
    assert True

def test_empty_insert():
    tree = AVLNode()

    tree.insert(5)
    
    list_version = []
    tree.traverse(lambda x: list_version.append(x))

    assert(len(list_version) == 1)
    assert(list_version[0] == 5)
    
