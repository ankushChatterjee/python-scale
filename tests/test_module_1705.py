"""Tests for test module 1705 — covers src modules [6817, 6818, 6819, 6820]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6817 import add_6817
from module_6818 import subtract_6818
from module_6819 import multiply_6819
from module_6820 import divide_6820

def test_add_6817():
    assert add_6817(2, 3) == 5

def test_subtract_6818():
    assert subtract_6818(10, 4) == 6

def test_multiply_6819():
    assert multiply_6819(3, 7) == 21

def test_divide_6820():
    assert divide_6820(10, 2) == 5.0
