"""Tests for test module 2205 — covers src modules [8817, 8818, 8819, 8820]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8817 import add_8817
from module_8818 import subtract_8818
from module_8819 import multiply_8819
from module_8820 import divide_8820

def test_add_8817():
    assert add_8817(2, 3) == 5

def test_subtract_8818():
    assert subtract_8818(10, 4) == 6

def test_multiply_8819():
    assert multiply_8819(3, 7) == 21

def test_divide_8820():
    assert divide_8820(10, 2) == 5.0
