"""Tests for test module 1465 — covers src modules [5857, 5858, 5859, 5860]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5857 import add_5857
from module_5858 import subtract_5858
from module_5859 import multiply_5859
from module_5860 import divide_5860

def test_add_5857():
    assert add_5857(2, 3) == 5

def test_subtract_5858():
    assert subtract_5858(10, 4) == 6

def test_multiply_5859():
    assert multiply_5859(3, 7) == 21

def test_divide_5860():
    assert divide_5860(10, 2) == 5.0
