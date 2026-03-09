"""Tests for test module 1715 — covers src modules [6857, 6858, 6859, 6860]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6857 import add_6857
from module_6858 import subtract_6858
from module_6859 import multiply_6859
from module_6860 import divide_6860

def test_add_6857():
    assert add_6857(2, 3) == 5

def test_subtract_6858():
    assert subtract_6858(10, 4) == 6

def test_multiply_6859():
    assert multiply_6859(3, 7) == 21

def test_divide_6860():
    assert divide_6860(10, 2) == 5.0
