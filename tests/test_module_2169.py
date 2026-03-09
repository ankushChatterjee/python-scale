"""Tests for test module 2169 — covers src modules [8673, 8674, 8675, 8676]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8673 import add_8673
from module_8674 import subtract_8674
from module_8675 import multiply_8675
from module_8676 import divide_8676

def test_add_8673():
    assert add_8673(2, 3) == 5

def test_subtract_8674():
    assert subtract_8674(10, 4) == 6

def test_multiply_8675():
    assert multiply_8675(3, 7) == 21

def test_divide_8676():
    assert divide_8676(10, 2) == 5.0
