"""Tests for test module 409 — covers src modules [1633, 1634, 1635, 1636]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1633 import add_1633
from module_1634 import subtract_1634
from module_1635 import multiply_1635
from module_1636 import divide_1636

def test_add_1633():
    assert add_1633(2, 3) == 5

def test_subtract_1634():
    assert subtract_1634(10, 4) == 6

def test_multiply_1635():
    assert multiply_1635(3, 7) == 21

def test_divide_1636():
    assert divide_1636(10, 2) == 5.0
