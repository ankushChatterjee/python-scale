"""Tests for test module 389 — covers src modules [1553, 1554, 1555, 1556]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1553 import add_1553
from module_1554 import subtract_1554
from module_1555 import multiply_1555
from module_1556 import divide_1556

def test_add_1553():
    assert add_1553(2, 3) == 5

def test_subtract_1554():
    assert subtract_1554(10, 4) == 6

def test_multiply_1555():
    assert multiply_1555(3, 7) == 21

def test_divide_1556():
    assert divide_1556(10, 2) == 5.0
