"""Tests for test module 2215 — covers src modules [8857, 8858, 8859, 8860]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8857 import add_8857
from module_8858 import subtract_8858
from module_8859 import multiply_8859
from module_8860 import divide_8860

def test_add_8857():
    assert add_8857(2, 3) == 5

def test_subtract_8858():
    assert subtract_8858(10, 4) == 6

def test_multiply_8859():
    assert multiply_8859(3, 7) == 21

def test_divide_8860():
    assert divide_8860(10, 2) == 5.0
