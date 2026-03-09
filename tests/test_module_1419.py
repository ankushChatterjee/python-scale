"""Tests for test module 1419 — covers src modules [5673, 5674, 5675, 5676]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5673 import add_5673
from module_5674 import subtract_5674
from module_5675 import multiply_5675
from module_5676 import divide_5676

def test_add_5673():
    assert add_5673(2, 3) == 5

def test_subtract_5674():
    assert subtract_5674(10, 4) == 6

def test_multiply_5675():
    assert multiply_5675(3, 7) == 21

def test_divide_5676():
    assert divide_5676(10, 2) == 5.0
