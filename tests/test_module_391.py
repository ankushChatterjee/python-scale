"""Tests for test module 391 — covers src modules [1561, 1562, 1563, 1564]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1561 import add_1561
from module_1562 import subtract_1562
from module_1563 import multiply_1563
from module_1564 import divide_1564

def test_add_1561():
    assert add_1561(2, 3) == 5

def test_subtract_1562():
    assert subtract_1562(10, 4) == 6

def test_multiply_1563():
    assert multiply_1563(3, 7) == 21

def test_divide_1564():
    assert divide_1564(10, 2) == 5.0
