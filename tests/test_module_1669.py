"""Tests for test module 1669 — covers src modules [6673, 6674, 6675, 6676]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6673 import add_6673
from module_6674 import subtract_6674
from module_6675 import multiply_6675
from module_6676 import divide_6676

def test_add_6673():
    assert add_6673(2, 3) == 5

def test_subtract_6674():
    assert subtract_6674(10, 4) == 6

def test_multiply_6675():
    assert multiply_6675(3, 7) == 21

def test_divide_6676():
    assert divide_6676(10, 2) == 5.0
