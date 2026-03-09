"""Tests for test module 215 — covers src modules [857, 858, 859, 860]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_857 import add_857
from module_858 import subtract_858
from module_859 import multiply_859
from module_860 import divide_860

def test_add_857():
    assert add_857(2, 3) == 5

def test_subtract_858():
    assert subtract_858(10, 4) == 6

def test_multiply_859():
    assert multiply_859(3, 7) == 21

def test_divide_860():
    assert divide_860(10, 2) == 5.0
