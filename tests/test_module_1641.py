"""Tests for test module 1641 — covers src modules [6561, 6562, 6563, 6564]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6561 import add_6561
from module_6562 import subtract_6562
from module_6563 import multiply_6563
from module_6564 import divide_6564

def test_add_6561():
    assert add_6561(2, 3) == 5

def test_subtract_6562():
    assert subtract_6562(10, 4) == 6

def test_multiply_6563():
    assert multiply_6563(3, 7) == 21

def test_divide_6564():
    assert divide_6564(10, 2) == 5.0
