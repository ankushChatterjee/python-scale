"""Tests for test module 891 — covers src modules [3561, 3562, 3563, 3564]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3561 import add_3561
from module_3562 import subtract_3562
from module_3563 import multiply_3563
from module_3564 import divide_3564

def test_add_3561():
    assert add_3561(2, 3) == 5

def test_subtract_3562():
    assert subtract_3562(10, 4) == 6

def test_multiply_3563():
    assert multiply_3563(3, 7) == 21

def test_divide_3564():
    assert divide_3564(10, 2) == 5.0
