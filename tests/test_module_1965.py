"""Tests for test module 1965 — covers src modules [7857, 7858, 7859, 7860]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7857 import add_7857
from module_7858 import subtract_7858
from module_7859 import multiply_7859
from module_7860 import divide_7860

def test_add_7857():
    assert add_7857(2, 3) == 5

def test_subtract_7858():
    assert subtract_7858(10, 4) == 6

def test_multiply_7859():
    assert multiply_7859(3, 7) == 21

def test_divide_7860():
    assert divide_7860(10, 2) == 5.0
