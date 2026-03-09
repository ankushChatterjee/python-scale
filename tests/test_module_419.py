"""Tests for test module 419 — covers src modules [1673, 1674, 1675, 1676]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1673 import add_1673
from module_1674 import subtract_1674
from module_1675 import multiply_1675
from module_1676 import divide_1676

def test_add_1673():
    assert add_1673(2, 3) == 5

def test_subtract_1674():
    assert subtract_1674(10, 4) == 6

def test_multiply_1675():
    assert multiply_1675(3, 7) == 21

def test_divide_1676():
    assert divide_1676(10, 2) == 5.0
