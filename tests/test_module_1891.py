"""Tests for test module 1891 — covers src modules [7561, 7562, 7563, 7564]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7561 import add_7561
from module_7562 import subtract_7562
from module_7563 import multiply_7563
from module_7564 import divide_7564

def test_add_7561():
    assert add_7561(2, 3) == 5

def test_subtract_7562():
    assert subtract_7562(10, 4) == 6

def test_multiply_7563():
    assert multiply_7563(3, 7) == 21

def test_divide_7564():
    assert divide_7564(10, 2) == 5.0
