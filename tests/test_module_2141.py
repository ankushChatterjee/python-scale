"""Tests for test module 2141 — covers src modules [8561, 8562, 8563, 8564]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8561 import add_8561
from module_8562 import subtract_8562
from module_8563 import multiply_8563
from module_8564 import divide_8564

def test_add_8561():
    assert add_8561(2, 3) == 5

def test_subtract_8562():
    assert subtract_8562(10, 4) == 6

def test_multiply_8563():
    assert multiply_8563(3, 7) == 21

def test_divide_8564():
    assert divide_8564(10, 2) == 5.0
