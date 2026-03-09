"""Tests for test module 955 — covers src modules [3817, 3818, 3819, 3820]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3817 import add_3817
from module_3818 import subtract_3818
from module_3819 import multiply_3819
from module_3820 import divide_3820

def test_add_3817():
    assert add_3817(2, 3) == 5

def test_subtract_3818():
    assert subtract_3818(10, 4) == 6

def test_multiply_3819():
    assert multiply_3819(3, 7) == 21

def test_divide_3820():
    assert divide_3820(10, 2) == 5.0
