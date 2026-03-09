"""Tests for test module 1919 — covers src modules [7673, 7674, 7675, 7676]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7673 import add_7673
from module_7674 import subtract_7674
from module_7675 import multiply_7675
from module_7676 import divide_7676

def test_add_7673():
    assert add_7673(2, 3) == 5

def test_subtract_7674():
    assert subtract_7674(10, 4) == 6

def test_multiply_7675():
    assert multiply_7675(3, 7) == 21

def test_divide_7676():
    assert divide_7676(10, 2) == 5.0
